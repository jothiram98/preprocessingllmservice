# Docling Local Pipeline

This workspace contains a local-first document processing pipeline built on Docling. It extracts document text, exports screenshots as image files, injects stubbed LLM image notes into Markdown, and generates a DOCX from the augmented Markdown.

## What the pipeline produces

When you run `scripts/unified_pipeline.py`, it creates:

- `<name>_document.json`: Docling structured export
- `<name>_read_llm.md`: base Markdown with referenced image tags
- `<name>_read_llm_augmented.md`: Markdown with an `LLM image note` inserted after each image tag
- `<name>_read_llm.docx`: DOCX generated from the augmented Markdown
- `images/`: extracted picture assets from the input file

This is designed for the workflow where screenshots are extracted locally first, then later passed to an OpenAI vision call by replacing the stub in `describe_image_with_llm(...)`.

## Install dependencies

Use the active virtual environment:

```bash
python -m pip install -r requirements.txt
```

## Download Docling models

Prefetch the local Docling artifacts into this repo:

```bash
.venv/bin/docling-tools models download --output-dir models/docling
```

You can then point the pipeline to `models/docling` with `--artifacts-path models/docling`.

If your virtual environment is already activated, the equivalent command is:

```bash
docling-tools models download --output-dir models/docling
```

## Expected folder layout

The unified pipeline works best with this structure:

```bash
Docling/
  scripts/
    unified_pipeline.py
  models/
    docling/
  outputs/
```

What matters:

- `scripts/unified_pipeline.py` is the main runner
- `models/docling/` stores the local Docling artifacts
- `outputs/` is where the pipeline writes `<name>_read_llm.md`, `<name>_read_llm_augmented.md`, `<name>_read_llm.docx`, `<name>_document.json`, and the extracted `images/`
- you can keep inputs at the repo root or pass any absolute path to the script

## Recommended settings

For your current product flow, the best validated setup is:

- `--ocr-engine none` for text-based PDFs and Office docs
- `--ocr-engine rapidocr` for scanned PDFs
- `--image-scale 2`
- `--verbose`

Why:

- OCR is not needed when screenshots are only being extracted as images and will later be sent to an LLM.
- `image-scale 2` improves extracted screenshot quality compared to the default scale.
- verbose logging shows the full processing flow and total elapsed time.

## Run the unified pipeline

Recommended command for PDF:

```bash
python scripts/unified_pipeline.py Update_Country_Code_Template.pdf --output-dir outputs/pipeline_ocr_off_hq --artifacts-path models/docling --ocr-engine none --image-scale 2 --verbose
```

Office documents use the same command shape:

```bash
python scripts/unified_pipeline.py sample.docx --output-dir outputs/sample_docx
python scripts/unified_pipeline.py sample.pptx --output-dir outputs/sample_pptx
python scripts/unified_pipeline.py sample.xlsx --output-dir outputs/sample_xlsx
```

What this does:

- parses the input file with Docling using the appropriate backend
- exports referenced images into `outputs/pipeline_ocr_off_hq/images/`
- writes `<name>_read_llm.md`
- scans `<name>_read_llm.md` for image tags
- calls `describe_image_with_llm(image_path)` as a stub
- writes `<name>_read_llm_augmented.md`
- generates `<name>_read_llm.docx`
- logs total processing time from start to finish

## How image notes work

The current implementation does not call any external LLM yet.

Instead, `scripts/unified_pipeline.py` contains:

- `describe_image_with_llm(image_path)`: stub function to replace later with your OpenAI vision call

Current behavior:

- finds each Markdown image tag
- resolves the local PNG path
- inserts a line like:

```markdown
*LLM image note:* Stub response for image_000001.png...
```

This keeps the note anchored to the same image location in the Markdown.

## Notes on chunking and embeddings

For RAG and embeddings, the current augmented Markdown structure is already usable because:

- each image note sits next to the correct image reference
- screenshots remain inside the right section context
- the surrounding headings and step text provide semantic grounding

Recommended embedding strategy:

- chunk by section or subsection heading
- keep the nearby image note in the same chunk or attach it as a sibling chunk
- store metadata such as:
  - `section`
  - `image_path`
  - `source_file`
  - `chunk_type`

Perfect visual placement is less important for embeddings than strong semantic grouping.

## Timing and quality

The unified pipeline logs:

- processing start configuration
- output locations
- total processing time

If image quality still needs improvement, try:

```bash
--image-scale 3
```

This will usually improve screenshot clarity further, but it will also increase processing time and memory usage.

## Future OpenAI integration point

When you are ready to connect OpenAI, replace the body of:

```python
describe_image_with_llm(image_path: Path) -> str
```

in `scripts/unified_pipeline.py`.

That is the only place you need to swap from stubbed behavior to the real vision API call.
