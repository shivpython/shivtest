#Ans4.
def fiboanc_sum(limit):
    sum = 0
    fib1, fib2 = 0, 1
    while fib2 < 4000000:
        if fib2 % 2 == 0:
            sum += fib2
        fib1, fib2 = fib2, fib1 + fib2
    return (sum)
print 'summm',fiboanc_sum(4000000)

#Ans 2.
naturalnumber =[each for each in xrange(1,1000) if each%3 == 0 or each%5 == 0 ]
print 'naturalnumber', sum(naturalnumber)


#Ans1.
your_input = raw_input()#"We are at Ignite Solutions! Their email-id is careers@ignitesol.com"
output = ""
delimiters = ["@","!"," ", ",", ";", ".", "\n"]
i = 0
for j in range(1, len(your_input)):
    if your_input[j] in delimiters:
        output += your_input[i:j][::-1] + your_input[j]
        i = j+1
    elif j==len(your_input)-1:
        output += your_input[i:j+1][::-1]

print output
