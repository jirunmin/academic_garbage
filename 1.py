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

o1 = ReadCode("Code\centralCore.java")
operations = o1.extract()
for operation in operations:
    update(operation)
print(operations)
str1 = ("A", operations)

o2 = ReadCode("Code\centralCore_Copy.java")
operations = o2.extract()
for operation in operations:
    update(operation)
# print(operations)
str2 = ("B", operations)

o3 = ReadCode("Code\centralCoreOther.java")
operations = o3.extract()
for operation in operations:
    update(operation)
# print(operations)
str3 = ("C", operations)

o4 = ReadCode("Code\centralCoreOther_Copy.java")
operations = o4.extract()
for operation in operations:
    update(operation)
#print(operations)
str4 = ("D", operations)

# o = Detect((str1, str2, str3, str4), 3, 4, operationHash)
# o.get_pairwise()