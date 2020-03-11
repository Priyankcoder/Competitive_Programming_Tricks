''' 
fast I/O methods in python for competitive programming:

In competitive programming it is important to read the input as fast as possible so we don’t lose valuable 
time. We can test our input and output methods on the problem INTEST – Enormous Input Test on SPOJ. 
Before you keep on reading I encourage you to solve the problem first.

– Bad way:

The program below uses input and print and gets the verdict time limit exceeded.'''

def main():
    n, k = [int(c) for c in input().split()]
    cnt = 0
    for _ in range(n):
        t = int(input())
        if t % k == 0:
            cnt += 1
    print(cnt)
 
if __name__ == "__main__":
    main()    

'''
+ Good way:

Instead of input and print we should use stdin.readline() and stdout.write(). The program below 
gets accepted with a runtime of 2.36 seconds.
'''

from sys import stdin, stdout 
 
def main():
    n, k = [int(c) for c in input().split()]
    cnt = 0
    for _ in range(n):
        t = int(stdin.readline())
        if t % k == 0:
            cnt += 1
    stdout.write(str(cnt))
if __name__ == "__main__":
    main()  

'''
++ Better way:
We can read the whole input at once and load it into a list. The code below gets accepted with 
a runtime of 1.70 seconds. 
'''
def main():
    from sys import stdin, stdout
    n, k = stdin.readline().split()
    n = int(n)
    k = int(k)
     
    cnt = 0
    lines = stdin.readlines()
    for line in lines:
        if int(line) % k == 0:
            cnt += 1
 
    stdout.write(str(cnt))
 
if __name__ == "__main__":
    main()



'''
How to read input in Python in Codeforces

Suppose in Codeforces (or a similar online judge) you have to read numbers a b c d and print their product. In Python 3.4 you can do it as follows:

Method 1a: Using a list comprehension
'''

a, b, c, d = [int(x) for x in input().split()]
print(a*b*c*d)

# Method 1b: Using the map function

a, b, c, d = map(int, input().split())
print(a*b*c*d)

# A faster way is to use stdin and stdout:
# Method 2a: List comprehension with stdin and stdout

from sys import stdin, stdout
a, b, c, d = [int(x) for x in stdin.readline().rstrip().split()]
stdout.write( str(a*b*c*d) + "\n" )

# Method 2b: Map with stdin and stdout

from sys import stdin, stdout
a, b, c, d = map( int, stdin.readline().rstrip().split() )
stdout.write( str(a*b*c*d) + "\n" )

# Note that you have to convert the output a*b*c*d to a string when passing
# it to the function stdout.write(…).
