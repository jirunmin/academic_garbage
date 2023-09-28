from KGramHash import KGramHash
from Detect import Detect
from ReadCode import ReadCode

# str1 = ("A", "yabbadabbadoo")
# str2 = ("B", "scoobydoobydoo")
# str3 = ("C", "doobeedoobeedoo")

# o = Detect((str1, str2, str3), 3, 4)
# o.get_pairwise()


o1 = ReadCode("Code\Fib1.java")
print(o1.extract())
# print(KGramHash(3, o1.extract()).get_hashes())

o2 = ReadCode("Code\Fibonacci3.java")
print(o2.extract())

o3 = ReadCode("Code\Fibonacci4.java")
print(o3.extract())
