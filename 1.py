from KGramHash import KGramHash
from Detect import Detect
from ReadCode import ReadCode

# str1 = ("A", "yabbadabbadoo")
# str2 = ("B", "scoobydoobydoo")
# str3 = ("C", "doobeedoobeedoo")

# o = Detect((str1, str2, str3), 3, 4)
# o.get_pairwise()

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
o = KGramHash(3, operations, operationHash)
print(o.extract(4))

o2 = ReadCode("Code\Fibonacci3.java")
operations = o2.extract()
for operation in operations:
    update(operation)
o = KGramHash(3, operations, operationHash)
print(o.extract(4))

o3 = ReadCode("Code\Fibonacci4.java")
operations = o3.extract()
for operation in operations:
    update(operation)
o = KGramHash(3, operations, operationHash)
print(o.extract(4))