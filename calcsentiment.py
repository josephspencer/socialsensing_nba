# outputs the total sentiment of all teams
# command line: python calcsentiment.py month_day.pkl

import sys
sys.path.append('..')
import tweepy
import json
from textblob import TextBlob
from operator import itemgetter
import pickle
import os

if __name__ == '__main__':

	filename = sys.argv[1]

	scores = {} # sentiment analysis scores
        avg = {}

        # load in dictionary containing previous scores for appending data
        scores = pickle.load(open(filename, "rb"))

	totalTweets = 0
	for key, values in scores.items():
		totalTweets += len(values)
                print "Total tweets for " + str(key) + " is " + str(len(values))
                score = float(sum(values)) / float(len(values))
                avg[key] = score

	print "total tweets for all teams is " + str(totalTweets)

        print "\nScores:"
        for k, v in sorted(avg.items(), key=itemgetter(1)):
                print str(k) + ": " + str(v)
