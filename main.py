from InputText import TextExtraction
import aqgFunction
from keywordExtraction import preprocessText, GetKeywords, createMasterDict, keywordSearch
from allennlp.predictors.predictor import Predictor
import time
#import os.path
#import keyboard
#from summa import summarizer


# Extracting keywords
def ExtractKeywords(fileName):
    doc_data = preprocessText(fileName)
    keywords= GetKeywords(doc_data)
    return keywords


# Extracting the subtopics from the document
def subTopicSeperation(fileName):
    doc_data= preprocessText(fileName)
    topicDict= createMasterDict(doc_data,'rake')
    return topicDict

# Cleaning the output question
def CleanQues(ListofQuestions):
    question_copy= ListofQuestions
    for items in question_copy:
        if len(items.split())<4:
            ListofQuestions.remove(items)
    
    return ListofQuestions

# Getting the answers of the question
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

def Answers(passage, ListofQuestion):
    answers=[]
    for question in ListofQuestion:
        result=predictor.predict(
        passage=passage,
        question= question)
        answers.append(result['best_span_str'])
    return answers





# Main Function
def main():
    # Getting the Input from the User
    fileName= str(input('Enter the path of the file '))
    # Text Extraction from the input
    text= TextExtraction(fileName)
    
    #saving the text extracted
    name='document.txt'
    file= open('document.txt', 'w')
    file.write(text)
    file.close()
    
    # Which part to learn
    read= str(input('Do you want to learn:\n a) whole document\n b) Part of document\n'))
        
    if read.lower()=='whole document':
        name= 'document.txt'
    
    else:
        keywords=ExtractKeywords(name)
        doc_dict=subTopicSeperation(name)
        print(keywords)
        subtopic=str(input('Select the topics from the above list:\n'))
        subtopic=subtopic.split()
        text= keywordSearch(doc_dict, subtopic)
        name= 'currentTopic.txt'
        file= open('currentTopic.txt', 'w')
        file.write(text)
        file.close()

    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    #inputTextPath = name
    readFile = open(name, 'r+')
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

    inputText = readFile.read()

    questionList = aqg.aqgParse(inputText)
    output=aqg.display(questionList)
    output= CleanQues(output)
    answers= Answers(text,output)
    # Giving the question to the user
    for i in range (len(answers)):
        print('Q. {}'.format(output[i]))
        time.sleep(5)
        print('Ans: {}'.format(answers[i]))
        print('\n')

#    return output

# Call Main Function
if __name__ == "__main__":
    main()







    
    

        
        
    








