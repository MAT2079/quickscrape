import tkinter as tk
from tkinter import ttk
from threading import Thread

from .scraper import scrape_to_markdown

class QuickScrapeGUI(tk.Tk):
    """Basic GUI skeleton for QuickScrape."""

    def __init__(self):
        super().__init__()
        self.title("QuickScrape")
        self.geometry("400x200")
        self._create_widgets()

    def _create_widgets(self):
        url_label = ttk.Label(self, text="URL to scrape:")
        url_label.pack(pady=(10, 0))
        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack()

        file_label = ttk.Label(self, text="Output file name:")
        file_label.pack(pady=(10, 0))
        self.file_entry = ttk.Entry(self, width=50)
        self.file_entry.pack()

        run_button = ttk.Button(self, text="Run", command=self.run_scraper)
        run_button.pack(pady=(10, 0))

        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(self, textvariable=self.status_var)
        status_label.pack(pady=(10, 0))

    def run_scraper(self):
        """Run the scraper in a background thread."""
        self.status_var.set("Running...")
        url = self.url_entry.get()
        filename = self.file_entry.get()

        def _task():
            try:
                scrape_to_markdown(url, filename)
                self.status_var.set("Done")
            except Exception as exc:
                self.status_var.set(f"Error: {exc}")

        Thread(target=_task, daemon=True).start()


def main():
    app = QuickScrapeGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
