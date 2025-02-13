# PDF Splitter & Rotator

This Python script allows users to select a PDF file, rotate its pages, and split it into separate PDF files containing two consecutive pages each.

## Features
- **Select a PDF file** using a file dialog.
- **Rotate all pages** by a user-specified angle (0, 90, 180, 270 degrees).
- **Split the PDF** into separate files, each containing two consecutive pages.
- **Automatically saves** split PDFs into a designated folder.

## Requirements
Make sure you have Python installed along with the required dependencies:

```bash
pip install pymupdf
```

## Usage
Run the script using:

```bash
python pdf_splitter.py
```

### Steps:
1. A file dialog will open to **select a PDF file**.
2. Enter the **rotation angle** (0, 90, 180, or 270 degrees).
3. The script will **split** the PDF into pairs of pages and **rotate** them.
4. The split PDFs will be saved in the `split_pairs` folder.

## Example Output
If the selected PDF has 6 pages, the script creates:
- `pages_1-2.pdf` (rotated as specified)
- `pages_3-4.pdf` (rotated as specified)
- `pages_5-6.pdf` (rotated as specified)

## GitHub Repository
To clone this repository, use:

```bash
git clone https://github.com/m6wt/pdf-splitter.git
cd pdf-splitter
```

## License
This project is open-source and available under the MIT License.
