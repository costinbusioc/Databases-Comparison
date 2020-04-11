import pandas

out_file = ''

df = pandas.read_csv('professors.csv')
nr_lines = df.shape[0]

out_file += 'INSERT INTO professors(id, full_name, specialization, office_room)\n'
out_file += 'VALUES\n'

for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	name = df.loc[i, 'Name']
	spec = df.loc[i, 'Specialization']
	office = df.loc[i, 'Office']

	curr_line = '(' + str(idd) + ', \'' + name + '\', \'' + spec + '\', \'' + office + '\')'

	if i != nr_lines - 1:
		curr_line += ',\n'
	else:
		curr_line += ';\n\n'

	out_file += curr_line

df = pandas.read_csv('students.csv')
nr_lines = df.shape[0]

out_file += 'INSERT INTO students(id, full_name, lives_in_campus, origin_city)\n'
out_file += 'VALUES\n'

for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	name = df.loc[i, 'Name']
	campus = 'TRUE' if df.loc[i, 'Lives in campus'] else 'FALSE'
	city = df.loc[i, 'City']

	curr_line = '(' + str(idd) + ', \'' + name + '\', ' + campus + ', \'' + city + '\')'

	if i != nr_lines - 1:
		curr_line += ',\n'
	else:
		curr_line += ';\n\n'

	out_file += curr_line


df = pandas.read_csv('thesis.csv')
nr_lines = df.shape[0]

out_file += 'INSERT INTO thesis(id, student_id, professor_id, thesis_area, thesis_title)\n'
out_file += 'VALUES\n'

for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	s_id = df.loc[i, 'Student_id']
	p_id = df.loc[i, 'Professor_id']
	area = df.loc[i, 'Area']
	title = df.loc[i, 'Title']

	curr_line = '(' + str(idd) + ', ' + str(s_id) + ', ' + str(p_id) + ', \'' + area + '\', \'' + title + '\')'

	if i != nr_lines - 1:
		curr_line += ',\n'
	else:
		curr_line += ';\n\n'

	out_file += curr_line


with open('insert.sql', 'w') as f:
	f.write(out_file)
	
