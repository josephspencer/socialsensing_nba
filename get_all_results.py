import subprocess

t1 = ""
t2 = ""
tw = ""
with open("all_games.txt") as f:
	for line in f.readlines():
		line = line.split(",")
		if len(line) == 1:
			date = line[0][:-1]
			continue
		else:		
			if line[0] == "Trail Blazers":
				t1 = line[0]
				t2 = line[1][:-1]
				args = '"Trail Blazers"' + ' "' + t2 + '"'
			elif line[1][:-1]  == "Trail Blazers":
				t1 = line[0]
				t2 = "Trail Blazers"
				args = '"' + t1 + '" ' + '"Trail Blazers"'
			else:
				t1 = line[0]
				t2 = line[1][:-1]
				args = t1 + " " + t2
		command_str = "python newmodel2.py " + date + ".pkl " + args

		result = subprocess.check_output(command_str, shell=True)[:-1]
		out_line = date + "," + t1 + "," + t2 + "," + result
		print out_line	
