import parser

# imput: =SUM((A:A 1:1))
# output 
# SUM <function> <start>
#     B5:B15 <operand> <range>
#  <function> <stop>
def checker(wb, relation_table):
	p = ExcelParser()
	for cell in wb:
		formula = p.parser(i)
		# 




