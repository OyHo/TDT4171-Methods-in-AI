__author__ = 'ultracakes'

from math import log
import random
from drawtree import draw_level_order
from drawtree import draw_bst
import array

target = -1
check = "test.txt"
train = "training.txt"


class node():
	def __init__(self, info):
		self.info = info
		self.children = {}

	def printTree(self):
		a = []
		if len(self.children) == 0:
			a.append(self.info)
		else:
			a.append(self.info)

		for key, test in self.children.items():
			a.append(self.children[key].printTree())

		return a

	def printTreeTest(self):
		if len(self.children) == 0:
			return str(self.info)
		else:
			temp = str(self.info)

		for key, test in self.children.items():
			temp += self.children[key].printTree()

		return temp

#from textbook
def deciciontreelearning(examples, attributes, parent_examples, importance_choose):
	if not examples:
		return node(pluralityvalue(parent_examples))
	elif sameClassification(examples):
		return node(examples[0][target])
	elif not attributes:
		return node(pluralityvalue(examples))
	else:
		if importance_choose:
			A = importance(examples, attributes)
		else:
			A = randomattributes(attributes)
		tree = node(A)
		for v in range(1,3):
			exs = []
			for e in examples:
				if int(e[A]) == v:
					exs.append(e)
			subtree = deciciontreelearning(exs, attributes, examples, importance_choose)
			tree.children[v] = subtree
	return tree

#from textbook
def entropy(info, attribute):
	pos = 0
	if len(info) == 0:
		return 0
	for i in info:
		if i[attribute] == info[0][attribute]: #positive attribute
			pos+=1
	return B(pos/len(info))


def importance(info, attributes):
	entro = {}
	for attribute in attributes:
		entro[attribute] = entropy(info,attribute)

	minval = 1
	for e in entro:
		if entro[e] < minval:
			minval = entro[e]
			chosenattribute = e
	return chosenattribute

#from textbook
def B(q):
	if q == 0 or q == 1:
		return q
	else:
		return -(q*math.log(q,2) + (1-q)*math.log((1-q),2))


def randomattributes(attributes):
	return attributes[random.randint(0, len(attributes)-1)]


def sameClassification(examples):
	target = -1
	classzero = examples[0][target]
	#for e in examples:
	for e in range(1,len(examples)):
		if examples[e][target] != classzero:
			return False
	return True


def pluralityvalue(examples):
	firstclass, secondclass = 0,0
	for e in examples:
		if examples[target] == '1': #examples[7] or examples[-1]
			firstclass += 1
		else:
			secondclass += 1
	if firstclass > secondclass:
		return 1
	else:
		return 2


def classify(node, example):
	while node.children:
		node = node.children[int(example[node.info])]
	return node.info


def testing(tree, info):
	match = 0
	for example in info:
		if example[target] == classify(tree, example):
			match += 1
	print "Tests matching: ",match


def read(filename):
	lines = []
	file = open(filename,'r')
	for l in file.readlines():
		l = l.replace("\n", "")
		l = l.replace("\t", "")
		lines.append(l)
	return lines


def main():
	checkInfo = read(check)
	trainInfo = read(train)
	attr = [x for x in range(len(trainInfo[0])-1)]
	print "Total tests: ",len(checkInfo)
	print attr
	print "Using random attributes: "
	tree = deciciontreelearning(trainInfo, attr, [], False)
	testing(tree, checkInfo)
	print tree.printTree()
	print "Using importance function: "
	tree = deciciontreelearning(trainInfo, attr, [], True)
	testing(tree, checkInfo)

	wut = tree.printTree()
	print wut
	#wuttree = "".join(wut)
	#draw_level_order(wuttree)
	#print [i for i, j in enumerate(wut) if j == '#']
	#for i in wut:
	#	if i == '#':
	#		print i
	#draw_level_order('{3,9,20,#,#,15,7}')
	draw_level_order('{0,1,1,#,#,2,2,1,2,2,1}')

	newlist = []
	#for i in wut:
	#	#if isinstance(i, int):
	#	#	newlist = i
	#	print i
	#	newlist.append(i)
	#print newlist
	#results = map(int, newlist)
	#print results

main()