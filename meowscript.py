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

def main(source,debug):
    src = open(source, "r").read().split("\n")
    lineno = 0
    grab = []

    while(lineno != len(src)):
        line = src[lineno].split(" ")
        grabptr = 0
        val = 0
        if(line[0] == "nya"):
            variables[getint(line[1])] = 0

        elif(line[0] == "nyya"):
            if(getint(line[1]) in variables):
                grab.append(getint(line[1]))
            else:
                errorreport(1)

        elif(line[0] == "nnyya"):
            if(getint(line[1]) in grab):
                grab.remove(getint(line[1]))
            else:
                errorreport(2)

        elif(line[0] == "nyaa"):
            val = getint(line[1])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] += val
                grabptr += 1

        elif(line[0] == "nnyaa"):
            val = getint(line[1])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] -= val
                grabptr += 1

        elif(line[0] == "nyyaa"):
            val = getint(line[1])
            while(grabptr != len(grab)):
                variables[grab[grabptr]] *= val
                grabptr += 1

        elif(line[0] == "nnyyaa"):
            val = getint(line[1])
            if(val != 0):
                while(grabptr != len(grab)):
                    variables[grab[grabptr]] //= val
                    grabptr += 1
            else:
                errorreport(4)

        elif(line[0] == "nnya"):
            val = getint(line[1])
            if(val == 0):
                while(grabptr != len(grab)):
                    print(variables[grab[grabptr]])
                    grabptr += 1
            elif(val == 1):
                while(grabptr != len(grab)):
                    print(chr(variables[grab[grabptr]]))
                    grabptr += 1

        elif(line[0] == "^_^"):
            pass

        else:
            errorreport(3)

        lineno += 1
        if(debug == True):
            print(lineno,line,grab,variables)

sourceraw = input()
if(sourceraw == "debug"):
    debug = True
    sourceraw = input()
else: debug = False
main(sourceraw,debug)
input("press enter to quit")
