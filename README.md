# question_answer_generator
This model takes any format (PDF, docx, txt, png, jpg, jpeg) of document and generates question and answers from the text in the document. 

I have added 2 new features in the model and that is:
- It takes multiple formats of document and extract text from the documents. If you want to read more about it, this is the <a href="https://github.com/ppcool1163/Extract-text">link</a> to it.

- It allows you to select the part of document you want to generate question-answer. For this feature I have used a model that extracts paragraphs from the document use keywords. if you want to read more gere is the <a href="https://github.com/ppcool1163/paragraph_extraction">link</a> to the paragraph extraction model. 


So this model will take the file path as an input and then ask whether the questions to be generated is from the whole document or a part of the document. If you want the questions to be generated from a part of the document it will then list out the keywords for you to select the keywords you want questions about. Then it will get the paragraphs corresponding to that keyword and generates the question-answer pairs from it.


# Requirements
- Python 3.5+
- NLTK
- Spacy
- Numpy
- AllenNLP
- Rake-NLTk 
- PyPDF2 (for extracting text from a PDF)
- docx (for extracting text from a word document)
- openCV (cv2) and pytesseract (for extracting text from images)


# How to Use
I have made using the model easy. clone the repo and then run main.py file either in your environment or in Anaconda prompt. 
Note: If there is any form of runtime error refresh the kernel and again run the model.

