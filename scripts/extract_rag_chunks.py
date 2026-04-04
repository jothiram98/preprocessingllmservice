from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Optional

from docling_core.types.doc.document import DoclingDocument


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn a Docling JSON export into embedding-ready chunks."
    )
    parser.add_argument(
        "document_json",
        type=Path,
        help="Docling JSON export (`save_as_json` output).",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path("outputs/docling_chunks.jsonl"),
        help="JSONL file where each line is a chunk (text or image).",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=1200,
        help="Approximate maximum characters per text chunk.",
    )
    parser.add_argument(
        "--save-images",
        action="store_true",
        help="Save embedded images as PNG files so the vector store can reference them.",
    )
    parser.add_argument(
        "--image-dir",
        type=Path,
        default=Path("outputs/chunks_images"),
        help="Directory to drop PNGs when --save-images is enabled.",
    )
    return parser.parse_args()


def split_paragraphs(text: str, max_chars: int) -> list[str]:
    paragraphs = [para.strip() for para in text.split("\n\n") if para.strip()]
    chunks: list[str] = []
    current: list[str] = []

    def flush():
        if current:
            chunks.append("\n\n".join(current))
            current.clear()

    for para in paragraphs:
        candidate = "\n\n".join(current + [para]) if current else para
        if current and len(candidate) > max_chars:
            flush()
            current.append(para)
        else:
            current.append(para)

    flush()
    return chunks


def save_image(
    pic_item, doc: DoclingDocument, image_dir: Path, prefix: str, index: int
) -> Optional[str]:
    if pic_item.image is None:
        return None

    pil = pic_item.get_image(doc)
    if pil is None:
        return None

    image_dir.mkdir(parents=True, exist_ok=True)
    target = image_dir / f"{prefix}-{index}.png"
    pil.save(target)
    return str(target)


def build_picture_text(pic, doc: DoclingDocument) -> str:
    chunks: list[str] = []
    for child in pic.children:
        resolved = child.resolve(doc)
        if hasattr(resolved, "text"):
            chunks.append(resolved.text.strip())
    caption_text = pic.caption_text(doc)
    if caption_text:
        chunks.insert(0, caption_text.strip())
    return " ".join(filter(None, chunks))


def main() -> None:
    args = parse_args()
    doc = DoclingDocument.model_validate_json(args.document_json.read_text(encoding="utf-8"))

    text_source = doc.export_to_text(traverse_pictures=True)
    text_chunks = split_paragraphs(text_source, args.max_chars)

    output_chunks: list[dict] = []

    for idx, chunk in enumerate(text_chunks, start=1):
        output_chunks.append(
            {
                "id": f"text-{idx}",
                "type": "text",
                "source": doc.name or args.document_json.name,
                "document": str(args.document_json),
                "text": chunk,
            }
        )

    for idx, pic in enumerate(doc.pictures, start=1):
        picture_text = build_picture_text(pic, doc)
        prov = pic.prov[0] if pic.prov else None
        bbox = (
            {
                "l": prov.bbox.l,
                "t": prov.bbox.t,
                "r": prov.bbox.r,
                "b": prov.bbox.b,
            }
            if prov
            else None
        )
        saved_image = None
        if args.save_images:
            saved_image = save_image(pic, doc, args.image_dir, "picture", idx)

        output_chunks.append(
            {
                "id": f"picture-{idx}",
                "type": "picture",
                "source": doc.name or args.document_json.name,
                "document": str(args.document_json),
                "page": prov.page_no if prov else None,
                "bbox": bbox,
                "text": picture_text,
                "image_uri": str(pic.image.uri) if pic.image is not None else None,
                "image_path": saved_image,
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as fw:
        for chunk in output_chunks:
            fw.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"Wrote {len(output_chunks)} chunks to {args.output}")


if __name__ == "__main__":
    main()
