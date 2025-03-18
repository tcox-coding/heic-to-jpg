import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter import filedialog
import os
from PIL import Image

from pillow_heif import register_heif_opener
register_heif_opener()

class HeicToJpgConverter:
    def __init__(self):
        self.WIDTH = 400
        self.HEIGHT = 400
        self.main_window = tk.Tk()
        self.main_window.config(
            width=self.WIDTH,
            height=self.HEIGHT,
            padx=100,
            pady=50
        )
        self.main_window.title("Heic to Jpg Converter")

        # Label for saying the directory of the HEIC files
        self.label = ttk.Label(
            self.main_window,
            text="Directory of HEIC Files"
        )
        self.label.pack()

        # Choose Directory Button
        self.button_open = ttk.Button(
            self.main_window,
            text="Choose Directory of HEIC Files",
            command=self.open_file,
            padding=10
        )
        self.button_open.pack()

        # Progress Bar
        self.pb = ttk.Progressbar(
            self.main_window,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        self.pb.pack(pady=10)

        # Convert Button
        self.button_convert = ttk.Button(
            self.main_window,
            text="Convert",
            command=self.convert,
            padding=10
        )
        self.button_convert.pack()

        self.main_window.mainloop()

    '''Convert all the HEIC files in the directory to JPG'''
    def convert(self):
        if not self.filename:
            print("No file selected")
            return
        print("Converting HEIC files to JPG")
        self.pb['value'] = 0
        self.pb['maximum'] = 100
        self.pb.step(10)

        # Get all the files in the directory
        os.chdir(self.filename)

        # Check if the file is HEIC
        # List all the files of the current directory
        files = os.listdir(self.filename)
        cur_progress = 100/len(files)
        print(files)
        for i, file in enumerate(files):
            print(i, file)
            cur_progress += 100/len(files)
            self.pb.step(cur_progress)
            self.pb.update()
            self.pb.update_idletasks()
            if file.endswith(".heic") or file.endswith(".HEIC"):
                file_path = os.path.join(self.filename, file)
                print(file_path)
                
                # Convert HEIC to a PIL Image
                image = Image.open(file_path)
                
                # Save the image as JPG
                print(file_path.strip(".heic") + ".jpg")
                image.save(file_path.strip(".heic") + ".jpg")


        # Convert the files to JPG
        # Save the files in the same directory
        # Update the progress bar



    def open_file(self):
        self.filename = filedialog.askdirectory() # show an "Open" dialog box and return the path to the selected file
        print(self.filename)
        self.label.config(text=self.filename)

if __name__ == "__main__":
    HeicToJpgConverter()