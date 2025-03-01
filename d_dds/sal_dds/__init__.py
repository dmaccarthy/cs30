from random import randint, choice

def randchar():
    "Return a random character"
    return chr(ord(choice(['a', 'A'])) + randint(0, 25))

def randstr(c=None):
    s = ""
    if c is None: c = randint(1, 16)
    for c in range(c):
        s += randchar()
    return s

names = ['Liam', 'Olivia', 'Benjamin', 'Emma', 'Lucas', 'Sophia', 'Oliver',
	'Ava', 'Noah', 'Emily', 'William', 'Charlotte', 'Ethan', 'Amelia', 'Jack',
	'Abigail', 'Lincoln', 'Chloe', 'Owen', 'Aria', 'Jacob', 'Grace', 'Isabella',
	'Alexander', 'James', 'Logan', 'Avery', 'Elizabeth', 'Hunter', 'Lily',
	'Nathan', 'Hannah', 'Carter', 'Ella', 'Grayson', 'Henry', 'Ellie', 'Quinn',
	'Scarlett', 'Isaac', 'Mason', 'Anna', 'Jackson', 'Harper', 'Gabriel',
	'Hailey', 'Daniel', 'Luke', 'Brooklyn', 'Evelyn', 'Samuel', 'Wyatt', 'Isla',
	'Mia', 'Connor', 'Sarah', 'Hudson', 'Claire', 'Bennett', 'Elijah', 'Madison',
	'Mila', 'Joshua', 'Victoria', 'Thomas', 'Addison', 'Caleb', 'Emmett',
	'Natalie', 'Zoey', 'Adam', 'Hazel', 'Matthew', 'Eva', 'Maya', 'David',
	'Zachary', 'Isabelle', 'Michael', 'Sadie', 'Sophie', 'Aiden', 'Jaxon',
	'Everly', 'Sofia', 'Violet', 'Ryan', 'Austin', 'Jayden', 'John', 'Ivy',
	'Paisley', 'Max', 'Brielle', 'Zoe', 'Parker', 'Levi', 'Aubrey', 'Leo',
	'Theodore', 'Nora', 'Audrey', 'Asher', 'Stella', 'Cooper', 'Sebastian',
	'Aurora', 'Alice', 'Dominic', 'Gavin', 'Nolan', 'Piper', 'Kinsley', 'Julia',
	'Naomi', 'Ruby', 'Willow', 'Joseph', 'Eli', 'Blake', 'Harrison', 'Ryker',
	'Sawyer', 'Layla', 'Samantha', 'Mackenzie', 'Brody', 'Clara', 'Leah', 'Maria',
	'Penelope', 'Riley', 'Dylan', 'Evan', 'Marcus', 'Andrew', 'Charles', 'Ryder',
	'Lillian', 'Alexandra']

surnames = ['Smith', 'Brown', 'Tremblay', 'Martin', 'Roy', 'Wilson', 'Macdonald', 
	'Gagnon', 'Johnson', 'Taylor', 'Cote', 'Campbell', 'Anderson', 'Leblanc', 
	'Lee', 'Jones', 'White', 'Williams', 'Miller', 'Thompson', 'Gauthier', 'Young', 
	'Van', 'Morin', 'Bouchard', 'Scott', 'Stewart', 'Belanger', 'Reid', 'Pelletier', 
	'Moore', 'Lavoie', 'King', 'Robinson', 'Levesque', 'Murphy', 'Fortin', 'Gagne', 
	'Wong', 'Clark', 'Johnston', 'Clarke', 'Ross', 'Walker', 'Thomas', 'Boucher', 
	'Landry', 'Kelly', 'Bergeron', 'Davis', 'Mitchell', 'Murray', 'Poirier', 'Mcdonald',
	'Richard', 'Wright', 'Girard', 'Lewis', 'Baker', 'Roberts', 'Simard', 'Graham', 
	'Caron', 'Harris', 'Jackson', 'Green', 'Beaulieu', 'Fraser', 'Fournier', 'Kennedy',
	'Hall', 'Hill', 'Chan', 'Wood', 'Lapointe', 'Ouellet', 'Bell', 'Dube', 'Allen', 
	'Adams', 'Cloutier', 'Bennett', 'Lefebvre', 'Watson', 'Robertson', 'Walsh',
	'Collins', 'Evans', 'Hebert', 'Hamilton', 'Cameron', 'Desjardins', 'Russell',
	'Nadeau', 'Cook', 'Michaud', 'Morrison', 'Singh', 'Grant', 'Parsons']

def surname(**k): return choice(surnames)
def givenname(**k): return choice(names)
