import random
from helpers import write_csv

cities_list = []
with open('cities.txt', 'r') as f:
	for line in f.readlines():
		cities_list.append(line.strip())


ids = []
names = []
cities = []
lives_in_campus = []

i = 0
with open('students.txt', 'r') as f:
	for line in f.readlines():
		if len(line.strip()) > 20:
			continue
		i += 1
		ids.append(i)
		names.append(line.strip())
		cities.append(random.choice(cities_list))
		lives_in_campus.append(random.choice([True, False]))


write_csv('students.csv', ['Id', 'Name', 'City', 'Lives in campus'], [ids, names, cities, lives_in_campus])
