variables = {}

def getint(value):
    global variables
    if(value[0] == "~"):
        if(len(value)-4 in variables):
            return(variables[len(value) - 4])
        else:
            print("error 0")
            quit()
    else:
        return(len(value) - 3)

def main(source):
    src = open(source, "r").read().split("\n")
    lineno = 0
    grab = []

    while(lineno != len(src)):
        line = src[lineno].split(" ")
        arg = 0
        grabptr = 0
        val = 0
        if(line[arg] == "nya"):
            arg += 1
            variables[getint(line[arg])] = 0

        elif(line[arg] == "nyya"):
            arg += 1
            if(getint(line[arg]) in variables):
                grab.append(getint(line[arg]))
            else:
                print("error 1")
                quit()

        elif(line[arg] == "nnyya"):
            arg += 1
            if(getint(line[arg]) in grab):
                grab.remove(getint(line[arg]))
            else:
                print("error 2")
                quit()

        elif(line[arg] == "nyaa"):
            arg += 1
            val = getint(line[arg])

            while(grabptr != len(grab)):
                variables[grab[grabptr]] += val
                grabptr += 1

        elif(line[arg] == "nnyaa"):
            arg += 1
            val = getint(line[arg])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] -= val
                grabptr += 1

        elif(line[arg] == "nyyaa"):
            arg += 1
            val = getint(line[arg])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] *= val
                grabptr += 1

        elif(line[arg] == "nnyyaa"):
            arg += 1
            val = getint(line[arg])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] /= val
                grabptr += 1

        else:
            print("error 3")
            quit()

        lineno += 1
    print(variables)
main(input())
