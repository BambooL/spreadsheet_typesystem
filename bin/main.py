import openpyxl
import parser
import os
import re
from openpyxl import Workbook
from openpyxl import load_workbook
import spatial
import checker
from openpyxl.formula import Tokenizer
import headerchecker

class Header_cell:
	def __init__(self, cell_type, cell_value):
        self.header = []
        self.type = cell_type
        self.value = cell_value

    def add_header(self, header):
    	self.header.append(header)

    def add_OR_header(self, cell_range):
		start = cell_range.split(":")[0]
		end = cell_range.split(":")[1]
		start_letter = re.findall('[a-zA-Z]+', start)[0]
		start_digit = re.findall('\d+', start)[0]
		end_letter = re.findall('[a-zA-Z]+', end)[0]
		end_digit = re.findall('\d+', end)[0]
		or_type = []
		if (int(end_digit) - int(start_digit) != 0 and start_letter == end_letter):
			for i in range(int(end_digit) - int(start_digit) + 1):
				or_type.append(start_letter + str(int(start_digit) + i))
    	self.header.append(or_type) 

if __name__ == "__main__":
	rootdir ='../data/alldata/'
	# loop inside the workbook
	for files in os.walk(rootdir):
		print type(files)
		folder = files[2]
		for i in range(len(folder)):
			if (re.search("xlsx", str(folder[i]))):
				wb = load_workbook(filename = rootdir + folder[i])
				for sheet in wb:
					store_header = {}
					problem_cell = []
					for cell in sheet:
						if (is_header(cell)):
							for sub_cell in following_column:
								store_header = update1(cell, sub_cell, store_header)
							for sub_cell in following_row:
								store_header = update1(cell, sub_cell, store_header)
						elif (cell.data_type = 'f'):
							tok = Tokenizer(cell._value)
							tok.parse()
							for token in tok.items:
								if (token.type == 'FUNC'):
									if (token.value == "AVERAGE(" or token.value == "SUM("):
										refrange = re.search(r'[A-Z][0-9]+\:[A-Z][0-9]+', cell._value)
										store_header = update2(cell, refrange, store_header)
									if (token.value == ""): # refer to other cell
										refcell =
										store_header = update1(cell, refcell, store_header)
					# {A5:A2, A2:A1} 
					for key, value in store_header.iteritems():
						if (headerchecker.check_and(key, store_header)):
							continue
						else:
							problem_cell.append(key)




def update1(cell, sub_cell, store_header):
	if sub_cell.coordinate in store_header.keys():
		store_header[sub_cell.coordinate] = store_header[sub_cell.coordinate].add_header(cell.coordinate)
	else:
		header = Header_cell(sub_cell.data_type, sub_cell._value)
		header.add_header(cell.coordinate)
		store_header[sub_cell.coordinate] = header
	return store_header

def update2(cell, refrange, store_header):
	if cell.coordinate in store_header.keys():
		store_header[cell.coordinate] = store_header[cell.coordinate].add_OR_header(refrange)
	else:
		header = Header_cell(cell.data_type, cell._value)
		header.add_OR_header(refrange)
		store_header[cell.coordinate] = header
	return store_header

def is_header(cell):
	if (cell)










				
