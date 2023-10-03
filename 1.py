from MainProcedure import MainProcedure

o = MainProcedure("Code")
ans = o.start(50)

# for (key, similarity) in ans:
#     print(key, ": ", '{:.3%}'.format(similarity))  # 打印文档对和匹配信息