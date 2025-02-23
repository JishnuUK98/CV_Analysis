import pytest
import sys
import os

# Ensure the test script finds cv_analysis.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cv_analysis  # Explicitly import cv_analysis.py

# Define test file paths
TEST_DIR = os.path.abspath(os.path.dirname(__file__)) + "/sample_files/"
TEST_PDF = os.path.join(TEST_DIR, "sample_cv.pdf")
TEST_DOCX = os.path.join(TEST_DIR, "sample_cv.docx")
TEST_IMAGE = os.path.join(TEST_DIR, "sample_cv.png")

# Test extracting text from PDF
def test_extract_text_from_pdf():
    assert os.path.exists(TEST_PDF), f"Test file not found: {TEST_PDF}"
    text = cv_analysis.extract_text_from_pdf(TEST_PDF)
    assert isinstance(text, str)
    assert len(text) > 0

# Test extracting text from Word
def test_extract_text_from_word():
    assert os.path.exists(TEST_DOCX), f"Test file not found: {TEST_DOCX}"
    text = cv_analysis.extract_text_from_word(TEST_DOCX)
    assert isinstance(text, str)
    assert len(text) > 0

# Test PDF to Image Conversion
def test_convert_pdf_to_images():
    assert os.path.exists(TEST_PDF), f"Test file not found: {TEST_PDF}"
    images = cv_analysis.convert_pdf_to_images(TEST_PDF)
    assert isinstance(images, list)
    assert len(images) > 0

# Test OCR on Image
def test_extract_text_from_image():
    assert os.path.exists(TEST_IMAGE), f"Test file not found: {TEST_IMAGE}"
    text = cv_analysis.extract_text_from_image(TEST_IMAGE)
    assert isinstance(text, str)
    assert len(text) > 0
