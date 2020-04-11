import random
from helpers import write_csv

spec = ['Robotics', 'Algorithms', 'Semantics', 'Distributed Systems', 'Computer Graphics', 'Computer Architecture', 'Computer Systems']

ids = []
names = []
specializations = []
office_rooms = []

i = 0
with open('professors.txt', 'r') as f:
	for line in f.readlines():
		if len(line.strip()) > 20:
			continue
		i += 1
		ids.append(i)
		names.append(line.strip())
		specializations.append(random.choice(spec))

		dig1 = random.choice([i for i in range(1, 7)])
		dig2 = random.choice([i for i in range(1, 9)])
		office_rooms.append('PR' + str(dig1) + '0' + str(dig2))


write_csv('professors.csv', ['Id', 'Name', 'Specialization', 'Office'], [ids, names, specializations, office_rooms])
