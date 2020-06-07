import re

print("Our magical Calculator")
print("Type 'quit' for exit\n")

run = True
previous = 0

def calculate():
    global run
    global previous

    equation = input("Enter the equation:")
    if equation == "quit":
        run = False
    
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','', equation)
        previous = eval(equation)


        print("your answer is ", previous)

while run:
    calculate()