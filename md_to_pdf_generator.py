import requests
import os
import re
from urllib.parse import urlparse
import nbformat
from nbformat.v4 import new_notebook, new_code_cell
import weasyprint
from markdown import Markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
import tempfile
import base64
from IPython.display import IFrame, display, HTML
import warnings
warnings.filterwarnings("ignore")

def is_github_markdown_url(url):
    """Check if the URL is a GitHub raw markdown file or a regular GitHub file URL"""
    parsed_url = urlparse(url)
    
    # Check if it's a raw GitHub URL
    if parsed_url.netloc == 'raw.githubusercontent.com' and url.endswith('.md'):
        return True, url
    
    # Check if it's a regular GitHub URL and convert to raw if needed
    if parsed_url.netloc == 'github.com':
        path_parts = parsed_url.path.split('/')
        if len(path_parts) >= 5 and path_parts[3] == 'blob' and path_parts[-1].endswith('.md'):
            # Convert github.com URL to raw.githubusercontent.com URL
            raw_url = f"https://raw.githubusercontent.com/{path_parts[1]}/{path_parts[2]}/{'/'.join(path_parts[4:])}"
            return True, raw_url
    
    return False, url

def download_markdown_content(url):
    """Download markdown content from a GitHub URL"""
    is_github, raw_url = is_github_markdown_url(url)
    
    if not is_github:
        raise ValueError("The provided URL does not appear to be a valid GitHub markdown file URL")
    
    response = requests.get(raw_url)
    if response.status_code == 200:
        return response.text
    else:
        raise ValueError(f"Failed to download markdown content. Status code: {response.status_code}")

