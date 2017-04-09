"""PROBLEM
1. Create a file named mydata2.txt
2. Use what you learned in part 8 to find out how to open a file without with 
(Open in try)
3. Catch FileNotFoundError
4. In else print contents
5. In finally print message
6. Open nonexistent file mydata3.txt
"""

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def set_window_size(cols, lines):
    os.system('mode con: cols={0} lines={1}'.format(cols, lines))


"""Windows Console size variables"""
win_console_width = 180
win_console_height = 50

"""current working file STR"""
cwfile = None


def startprogram():
    cwdir()

    decision = input(
        'Press:\n'
        '   1   to work \n'
        'N to work with another file\n'
        'X to end')

    if decision.lower() in ('yes', 'y', 'c', 'cont', 'continue', ''):
        contwork()
    elif decision.lower() in ('no', 'n', 'not', 'next', 'new'):
        otherwork()
    elif decision.lower() in ('exit', 'quit', 'x'):
        endprog()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        endprog()


def cwdir():
    print('Your current working directory is: {}'.format(os.getcwd()))


def askfilehandle():
    """
    User input:

    :return: 
    """

    clear_screen()

    decision = input(
        'Press:\n'
        'Y to continue with current file\n'
        'N to work with another file\n'
        'X to end')

    if decision.lower() in ('yes', 'y', 'c', 'cont', 'continue', ''):
        contwork()
    elif decision.lower() in ('no', 'n', 'not', 'next', 'new'):
        otherwork()
    elif decision.lower() in ('exit', 'quit', 'x'):
        endprog()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        endprog()


def contwork():
    """
    continue working on current file

    :return: 
    """


def otherwork():
    """
    work on different file than current myfile

    :return: 
    """


def endprog():
    """
    handle end of the program
    :return: 
    """
    input('Thank you for using this program!\n\n'
          'Press ENTER to EXIT')


# user input file name
def txtfilename():
    """
    get the name of the file and store as temporary variable for later use

    :return: cwfile -- STR
    """

    global cwfile
    cwfile = input(str('Enter file name: '))
    test = a.split('.')
    try:
        if c == test[0] + '.txt':
            print('Your new file is named {0} and is located:\n'
                  '{1}'.format(cwfile, os.getcwd()))
            return cwfile
        else:
            txtfilename()
    except:
        txtfilename()


def multiinput():
    """
    input over multiple lines
    ends on no data input

    :return: input() -- multiple input() results in one input
    """

    try:
        while True:
            data = input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return


def writetext():
    """
    capture any text entered by user

    :return: userinput -- list of user entries
    """

    print('Enter text:\n')
    userinput = list(multiinput())
    return userinput


# create file
def createfile():
    """
    create file
    mode: WRITE
    coding: UTF-8

    :return: myfile -- variable 
    """

    with open(txtfilename(), mode='w', encoding='utf-8') as myfile:
        return myfile


def appendtofile():
    global cwfile
    with open(cwfile, mode='a', encoding='utf-8') as myfile:
        for i in writetext():
            myfile.write('{}\n'.format(i))
            askfilehandle()


def main():
    """
    main runtime

    1) Create file based on user entry
    2) Ask the next action

    :return: 
    """
    set_window_size(win_console_width, win_console_height)
    clear_screen()

    print('          FILE HANDLING TOOL by s3icc0          ')
    print()

    startprogram()

    createfile()
    askfilehandle()


main()
