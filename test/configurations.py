#test out reading and writing the first configurations file format for Sprint 1

num_lineups = 20
budget = 105
num_players = 11
budget_column = 'cost'
projections_column = 'Final Model'
input_csv_location = 'screened current predictions.csv'

f = open('configurations.txt','w')
f.write('1 ' + str(num_lineups) + '\n')
f.write('2 ' + str(num_players) + '\n')
f.write('3 ' + projections_column + '\n')
f.write('4 ' + str(budget) + '\n')
f.write('5 ' + budget_column + '\n')
f.write('6 ' + input_csv_location + '\n')
f.close()

#reset
num_lineups = 0
budget = 0
num_players = 0
budget_column = 'a'
projections_column = 'a'
input_csv_location = 'a'

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

print('1  ' + str(num_lineups))
print('2  ' + str(num_players))
print('3  ' + projections_column)
print('4  ' + str(budget))
print('5  ' + budget_column)
print('6  ' + input_csv_location)