from monkeylearn import MonkeyLearn
from rake_nltk import Rake
import pprint

# Opening the text file and splitting it into a list of strings
# filepath --> path to input text file (string)
# returns a list of strings, each string contains a paragraph
def preprocessText(filepath):
    with open(filepath, "r") as file:
        data_text = file.read()
    data_split=data_text.split('\n')
    # print(data_split)
    with open(filepath, "r") as file:
        data_text_copy = file.read()
    data_split_copy=data_text_copy.split('\n')
    while '' in data_split:
        data_split.remove('')
    while '' in data_split_copy:
        data_split_copy.remove('')
    for string in data_split_copy:
        if len(string)<40:    # to remove the title of paragraphs
            #print(string,len(string))
            temp = string
            data_split.remove(string)
    return data_split


# Getting the Keywords for the paragraph
def GetKeywords(input_list):
    r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
    keywords=[]
    for para in input_list:
        r.extract_keywords_from_text(para)
        #print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.
        keywords.append(r.get_ranked_phrases())
    return keywords
    

# Creating master dictionary
# input_list --> List of paragraph strings
# model --> The keyword extraction model to be used. Options are Rake or MonkeyLearn
# API_token --> API token for MonkeyLearn. Default value is mine. Optional argument, needed only if model is MonkeyLearn Limited to 300 queries per month in the free account. 
# Return value: consolidated--> A dictionary containing paragraph string (key--> paragraph), paragraph ID(key--> para_ID) and keywords (key--> keywords)
def createMasterDict(input_list,model, API_token ='06f65ed21f102ecd78427152869791eb66fe5772' ):
    if model in ["MonkeyLearn","ML","ml","monkeylearn"]:
        ml = MonkeyLearn(API_token)    
        model_id = 'ex_YCya9nrn'
        consolidated=[]
        j = 1
        for data in input_list:
            features = {}
            features['paragraph']=data
            features['para_ID']=j
            j+=1
            result = ml.extractors.extract(model_id, [data])
            extrac=result.body[0]['extractions']
            keywords=[]
            for i in range(len(extrac)):
                keywords.append(extrac[i]['parsed_value'])
            features['keywords']=keywords
            consolidated.append(features)
        return consolidated
    elif model in ["rake","Rake"]:
        r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
        consolidated = []
        k=1
        for para in input_list:
            features_={}
            features_['para_ID']=k
            features_['paragraph']=para
            k+=1
            r.extract_keywords_from_text(para)
            #print(r.get_ranked_phrases()) # To get keyword phrases ranked highest to lowest.
            features_['keywords']=r.get_ranked_phrases()
            consolidated.append(features_)
        return consolidated

# Running the search for a keyword
# master_dict --> dictionary with keywords, paragraph_IDs and paragraphs; The create_master_dict() returns the dictionary to be used here
# keyword_list --> A list of keywords to search for
# Return value: para_ID_list--> A list of pargraph IDs that contain the searched keywords. This can be used to access the required paragraphs from the input dictionary
def keywordSearch(master_dict,keyword_list):
    text=""
    for word in keyword_list:
        for item in master_dict:
            if word in item['keywords']:
                text+=item['paragraph']
    return text


#help
def helps():
    print("Available functions:\n")
    
    print("\npreprocess_text(filepath): Opening the text file and splitting it into a list of strings\n")
    print("filepath --> path to input text file (string)\nReturn value: data_split--> a list of strings, each string contains a paragraph\n")
    
    print("\ncreate_master_dict(input_list,model, API_token): Creating a dictionary containing paragraphs linked to the keywords")
    print("input_list --> List of paragraph strings")
    print("model --> The keyword extraction model to be used. Options are Rake or MonkeyLearn")
    print("API_token --> API token for MonkeyLearn. Default value is mine. Optional argument, needed only if model is MonkeyLearn Limited to 300 queries per month in the free account.")
    print("Return value: consolidated--> A dictionary containing paragraph string (key--> paragraph), paragraph ID(key--> para_ID) and keywords (key--> keywords)\n")

    print("\nkeyword_search(master_dict,keyword_list): Running the search for a keyword")
    print("master_dict --> dictionary with keywords, paragraph_IDs and paragraphs; The create_master_dict() returns the dictionary to be used here")
    print("keyword_list --> A list of keywords to search for")
    print("Return value: para_ID_list--> A list of pargraph IDs that contain the searched keywords. This can be used to access the required paragraphs from the input dictionary\n")
    return 0
