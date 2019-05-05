# Using Twitter to Predict NBA Outcomes

## Programs
This github contains all the code that was written for the completion of our project. The programs function as follows:
- nba_initialstart.py: This program was run at the beginning of each gameday and initalizes a new pkl file for tweet collection as well as collects the first group of tweets
- nba_continue.py: This program was run subsequently multiple times throughout gamedays, adding new tweets to the pkl files
- calcsentiment.py: This program was used to evaluate the sentiment score of each time, as well as output the total number of tweets collected
- predict.py: This program was the original prediction tool we used, utilizing only sentiment scores
- newmodel.py: This program was the updated prediction tool, which incorporated home/away probabilities
- newmodel2.py: This program is identical to newmodel.py, with only a slightly different output
- get_all_results.py: This program runs the newmodel.py program on all previous gamedays
- finalmodel.py: This model takes all the prediction outputs from our twitter model as well as FiveThirtyEight, and merges results together
