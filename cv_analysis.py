import os
import pdfplumber
import pytesseract
import cv2
import fitz
import docx
import numpy as np
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

def extract_text_from_word(docx_path):
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"File not found: {docx_path}")
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def convert_pdf_to_images(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    return convert_from_path(pdf_path)

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text
