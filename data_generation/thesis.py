import random
import pandas
from helpers import write_csv

spec = ['Robotics', 'Algorithms', 'Semantics', 'Distributed Systems', 'Computer Graphics', 'Computer Architecture', 'Computer Systems']

areas = [['Autonomous Robotics', 'Autonomus Multi-Robot'], ['Machine Learning', 'Artifficial Intelligence', 'Algorithms Analysis'], ['Semantic Web', 'Human Computer Interaction', 'NLP'], ['Containers', 'Cluster Computing', 'Grid Computing', 'Big Data'], ['Unity Games', 'Modelling', 'Animation'], ['CPU Analysis', 'Memory Analysis'], ['Operating Systems', 'Security', 'Compilers', 'Drivers']]

ids = []
student_ids = []
professor_ids = []
thesis_areas = []
thesis_title = []

professors = pandas.read_csv('professors.csv')

for i in range(1, 10001):
	ids.append(i)
	student_ids.append(i)
	
	prof = random.choice([i for i in range(1, 201)])
	professor_ids.append(prof)

	specialization = professors.loc[prof - 1, 'Specialization']
	specialization = spec.index(specialization)

	area = random.choice(areas[specialization])
	thesis_areas.append(area)
	thesis_title.append(area + ' ' + str(random.choice([i for i in range(1, 101)])))

student_ids = random.sample(student_ids, len(student_ids))
write_csv('thesis.csv', ['Id', 'Student_id', 'Professor_id', 'Area', 'Title'], [ids, student_ids, professor_ids, thesis_areas, thesis_title])
