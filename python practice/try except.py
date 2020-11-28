# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:35:19 2020

@author: Administrator
"""
#Error 발생 전까지는 정상적으로 작동하고 error 가 발생되는 Exception을 만나면 except로 가서 실행함
#But in try section if there was no error then try section is performed and else
#section is performed as well.
try:
    print(2)
    x=int(input('x에 넣을 값을 입력하시오'))
#raise 
    if x%3==0:
        raise Exception('x는 3의 배수입니다.')
    
    print(3)
   
    print(5)
#I can determine which error i want to check
except Exception:
    print('x는 3의 배수입니다 exception')
#if in try section no error occured
else:
    print('else')
#After process is performed 
#No matter what result was get in before processes
#그냥 finally 없이 써도 되는거 아닌가
finally:
    print(3)