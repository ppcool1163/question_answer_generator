# Function to extract the text from the input file


# function for text extraction
def TextExtraction(fileName):
    
    #if the input is a PDF
    if fileName.lower().endswith('.pdf'):
        # Importing the required Package
        import PyPDF2

        pdfFileObj = open(fileName,'rb')
        
        # Reading the input file
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        
        # Text extraction from the file
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()
            
        # Checking whether the text is empty
        if text != "":
           text = text
        
        else:
            text = 'The file is empty'
        
        
    #if the input is a Docx
    if fileName.lower().endswith(('.docx', '.doc')):
        # Importing the required package
        import docx
        doc= docx.Document(fileName)

        data=''
        fulltext=[]
        
        # Reading the file and extracting the text
        for para in doc.paragraphs:
            fulltext.append(para.text)
            data='\n'.join(fulltext)
        
        # Checking whether data is not empty
        if data!= '':
            text= data
        
        else:
            text='there was error in loading the file'
            
        
    # If the input is Image
    if fileName.lower().endswith(('.png','.jpeg','.jpg')):
        # Importing the required files
        import cv2
        import pytesseract
        
        # Giving the location of pytesseract
        pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Reading the Image using OpenCV
        img= cv2.imread(fileName)
        
        # Using pytesseract to read the text from the Image
        text= pytesseract.image_to_string(img)
    
    # If text file is in .txt format
    if fileName.lower().endswith('.txt'):
        file= open(fileName, 'r')
        text= file.read()
    
    return text



        
    
    



    
    
        
        
        


