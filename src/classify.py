import operator
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown

def getwords_dict():
    category_noun_dictionary = {}

    categories=['adventure', 'fiction', 'mystery', 'reviews', 'science_fiction','news']
    #Finding top 500 words from categories
    for category in categories:
        top_words_category=[]
        words_of_category = brown.words(categories=category)
        category_word_freq = nltk.FreqDist(w.lower() for w in words_of_category)
        top_in_category = category_word_freq.most_common(500)
        for i in top_in_category:
            top_words_category.append(i[0])
        top_words_category = set(top_words_category)
        category_noun_dictionary[str(category)] = top_words_category

    plfile = open("PL_corpora.txt").read()
    pl_top=[]
    plwords=word_tokenize(plfile);
    pl_freq = nltk.FreqDist(w.lower() for w in plwords)
    pl_topf=pl_freq.most_common(500)
    for i in pl_topf:
       pl_top.append(i[0])
    pl_top = set(pl_top)
    category_noun_dictionary['programming_language'] = pl_top

    return category_noun_dictionary

def classify_file(filename,category_noun_dictionary):


    #Reading input file
    inputfile = open(filename).read()

    #Tokenizing
    inputwords=word_tokenize(inputfile)

    #POS Tagging
    tagged=nltk.pos_tag(inputwords)

    #Extracting Nouns using Chunking
    chunk_nouns = r"""Chunk: {<NN.?.?>}"""
    chunkParser = nltk.RegexpParser(chunk_nouns)

    #Get Parse Tree
    chunked = chunkParser.parse(tagged)

    #Initialise
    inputfinal=[]
    content_top=[]

    features_dict={}

    #Append Nouns to Array
    for subtree in chunked.subtrees():
       if subtree.label() == 'Chunk':
            inputfinal.append(subtree[0][0])

    #Frequency Distribution
    freq_words = nltk.FreqDist(w.lower() for w in inputfinal)

    #Get top 500 words from Content
    content_topf=freq_words.most_common(500)
    for i in content_topf:
        content_top.append(i[0])

    #Searching
    for category in category_noun_dictionary.keys() :
        count=0
        for i in content_top:
            if i in category_noun_dictionary[category] :
                count+=1
        features_dict[category]= count

    default=5 #Threshold value
    features_dict['Other']= default
    print(features_dict)
    #Print File Name
    print ("The file"+ filename+"is Processing.")

    #Get MAX of count from dictionary of counts
    maxkey=max(features_dict.items(), key=operator.itemgetter(1))[0]
    print ("Matched "+str(features_dict[maxkey])+" words with category "+maxkey+". The file is moving to the "+maxkey+" category.");
    return maxkey
