
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#Q1_T2
#Textbook pp172 the design of the text analysis program
#Create a structure Chart?
#pip install or python3<FILE_NAME>.py install

#Install the libraries(SpaCy – scispaCy – ‘en_core_sci_sm’/’en_ner_bc5cdr_md’).
#Biomedical information processing library
#Link to directory (change to /)
dir_library="E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_Libraries"

#Install the libraries (Transformers (Hugging Face)
#pip install git+https://github.com/huggingface/transformers
#Open sourced library for python that provides access to pre trained transformers models for natural language processing
#The hugging face hub is a collaboration plarform that hosts opensource models and datasets for machine learning. It is used in conjunction with the transformers library

#Install any bio-medical model (BioBert) that can detect drugs, diseases, etc from the text).
#BioBERT: a pre-trained biomedical language representation model for biomedical text mining.
"""
Make sure to specify the versions of pre-trained weights used in your works. 
If you have difficulty choosing which one to use, we recommend using BioBERT-Base v1.1 (+ PubMed 1M) 
or BioBERT-Large v1.1 (+ PubMed 1M) depending on your GPU resources. 
Note that for BioBERT-Base, we are using WordPiece vocabulary (vocab.txt) provided by Google 
as any new words in biomedical corpus can be represented with subwords (for instance, 
Leukemia => Leu + ##ke + ##mia). More details are in the closed issue #1.
"""

#Do we uninstall libraries after use? Do they run in a virtual environment? I have gone down a rabbit hole?????????

#import SpaCy
#import scispaCy
#import transformers
#import Biobert

#task 3.1 Using any python library find the top 30 words and store in csv
#Cite language library publishers
#Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
#cmd "pip install nltk" "nltk.download('all')"
#In Python tokenization basically refers to splitting up a larger body of text into smaller lines, words or even creating words for a non-English language.
import nltk

#set directory of .txt file aquired in Q1_Task1
output_txt ="E:/chuditchwerkroom/2024_Werkroom/0000_CDU/2024_CDU/2024 SEM 2/HIT137/Working_Python Files/Assignment 2_HIT137_CAS_080/Q1_txt file_output/HIT137_A2_Q1.1.txt"
#open and read content of output_text from Q1 task 1
raw_output_text = open(output_txt).read()
print('reading')
#tokenize words to allow nltk library to read only legitimate words
tokens = nltk.word_tokenize(raw_output_text)
text = nltk.Text(tokens)
#address case sensitive situations
tokens_l = [w.lower() for w in tokens]
#Remove all non noun words
only_nn = [x for (x,y) in pos if y in ('NN')]
print("searching")
print("SEARCHING")
#find the most frequent words
freq = nltk.FreqDist(only_nn)
#most common 30 words
print(freq.most_common(30))
