#####Insertion Sort- Part 1 (1)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    curr_min=arr[n-1] 
    for i in range(n-1,0,-1):
        if arr[i-1]>curr_min:
            arr[i]=arr[i-1]
            print(" ".join(map(str, arr)))
        else:
            arr[i]=curr_min
            print(" ".join(map(str, arr)))
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


####Number Line Jumps (2)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1<x2 and v1<v2: return('NO')
    if x1==x2 and v1==v2: return('YES')
    if x1<x2 and v1>v2 and (x2-x1)%(v1-v2)== 0:return('YES')
    if x1>x2 and v1<v2 and (x1-x2)%(v2-v1) == 0:return('YES')
    else:return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


###Birthday Cake Candles (3)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    massimo=max(candles)
    count=0
    for i in range(len(candles)):
        if candles[i]==massimo: count+=1
    return(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


###collections.Counter (4)
from collections import Counter
N_scarpe=int(input())
size=Counter(map(int, input().split()))
N_clienti=int(input())
size_richiesta_e_prezzo=[list(map(int, input().split())) for i in range(N_clienti)]
incasso=0
for taglia, prezzo in size_richiesta_e_prezzo:
    if size[taglia]>0:
        incasso+=prezzo
        size[taglia]-=1

print(incasso)

###Concatenate (5)
import numpy
N,M,P=map(int, input().split())
array1=numpy.array([list(map(int,input().split())) for i in range(N)])
array2=numpy.array([list(map(int,input().split())) for i in range(M)])
print(numpy.concatenate((array1, array2),axis=0))


###Transpose and Flatten (6)
import numpy as np 
N,M=map(int, input().split())
my_array=np.array([list(map(int, input().split()))
  for i in range(N)])
print (np.transpose(my_array))
print (my_array.flatten())


###Arrays (7)
import numpy

def arrays(arr):
    r=numpy.array(list(reversed(arr)),float)
    return r

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

###Set.add() (8)
n=int(input())
paesi=set()
for i in range(n):
    paese=input()
    paesi.add(paese)
print(len(paesi))

###Symmetric Difference (9)
int1=input()
a=set(map(int, input().split()))
int2=input()
b=set(map(int, input().split()))
s=a.union(b)
I=a.intersection(b)
for i in I:
    s.remove(i)
s=sorted(s)
for i in s:
    print(i)

###Introduction to Sets (10)
def average(array):
    return(sum(set(array))/len(set(array)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

###The Minion Game (11)
def minion_game(string):
    K_score=0
    S_score=0
    elenco=list()
    n=len(string)
    
    for i in range(n):
        for j in range(i+1, n+1):
            elenco.append(string[i:j])
    
    for i in elenco:
        if i[0] in "AEIOU":
            K_score=K_score+1
        else: S_score=S_score+1
    
    if K_score>=S_score: print(f"Kevin {K_score}")
    if K_score==S_score:print("Draw")
    else: print(f"Stuart {S_score}")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)

###Capitalize! (12)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    v=s.split(' ')
    for i in range(len(v)):
        v[i]=v[i].capitalize()
    return(' '.join(v))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


###sWAP cASE (13)
def swap_case(s):
    return(s.swapcase())

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

###Text Wrap (14)
import textwrap

def wrap(string, max_width):
    s=list(string)
    count=0
    for i in range(max_width,len(string),max_width):
      s.insert(i+count,'\n')
      count=count+1
    string=''.join(s)
    return(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

###Text Alignment (15)
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
    

###String Validators (16)
if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
      if s[i].isalnum(): 
        print(True) 
        break
      if i==len(s)-1: print(False)
    
    for i in range(len(s)):
      if s[i].isalpha():
        print(True) 
        break
      if i==len(s)-1: print(False)
    
    for i in range(len(s)):
      if s[i].isdigit():
        print(True)
        break
      if i==len(s)-1: print(False)
    
    for i in range(len(s)):  
      if s[i].islower():
        print(True)
        break 
      if i==len(s)-1: print(False)
    
    for i in range(len(s)):
      if s[i].isupper():
        print(True) 
        break
      if i==len(s)-1: print(False)
    

###Find a string (17)
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:(i+len(sub_string))]==sub_string:
            count=count+1

    return (count)

if __name__ ==
  string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

###Mutations (18)
def mutate_string(string, position, character):
    string=string[:position]+character+string[position+1:]
    return(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

###What's Your Name? (19)
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print('Hello', first,last+'! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

###String Split and Join (20)
def split_and_join(line):
    line=line.split(" ")
    return("-".join(line))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

###Nested Lists (21)
if __name__ == '__main__':
    name=[]
    score=[]
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    
    m=min(score)
    
    i=score.index(m)
    
    score.pop(i)
    name.pop(i)
    
    for j in range(len(name)):
        if score[j]==m:
            score.pop(j)
            name.pop(j)
     
    m2=min(score)
    risultato=[]
    
    for j in range(len(name)):
        if score[j]==m2: risultato.append(name[j])
    
    risultato=sorted(risultato,key=str.casefold)
    
    for j in range(len(risultato)):
        print(risultato[j])

###Finding the percentage (22)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    media=sum(student_marks[query_name])/3
    print(f"{media:.2f}")

###List Comprehensions (23)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    t=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
              if i+j+k!=n:
                t.append([i,j,k])
    print(t)
              
        
###Find the Runner-Up Score! (24)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a2=set(arr)
    a2.remove(max(a2))
    print(max(a2))

###Python If-Else (25)
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2==1:
        print("Weird")
    
    else:
        if n in range(2,6): print("Not Weird")
        elif n in range(6,21): print("Weird")
        else: print("Not Weird")

###Print Function (26)
if __name__ == '__main__':
    n = int(input())
    l=list(range(1,n+1))
    for i in range(n):
      l[i]=str(l[i])
    print("".join(l))
    
###Write a function (27)
def is_leap(year):
    leap = False

    if year%100==0:
      if year%400==0:
        leap=True
        return leap
      else: return leap
    
    elif year%4==0: 
      leap=True
      return leap
    
    else: return leap
      

year = int(input())
print(is_leap(year))

###Loops (28)
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

###Python: Division (29)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

###Arithmetic Operators (30)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

###Say "Hello, World!" With Python (31)
my_string = "Hello, World!"
print(my_string)


