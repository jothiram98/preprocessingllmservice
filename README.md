# Docling local pipeline test

This workspace contains a minimal Docling pipeline for testing local document processing with local model artifacts.

## 1. Install dependencies into the active virtual environment

```bash
python -m pip install -r requirements.txt
```

Docling installation guidance:

- The Docling docs say the base install is `pip install docling`.
- For local/offline usage, the docs recommend prefetching models and passing `artifacts_path` or `DOCLING_ARTIFACTS_PATH`.
- On macOS, `OcrMacOptions` is a supported OCR engine for local OCR.

Sources:

- [Installation](https://docling-project.github.io/docling/getting_started/installation/)
- [Quickstart](https://docling-project.github.io/docling/getting_started/quickstart/)
- [Advanced options](https://docling-project.github.io/docling/usage/advanced_options/)

## 2. Download the local Docling models

After Docling is installed, prefetch models:

```bash
.venv/bin/docling-tools models download --output-dir models/docling
```

The installed `docling-tools` CLI supports `--output-dir`, so this keeps the local model cache inside the project.

You can then either:

- point the script to `models/docling` with `--artifacts-path models/docling`
- or export `DOCLING_ARTIFACTS_PATH="$PWD/models/docling"`
- or use the Docling default cache path if you prefer a shared cache

If you want the script to enforce offline mode, pass `--force-offline`.

## 3. Run the sample pipeline

Use a local PDF file:

```bash
python scripts/local_docling_pipeline.py /absolute/path/to/document.pdf \
  --artifacts-path models/docling \
  --output-dir outputs \
  --force-offline \
  --image-mode embedded
```

Outputs:

- `outputs/<filename>.md`
- `outputs/<filename>.json`

## Notes

- The script keeps `enable_remote_services=False`, so it stays on local execution for document processing.
- OCR now defaults to `rapidocr` for cross-platform consistency; use `--ocr-engine ocrmac` if you specifically need that engine on macOS or `--ocr-engine easyocr` when you want EasyOCR.
- By default the script embeds extracted page/diagram thumbnails into the Markdown/JSON outputs (`--image-mode embedded`). Pass `--image-mode referenced` to release each image into `outputs/images/` (and let the Markdown link to that file) or `--image-mode placeholder` if you just want the document outline without image stubs.

## Generate RAG chunks

Once you have the JSON output from Docling you can feed it into a vector database with another helper:

```bash
.venv/bin/python scripts/extract_rag_chunks.py \
  outputs/Update_Country_Code_Template_embedded.json \
  --output outputs/Update_Country_Code_Template_chunks.jsonl \
  --max-chars 1200 \
  --save-images
```

- `Update_Country_Code_Template_chunks.jsonl` contains text chunks plus picture records (with OCR captions for each screenshot). Each line is a JSON object that you can embed, store metadata from, or trace back to `source` + `page`.
- `--save-images` writes the base64 images embedded in the JSON into `outputs/chunks_images/picture-#.png`, giving you a PNG to inspect if you want to embed image data or show the screenshot alongside the vector chunk.

## Create annotated DOCX

- If you want a DOCX that mirrors the PDF and keeps the screenshot captions/descriptions, run:

```bash
.venv/bin/python scripts/docling_to_docx.py \
  outputs/Update_Country_Code_Template_embedded.json \
  --output outputs/Update_Country_Code_Template.docx \
  --image-width 5
```

- The script walks `doc.body`, writes each text block into the DOCX, inserts each picture as a PNG, and prefixes the embedded screenshot with “Screenshot description:” plus the OCR text extracted from the figure.
- You can open `outputs/Update_Country_Code_Template.docx` to verify that every image and its description are preserved in the same order as the original document.
- If your PDF already contains selectable text, you can skip OCR with `--ocr-engine none`.
- If you want a simpler first pass, disable table extraction with `--no-tables`.

## Create placeholder DOCX with Hugging Face

When your product only needs to keep the image path plus an HF-generated description (rather than embedding the PNG), run:

```bash
.venv/bin/python scripts/image_placeholder_docx.py \
  outputs/Update_Country_Code_Template_embedded.json \
  --output outputs/Update_Country_Code_Template_placeholders.docx \
  --image-dir outputs/extracted_images \
```

- Each PictureItem is saved into `outputs/extracted_images/picture-#.png`; the helper resizes the PNG, encodes it, and posts it to Hugging Face’s `meta-llama/llama-4-scout-17b-16e-instruct` multimodal endpoint along with the instruction “Describe the contents...”.
- The DOCX is generated in document order; paragraphs stay where they were, and each time an image occurs it emits `Image: outputs/extracted_images/picture-#.png` followed by `Description: <HF text>`.
- Set `HUGGINGFACE_API_TOKEN` inside `.env` before running so the request can authenticate, and watch the console as each description arrives if you want to see the text in real time.
```

The script sends each PictureItem to Hugging Face’s `Qwen2.5-VL-7B-Instruct` endpoint with the prompt “Describe the contents of this screenshot in a concise sentence.”  
The DOCX is generated in document order, inserting `Image: outputs/extracted_images/picture-#.png` followed by `Description: ...` (the HF response) whenever an image appears.  
Ensure `HUGGINGFACE_API_TOKEN` is set in `.env` (the repo ships one for local experimentation) so the HTTP request can authenticate.

You can quickly verify the Hugging Face API is reachable by running:

```bash
.venv/bin/python scripts/test_hf_connection.py \
  --model https://api-inference.huggingface.co/models/microsoft/trocr-base-printed \
  --image outputs/extracted_images/picture-1.png
```

- The repository already ships a `.env` file with the API key (for local experimentation); make sure you never commit a production key and prefer secrets managers for deployed runs.


The repository includes a `.env` with `HUGGINGFACE_API_TOKEN` for local runs; replace it with your own secret or wire in a secret manager before deploying.
