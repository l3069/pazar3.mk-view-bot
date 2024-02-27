# Author: Leonid Krstevski

# Опомена: Овој проект не е наменет за било какви сајбер нарушувања или незаконски цели. Авторот не носи одговорност за било каква злоупотреба на овој код.

import asyncio
import aiohttp
import time
import tkinter as tk
from tkinter import ttk
from threading import Thread
import webbrowser

async def refresh_url(url, num_refreshes, output_text):
    output_text.insert(tk.END, f"Се додаваат прегледи на страната: {url}\n\n")
    output_text.insert(tk.END, f"Прегледите започнаа\n\n")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_refreshes):
            task = asyncio.ensure_future(session.get(url))
            tasks.append(task)
        await asyncio.gather(*tasks)
    output_text.insert(tk.END, "Успешно\n\n")
    end_time = time.time()
    duration = end_time - start_time
    output_text.insert(tk.END, f"Вкупно време за додавање прегледи: {duration:.2f} секунди\n")
    output_text.insert(tk.END, f"Успешно додаено: {num_refreshes} прегледи\n")

def start_refresh(url_entry, num_refreshes_entry, output_text):
    global start_time
    start_time = time.time()

    url = url_entry.get()
    num_refreshes = int(num_refreshes_entry.get())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(refresh_url(url, num_refreshes, output_text))
    loop.close()

def run_refresh(url_entry, num_refreshes_entry, output_text):
    thread = Thread(target=start_refresh, args=(url_entry, num_refreshes_entry, output_text))
    thread.start()

def toggle_mode():
    if root.cget("bg") == "white":  # If currently in normal mode, switch to dark mode
        root.configure(bg="#303030")
        frame.configure(style="Dark.TFrame")
        start_button.configure(style="Dark.TButton")
        url_label.configure(style="Dark.TLabel")
        num_refreshes_label.configure(style="Dark.TLabel")
        output_text.configure(bg="#303030", fg="white")
    else:  # If currently in dark mode, switch to normal mode
        root.configure(bg="white")
        frame.configure(style="Normal.TFrame")
        start_button.configure(style="Normal.TButton")
        url_label.configure(style="Normal.TLabel")
        num_refreshes_label.configure(style="Normal.TLabel")
        output_text.configure(bg="white", fg="black")

if __name__ == "__main__":
    # Open the website when the application starts
    webbrowser.open("facebook.com")

    root = tk.Tk()
    root.title("Додавање на прегледи")
    root.configure(bg="white")  # Normal mode by default

    style = ttk.Style()
    style.theme_use('clam')  # Use 'clam' theme for ttk widgets

    frame = ttk.Frame(root, padding="10", style="Normal.TFrame")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    url_label = ttk.Label(frame, text="Вметни го линкот од pazar3.mk:", style="Normal.TLabel")
    url_label.grid(row=0, column=0, sticky=tk.W)

    url_entry = ttk.Entry(frame, width=50)
    url_entry.grid(row=1, column=0, padx=(0, 10), sticky=tk.W)

    num_refreshes_label = ttk.Label(frame, text="Внеси бројка на прегледи (Препорачливо 1-200):", style="Normal.TLabel")
    num_refreshes_label.grid(row=2, column=0, sticky=tk.W)

    num_refreshes_entry = ttk.Entry(frame)
    num_refreshes_entry.grid(row=3, column=0, padx=(0, 10), sticky=tk.W)

    start_button = ttk.Button(frame, text="Започни", command=lambda: run_refresh(url_entry, num_refreshes_entry, output_text), style="Normal.TButton")
    start_button.grid(row=4, column=0, pady=(10, 0))

    output_text = tk.Text(frame, width=60, height=15)
    output_text.grid(row=5, column=0, pady=(10, 0), sticky=(tk.W, tk.E))

    mode_button = ttk.Button(root, text="Промени стил", command=toggle_mode)
    mode_button.grid(row=1, column=0, pady=5, padx=5, sticky=tk.EW)

    # Centering the buttons below
    root.grid_columnconfigure(0, weight=1)

    # Add a label to display the author's name
    author_label = tk.Label(root, text="Автор: Leonid Krstevski", bg="white")
    author_label.grid(row=2, column=0, pady=(0, 10), sticky=tk.EW)

    style.configure("Normal.TFrame", background="white")
    style.configure("Normal.TLabel", background="white")
    style.configure("Normal.TButton", background="white")

    style.configure("Dark.TFrame", background="#303030", foreground="white")
    style.configure("Dark.TLabel", background="#303030", foreground="white")
    style.configure("Dark.TButton", background="#303030", foreground="black")

    # Adjust style map for the start button to prevent color change on hover
    style.map("Normal.TButton",
              background=[("active", "white"), ("!disabled", "white")],
              foreground=[("active", "#000000")])

    root.mainloop()
    # Author: Leonid Krstevski
