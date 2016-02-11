#Import Library Files

import sys
import nltk
import operator
import shutil
from nltk.tokenize import word_tokenize
from nltk.corpus import brown

path = ['files/input_files/Gravity (film).txt','files/input_files/Minions (film).txt',
'files/input_files/java(tech).txt','files/input_files/reboot(science_friction).txt',
 'files/input_files/Python (programming language).txt',
 'files/input_files/GreatestMysteries(science_friction).txt']

for pid in path:
    #Reading  input file one at a time
    inputfile = open(pid).read() 

  
    #Tokenizing 
    inputwords=word_tokenize(inputfile);

    #Parts of speech tagging
    tagged=nltk.pos_tag(inputwords)
    
    #Extracting Nouns using Chunking
    chunk_nouns = r"""Chunk: {<NN.?.?>}"""
    chunkParser = nltk.RegexpParser(chunk_nouns)

    #convert to parse tree
    chunked = chunkParser.parse(tagged)

    #Initialisation
    inputfinal=[]
    scifi_most=[]
	movie_most=[]
    content_most=[]
    programming_most=[]

    #adding Nouns to Array
    for subtree in chunked.subtrees():
       if subtree.label() == 'Chunk':
            inputfinal.append(subtree[0][0])

    # calcute Frequency Distribution
    freq_db= nltk.FreqDist(w.lower() for w in inputfinal)
    
    #Get top 100 words from Content
    content_top=freq_db.most_common(100)
    for i in content_top:
        content_top.append(i[0])

    #Get top 100 words from Science Fiction
    scifi = brown.words(categories='science_fiction')
    scifi_freq = nltk.FreqDist(w.lower() for w in scifi)
    scifi_mostf=scifi_freq.most_common(100)
    for i in scifi_mostf:
       scifi_most.append(i[0])
    
    #Get top 100 words from Programming Language   
    plfile = open("PL_corpora.txt").read()
    plwords=word_tokenize(plfile);
    pl_freq = nltk.FreqDist(w.lower() for w in plwords)
    programming_mostf=pl_freq.most_common(100)
    for i in programming_mostf:
      programming_most.append(i[0])
	  
	  
 #Get top 100 words from Movies
    movie = brown.words(categories='movies')
    movie_freq = nltk.FreqDist(w.lower() for w in movie)
    movie_mostf=movie_freq.most_common(100)
    for i in movie_mostf:
       movie_most.append(i[0])
	   
    scifi_count=0
    programming_count=0
	movie_count=0
    
    
    

    #checking for match
    for i in content_top:
       if i in scifi_most:
          #print "Matched word: "+i
          scifi_count+=1
       if i in programming_most:
          #print "Matched word: "+i
          programming_count+=1
		if i in movie_most:
          #print "Matched word: "+i
          movie_count+=1
    
    
    #Get MAX of count from dictionary of counts
    countd={'SciFi': scifi_count,'Programming': programming_count,'movie': movie_count}
    maxkey=max(countd.iteritems(), key=operator.itemgetter(1))[0]
    
    #Classification based on count
    if(maxkey=='SciFi'):
        shutil.move(pid, 'files/categories/fiction')
    elif(maxkey=='Programming'):
        shutil.move(pid, 'files/categories/technologies and ProgrammingLanguages')
    elif(maxkey=='movie'):
        shutil.move(pid, 'files/categories/movies')
    
    