from gtts import gTTS
import PyPDF2
from tkinter.filedialog import askopenfilename
import tkinter as tk
import os

# Initialize Tkinter root window (needed for file dialog)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open file dialog to select a PDF file
book = askopenfilename(filetypes=[("PDF files", "*.pdf")])
if not book:
    print("Invalid file.")
    exit()

try:
    # Open and read the selected PDF file
    with open(book, 'rb') as file:
        pdfReader = PyPDF2.PdfReader(file)
        numPages = len(pdfReader.pages)

        # Read and speak each page
        for num in range(numPages):
            page = pdfReader.pages[num]
            text = page.extract_text()
            if text:
                tts = gTTS(text=text, lang='en')
                tts.save("temp.mp3")
                os.system("afplay temp.mp3")  # macOS command to play audio
                os.remove("temp.mp3")
            else:
                print(f"Page {num + 1} is empty or could not be read.")
except Exception as e:
    print(f"An error occurred: {e}")
