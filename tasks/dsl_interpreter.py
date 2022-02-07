# Use this interpreter, by typing 'python dsl_interpreter.py habits_tracker.dsl' into the console.
# If you want to use some other .dsl file, just change the path :)

import sys

# my functions:
# (could be outsourced in its own module)

functions = {'mins': lambda a, b: a + round((b/60),2),
             'hrs': lambda a, b: a + b}

variables = {}

# check if exactly two files are given (interpreter + dsl)
if len(sys.argv) != 2:
    sys.exit(1)

# open .dsl and check each line
with open(sys.argv[1]) as file:
    # initialization for actual parking situation
    habits = {"read": 0,
               "yoga": 0,
               "meditate": 0,
               "walk": 0,
               "study": 0,
               "relax": 0
               }

    for line in file:
        line = line.strip()

        # check if the line is a comment
        if not line or line[0] == '>':
            continue
        parts = line.split()
        #print("parts: " + parts[0])

        # check the instructions for each line and execute them
        if parts[0] == 'Time':
            print("You spent:" + str(habits[parts[3]]) + " hrs " + parts[3] + " this week ")

        else:
            a = habits[parts[2]]
            #print("a: " + str(a))
            #print(type(a))
            b = float(parts[0])
            #print("b: " + str(b))
            #print(type(b))
            habits[parts[2]] = functions[parts[1]](a, b)

