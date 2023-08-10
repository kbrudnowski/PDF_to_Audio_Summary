# PDF to Audio Converter and Summarizer

The **PDF to Audio Converter and Summarizer** is a Python application that allows you to convert PDF files into audio format and generate summarized versions of the content. This tool utilizes the tkinter library for creating a graphical user interface (GUI) and leverages other Python libraries such as pyttsx3, PyPDF2, summarize, and Selenium to facilitate the conversion process.

## Features

- **Drag and Drop PDF Upload:** The application provides an intuitive drag and drop area where you can easily upload your PDF files.

- **Text Extraction:** The uploaded PDF file is processed to extract text content from each page. The extracted text is then used as the source for audio conversion.

- **Full and Summarized Audio Generation:** You have the option to generate two types of audio:
  - Full Version: Converts the entire extracted text into audio.
  - Summarized Version: Utilizes the summarize library to create a summarized version of the text before converting it into audio.

- **Customizable Voice Settings:** You can adjust the voice settings such as voice type, speed rate, and volume to personalize the audio output.

- **File Saving:** The generated audio files are saved in the "Downloads" directory with appropriate file names indicating the source PDF file and whether it's a full or summarized version.

## Summarizer Module

The **Summarizer** module is an integral part of the PDF to Audio Converter and Summarizer application. It uses the Selenium library to interact with the summarizer.org website for text summarization.

Please note that the `Summarizer` class interacts with an external website, and changes to the website could impact functionality.

## Clone and Run

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone https://github.com/your-username/PDF_to_Audio_Summary.git`.

2. **Navigate to the Directory:**
   - Change your working directory to the cloned repository using `cd PDF_to_Audio_Summary`.

3. **Install Dependencies:**
   - Install the required libraries by running `pip install -r requirements.txt`.

4. **Running the Application:**
   - Execute the script using `python main.py` in the command line.
   - The application window will appear.

5. **Generating Audio:**
   - After uploading a PDF file, you can generate audio:
     - Click "Download Full Version" to generate audio from the full text.
     - Click "Download Summarized Version" to generate audio from a summarized version.

6. **Customizing Voice Settings:**
   - Customize voice settings (voice type, speed rate, volume) by modifying constants in the script (`VOICE_ID`, `VOICE_SPEED_RATE`, `VOICE_VOLUME`).

7. **File Saving:**
   - Generated audio files are saved in the "Downloads" directory, with file names indicating source PDF and version.

## Notes

- This application is based on the Python tkinter library, providing a graphical user interface for easy interaction.
- The application extracts text content from each page of the uploaded PDF using the PyPDF2 library.
- Summarization of text uses the summarize library, and it relies on external automation through Selenium.
- Audio generation is handled by the pyttsx3 library, allowing customization of voice settings.
- The application provides an easy way to convert PDF files into audio for greater accessibility.

