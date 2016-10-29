import operator
import sys
def operators(op):                  #define operators
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '//': operator.floordiv,
        '%' : operator.mod,
        '**': operator.pow
        }[op]
def help():                                                         #define an operators list 
    print('\033[1m'+'You can use following operators:'+'\033[0m'+
    '''
    " + " to add
    " - " to subtract
    " * " to multiplie
    " / " to divide
    "// " for floor division
    " % " to calculate a modulo
    "** " for exponentiation
    ''')
def calculate():
    while True:
        a = input('Enter a number (or a letter to ' + '\033[1m' + 'exit' + '\033[0m' + '): ')
        while True:                         #check if input is a letter or intiger
            try:
                if a.isalpha() == True:
                    sys.exit()
                else:
                    a = int(a)
                    break
            except ValueError:
                print('Invalid sign!')
                a = input('Enter a number (or a letter to ' + '\033[1m' + 'exit' + '\033[0m' + '): ')
        op_char = input('Enter an operation (Enter --help to check the operators list): ')
        while op_char == '--help':
            help()
            op_char = input('Enter an operation (Enter --help to check the operators list): ')
        while op_char!='--help' and op_char !='+' and op_char !='-' and op_char !='*' and op_char !='/' and op_char !='//' and op_char !='%' and op_char !='**':    #validate an aperator
            print('Invalid sign!')
            op_char = input('Enter an operation (Enter --help to check the operators list): ')
        while True:                     #validate the second number input
            try:
                b = int(input('Enter another number: '))
                break
            except ValueError:
                print('Invalid sign!')
        result = operators(op_char)(a, b)
        print('Result: ' + str(result) + '\n')
calculate()
