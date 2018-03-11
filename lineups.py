import pandas as pd
import numpy as np
import math
import pulp
from pulp import *
import os

# basic constraints/file locations
# writing out to text file
locLineups = 'temp_output.csv'
with open('configurations.txt') as f:
    content = f.readlines()
f.close()
content = [line.strip() for line in content]
for line in content:
	line = line.split(' ', 1)
	if line[0] is '1':
		numLineups = int(line[1])
	elif line[0] is '2':
		numPlayers = int(line[1])
	elif line[0] is '3':
		projectionsColumn = line[1]
	elif line[0] is '4':
		budget = int(line[1])
	elif line[0] is '5':
		budgetColumn = line[1]
	elif line[0] is '6':
		inputCSVLocation = line[1]
	elif line[0] is '7':
		line2 = line[1].split(' ', 1)
		if line2[0] == '':
			line2[0] = 0
		maxSameTeam = int(line2[0])
		teamColumn = line2[1]
#numLineups = gui.lineups.get()
#numPlayers = gui.players.get()
#budget = gui.maxCost.get()
#maxSameTeam = gui.numPos.get()

#projectionsColumn = settings.projectionsHeaderList[0]
#budgetColumn = settings.budgetHeaderList[0]
#teamColumn = 
#inputCSVLocation = 
		
# creates a temp folder in the same directory
currentDirectory = os.getcwd()
finalDirectory = os.path.join(currentDirectory, r'temp_folder')
if not os.path.exists(finalDirectory):
   os.makedirs(finalDirectory)

# read csv using pandas to store data
df = pd.read_csv(inputCSVLocation, sep=',')
df['lineup exposure'] = 0 #new column for lineup usage for each player

# create the 'prob' variable to contain the problem data
prob = pulp.LpProblem('DFSLineups', pulp.LpMaximize)

# define objective function(projected points) and constraints
objectiveFunction = ''
numPlayersConstraint = ''
costConstraint = ''

df['temp_index'] = df.index

# create pulp variables for each player's row and build constraints
for uniqueColumn in df[teamColumn].unique():
	tempConstraint = ''

	for index, row in df.loc[df[teamColumn] == uniqueColumn].iterrows():
		varName = 'p' + str(row['temp_index'])
		variable = pulp.LpVariable(varName, lowBound=0, upBound=1, cat=pulp.LpInteger) #make binary player variable(0 for not in lineup, 1 for in lineup)

		#update constraints with player's projections and cost
		objectiveFunction += row[projectionsColumn] * variable
		numPlayersConstraint += variable
		costConstraint += row[budgetColumn] * variable
		tempConstraint += variable

	prob += (tempConstraint <= maxSameTeam)

# add objective function(projected points), the number of players chosen constraint, cost constraint, position constraints, and team constraints to problem
prob += objectiveFunction
prob += (numPlayersConstraint == numPlayers)
prob += (costConstraint <= budget)

# solve for the specified number of lineups
for i in range(1, numLineups+1):
	#find solution
	prob.solve()

	#create binary column for this specific lineup
	lineupCol = 'lineup_' + str(i)
	df[lineupCol] = 0

	#add solution players to this lineup's column
	#also add a new constraint so the solver doesn't select same lineup again
	newConstraint = ''
	for variable in prob.variables():
		if variable.varValue == 1:
			rowNum = int(variable.name[1:])
			df.ix[rowNum, lineupCol] = 1
			df.ix[rowNum, 'lineup exposure'] += 1 #right now lineup exposure is just the number of lineups player is in - at the end it will be divided by the number of lineups
			newConstraint +=  variable

	prob += (newConstraint <= numPlayers - 1) #using <= and subtracting 1 since it throws an error if < is used
	#print('optimized lineup no. ' + str(i))

# change lineup exposure from number of lineups appeared in to ratio of lineups included in to number of lineups
df['lineup exposure'] /= numLineups

# first sort by projections, then sort by lineups
df.sort_values(by=projectionsColumn, ascending=False, inplace=True)
df.sort_values(by=['lineup_' + str(i) for i in range(1, numLineups+1)], ascending=False, inplace=True)

# write to csv
path = r'temp_folder'
df.to_csv(os.path.join(path, locLineups), sep=',', index=False)
