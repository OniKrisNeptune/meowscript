# meowscript, an esolang designed for catboys/catgirls/nyanbinaries
the interpreter is a wip as of now
usage: run meowscript.exe or meowscript.py, enter the file name on the next line
## version specific notes:
you can create new variables, grab/release variables and do operations, uiilize basic input/ouput
## guide:
### basic concepts
### comments: add `^_^` at the beginning of the line
variable: has a name(int) and a value(int)

[value] in any instruction, [value] gets:

a) the value that was written

OR

b) the value of the variable specified 

OR

c) input

`a` is represented as meow with varying amounts of o

for example: `meow` is 1, `meooow` is 3, `mew` is 0

`b` gets the value of the variable specified. its name is also done using meows described in `a`, and to specify its a variable, it must be prefixed with `~`

`c` gets input if you write `~~`, as of v0.4 it just lets you enter an integer.(subject to change)

for example: `~meow` gives the value of variable named 1, `~meoow~` gives the value of the variable named 2, and `~mew` gives the value of a variable named 0

to modify a variable, you must grab it first

### basic instructions
`nya [value]` creates a variable named [value]

*the name of the variable can itself be a variable*

`nyya [value]` "grabs" a variable named [value]

*multiple variables may be grabbed, any operation will be applied to every grabbed variable individually*

*a variable may be grabbed multiple times, in that case any operation will be applied to it as many times as it has been grabbed*

`nnyya [value]` "ungrabs" a variable named [value]

`nnya` is going to let you output, however how it will do it has not been decided yet

### arithmetic operations

they all follow a syntax of `[operation] [value]`
operations: 
```
nyaa - add
nnyaa - substract
nyyaa - multiply
nnyyaa - floor divide
```
examples: `nyaa meow` adds 1 to every grabbed variable

`nyyaa ~meow` multiplies every grabbed variable by the value of variable `meow`

*if variable x is grabbed and you attempt to perform an operation using x as a value, the value of x before the operation will be used for every grabbed variable*

*no you cannot divide by zero*
### output: 
as of v0.4 nnya prints the value of every grabbed variable(subject to change)
### control flow
theres gonna be an if and a while loop, however i am too lazy to document them rn and theyre not implemented yet

## example

prints the square of the input

```
nya mew
nyya mew
nyaa ~~
nyyaa mew
nnya```