pred_538 = dict()
pred_twitter = dict()
actual_winners = dict()

with open("results_twitter.txt") as f:
	for line in f.readlines():
		line = line.split(',')
		k = line[0]+','+line[1]+','+line[2]
		if line[3] != line[2]:
			v = [line[3],line[2],float(line[4][:-1])]
		else:
			v = [line[3],line[1],float(line[4][:-1])]
		pred_twitter[k] = v

with open("results_538.txt") as f:
	for line in f.readlines():
		line = line.split(',')
		k = line[0]+','+line[1]+','+line[2]
		prob = float(line[3])
		if prob > .5:
			v = [line[1],line[2],prob]
		else:
			v = [line[2],line[1],1-prob]
		pred_538[k] = v
		actual_winners[k] = line[5][:-1]

lower_threshold = .6
upper_threshold = 1


num_games = 0
num_correct = 0
for game in pred_twitter.keys():
	t_winner = pred_twitter[game][0]
	t_prob = pred_twitter[game][2]
	actual_winner = actual_winners[game]
	if t_prob > lower_threshold and t_prob < upper_threshold:
		if t_winner == actual_winner:
			num_correct += 1
		num_games += 1

print float(num_correct) / num_games
print num_games

num_games = 0
num_correct = 0
for game in pred_538.keys():
	f_winner = pred_538[game][0]
	f_prob = pred_538[game][2]
	actual_winner = actual_winners[game]
	if f_prob > lower_threshold and f_prob < upper_threshold:
		if f_winner == actual_winner:
			num_correct += 1
		num_games += 1

print float(num_correct) / num_games
print num_games

num_games = 0
num_correct = 0
for game in pred_twitter.keys():
	actual_winner = actual_winners[game]
	t_winner = pred_twitter[game][0]
	f_winner = pred_538[game][0]
	t_prob = pred_twitter[game][2]
	f_prob = pred_538[game][2]
	if t_winner == f_winner:
		combined_prob = .55*f_prob + .45*t_prob
		combined_winner = t_winner
	else:
		combined_prob = .55*f_prob + .45*(1-t_prob)
		combined_winner = f_winner
		if combined_prob < .5:
			combined_prob = .55*(1-f_prob) + .45*t_prob
			combined_winner = t_winner
	if combined_prob > lower_threshold and combined_prob < upper_threshold:
		if combined_winner == actual_winner:
			num_correct += 1
		num_games += 1

print float(num_correct) / num_games
print num_games
