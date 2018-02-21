import pandas as pd
import numpy as np
import math
import pulp
from pulp import *

# basic constraints/file locations
# writing out to text file
loc_lineups = 'temp_output.csv'
with open('configurations.txt') as f:
    content = f.readlines()
f.close()
content = [line.strip() for line in content]
for line in content:
	line = line.split(' ', 1)
	if line[0] is '1':
		num_lineups = int(line[1])
	elif line[0] is '2':
		num_players = int(line[1])
	elif line[0] is '3':
		projections_column = line[1]
	elif line[0] is '4':
		budget = int(line[1])
	elif line[0] is '5':
		budget_column = line[1]
	elif line[0] is '6':
		input_csv_location = line[1]
	elif line[0] is '7':
		max_same_team = line[1]
		team_column = line[2]

# creates a temp folder in the same directory
current_directory = os.getcwd()
final_directory = os.path.join(current_directory, r'temp_folder')
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

# read csv using pandas to store data
df = pd.read_csv(loc_projections, sep=',')
df['lineup exposure'] = 0 #new column for lineup usage for each player

# create the 'prob' variable to contain the problem data
prob = pulp.LpProblem('DFSLineups', pulp.LpMaximize)

# define objective function(projected points) and constraints
objective_function = ''
num_players_constraint = ''
cost_constraint = ''

# create pulp variables for each player's row and build constraints
for row_num, row in df.iterrows():
	variable = pulp.LpVariable('p' + str(row_num), lowBound=0, upBound=1, cat=pulp.LpInteger) #make binary player variable(0 for not in lineup, 1 for in lineup)

	#update constraints with player's projections and cost
	objective_function += row[projections_column] * variable
	num_players_constraint += variable
	cost_constraint += row[budget_column] * variable

# add objective function(projected points), the number of players chosen constraint, cost constraint, position constraints, and team constraints to problem
prob += objective_function
prob += (num_players_constraint == num_players)
prob += (cost_constraint <= budget)

# solve for the specified number of lineups
for i in range(1, num_lineups+1):
	#find solution
	prob.solve()

	#create binary column for this specific lineup
	lineup_col = 'lineup_' + str(i)
	df[lineup_col] = 0

	#add solution players to this lineup's column
	#also add a new constraint so the solver doesn't select same lineup again
	new_constraint = ''
	for variable in prob.variables():
		if variable.varValue == 1:
			row_num = int(variable.name[1:])
			df.ix[row_num, lineup_col] = 1
			df.ix[row_num, 'lineup exposure'] += 1 #right now lineup exposure is just the number of lineups player is in - at the end it will be divided by the number of lineups
			new_constraint +=  variable

	prob += (new_constraint <= num_players - 1) #using <= and subtracting 1 since it throws an error if < is used
	print('optimized lineup no. ' + str(i))

# change lineup exposure from number of lineups appeared in to ratio of lineups included in to number of lineups
df['lineup exposure'] /= num_lineups

# first sort by projections, then sort by lineups
df.sort_values(by=projections_column, ascending=False, inplace=True)
df.sort_values(by=['lineup_' + str(i) for i in range(1, num_lineups+1)], ascending=False, inplace=True)

# write to csv
path = r'temp_folder'
df.to_csv(os.path.join(path, loc_lineups), sep=',', index=False)
