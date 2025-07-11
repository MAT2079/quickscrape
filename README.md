# quickscrape

A simple tool to scrape web pages. The application features a graphical user
interface that lets you specify a URL and an output file. A status label
reports progress while the scraper runs in a background thread.

The scraper downloads the web page, removes all HTML tags and saves the plain
text to a Markdown file. Required dependencies are listed in
`requirements.txt`.

## Running the application

```bash
pip install -r requirements.txt
python main.py
```

## Packaging as an executable

Once Python code is complete you can generate a Windows executable using
[PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

This will create a `dist/main.exe` file that runs the application without
requiring a Python installation.
