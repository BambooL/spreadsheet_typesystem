import parser
import re
from itertools import chain, imap

class t:
  def __init__(self, value):
    self.value = value
    self.children = []
  def __iter__(self):
    for v in chain(*imap(iter, self.children)):
      yield v
    yield self.value
 
def check_and(key, store):
	global store_header
	store_header = store
	headers = store_header[key]
	allheaders = []
	if (len(headers) == 1):
		return True
	for i in range(len(headers) - 1):
		if headers[i] == "1":
			continue
		if type(headers[i]) is list:
			if (check_or(headers[i])):
				continue
			else:
				return False
		for j in range(i + 1, len(headers) - i):
			if headers[j] == '1':
				continue
			if type(headers[j]) is list:
				if (check_or(headers[j])):
					continue
				else:
					return False
			if common_ancestor(headers[i], headers[j]):
				return False
	return True

def check_or(headers):	
	for i in range(len(headers)):
		for j in range(len(headers) - i):
			if common_ancestor(headers[i], headers[j]):
				continue
			else:
				return False
	return True

# {B3:[A2, C1],  B2:[B1],  A2:[A1], C1:[1], A1:[1]}  common_ancestor(B3, B2) -> False
# {B3:[A3],  B2:[B1, A1],  B1:[1], A3:[A2], A2: [A1], A1:[1]} common_ancestor(B3, B2) -> True
def common_ancestor(cell1, cell2):
	global list1 
	global list2 
	list1 = []
	list2 = []
	add_node1(cell1)
	add_node2(cell2)
	return intersect(list1, list2)

def add_node1(cell1):
	if (cell1 in store_header.keys()):
		for item in store_header[cell1]:
			if item != "1":
				list1.append(item)
			add_node1(item)
	else:
		return
			
def add_node2(cell1):
	if (cell1 in store_header.keys()):
		for item in store_header[cell1]:
			if item != "1":
				list2.append(item)
			add_node2(item)
	else:
		return

def intersect(a, b):
    if (len(list(set(a) & set(b))) != 0):
    	return True
    else:
    	return False
