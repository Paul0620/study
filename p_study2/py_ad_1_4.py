"""
Chapter1 Advanced(1) - Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception
"""
"""
컨텍스트 매니저란? - 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할을 한다.
가장 대표적인 with 구문을 이해해야 한다.
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)
"""

# Ex1
file = open("./testfile1.txt", "w")
try:
    file.write("Context Manger Test1.\nContextlib Test1.")
finally:
    file.close()


# Ex2
# with문 안에서 close기능까지 다 가지고 있음.
with open("./testfile2.txt", "w") as f:
    f.write("Context Manger Test2.\nContextlib Test2.")


# Ex3
# Use Class -> Context Manager with exception handling
class MyfileWriter:
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print(f"Logging exception {(exc_type, value, trace_back)}")
            self.file_obj.close()


with MyfileWriter("./testfile3.txt", "w") as f:
    f.write("Context Manger Test3.\nContextlib Test3.")
