memo_recursion={}
memo_iteration={}
def fibo_recursion(n):
    if n in memo:
        return memo[n]
    else:
        if n<=2:
            memo[n]=1
            return 1
        else:
            memo[n]=fibo(n-1)+fibo(n-2)
            return fibo(n-1)+fibo(n-2)
def fibo_iteration(n):
    for i in range(1,n+1):
        if i<=2:
            memo_iteration[i]=1
        else:
            memo_iteration[i]=memo_iteration[i-1]+memo_iteration[i-2]





fibo_iteration(1500)

print(memo_iteration[1500])