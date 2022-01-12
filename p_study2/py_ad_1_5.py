"""
Chapter1 Advanced(1) - Context Manager(2)
Keyword - Contextlib, __endter__, __exit__
"""
"""
Contextlib - Measure  execution(타이머) 제작
"""

# Ex1
# Use Class
import time


class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return f"{self._start}초"

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:  # 예외가 발생하면
            print(f"Logging exception {(exc_type, exc_value, exc_traceback)}")
        else:
            print(f"{self._msg} : {time.monotonic() - self._start} s")
        return True  # 잘 마무리 했다라고 명시해주기


with ExcuteTimer("걸린시간") as v:
    print(f"Received start monotonic1 : {v}")

    # Excute job, 테스트 하고 싶은 내용을 여기에 작성
    for i in range(100000000):
        pass

    raise Exception("Raise! Exception!!")  # 강제로 발생
