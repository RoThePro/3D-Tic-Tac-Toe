import random
import itertools
import math

class coor:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)

magicCube = [
[
	[8,24,10],
    [12,7,23],
    [22,11,9]
],
[
	[15,1,26],
	[25,14,3],
	[2,27,13]
],
[
	[19,17,6],
	[5,21,16],
	[18,4,20]
]
]

center = [coor(1,1,1)]
corners = [coor(0,0,0),coor(0,2,0),coor(2,0,0),coor(2,2,0),coor(0,0,2),coor(2,0,2),coor(0,2,2),coor(2,2,2)]
edges = [coor(0,0,1),coor(0,1,0),coor(0,1,2),coor(0,2,1),coor(0,1,1),coor(2,0,1),coor(2,1,0),coor(2,1,2),coor(2,2,1),coor(2,1,1),coor(1,0,0),coor(1,0,1),coor(1,0,2),coor(1,1,0),coor(1,1,2),coor(1,2,0),coor(1,2,1),coor(1,2,2)]

compCoor = []
playerCoor = []

def compPlay():

	if(len(compCoor)>=2):
		for combos in list(itertools.combinations(compCoor, 2)):
			chance = 42 - (magicCube[combos[0].z][combos[0].y][combos[0].x] + magicCube[combos[1].z][combos[1].y][combos[1].x])
			for i in range(len(magicCube)):
				for j in range(len(magicCube)):
					if(chance in magicCube[i][j]):
						coordinate = coor(magicCube[i][j].index(chance),j,i)
						if(coordinate in center):
							center.remove(coordinate)
							compCoor.append(coordinate)
							return
						elif(coordinate in corners):
							corners.remove(coordinate)
							compCoor.append(coordinate)
							return
						elif(coordinate in edges):
							edges.remove(coordinate)
							compCoor.append(coordinate)
							return
						else: 
							pass

	if(len(playerCoor)>=2):
		for combos in list(itertools.combinations(playerCoor, 2)):
				chance = 42 - (magicCube[combos[0].z][combos[0].y][combos[0].x] + magicCube[combos[1].z][combos[1].y][combos[1].x])
				for i in range(len(magicCube)):
					for j in range(len(magicCube)):
						if(chance in magicCube[i][j]):
							coordinate = coor(magicCube[i][j].index(chance),j,i)
							if(coordinate in center):
								center.remove(coordinate)
								compCoor.append(coordinate)
								return
							elif(coordinate in corners):
								corners.remove(coordinate)
								compCoor.append(coordinate)
								return
							elif(coordinate in edges):
								edges.remove(coordinate)
								compCoor.append(coordinate)
								return
							else: 
								pass

	if(len(center)>0):
		compCoor.append(center[0])
		center.pop(0)
		return
	elif(len(corners)>0):
		coordinate = random.choice(corners)
		compCoor.append(coordinate)
		corners.remove(coordinate)
		return
	elif(len(edges)>0):
		coordinate = random.choice(edges)
		compCoor.append(coordinate)
		edges.remove(coordinate)
		return
	else:
		return

def playerPlay():	
	while True:
		num = input("Which square would you like to pick? ")
		sudo_num = num-1

		z = int(math.floor((sudo_num)/9))
		sudo_x = 9 if num%9==0 else num%9
		x = (sudo_x-1)%3
		y = int(math.floor(int(sudo_x-1)/3))
		coordinate = coor(x,y,z)

		if(coordinate in center):
			center.remove(coordinate)
			playerCoor.append(coordinate)
			return
		elif(coordinate in corners):
			corners.remove(coordinate)
			playerCoor.append(coordinate)
			return
		elif(coordinate in edges):
			edges.remove(coordinate)
			playerCoor.append(coordinate) 
			return

		print "Pick another square!"

def printCoor(coor):
	print str(coor.x) + " " + str(coor.y) + " " + str(coor.z)


def check():
	if(len(playerCoor)>=3):
		for combos in list(itertools.combinations(playerCoor, 3)):
			sum = 0
			for combo in combos:
				sum+=magicCube[combo.x][combo.y][combo.z]
			if(sum == 42):
				print "WON!!!!!!"
				return True

	if(len(compCoor)>=3):
		for combos in list(itertools.combinations(compCoor, 3)):
			sum = 0
			for combo in combos:
				sum+=magicCube[combo.x][combo.y][combo.z]
			if(sum == 42):
				print "LOST!!!!!!"
				return True

	if(len(corners) == 0 and len(center) == 0 and len(edges) == 0):
		print "Tie"
		return True

	return False

def render():
	print 'Computer points'
	for coordinate in compCoor:
		print str(coordinate.x) + " " + str(coordinate.y) + " " + str(coordinate.z)
	print 'Player points'
	for coordinate in playerCoor:
		print str(coordinate.x) + " " + str(coordinate.y) + " " + str(coordinate.z)

def render():
	for i in range(3):	
		print "Layer " + str(i+1)
		spaces = [" "," "," "," "," "," "," "," "," "]
		for coordinate in compCoor:
			if(coordinate.z==i):
				spaces[3*(coordinate.y)+coordinate.x] = "X"
			
		for coordinate in playerCoor:
			if(coordinate.z==i):
				spaces[3*(coordinate.y)+coordinate.x] = "O"

		print("{0} | {1} | {2}".format(spaces[0],spaces[1],spaces[2]))
		print("---------")
		print("{0} | {1} | {2}".format(spaces[3],spaces[4],spaces[5]))
		print("---------")
		print("{0} | {1} | {2}".format(spaces[6],spaces[7],spaces[8]))

def intro():
	print "Welcome to the game of Computer Tic Tac Toe!!!!"
	print "Use this numbering system when inputing your move. \n"
	for i in range(3):
		spaces=[" "," "," "," "," "," "," "," "," "]
		print "Layer " + str(i+1)
		for j in range(9):	
			spaces[j]=str((i*9)+j+1)
		print("{0} | {1} | {2}".format(spaces[0],spaces[1],spaces[2]))
		print("---------")
		print("{0} | {1} | {2}".format(spaces[3],spaces[4],spaces[5]))
		print("---------")
		print("{0} | {1} | {2}".format(spaces[6],spaces[7],spaces[8]))
		print "\n\n"


def main():
	intro()
	while True:
		print "Computer move"
		compPlay()
		render()
		if(check()):
			break
		playerPlay()
		print "\nPlayer move"
		render()
		if(check()):
			break

main()


'''
num = input()

sudo_num = num-1
z = int(math.floor((sudo_num)/9))
print z
sudo_y = 9 if num%9==0 else num%9
y = (sudo_y-1)%3
print y
x = int(math.floor(int(sudo_y-1)/3))
print x



print str(x) + " " + str(y) + " " + str(z)
print magicCube[z][y][x]

for i in range(3):
	for j in range(3):
		for k in range(3):
			print str(i) + "," + str(j) + "," + str(k)
			print magicCube[i][j][k]

'''