## 📄 Text Detection from Images or Webcam (Multilingual OCR)

This Python script allows users to extract text from an image or a live webcam feed using **Tesseract OCR**. The tool supports **multiple languages** (including Persian) and works entirely in the terminal — **no GUI is used**.


### ✅ **Features**

* Choose from **9 popular languages** for OCR (e.g., English, French, Arabic, Persian, etc.)
* Choose image input method:

  * 📷 Live capture from webcam
  * 🖼️ Load from an existing image file
* Uses `pytesseract` to detect text in the selected language
* Automatically copies the extracted text to the system clipboard
* Lightweight and **no graphical interface**

---

### 🚀 How It Works

1. The user selects one of the supported languages (by number).
2. The user chooses whether to:

   * Capture an image using their **webcam** (press `s` to save frame),
   * Or load an existing **image file**.
3. The script uses OpenCV to load or capture the image.
4. Tesseract OCR is used to detect and extract text.
5. The extracted text is:

   * Printed in the terminal
   * Automatically copied to the clipboard using `pyperclip`

---

### ⚙️ System Requirements

This script runs on:

* Windows
* macOS
* Linux (with OpenCV and Tesseract support)

#### ⚠️ Important: Tesseract OCR

You **must install Tesseract OCR** separately from the Python packages.

**For Windows:**

Download and install from this link (recommended version):
👉 [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

After installation, if Tesseract is **not in your PATH**, add this line to your script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

### 📦 Installation (Python Packages)

Before running the script, install the required Python packages:

```bash
pip install opencv-python pytesseract pyperclip
```

> Note: You may also need `pillow` in some environments.

---

### 📁 Language Support in Tesseract

To use specific languages (like **Persian**, **Arabic**, **Japanese**, etc.), you must install the corresponding trained language data files.

* Default Tesseract usually comes with `eng` only.
* For Persian (`fas`) and others, you may need to manually download them from:

  * [https://github.com/tesseract-ocr/tessdata](https://github.com/tesseract-ocr/tessdata)

Place the `.traineddata` files into your Tesseract `tessdata` folder (usually at `C:\Program Files\Tesseract-OCR\tessdata` on Windows).

---

### 🧪 Example Usage

```bash
python ocr_script.py
```

1. Select language (e.g., `1` for English)
2. Choose input method (`1` for webcam, `2` for file)
3. If webcam: Press `s` to take snapshot
4. Output appears in terminal and is copied to clipboard

---

### 🛠️ Future Improvements

* Save output to a `.txt` file
* Add a GUI (with PyQt or Tkinter)
* Support image preprocessing options (e.g., noise removal, thresholding)

