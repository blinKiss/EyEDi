def func_test(): #인자값을 멀티가능
    print('헬로우 사용자함수')

def func_test2(x, y): 
    print('헬로우 사용자함수')
    rst = x + y
    return rst

# 리턴값이 없으면 일만하는 함수
func_test()
# 리턴값이 있으면 일하고 반환하는 함수
z = func_test2(100,200)
print('리턴값출력', z)
    
    