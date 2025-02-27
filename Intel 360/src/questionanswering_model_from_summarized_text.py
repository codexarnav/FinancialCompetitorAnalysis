# -*- coding: utf-8 -*-
"""QuestionAnswering model from summarized text.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NRhdsgjWpQpFCwxi2lLCDv1Ab6sDJZDV
"""

!pip install transformers

from transformers import AutoTokenizer, AutoModelForQuestionAnswering,pipeline

model_name="deepset/roberta-base-squad2"

model=AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer=AutoTokenizer.from_pretrained(model_name)

nlp=pipeline("question-answering",model=model,tokenizer=tokenizer)
QA_input={
    'question':'Why is model conversion important?',
    'context':'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res=nlp(QA_input)

