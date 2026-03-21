import math

memory = 0

def calculator():
    global memory
    print("-------------Advance python calulator-------------")
    print("Available operators:")
    print("+ - * / ** sqrt sin cos tan log exp")
    print("Memory: M+, M-, MR, MC")
    print("Type exit to quit\n")
    
    while True:
        expression = input("Enter your expression: ")
        
        if expression.lower() == "exit":
            print("Goodbye! 👋")
            break
        elif expression.upper() == "M+":
            val = float(input("Enter value to add to the memory: "))
            memory+=val
            print("Memory =", memory)
        elif expression.upper() == "M-":
            val = float(input("Enter the value to subtract from the memory: "))
            memory-=val
            print("Memory =", memory)
        elif expression.upper() == "MR":
            print("Memory Recall =", memory)
        
        elif expression.upper() == "MC":
            memory = 0
            print("Memory cleared")
            
        else:
            try:
                expression = expression.replace("sqrt", "math.sqrt")
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('log', 'math.log')
                expression = expression.replace('exp', 'math.exp')
                result = eval(expression)
                print("Result =", result)
            except Exception as e:
                print("Error:", e)

calculator()

            
