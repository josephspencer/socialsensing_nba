# this tool queries the score dict to determine who will win based on teams passed in on the command line. Run the program by typing: python predict.py team1 team2
# For example: python predict.py Lakers Celtics

import sys
sys.path.append('..')
import tweepy
import json
from textblob import TextBlob
from operator import itemgetter
import pickle
import os

if __name__ == '__main__':

	
	scores = {} # sentiment analysis scores
        avg = {}

        # load in dictionary containing previous scores for appending data
        scores = pickle.load(open(sys.argv[1], "rb"))

	for key, values in scores.items():
                score = float(sum(values)) / float(len(values))
                avg[key] = score

	team1 = sys.argv[2]
	team2 = sys.argv[3]

        if team1 and team2 in scores.keys():
		if avg[team1] < 0.0:
			avg[team1] = abs(avg[team1])
			avg[team2] += abs(avg[team1])
		elif avg[team2] < 0.0:
			avg[team2] = abs(avg[team2])
			avg[team1] += abs(avg[team2])
		tot = avg[team1] + avg[team2]
		team1_tweetH = ((avg[team1] / tot) * 0.6) + (0.4 * 0.599)
		team2_tweetA = ((avg[team2] / tot) * 0.6) + (0.4 * 0.401)
		#print str(team1) + " score " + str(team1_tweetH) + "%"
		#print str(team2) + " score " + str(team2_tweetA) + "%"
		if team1_tweetH > team2_tweetA:
			print str(team1) + "," + str(team1_tweetH)
		elif team1_tweetH < team2_tweetA:
			print str(team2) + "," + str(team2_tweetA)
	else:
		print "Incorrect team names. Try again."
