# Document-Feature-Identification-Vasavi
The project will be about taking random text documents of different topic scenarios and grouping/classifying these documents into respective domain areas by creating a powerful algorithm.In this project we use python programming language with Natural Language Tool Kit .firstly, we take data in the form of files by browsing them in a web page . After adding all the files to the list we send them to a classification algorithm. The classification algorithm takes all the files into an array. Chunking and parts of speech tagging is done on the data array. We get the parse tree and now append the nouns to an array. Frequency distribution is calculated on the first file in  array. We get top 100(we can change this number) frequent words from the frequency distribution . now get top 100(number can be changed) words from the category we want to compare .Start comparing every word from frequency distribution with all categories necessary and increase the count variable of that respective category. The file is then moved to the folder which got more number of word matches.