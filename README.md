# makdown_to_pdf_downloader

I've created a comprehensive Python script that converts a Markdown file from GitHub to PDF. This script is designed to run in a Jupyter notebook and includes a user-friendly interface.
Features of the Markdown to PDF Converter:

GitHub URL Processing:

Accepts both regular GitHub URLs (github.com/username/repo/blob/master/file.md) and raw GitHub URLs
Automatically converts regular GitHub URLs to raw format for downloading


Markdown Rendering:

Uses Python's markdown library with extensions for tables, code blocks, and other formatting
Applies GitHub-style CSS for a clean, professional appearance


PDF Conversion:

Utilizes WeasyPrint to convert HTML to PDF with proper styling
Preserves formatting, tables, code blocks, and other markdown elements


Interactive UI:

Provides a user-friendly interface right in the notebook
Allows specifying custom output file paths



How to Use:

Install Dependencies:
First, run this in a cell to install the required packages:
python!pip install requests nbformat weasyprint markdown Pygments

Run the Script:

Copy the code into a Jupyter notebook cell and run it
The UI will appear with input fields for the GitHub URL and output file path


Convert Your Markdown:

Enter the GitHub URL of your markdown file
Optionally specify an output path for the PDF
Click "Convert to PDF"


View Results:

The PDF will be displayed directly in the notebook
The file will also be saved to your specified location



Example Usage:
If you prefer to use the function directly in your code instead of the UI:
python# Convert from GitHub URL to PDF
markdown_to_pdf("https://github.com/username/repo/blob/master/README.md", "output.pdf")

# With default output filename (based on the markdown filename)
markdown_to_pdf("https://github.com/username/repo/blob/master/README.md")
