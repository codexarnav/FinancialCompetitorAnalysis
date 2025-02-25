# -*- coding: utf-8 -*-
"""
AI-Driven Competitor Analysis Dashboard
Python package initialization file

This package contains modules for processing quarterly reports, extracting insights,
and analyzing competitor data using various NLP and AI techniques.
"""

__version__ = '0.1.0'
__author__ = 'arnav'

# Import key functions to make them available directly from the package
from .text_extraction import extract_text_from_pdfs
from .entity_recognition import extract_entities
from .summarization import summarize_text
from .question_answering import question_answering
from .trend_prediction import predict_trends

# Export key functions
__all__ = [
    'extract_text_from_pdfs',
    'extract_entities',
    'summarize_text',
    'question_answering',
    'predict_trends'
]