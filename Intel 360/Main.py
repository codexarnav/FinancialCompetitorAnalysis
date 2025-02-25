# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 01:32:51 2025

@author: arnav
"""

import streamlit as st
import PyPDF2
import torch

import json
import spacy
import google.generativeai as genai
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering

# Configure Gemini API
genai.configure(api_key="AIzaSyCyIBJGvOp0s5BFUjF4rsbchYcXeorsIeU")

# Function to extract text from PDF files
def extract_text_from_pdfs(pdf_files):
    extracted_text = ""
    for pdf in pdf_files:
        reader = PyPDF2.PdfReader(pdf)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
    return extracted_text.strip()

# Function to summarize text using BART
def summarize_text(text):
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs.input_ids, max_length=200, min_length=40, length_penalty=2.0, num_beams=4)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True).strip()

# Function for Question Answering
def question_answering(summary, question):
    tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
    nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

    QA_input = {"question": question, "context": summary}
    res = nlp(QA_input)
    return res["answer"]

# Function to extract named entities
def extract_entities(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        if ent.text not in entities[ent.label_]:
            entities[ent.label_].append(ent.text)
    return entities

# Function to predict business trends using Gemini AI
def predict_trends(text):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    Based on the following extracted text from a competitor analysis document:
    {text[:5000]} 
    Predict key business trends including:
    - Market Positioning
    - Strengths
    - Weaknesses
    - Business Opportunities
    Provide structured insights.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

# Function to process multiple quarterly reports
def process_quarterly_reports(pdf_files):
    cumulative_entities = {}
    cumulative_trends = ""
    report_results = {}

    for pdf_file in pdf_files:
        text = extract_text_from_pdfs([pdf_file])
        if text:
            entities = extract_entities(text)
            trends = predict_trends(text)
            summary = summarize_text(text)

            report_results[pdf_file.name] = {
                "entities": entities,
                "trends": trends,
                "summary": summary
            }

            for key, values in entities.items():
                cumulative_entities.setdefault(key, set()).update(values)

            cumulative_trends += f"Report: {pdf_file.name}\n{trends}\n\n"

    cumulative_analysis = {
        "entities": {k: list(v) for k, v in cumulative_entities.items()},
        "overall_trends": cumulative_trends.strip()
    }

    return {"quarterly_reports": report_results, "cumulative_analysis": cumulative_analysis}

# Streamlit UI Implementation
st.set_page_config(page_title="Competitor Analysis Dashboard", layout="wide")
st.title("📊 AI-Driven Competitor Analysis")

# Sidebar for File Uploads
st.sidebar.header("Upload Quarterly Reports")
uploaded_files = st.sidebar.file_uploader("Upload PDFs", accept_multiple_files=True, type=["pdf"])

if uploaded_files:
    st.sidebar.success("Files uploaded successfully!")
    results = process_quarterly_reports(uploaded_files)

    # Tabs for UI Experience
    tab1, tab2 = st.tabs(["📄 Individual Reports", "📌 Cumulative Analysis"])

    with tab1:
        for pdf_file in uploaded_files:
            st.subheader(f"📑 Report: {pdf_file.name}")
            st.write("**Extracted Entities:**", results["quarterly_reports"][pdf_file.name]["entities"])
            st.write("**Predicted Trends:**")
            st.text_area("", results["quarterly_reports"][pdf_file.name]["trends"], height=150)
            st.write("**Summary:**")
            st.text_area("", results["quarterly_reports"][pdf_file.name]["summary"], height=150)

    with tab2:
        st.header("📌 Cumulative Analysis")
        st.write("**Overall Extracted Entities:**", results["cumulative_analysis"]["entities"])
        st.write("**Overall Predicted Trends:**")
        st.text_area("", results["cumulative_analysis"]["overall_trends"], height=200)

    # Question Answering Section
    st.sidebar.subheader("🔍 Ask Questions on Summary")
    question = st.sidebar.text_input("Enter your question:")
    if question:
        answer = question_answering(results["cumulative_analysis"]["overall_trends"], question)
        st.sidebar.write("**Answer:**", answer)

    # Download Button
    st.sidebar.download_button(
        label="📥 Download Cumulative Analysis",
        data=json.dumps(results["cumulative_analysis"], indent=4),
        file_name="cumulative_analysis.json",
        mime="application/json"
    )

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Built for the Hackathon 🚀")

