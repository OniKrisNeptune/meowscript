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
    grab = []
    for lineno, line in enumerate(src):
        line = line.split(" ")
        grabptr = 0
        val = 0
        match line[0]:
            case "nya":
                variables[getint(line[1])] = 0

            case "nyya":
                if(getint(line[1]) in variables):
                    grab.append(getint(line[1]))
                else:
                    errorreport(1)

            case "nnyya":
                if(getint(line[1]) in grab):
                    grab.remove(getint(line[1]))
                else:
                    errorreport(2)

            case "nyaa":
                val = getint(line[1])
                while(grabptr != len(grab)):
                    variables[grab[grabptr]] += val
                    grabptr += 1

            case "nnyaa":
                val = getint(line[1])
                while(grabptr != len(grab)):
                    variables[grab[grabptr]] -= val
                    grabptr += 1

            case "nyyaa":
                val = getint(line[1])
                while(grabptr != len(grab)):
                    variables[grab[grabptr]] *= val
                    grabptr += 1

            case "nnyyaa":
                val = getint(line[1])
                if(val != 0):
                    while(grabptr != len(grab)):
                        variables[grab[grabptr]] /= val
                        grabptr += 1
                else:
                    errorreport(4)

            case "nnya":
                while(grabptr != len(grab)):
                    print(variables[grab[grabptr]])
                    grabptr += 1

            case "^_^":
                pass

            case _:
                errorreport(3)

main(input())
input("press enter to quit")
