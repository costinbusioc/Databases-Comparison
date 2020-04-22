import pandas

out_file = ''

df = pandas.read_csv('professors.csv')
nr_lines = df.shape[0]

out_file += 'INSERT ALL\n'
for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	name = df.loc[i, 'Name']
	spec = df.loc[i, 'Specialization']
	office = df.loc[i, 'Office']
	
	out_file += 'INTO professors(id, full_name, specialization, office_room) VALUES '
	curr_line = '(' + str(idd) + ', \'' + name + '\', \'' + spec + '\', \'' + office + '\')\n'

	out_file += curr_line

df = pandas.read_csv('students.csv')
nr_lines = df.shape[0]
out_file += 'select * from dual;\n'

out_file += 'INSERT ALL\n'

for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	name = df.loc[i, 'Name']
	campus = '1' if df.loc[i, 'Lives in campus'] else '0'
	city = df.loc[i, 'City']

	out_file += 'INTO students(id, full_name, lives_in_campus, origin_city) VALUES '
	curr_line = '(' + str(idd) + ', \'' + name + '\', ' + campus + ', \'' + city + '\')\n'

	out_file += curr_line


df = pandas.read_csv('thesis.csv')
nr_lines = df.shape[0]
out_file += 'select * from dual;\n'

out_file += 'INSERT ALL\n'
for i in range(nr_lines):
	idd = df.loc[i, 'Id']
	s_id = df.loc[i, 'Student_id']
	p_id = df.loc[i, 'Professor_id']
	area = df.loc[i, 'Area']
	title = df.loc[i, 'Title']

	out_file += 'INTO thesis(id, student_id, professor_id, thesis_area, thesis_title) VALUES '
	curr_line = '(' + str(idd) + ', ' + str(s_id) + ', ' + str(p_id) + ', \'' + area + '\', \'' + title + '\')\n'
	out_file += curr_line

out_file += 'select * from dual;'

with open('insert.sql', 'w') as f:
	f.write(out_file)
	
