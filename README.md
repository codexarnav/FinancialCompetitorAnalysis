# AI-Driven Competitor Analysis Dashboard

An AI-powered dashboard that analyzes competitor quarterly reports to extract insights, identify trends, and enable competitive intelligence through natural language processing.

## 🚀 Features

- **PDF Processing**: Extract text from uploaded quarterly reports and financial documents
- **Named Entity Recognition**: Identify companies, metrics, events, and business activities using customized NER
- **AI-Powered Trend Analysis**: Generate insights on market positioning, competitive strengths/weaknesses using Gemini AI
- **Document Summarization**: Create concise summaries of lengthy reports using BART models
- **Q&A Capabilities**: Ask questions about the analyzed data and receive answers based on the processed content
- **Cumulative Analysis**: Compare and consolidate findings across multiple documents
- **Downloadable Results**: Export insights in JSON format for further analysis

## 📋 Requirements

- Python 3.8+
- Libraries listed in `requirements.txt`
- Gemini API key
- Internet connection (for model downloads)

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/competitor-analysis-dashboard.git
   cd competitor-analysis-dashboard
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download required SpaCy model:
   ```bash
   python -m spacy download en_core_web_lg
   ```

5. Set up your Gemini API key:
   - Get an API key from [Google AI Studio](https://ai.google.dev/)
   - Either add it directly in the code (not recommended for production) or set it as an environment variable:
     ```bash
     export GEMINI_API_KEY="your-api-key-here"
     ```

## 🔧 Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload competitor reports in PDF format using the file uploader in the sidebar

4. View extracted entities, trends, and summaries for each report

5. Ask questions about the analysis in the sidebar's question input box

6. Download the cumulative analysis as a JSON file for further processing

## 📊 Example

```python
# Example programmatic usage
from src import extract_text_from_pdfs, extract_entities, predict_trends, summarize_text

# Process a single report
pdf_path = "examples/sample_report.pdf"
with open(pdf_path, "rb") as f:
    text = extract_text_from_pdfs([f])
    entities = extract_entities(text)
    trends = predict_trends(text)
    summary = summarize_text(text)

print("Entities found:", entities)
print("Summary:", summary)
```

## 📂 Project Structure

```
competitor-analysis-dashboard/
│
├── app.py                              # Main Streamlit application
├── requirements.txt                    # Dependencies
│
├── src/                                # Source code modules
│   ├── __init__.py                     # Package initialization
│   ├── text_extraction.py              # PDF processing
│   ├── entity_recognition.py           # NER functionality
│   ├── summarization.py                # Text summarization
│   ├── question_answering.py           # Q&A capabilities 
│   └── trend_prediction.py             # AI trend analysis
│
├── examples/                           # Example files
├── tests/                              # Test scripts
├── notebooks/                          # Development notebooks
└── docs/                               # Documentation
```

## ⚠️ Limitations

- PDF extraction may not handle all document formats perfectly
- AI predictions are based on available context and may require human validation
- Large documents may require significant processing time and memory
- API rate limits apply to the Gemini AI service

## 🔒 Security Note

- This application processes potentially sensitive business documents
- Ensure you have appropriate permissions to analyze competitor materials
- Do not expose your API keys in public repositories

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
