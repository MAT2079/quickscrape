# quickscrape

A simple tool to scrape web pages. This repository currently contains a 
skeleton application with a basic graphical user interface. The GUI allows
you to specify a URL and the name of the file to save the results. A status
label reports the progress of the scraping process.

The scraping logic is **not** implemented yet. Future updates will add the
actual scraping functionality.

## Running the application

```bash
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
