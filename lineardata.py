#1. Find pairs whose sum is equal to given num:
def pairs(x):
    sum = 5
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if x[i] + x[j] == sum:
                print('(',x[i], x[j],')')
x = [2, 1, 4, -2, 7, 3]
print(pairs(x))

#2. Reverse an array:
def reverse(x, start, end):
    while start < end:
        x[start], x[end] = x[end], x[start]
        start += 1
        end -= 1
x = [2, 1, 4, -2, 7, 3]
reverse(x,0,5)
print(x)

#3. Strings are rotation each other:
def rotation(str1,str2):
    if len(str1) != len(str2):
        return False
    string = str1 + str2
    if str2 in string:
        print("Strings are rotation each other")
    else:
        print("Strings are not rotation each other")
str1 = "edyoda"
str2 = "adoyde"
rotation(str1,str2)

#4. Non repeating character:
string = input()
repeat = ''
if len(string)==0:
    print("Empty string")
for i in string:
    if string.count(i) == 1:
        repeat += i
        break
print(repeat)

#5. Tower of Hanoi:
def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    hanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    hanoi(n-1, aux_rod, to_rod, from_rod)
hanoi(2, 'A', 'C', 'B')

#6. Convert postfix to prefix:
def isoperator(x):
    if x=='+':
        return True
    if x=='-':
        return True
    if x=='*':
        return True
    if x=='/':
        return True
    return False
def prefix(exp):
    s = []
    l = len(exp)
    for i in range(l):
        if isoperator(exp[i]):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = exp[i]+op2+op1
            s.append(temp)
        else:
            s.append(exp[i])
    result = ""
    for i in s:
        result += i
        return result
exp = 'ab+cd-*'
print(prefix(exp))

#7. Convert to prefix to infix:
def isoperator(x):
    if x=='+':
        return True
    if x=='-':
        return True
    if x=='*':
        return True
    if x=='/':
        return True
    return False
def infix(exp):
    s = []
    i = len(exp) - 1
    while i >= 0:
        if not isoperator(exp[i]):
            s.append(exp[i])
            i -= 1
        else:
            str = "(" + s.pop() + exp[i] + s.pop() + ")"
            s.append(str)
            i -= 1
    return s.pop()
exp = '*-a/bc-/akl'
print(infix(exp))

#8. Brackets are closed:
def brackets(exp):
    stack = []
    open = ['(', '[', '{']
    close = [')', ']', '}']
    for i in exp:
        if i in open:
            stack.append(i)
        elif i in close:
            stack.pop()
    if len(stack) == 0:
        print("Brackets are closed")
    else:
        print("Brackets are not closed")
exp = input()
brackets(exp)

#9. Reverse stack:
def createStack():
    stack = []
    return stack
def push(stack, item):
    stack.append(item)
def reverse(stack):
    if stack != 0:
        rev = []
        rev.append(stack.pop())
        return rev
        
stack = createStack()
push(stack, (4))
push(stack, (3))
push(stack, (2))
push(stack, (1))
print("Original Stack ")
print(stack)
print("Reversed Stack ")
print(reverse(stack))
print(reverse(stack))
print(reverse(stack))
print(reverse(stack))

#10. Smallest num using stack:
def createStack():
    stack = []
    return stack
def push(stack, item):
    stack.append(item)
def small(stack):
    stack.sort()
    return stack[0]
stack = createStack()
push(stack, (4))
push(stack, (3))
push(stack, (2))
push(stack, (1))
print("Original Stack ")
print(stack)
print("Smallest num:", small(stack))

