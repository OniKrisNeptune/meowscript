variables = {}
def errorreport(error):
    input("error " + str(error) + "\npress enter to close")
    quit()
def getint(value):
    global variables
    if(value[0] == "~"):
        if(value[1] == "~"):
            return(int(input()))
        else:
            if(len(value)-4 in variables):
                return(variables[len(value) - 4])
            else:
                errorreport(0)
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
                errorreport(1)

        elif(line[arg] == "nnyya"):
            arg += 1
            if(getint(line[arg]) in grab):
                grab.remove(getint(line[arg]))
            else:
                errorreport(2)

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
            if(val != 0):
                while(grabptr != len(grab)):
                    variables[grab[grabptr]] /= val
                    grabptr += 1
            else:
                errorreport(4)
                
        elif(line[arg] == "nnya"):
            while(grabptr != len(grab)):
                print(variables[grab[grabptr]])
                grabptr += 1
            
        elif(line[arg] == "^_^"):
            pass

        else:
            errorreport(3)

        lineno += 1
main(input())
input("press enter to quit")
