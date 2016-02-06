import csv;
import time;
from sklearn.feature_extraction.text import TfidfVectorizer;

def prepareExpectedResults(fileName):
	csvFile  = open(fileName, "rb");
	reader = csv.reader(csvFile);
	corpus = [];
	test_corpus = [];
	sentence = "RIDGID X4 18-Volt Lithium-Ion Cordless Drill and Impact Driver Combo Kit (2-Tool)";
	vectorizer = TfidfVectorizer(smooth_idf = True, ngram_range = (1, 3), use_idf = True, lowercase = True);

	for rowIndex,row in enumerate(reader):
		if(rowIndex != 1):
			corpus.append(row[1]);
	csvFile.close();

	X_train = vectorizer.fit_transform(corpus);
	test_corpus.append(sentence);
	sample = vectorizer.transform(test_corpus);
	print "features are ", sample;
    
prepareExpectedResults("../product_descriptions.csv");