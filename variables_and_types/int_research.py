#int_research.py
#gold task: researching what strings int() can convert
#1 and 2. predict and write in comments why they work or fail:
#ستعمل  بنجاح : لان بايثون يتجنب المسافات الفارغة المحيطة بالرقم تلقائيا 
print(int( " 22 "))
#predict: works. reason: python accepts optional sign indicators (+or-) before digits.
print(int("+22"))
#predict: works. reason: leading zeros in a string are handled correctly by int()
print(int("0022"))
#predict: works. reason: underscores are allowed in numeric literals for readability
print(int("2_2"))
#4.cite: the address of the official python documentation page used:
#decumentation link: https://docs.python.org/3/library/functions.html#int
