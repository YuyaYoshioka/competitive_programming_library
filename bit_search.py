numbers=[]
answers=[]
for i in range(2**n):
    number=[]
    for j in range(n):
        if ((i>>j)&1):
            number.append(numbers[j])
    answers.append(number)
