# 예제 9.3
def test(func):
    def new_function(*args,**kwargs):
        print("start")
        result = func(*args,**kwargs)
        print(result)
        print("end")
    return new_function

@test
def add(a,b):
    return a + b
add(1,2)

#예제 9.4
class OopsException(Exception):
    print("Caught an oops")
try:
    raise OopsException
except OopsException as exc:
    print(exc)
