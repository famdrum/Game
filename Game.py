#File: game.py
#A battleship game


def read_field(fieldname):
	"""
	(str) --> (data)

	Reads the field from the file
	"""
	with open(fieldname, 'r') as text:
		data = text.read()
	lst = [i for i in data if not i == '\n']
	st= {}
	count = 1
	while not lst == []:
		st[count] = []
		for i in range(10):
			st[count].append(lst[0])
			lst.remove(lst[0])
		count += 1
	return st


def has_ship(fieldname, aim):
	"""
	(tuple) --> (bool)

	Return the answer whether you striked
	"""
	import string
	st = read_field(fieldname)
	x,y = aim
	return st[y][string.ascii_letters.index(x.lower())] == '*'


def ship_size(fieldname, aim):
	"""
	(tuple) --> (tuple)

	Returns size of the specified ship

	>>> ship_size(('C', 3))
	(1, 3)
	"""
	import string
	x,y = aim
	st = read_field(fieldname)
	counter = 0
	var = string.ascii_letters.index(x.lower())
	for i in range(var, 10):
		if st[y][i] == '*':
			counter += 1
		else:
			break
	for i in range(var - 1, 0, -1):
		if st[y][i] == '*':
			counter += 1
		else:
			break
	if counter == 1:
		counter = 0
		for i in range(y, 10):
			if st[i][string.ascii_letters.index(x.lower())] == '*':
				counter += 1
			else:
				break
		for i in range(y - 1, 0, -1):
			if st[i][string.ascii_letters.index(x.lower())] == '*':
				counter += 1
			else:
				break
		return (1, counter)
	else:
		return (1, counter)


def is_valid(fieldname):
	"""
	(data) --> (bool)

	Checks your field
	"""
	with open(fieldname, 'r') as text:
		data = text.read()
	lst = [i for i in data if not i == '\n']
	if len(lst) != 100:
		print(len(lst))
		return False
	st = read_field(fieldname)
	for i in range(1, 11):
		if len(st[i]) != 10:
			len(st[i])
			return False
	for i in st:
		c = 0
		for k in st[i]:
			if k == '*':
				c += 1
			if k == ' ':
				c = 0
			if c > 4:
				return False
	for i in range(10):
		c = 0
		for k in st:
			if st[k][i] == '*':
				c += 1
			if st[k][i] == ' ':
				c = 0
			if c > 4:
				return False
	return True


def field_to_str(fieldname):
	"""
	(data) --> (str)

	Transforms your data into str
	"""
	st = read_field(fieldname)
	fin = ""
	for i in st:
		for k in st[i]:
			fin += k
		fin += '\n'
	return fin


def generate_field():
	"""
	() --> (data)

	Generates a game field
	"""
	import random
	map_choice = [1, 2, 3, 4, 5]
	return read_field(('map{}.txt').format(str(random.choice(map_choice))))
