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


def cwdir():

    print('Your current working directory is: {}'.format(os.getcwd()))

    decide = input(str(
        'Press:\n'
        '   1   List files'
        '   3   Change directory'
        '   4   Enter known filename'
        '   5   Create new file only'
        '   6   Create new file and edit'
        '   7   Create new directory'
        '   8   Create new directory and change directory'))

    options = {
        '1': lstdecide,
        '3': chngdir,
        '4': gofile,
        '5': lambda: makefile(fmode='w'),
        '6': lambda: makefile(fmode='a'),
        '7': mkdir,
        '8': mkdirc}

    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        cwdir()


def lstdecide():
    clear_screen()

    decide = input(str(
        'Select option to list in current working directory:\n'
        '   1   List files only'
        '   2   List files including directories'
        '   3   List directories only'))

    options = {
        '1': lstfiles,
        '2': lstfdir,
        '3': lstall}

    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        lstfiles()


def lstfiles():

    print('Listing files in: {}'.format(os.getcwd()))

    for item in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), item)):
            print(item)


def lstall():

    print('Listing files and directories in: {}'.format(os.getcwd()))

    for item in os.listdir(os.getcwd()):
        print(item)


def lstdir():

    print('Listing directories in: {}'.format(os.getcwd()))

    for item in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), item)):
            print(item)


def chngdir():
    pass


def gofile():
    file = input(str('Enter file name: '))
    pass


def makefile(fmode):
    with open(txtfilename(), mode=fmode, encoding='utf-8') as f:
        return f


def makedir():
    pass


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

    try:
        while True:
            data = input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return


def writetext():

    print('Enter text:\n')
    userinput = list(multiinput())
    return userinput


# create file
def createfile():

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
