import subprocess
import os
import re
import shutil

class ReadCode:
    def __init__(self, filename):
        self.filename = filename

        self.replacement_dict = {
        'iconst': 'iPUSH',  
        'bipush': 'iPUSH',
        'sipush': 'iPUSH',
        'ldc': 'iPUSH',
        'ldc2_w': 'iPUSH',
        'aload': 'aLOAD',
        'iload': 'iLOAD',
        'if_icmpgt': 'iIFCMP',
        'if_icmpge': 'iIFCMP',
        'if_icmpeq': 'iIFCMP',
        'ireturn': 'iRETURN',
        'isub': 'iSUB',
        'iadd': 'iADD',
        'goto': 'GOTO'
        }
    
    def decompilation(self):
        java_source_file = self.filename

        try:
            subprocess.run(["javac", java_source_file], check=True)

            # 获取编译后的 .class 文件的路径
            class_file_name = os.path.splitext(java_source_file)[0] + ".class"
            class_file_path = os.path.abspath(class_file_name)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

        return class_file_path

    def transform(self):
        java_class_file = self.decompilation()

        # 使用 javap 工具获取汇编代码
        try:
            result = subprocess.run(["javap", "-c", java_class_file], stdout=subprocess.PIPE, text=True, check=True)
            assembly_code = result.stdout

        except subprocess.CalledProcessError as e:
            print("Error:", e)


        shutil.move(java_class_file, "Code\out", copy_function=shutil.copy2)
        return assembly_code
    
    def extract(self):
        decompileCode = self.transform()

        # 使用正则表达式提取每个命令的操作部分
        pattern = r'\d+: (.+?)\s+'  # 匹配操作部分
        operations = re.findall(pattern, decompileCode)
        
        
        pattern = r'\w+_\w+'
        # 打印提取的操作
        for i, operation in enumerate(operations):
            operations[i] = self.simplification(operation)
             
        return operations

    def simplification(self, operation):

        if '_' in operation:
            idx = operation.index('_')
            sub_s=operation[idx:]
            flag=False
            for elem in ('0','1','2','3','4','5','6','7','8','9'):
                if elem in sub_s:
                    flag=True
            if flag:
                operation = operation[0:idx]


        for old_instr, new_instr in self.replacement_dict.items():
            if operation.startswith(old_instr):
                return operation.replace(old_instr, new_instr)
        return operation  # 如果没有匹配的替换规则，则保持不变

