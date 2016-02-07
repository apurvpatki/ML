#code to analyze the attributes files for feature engineering
import csv;
from sklearn.feature_extraction.text import TfidfVectorizer;
from sys import argv;

def readCSVFile(fileName):
	csvFile  = open(fileName, "rb");
	reader = csv.reader(csvFile);
	dictionary = [];

	for rowIndex,row in enumerate(reader):
		if(rowIndex != 0):
			dictionary.append(row);
	csvFile.close();

	return dictionary;

def extractUniqueAttributeNames(attributes):
	attributeNames = set();
	for attribute in attributes:
		if attribute[1] not in attributeNames:
			attributeNames.add(attribute[1]);
	return attributeNames;

def extractRowsPerRelevance(trainingData):
	relevance3 = 0;
	relevance23 = 0;
	relevance2 = 0;
	relevance12 = 0;
	relevance1 = 0;
	for data in trainingData:
		score = float(data[4]);
		if score == float(3):
			relevance3 = relevance3 + 1;
		elif score > float(2):
			relevance23 = relevance23 + 1;
		elif score == float(2):
			relevance2 = relevance2 + 1;
		elif score > float(1):
			relevance12 = relevance12 + 1;
		elif score == float(1):
			relevance1 = relevance1 + 1;
	return (relevance1, relevance2, relevance3, relevance12, relevance23);

def extractRelevanceDistribution(trainingData):
	relevanceMap = dict();
	for data in trainingData:
		score = data[4];
		if score in relevanceMap:
			relevanceMap[score] = relevanceMap[score] + 1;
		else:
			relevanceMap[score] = 1;
	return relevanceMap;

def runAnalyzer(fileName, trainingPath):
	attributes = readCSVFile(fileName);
	trainingData = readCSVFile(trainingPath);

	uniqueProductIds = extractUniqueAttributeNames(trainingData);
	uniqueAttributesNames = extractUniqueAttributeNames(attributes);
	(relevance1, relevance2, relevance3, relevance12, relevance23) = extractRowsPerRelevance(trainingData);

	relevanceMap = extractRelevanceDistribution(trainingData);

	print "relevance score = 1 ", relevance1;
	print "relevance score bettwen (1,2) ", relevance12;
	print "relevance score = 2 ", relevance2;
	print "relevance score between (2,3) ", relevance23;
	print "relevance score = 3 ", relevance3;
	print "Number of unique product ids is ", len(uniqueProductIds);
	print "Number of unique attribtues are ", len(uniqueAttributesNames);
	print "Relevance distribution ", relevanceMap;


attibutesPath = argv[1];
trainingPath = argv[2];
runAnalyzer(attibutesPath, trainingPath);