from __future__ import annotations

import argparse
import platform
from pathlib import Path

from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    EasyOcrOptions,
    OcrMacOptions,
    PdfPipelineOptions,
    RapidOcrOptions,
    TableStructureOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a simple Docling pipeline using local model artifacts."
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to a local PDF file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs"),
        help="Directory where Markdown and JSON outputs will be written.",
    )
    parser.add_argument(
        "--artifacts-path",
        type=Path,
        default=Path("models/docling"),
        help="Directory containing pre-downloaded Docling model artifacts.",
    )
    parser.add_argument(
        "--device",
        choices=["auto", "cpu", "mps", "cuda", "xpu"],
        default="auto",
        help="Accelerator device for local inference.",
    )
    parser.add_argument(
        "--ocr-engine",
        choices=["auto", "rapidocr", "ocrmac", "easyocr", "none"],
        default="rapidocr",
        help="OCR engine to use for scanned documents.",
    )
    parser.add_argument(
        "--image-mode",
        choices=["placeholder", "embedded", "referenced"],
        default="embedded",
        help="How extracted page images should be represented in the Markdown/JSON outputs.",
    )
    parser.add_argument(
        "--no-tables",
        action="store_true",
        help="Disable table structure extraction.",
    )
    parser.add_argument(
        "--force-offline",
        action="store_true",
        help="Fail fast if the local artifacts directory does not exist.",
    )
    return parser.parse_args()


def build_ocr_options(engine: str):
    if engine == "none":
        return None
    if engine == "auto":
        return build_ocr_options("ocrmac" if platform.system() == "Darwin" else "rapidocr")
    if engine == "rapidocr":
        return RapidOcrOptions()
    if engine == "ocrmac":
        return OcrMacOptions()
    if engine == "easyocr":
        return EasyOcrOptions(download_enabled=False)
    return None


def build_converter(args: argparse.Namespace) -> DocumentConverter:
    accelerator_options = AcceleratorOptions(
        device=AcceleratorDevice(args.device),
    )

    pipeline_options = PdfPipelineOptions(
        artifacts_path=str(args.artifacts_path),
        enable_remote_services=False,
        accelerator_options=accelerator_options,
        do_ocr=args.ocr_engine != "none",
        do_table_structure=not args.no_tables,
        generate_picture_images=True,
    )
    pipeline_options.table_structure_options = TableStructureOptions()
    pipeline_options.table_structure_options.do_cell_matching = True

    ocr_options = build_ocr_options(args.ocr_engine)
    if ocr_options is not None:
        pipeline_options.ocr_options = ocr_options

    return DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def ensure_paths(args: argparse.Namespace) -> None:
    if not args.input_file.exists():
        raise FileNotFoundError(f"Input file not found: {args.input_file}")
    if args.input_file.suffix.lower() != ".pdf":
        raise ValueError("This sample pipeline is configured for PDF input files only.")

    if args.force_offline and not args.artifacts_path.exists():
        raise FileNotFoundError(
            "The artifacts directory does not exist. "
            "Download Docling models first or remove --force-offline."
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)


def main() -> None:
    args = parse_args()
    ensure_paths(args)

    converter = build_converter(args)
    result = converter.convert(str(args.input_file))
    doc = result.document

    stem = args.input_file.stem
    markdown_path = args.output_dir / f"{stem}.md"
    json_path = args.output_dir / f"{stem}.json"
    image_mode = ImageRefMode(args.image_mode)
    image_assets_dir = args.output_dir / "images" if image_mode == ImageRefMode.REFERENCED else None

    if image_mode == ImageRefMode.REFERENCED:
        doc.save_as_markdown(
            markdown_path,
            artifacts_dir=image_assets_dir,
            image_mode=image_mode,
        )
    else:
        markdown_path.write_text(
            doc.export_to_markdown(image_mode=image_mode),
            encoding="utf-8",
        )

    doc.save_as_json(
        json_path,
        artifacts_dir=image_assets_dir,
        image_mode=image_mode,
        indent=2,
        coord_precision=2,
    )

    print(f"Input: {args.input_file}")
    print(f"Artifacts: {args.artifacts_path}")
    print(f"Markdown: {markdown_path}")
    print(f"JSON: {json_path}")


if __name__ == "__main__":
    main()
