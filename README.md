# Markdown to PDF Converter

![image](https://github.com/user-attachments/assets/ad78a697-20e0-483c-9e79-6337a0a24d1b)


A Jupyter Notebook tool that converts GitHub Markdown files to beautifully formatted PDF documents with a single click.

## 🌟 Features

- **GitHub Integration**: Direct conversion from GitHub Markdown URLs (both regular and raw formats)
- **Beautiful Formatting**: GitHub-styled rendering of Markdown including:
  - Headers and text formatting
  - Code blocks with syntax highlighting
  - Tables
  - Lists and blockquotes
  - Images
- **Interactive UI**: Simple web interface within Jupyter notebooks
- **PDF Preview**: Instant preview of generated PDF within the notebook
- **Flexible Output**: Custom naming and path options for output files

## 📋 Requirements

- Python 3.7+
- Jupyter Notebook or JupyterLab
- Required Python packages:
  - `requests`
  - `nbformat`
  - `weasyprint`
  - `markdown`
  - `Pygments`

## 🚀 Installation

1. First, make sure you have all the required packages:

```python
!pip install requests nbformat weasyprint markdown Pygments
```

2. Copy the script into a Jupyter notebook cell and run it.

## 🔍 How It Works

The tool follows these steps to convert Markdown to PDF:

1. **URL Processing**: Validates and processes GitHub URLs, converting regular URLs to raw format if needed
2. **Content Download**: Fetches the Markdown content from GitHub
3. **HTML Conversion**: Transforms Markdown to HTML with proper styling using Python's markdown library
4. **PDF Generation**: Renders the HTML to PDF using WeasyPrint
5. **Display**: Shows the generated PDF directly in the notebook

## 🛠️ Usage

### Using the UI

After running the code cell, a user interface will appear:

1. Enter the GitHub URL of the Markdown file in the first field
2. Optionally specify an output path for the PDF file
3. Click "Convert to PDF"
4. The PDF will be generated and displayed in the notebook

### Using the Function Directly

You can also use the `markdown_to_pdf()` function directly in your code:

```python
# Basic usage with default output name (derived from markdown filename)
markdown_to_pdf("https://github.com/username/repo/blob/master/README.md")

# Specify custom output path
markdown_to_pdf("https://github.com/username/repo/blob/master/README.md", "output.pdf")
```

## 📝 Function Reference

### `markdown_to_pdf(github_url, output_pdf_path=None)`

Converts a GitHub Markdown file to PDF.

**Parameters:**
- `github_url` (str): URL to the GitHub markdown file
- `output_pdf_path` (str, optional): Path where the PDF will be saved. If None, a default name will be created based on the markdown filename.

**Returns:**
- `str`: Path to the created PDF file, or None if an error occurred

## 🔄 Supported URL Formats

The tool accepts GitHub URLs in these formats:

- Regular GitHub URLs:
  ```
  https://github.com/username/repository/blob/branch/path/to/file.md
  ```

- Raw GitHub URLs:
  ```
  https://raw.githubusercontent.com/username/repository/branch/path/to/file.md
  ```

## 🎨 CSS Styling

The generated PDFs use a custom CSS style that mimics GitHub's markdown rendering, including:

- Font styles and sizes based on GitHub's design
- Proper spacing and margins
- Code block styling with syntax highlighting
- Table formatting
- Responsive image sizing

## ⚠️ Troubleshooting

### Common Issues

- **WeasyPrint Dependencies**: WeasyPrint might require additional system dependencies. Please refer to [WeasyPrint's installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation) for platform-specific instructions.

- **SSL Certificate Errors**: If you encounter SSL certificate errors when accessing GitHub, you might need to install or update your certificate authorities.

- **Rendering Issues**: Some complex Markdown elements might not render exactly as they do on GitHub. The tool aims for close approximation but may differ in some edge cases.

## 🔄 Limitations

- The tool cannot access private GitHub repositories without proper authentication
- Very large Markdown files may take longer to process
- Complex custom HTML within Markdown might not render perfectly
- Some GitHub-specific Markdown extensions may not be fully supported

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Future Enhancements

Potential improvements for future versions:

- Support for private GitHub repositories via authentication
- Batch processing of multiple Markdown files
- Additional styling options and themes
- Support for more Markdown extensions
- Direct upload of local Markdown files
