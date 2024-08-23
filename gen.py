import markdown
import sys
import os
from datetime import datetime

def markdown_to_html(md_content, title, copyright_name):
    # Convert Markdown to HTML with extensions
    html_content = markdown.markdown(md_content, extensions=[
        'markdown.extensions.fenced_code',
        'markdown.extensions.tables',
        'markdown.extensions.footnotes',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.codehilite'
    ])

    # Define the CSS for the new layout and color scheme, including hyperlinks
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        html, body {
            height: 100%;
            margin: 0;
            overflow-x: hidden; /* Prevent horizontal scrolling */
            padding: 0;
        }
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #1a202c;
            color: #e2e8f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 0 15px; /* Add padding to prevent content from touching edges */
            box-sizing: border-box;
        }
        .container {
            max-width: 900px;
            width: 100%;
            padding: 20px;
            box-sizing: border-box;
            background-color: #2d3748;
            border-radius: 8px;
            color: #e2e8f0;
            text-align: left;
            margin: 20px 0;
            overflow-y: auto;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #edf2f7;
        }
        code {
            background-color: #4a5568;
            padding: 2px 4px;
            border-radius: 4px;
            color: #e2e8f0;
        }
        pre {
            background-color: #4a5568;
            padding: 10px;
            border-radius: 4px;
            overflow: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #4a5568;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #2d3748;
        }
        tr:nth-child(even) {
            background-color: #2d3748;
        }
        blockquote {
            border-left: 4px solid #4a5568;
            padding: 10px 20px;
            margin: 20px 0;
            background-color: #2d3748;
            color: #e2e8f0;
            font-style: italic;
        }
        a {
            color: #ffffff; /* White color for links */
            text-decoration: underline; /* Underline links */
        }
        a:hover {
            color: #e2e8f0; /* Light color for links on hover */
        }
        input[type="checkbox"] {
            margin-right: 5px;
        }
        hr {
            border: 0;
            height: 1px;
            background: #4a5568;
            margin: 20px 0;
        }
        footer {
            padding: 10px;
            font-size: 0.8em;
            color: #e2e8f0;
            background-color: #2d3748;
            border-top: 1px solid #4a5568;
            text-align: center;
        }
    </style>
    """

    # Generate timestamp with hour and seconds
    timestamp = datetime.now().strftime('%B %d, %Y at %H:%M:%S')

    # Construct the final HTML
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        {css}
    </head>
    <body>
        <div class="container">
            {html_content}
            <footer>
                <p>Copyright {copyright_name} &copy; {datetime.now().year}. Generated on {timestamp} with PageCraft</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return html

def main():
    if len(sys.argv) not in [2, 3]:
        print("Usage: python script.py <markdown_file> [copyright_name]")
        sys.exit(1)

    md_file = sys.argv[1]
    if not os.path.isfile(md_file):
        print(f"File {md_file} does not exist.")
        sys.exit(1)

    copyright_name = sys.argv[2] if len(sys.argv) == 3 else 'PageCraft'

    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    title = os.path.splitext(os.path.basename(md_file))[0]
    html_content = markdown_to_html(md_content, title, copyright_name)

    output_file = f"{title}.html"
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"HTML file generated: {output_file}")

if __name__ == "__main__":
    main()
