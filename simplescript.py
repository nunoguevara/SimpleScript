variables = {}

while True:
    arguments = input()

    words = arguments.split()
    syntax = words[0]

    if syntax == "out":
        if len(words) > 1:
           words = ' '.join(words[0:])
           print(words[3:]) 
        else:
            print("Error need two arguments!")
    elif syntax == "in":
        if len(words) < 1:
            user = input("Input: ")
        else:
            variable_name = words[1]
            words = ' '.join(words)
            user = input(f"{words[2:]} ")
            variables[variable_name] = user
    elif len(words) >= 3 and words[1] == "=":
        if len(words) < 1:
            print("Invalid Variable!")
        else:
            variable_name = words[0]
            variable_value = ' '.join(words[2:])
            variables[variable_name] = variable_value
    elif syntax in variables:
        print(variables[syntax])
    elif syntax == "abt":
        print("SimpleScript made with Python by Nuno337")
    else:
        print("Invalid Syntax") 