from KGramHash import KGramHash
from Detect import Detect
from ReadCode import ReadCode

operationHash = {}
idx = 0

def update(operation):
    global idx
    if operation not in operationHash:
        operationHash[operation] = idx
        idx += 1

o1 = ReadCode("Code\Fib1.java")
operations = o1.extract()
for operation in operations:
    update(operation)
str1 = ("A", operations)

o2 = ReadCode("Code\Fibonacci3.java")
operations = o2.extract()
for operation in operations:
    update(operation)
str2 = ("B", operations)

o3 = ReadCode("Code\Fibonacci4.java")
operations = o3.extract()
for operation in operations:
    update(operation)
str3 = ("C", operations)

o = Detect((str1, str2, str3), 3, 4, operationHash)
o.get_pairwise()