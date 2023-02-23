lineno = 0
variables = {}
def errorreport(error):
    global lineno
    errormsgs = open("errormsgs.txt", "r").read().split("\n")
    print("Error " + str(error) + " @ line " +
          str(lineno) + " : " + errormsgs[error])
    input("press enter to close")
    exit()
def getint(value, variables):
    if(value[0] == "~"):
        if(len(value) - 4 in variables):
            return(variables[len(value) - 4])
        else:
            errorreport(3)
    else:
        return(len(value) - 3)
def main():
    src = open(input(), "r").read().split("\n")
    global lineno
    argptr = 1
    grab = []
    global variables
    while(lineno != len(src)):
        line = src[lineno].split(" ")
        inst = line[0]
        grabptr = 0
        arg = line[argptr]
        print(lineno)

    #new
        if(inst == "new"):
            arg = line[argptr]
            variables[getint(arg, variables)] = 1

    #grab
        elif(inst == "grab"):
            arg = line[argptr]
            if(getint(arg,variables) in variables):
                grab.append(getint(arg, variables))
            else: errorreport(1, lineno)

    #ungrab
        elif(inst == "ungrab"):
            arg = line[argptr]
            if(getint(arg,variables) in grab):
                grab.remove(getint(arg, variables))
            else: errorreport(0, lineno)

    #add
        elif(inst == "add"):
            arg = line[argptr]
            while(grabptr != len(grab)):
                variables[grab[grabptr]] += getint(arg, variables)
                grabptr += 1

    #substract
        elif(inst == "sub"):
            arg = line[argptr]
            while(grabptr != len(grab)):
                variables[grab[grabptr]] -= getint(arg, variables)
                grabptr += 1

    #multiply
        elif(inst == "mul"):
            arg = line[argptr]
            while(grabptr != len(grab)):
                variables[grab[grabptr]] *= getint(arg, variables)
                grabptr += 1

    #divide
        elif(inst == "div"):
            arg = line[argptr]
            while(grabptr != len(grab)):
                variables[grab[grabptr]] /= getint(arg, variables)
                grabptr += 1

        else: errorreport(2)
        lineno += 1
    print(variables)
main()
