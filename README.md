# 📄 CV Analysis & Chatbot System

This project automates **CV analysis** by:
 Processing **multiple CVs** (PDF & DOCX)  
 Extracting **key information** (Personal Info, Education, Skills, Work Experience)  
 Using **OCR (Tesseract & pdfplumber)** for text extraction  
 **Storing structured CV data** for efficient querying  
 Integrating **LLM API (OpenAI GPT, Claude)** for smart analysis  
 Providing a **chatbot** to search for candidates by **skills, experience, and qualifications**  

---

## 🔹 **Project Features**
- **Document Processing:**  
  - Parses PDF & DOCX files  
  - Uses **OCR (Tesseract)** for scanned CVs  
  - Extracts **Name, Contact, Education, Experience, Skills, Certifications, Projects**  

- **LLM Integration:**  
  - Uses **Mistral AI** (or Claude) to analyze CVs  
  - Improves **candidate matching**  
  - Handles **API rate limits & errors gracefully**  

- **Chatbot Query System:**  
  - Supports **natural language queries**  
  - Can **find candidates** with **specific skills**  
  - Can **compare education levels**  
  - Can **search for industry experience**  
  - Supports **context-based follow-up questions**  

---

##  **Installation Guide**
### ** Clone the Repository**
```bash
git clone https://github.com/JishnuUK98/CV_Analysis.git
cd CV_Analysis

### ** Install Dependencies**

pip install -r requirements.txt


### ** Set Up API Keys**
This project requires LLM API keys (Mistral AI).
cp .env.example .env
OPENAI_API_KEY=your_api_key_here


### ** Process CVs and Extract Text**

from cv_analysis import process_cvs

# Process multiple CVs from a folder
cv_data = process_cvs("data/sample_cvs/")
print(cv_data)

### ** Query Candidate Information via Chatbot**

from chatbot import query_cv_data

response = query_cv_data("Find candidates with Python and Machine Learning experience")
print(response)


CV_Analysis/
│── cv_analysis.py         # Main script for extracting data from CVs
│── chatbot.py             # Chatbot interface for querying CV data
│── requirements.txt       # List of dependencies
│── .env.example           # Sample environment file
│── README.md              # Project documentation
│── data/
│   ├── sample_cvs/        # Sample CVs for testing
│   │   ├── sample_cv1.pdf
│   │   ├── sample_cv2.docx
│── tests/                 # Test folder
│   ├── test_cv_analysis.py    # Test cases
│   ├── __init__.py           # Init file for test folder


##  **Running Tests (Test Suite)**
This project includes unit tests for correctness.

pytest tests/

Expected output
=========================== test session starts ============================
collected 6 items
tests/test_cv_analysis.py .... ✅
tests/test_chatbot.py .... ✅



