file = "file.txt"

with open(file, "r") as f:
	data = f.readlines()
	
	for line in data:
		line = line.split()
		print("#".join(line))