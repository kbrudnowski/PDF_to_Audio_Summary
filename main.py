import tkinter as tk
from tkinter import ttk, filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
import pyttsx3
from PyPDF2 import PdfReader
import os
from summarize import Summarizer
import unicodedata

WINDOW_X = 500
WINDOW_Y = 550
VOICE_ID = 1
VOICE_SPEED_RATE = 155
VOICE_VOLUME = .75


class FileConverter:
    def __init__(self, root):
        # UI
        self.root = root
        self.root.title("PDF to audio")
        self.root.geometry(f"{WINDOW_X}x{WINDOW_Y}")

        style = ttk.Style()
        style.configure("TButton", padding = 10, font = ("Helvetica", 12))

        self.upload_frame = tk.Frame(root, bg = "#f0f0f0")
        self.upload_frame.pack(fill = "both", expand = True, padx = 20, pady = (40, 0))

        self.upload_label = tk.Label(
            self.upload_frame, text = "Drag and drop a PDF file here:", font = ("Helvetica", 14), wraplength = 450
        )
        self.upload_label.pack()

        self.upload_icon = tk.PhotoImage(file = "upload_icon.png").subsample(5, 5)
        self.upload_label_img = tk.Label(self.upload_frame, image = self.upload_icon, bg = "#f0f0f0")
        self.upload_label_img.pack()

        self.upload_button = ttk.Button(root, text = "Upload File", command = self.upload_file)
        self.upload_button.pack(pady = (0, 20), padx = 20, fill = "x")

        self.full_download_button = ttk.Button(
            root, text = "Download Full Version", command = lambda: self.make_audio(self.text)
        )
        self.full_download_button.pack(pady = 10, padx = 20, fill = "x")

        self.summary_download_button = ttk.Button(
            root, text = "Download Summarized Version", command = self.summarized_audio
        )
        self.summary_download_button.pack(pady = (0, 20), padx = 20, fill = "x")

        # center tk window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{WINDOW_X}x{WINDOW_Y}+{(screen_width - WINDOW_X) // 2}+{(screen_height - WINDOW_Y) // 2}")

        # drag and drop event listener
        self.drop_target = root
        self.drop_target.drop_target_register(DND_FILES)
        self.drop_target.dnd_bind('<<Drop>>', self.upload_file)

        # initialize variables
        self.file_path = None
        self.text = ""
        self.summary = ""

    # deal with uploaded files
    def upload_file(self, event=None):
        if event:
            self.file_path = event.data
        else:
            self.file_path = filedialog.askopenfilename(filetypes = [("All Files", "*.*")])

        self.upload_label.config(text = "File uploaded: " + self.file_path.split('/')[-1])
        self.read_pdf()

    # convert pdf into text
    def read_pdf(self):
        # clear 'text' content
        self.text = ""
        if self.file_path.split('.')[-1] == 'pdf':
            reader = PdfReader(self.file_path)
            page_number = 1
            for page in reader.pages:
                self.text += f'\npage {page_number}\n'
                self.text += page.extract_text()
                page_number += 1

            self.text = ''.join(c for c in unicodedata.normalize('NFC', self.text) if c <= '\uFFFF')

            print(self.text)

    def summarized_audio(self):
        summ_instance = Summarizer(self.text)
        self.summary = summ_instance.summarized_text
        self.make_audio(self.summary)

    def make_audio(self, source_text):
        engine = pyttsx3.init()

        # voice settings
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[VOICE_ID].id)
        engine.setProperty('rate', VOICE_SPEED_RATE)
        engine.setProperty('volume', VOICE_VOLUME)

        # save audio file into 'Downloads'
        if source_text == self.summary:
            save_path = os.path.join(
                os.path.expanduser('~'), "Downloads", f"audio_summary_of_{self.file_path.split('/')[-1].split('.')[0]}.mp3"
            )
        else:
            save_path = os.path.join(
                os.path.expanduser('~'), "Downloads", f"audio_of_{self.file_path.split('/')[-1].split('.')[0]}.mp3"
            )

        # convert text to audio
        engine.save_to_file(source_text, save_path)
        engine.runAndWait()


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = FileConverter(root)
    root.mainloop()
