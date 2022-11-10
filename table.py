
league = {
	"RBR PEREZ": 0,
	"RBR VERSTAPPEN": 0,
	"FER SAINZ": 0,
	"FER LECLERC": 0,
	"MER RUSSELL": 0,
	"MER HAMILTON": 0,
	"MCL RICCIARDO": 0,
	"MCL NORRIS": 0,
	"ALP OCON": 0,
	"ALP ALONSO": 0,
	"ALF ZHOU": 0,
	"ALF BOTTAS": 0,
	"AST VETTELL": 0,
	"AST STROLL": 0,
	"HAA SCHUMACHER": 0,
	"HAA MAGNUSSEN": 0,
	"APH TSUNODA": 0,
	"APH GASLY": 0,
	"WIL LATIFI": 0,
	"WIL ALBON": 0
}

scores = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# function to simulate table
# teams must be a dictionary of the teams as the keys and the points for each value (it is recommended that each value is a 0)
# points must be a list of numbers the same length as the teams dictionary
# loop must be a whole number, number of rounds that points are distributed
def simulate(teams, points, loop):

	# import tabulate to display the table
	# import random to randomly choose indexes in points list
	from tabulate import tabulate
	import random

	# input begins the simulation
	print("\n", "Press 'enter' to begin the simulation.")
	inp = input()

	# assign round variable to display round number when table is displayed
	global round
	round = 0

	# while loop runs for loop for as many times specified in loop parameter
	while loop > 0:
		removed = []

		# for loop iterates through every value in teams and adds a random item from points until points has no length
		for key, value in teams.items():
			random_points = random.choice(points)
			teams[key] = value + random_points
			points.remove(random_points)
			removed.append(random_points)

			# if statement checks if all items in points have been used and if so all of the items are reappended to points in order to be iterated again until while loop is met
			if len(points) == 0:
				round += 1
				points = removed

				# sort, sorts dictionary by values in reverse order
				sort = dict(sorted(teams.items(), key=lambda item: item[1], reverse = True))

				# turns sorted dictionary into lists which then get turned into a table and printed
				table = [["Teams", "Points"]]
				for key, value in sort.items():
					table.append([key, value])

				print("\n", "Round:", round, "\n", tabulate(table, headers='firstrow', showindex=range(1, len(teams.keys()) + 1)))

				loop -= 1

				# if statement checks for input and returns next loop after input is detected
				if loop == 0:
					print("\n", "Press 'enter' to END simulation.")
					inp = input()
				else:
					print("\n", "Press 'enter' to simulate next round.")
					inp = input()

simulate(league, scores, 23)

# add input after every round
# add tiebreaker rules