def markdown_to_html(markdown_content):
    """Convert markdown to HTML with proper styling"""
    # Use Python's markdown with extensions for better rendering
    md = Markdown(extensions=[
        'extra',
        TableExtension(),
        FencedCodeExtension(),
        CodeHiliteExtension(linenums=False, css_class='highlight'),
    ])
    
    html_content = md.convert(markdown_content)
    
    # Add CSS for proper styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 16px;
                line-height: 1.6;
                padding: 30px;
                color: #24292e;
                max-width: 900px;
                margin: 0 auto;
            }}
            h1, h2, h3, h4, h5, h6 {{
                margin-top: 24px;
                margin-bottom: 16px;
                font-weight: 600;
                line-height: 1.25;
            }}
            h1 {{ font-size: 2em; border-bottom: 1px solid #eaecef; padding-bottom: .3em; }}
            h2 {{ font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: .3em; }}
            h3 {{ font-size: 1.25em; }}
            h4 {{ font-size: 1em; }}
            p, blockquote, ul, ol, table {{ margin-bottom: 16px; }}
            code {{
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
                padding: 0.2em 0.4em;
                margin: 0;
                font-size: 85%;
                background-color: rgba(27, 31, 35, 0.05);
                border-radius: 3px;
            }}
            pre code {{
                display: block;
                padding: 16px;
                overflow: auto;
                font-size: 85%;
                line-height: 1.45;
                background-color: #f6f8fa;
                border-radius: 3px;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            table th, table td {{
                padding: 6px 13px;
                border: 1px solid #dfe2e5;
            }}
            table tr {{
                background-color: #fff;
                border-top: 1px solid #c6cbd1;
            }}
            table tr:nth-child(2n) {{
                background-color: #f6f8fa;
            }}
            img {{
                max-width: 100%;
                box-sizing: border-box;
            }}
            blockquote {{
                padding: 0 1em;
                color: #6a737d;
                border-left: 0.25em solid #dfe2e5;
            }}
            hr {{
                height: 0.25em;
                padding: 0;
                margin: 24px 0;
                background-color: #e1e4e8;
                border: 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    return styled_html

def html_to_pdf(html_content, output_file_path):
    """Convert HTML to PDF using WeasyPrint"""
    # Create a temporary HTML file
    with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_html:
        temp_html.write(html_content.encode('utf-8'))
        temp_html_path = temp_html.name
    
    # Convert HTML to PDF
    try:
        weasyprint.HTML(filename=temp_html_path).write_pdf(output_file_path)
        print(f"PDF created successfully: {output_file_path}")
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)

def display_pdf(file_path):
    """Display the PDF in the notebook"""
    # Define the width and height for the iframe
    width = 800
    height = 600
    
    # Display the PDF in an iframe
    display(IFrame(file_path, width=width, height=height))

def markdown_to_pdf(github_url, output_pdf_path=None):
    """
    Convert a GitHub Markdown file to PDF
    
    Parameters:
    github_url (str): URL to GitHub markdown file
    output_pdf_path (str, optional): Path where the PDF will be saved. 
                                    If None, a default name will be created.
    
    Returns:
    str: Path to the created PDF file
    """
    try:
        # Extract file name from URL for default output path
        if output_pdf_path is None:
            url_parts = urlparse(github_url).path.split('/')
            md_filename = url_parts[-1]
            base_name = os.path.splitext(md_filename)[0]
            output_pdf_path = f"{base_name}.pdf"
        
        print(f"Downloading Markdown from: {github_url}")
        md_content = download_markdown_content(github_url)
        
        print("Converting Markdown to HTML...")
        html_content = markdown_to_html(md_content)
        
        print(f"Converting HTML to PDF: {output_pdf_path}")
        html_to_pdf(html_content, output_pdf_path)
        
        # Display the PDF inline
        display_pdf(output_pdf_path)
        
        return output_pdf_path
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Example usage
markdown_to_pdf("https://github.com/aman-24052001/us_home_price_analysis_home_llc/blob/main/report.md", "output.pdf")

# Create a simple UI to run the conversion
def create_markdown_to_pdf_ui():
    html = """
    <div style="width: 100%; max-width: 800px; margin: 0 auto; padding: 20px; font-family: sans-serif;">
        <h2>GitHub Markdown to PDF Converter</h2>
        <div style="margin-bottom: 15px;">
            <label for="github_url" style="display: block; margin-bottom: 5px; font-weight: bold;">GitHub Markdown URL:</label>
            <input type="text" id="github_url" style="width: 100%; padding: 8px; box-sizing: border-box;" 
                placeholder="https://github.com/username/repo/blob/master/file.md">
        </div>
        <div style="margin-bottom: 15px;">
            <label for="output_path" style="display: block; margin-bottom: 5px; font-weight: bold;">Output PDF Path (optional):</label>
            <input type="text" id="output_path" style="width: 100%; padding: 8px; box-sizing: border-box;" 
                placeholder="Leave empty for default">
        </div>
        <button id="convert_button" style="padding: 10px 15px; background-color: #0366d6; color: white; border: none; border-radius: 4px; cursor: pointer;">
            Convert to PDF
        </button>
        <div id="result" style="margin-top: 20px;"></div>
    </div>
    
    <script>
    document.getElementById('convert_button').onclick = function() {
        var github_url = document.getElementById('github_url').value;
        var output_path = document.getElementById('output_path').value;
        
        if (!github_url) {
            document.getElementById('result').innerHTML = '<p style="color: red;">Please enter a GitHub Markdown URL</p>';
            return;
        }
        
        document.getElementById('result').innerHTML = '<p>Converting...</p>';
        
        // Send to Python
        var kernel = IPython.notebook.kernel;
        var command = `markdown_to_pdf("${github_url}"${output_path ? ', "' + output_path + '"' : ''})`;
        kernel.execute(command);
        
        // This doesn't give feedback, but at least starts the conversion
        document.getElementById('result').innerHTML = '<p>Conversion started. Check output below for progress.</p>';
    }
    </script>
    """
    display(HTML(html))

# Create the UI
create_markdown_to_pdf_ui()
