string=list(input())
zero_nine=[str(i) for i in range(1,10)]
def huwi(string,zero_nine):
    calc_stack = []
    result = []
    nums = []
    temp=[]
    sign=0
    for ch in string:
        
    for ch in string:
        if sign==1 :
            if ch != ')':
                temp.append(ch)
            elif ch == ')':
                sign=0
                call_num=huwi(temp,zero_nine)
                temp=[]
                if nums == []:
                    nums.append(call_num)
                elif nums != [] and calc_stack[-1] in '*/':
                    nums.append(call_num)
                    result.extend(nums)
                    result.append(calc_stack.pop())
                    nums = []
                elif nums != [] and calc_stack[-1] in '+-':
                    result.extend(nums)
                    nums = []
                    nums.append(call_num)


        elif sign==0:

            if ch in zero_nine:
                if nums==[]:
                    nums.append(ch)
                elif nums!=[] and calc_stack[-1] in '*/':
                    nums.append(ch)
                    result.extend(nums)
                    result.append(calc_stack.pop())
                    nums=[]
                elif nums!=[] and calc_stack[-1] in '+-':
                    result.extend(nums)
                    nums=[]
                    nums.append(ch)
            elif ch in '*/+-':
                calc_stack.append(ch)
            elif ch in '(':
                sign=1
    result.extend(nums)
    while calc_stack:
        result.append(calc_stack.pop())
    return result
result=huwi(string,zero_nine)
def print_recursive(result):
    for re in result:
        if type(re)==type('a'):
            print(re,end='')
        elif type(re)==type([1,2,3]):
            print_recursive(re)
print_recursive(result)



