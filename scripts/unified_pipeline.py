from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import Any, Dict

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


LOG = logging.getLogger("unified_pipeline")


def configure_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def build_ocr_options(ocr_engine: str):
    if ocr_engine == "none":
        return None
    if ocr_engine == "rapidocr":
        return RapidOcrOptions()
    if ocr_engine == "ocrmac":
        return OcrMacOptions()
    if ocr_engine == "easyocr":
        return EasyOcrOptions(download_enabled=False)
    if ocr_engine == "auto":
        return RapidOcrOptions()
    return None


def build_converter(args: argparse.Namespace) -> DocumentConverter:
    accelerator_options = AcceleratorOptions(device=AcceleratorDevice(args.device))

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
    if ocr_options:
        pipeline_options.ocr_options = ocr_options

    return DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )


def run_docling(args: argparse.Namespace) -> Path:
    converter = build_converter(args)
    result = converter.convert(str(args.input_pdf))
    doc = result.document

    args.output_dir.mkdir(parents=True, exist_ok=True)
    image_dir = args.output_dir / "images"
    markdown_path = args.output_dir / "read_llm.md"
    json_path = args.output_dir / "document.json"

    LOG.info("Saving JSON to %s", json_path)
    doc.save_as_json(
        json_path,
        artifacts_dir=image_dir,
        image_mode=ImageRefMode.REFERENCED,
        indent=2,
        coord_precision=2,
    )

    LOG.info("Saving LLM-ready markdown to %s", markdown_path)
    doc.save_as_markdown(
        markdown_path,
        artifacts_dir=image_dir,
        image_mode=ImageRefMode.REFERENCED,
    )
    return markdown_path


def build_llm_stub(markdown_path: Path) -> Dict[str, Any]:
    prompt_preview = markdown_path.read_text(encoding="utf-8")[:800]
    return {
        "message": "LLM call not executed (stub). Plug in OpenAI or Groq here.",
        "prompt_preview": prompt_preview,
        "markdown_path": str(markdown_path),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="One-shot Docling pipeline with LLM-ready Markdown output.")
    parser.add_argument("input_pdf", type=Path, help="Path to the PDF to process.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("outputs/pipeline"),
        help="Folder for JSON, markdown, and extracted images.",
    )
    parser.add_argument(
        "--artifacts-path",
        type=Path,
        default=Path("models/docling"),
        help="Local Docling model artifacts directory.",
    )
    parser.add_argument(
        "--ocr-engine",
        choices=["rapidocr", "ocrmac", "easyocr", "none", "auto"],
        default="rapidocr",
        help="OCR engine for scanned PDFs. Use none to disable.",
    )
    parser.add_argument(
        "--device",
        choices=["auto", "cpu", "mps", "cuda", "xpu"],
        default="auto",
        help="Inference device.",
    )
    parser.add_argument("--no-tables", action="store_true", help="Disable table structure extraction.")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logging(args.verbose)
    try:
        if not args.input_pdf.exists():
            raise FileNotFoundError(f"Input PDF not found: {args.input_pdf}")
        LOG.info("Processing %s", args.input_pdf)
        md_path = run_docling(args)
        llm_stub = build_llm_stub(md_path)
        LOG.info("Pipeline complete. Markdown ready at %s", md_path)
        LOG.debug("LLM stub response: %s", llm_stub)
    except Exception as exc:  # noqa: BLE001
        LOG.exception("Pipeline failed: %s", exc)
        raise


if __name__ == "__main__":
    main()
