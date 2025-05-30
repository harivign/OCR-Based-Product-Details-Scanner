
# 🧾 OCR-Based Product Details Scanner

A Streamlit app that extracts text from product images using OCR and fetches product details from the Open Food Facts database.

## 🚀 Project Overview

This application lets users upload an image of a product (like a packaged food item). It then uses EasyOCR to extract readable text from the image, searches the Open Food Facts API with the extracted text, and displays detailed product information including:

- Product Name  
- Brand  
- Categories  
- Ingredients (English only)  
- Nutrition Facts (calories, fat, proteins, sugars, salt, etc.)

## 🛠️ Features

- Upload images (JPG, JPEG, PNG)
- OCR text extraction using EasyOCR
- Query Open Food Facts API for product details
- Display product details in a clean, user-friendly UI
- Handles network errors and missing data gracefully

## 🖥️ How to Run Locally

### Prerequisites

- Python 3.7+
- Git (optional, for cloning repo)

### Setup

1. Clone the repository (or download the code):

```bash
git clone https://github.com/yourusername/ocr-product-scanner.git
cd ocr-product-scanner
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## 📁 Project Structure

```
ocr-product-scanner/
├── app.py               # Main Streamlit application
├── requirements.txt     # Project dependencies
├── README.md            # This file
└── assets/              # (Optional) Folder for images or additional files
```
## 📋 Usage

1. Click **Browse files** or drag and drop an image of a product package.
2. The app will extract text from the image.
3. It will search the Open Food Facts database.
4. If found, detailed product information will be shown.

## ⚙️ Dependencies

- [Streamlit](https://streamlit.io/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Pillow (PIL)](https://python-pillow.org/)
- [Requests](https://requests.readthedocs.io/)
- [NumPy](https://numpy.org/)

## 🔧 Possible Improvements

- Improve OCR accuracy with better text filtering or language support
- Support multiple languages for ingredient extraction
- Cache API responses for faster repeated lookups
- Add manual product search fallback if OCR fails
- Enhance UI design and theming
- Add unit tests and error logging

## 📬 Contact

Created by K.Hari Vignesh  
Mail Id: harivignesh1662002@gmail.com  


Feel free to open issues or submit pull requests!

