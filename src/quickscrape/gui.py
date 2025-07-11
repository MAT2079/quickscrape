import tkinter as tk
from tkinter import ttk

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
        """Placeholder for the scraping logic."""
        self.status_var.set("Running...")
        # TODO: implement scraping logic
        self.after(1000, lambda: self.status_var.set("Done"))


def main():
    app = QuickScrapeGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
