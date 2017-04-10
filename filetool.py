import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_window_size(cols, lines):
    os.system('mode con: cols={0} lines={1}'.format(cols, lines))

"""Windows Console size variables"""
cmd_width = 120
cmd_height = 35

"""current working file STR"""
cwfile = None

def filetool():
    """Navigate
    List files
    Change directory
    TODO: Create - new file, file and edit, new dir, dir and go to dir
    TODO: Work with known file
    """
    clear_screen()
    print('Your current working directory is:\n   {}\n'.format(os.getcwd()))
    decide = input(str(
        'Press:\n'
        '   1   List files\n'
        '   2   Change directory\n'
        '   3   Create new ...\n'
        '   4   Enter known filename\n'
        '   5   Exit\n'))
    options = {
        '1': lstdecide,
        '2': chngdir,
        '3': clear_screen,
        '4': clear_screen,
        '5': exitscript}
    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        input('Press ENTER to continue ...')
        filetool()

def exitscript():
    clear_screen()
    print('Thanks for using! Goodbye!')
    input('Press ENTER to EXIT ...')
    clear_screen()
    exit()

def lstdecide():
    clear_screen()
    decide = input(str(
        'Select option to list in current working directory:\n'
        '   1   List files only\n'
        '   2   List files including directories\n'
        '   3   List directories only\n'))
    options = {
        '1': lstfiles,
        '2': lstall,
        '3': lstdir}
    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        input('Press ENTER to continue ...')
        lstfiles()

def lstfiles():
    clear_screen()
    print('Listing files in:\n   {}\n'.format(os.getcwd()))
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), item)):
            print(item)
    input('\nDONE\nPress ENTER to continue ...')
    filetool()

def lstall():
    clear_screen()
    print('Listing files and directories in:\n   {}\n'.format(os.getcwd()))
    for item in os.listdir(os.getcwd()):
        print(item)
    input('\nDONE\nPress ENTER to continue ...')
    filetool()

def lstdir():
    clear_screen()
    print('Listing directories in:\n   {}\n'.format(os.getcwd()))
    for item in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), item)):
            print(item)
    input('\nDONE\nPress ENTER to continue ...')
    filetool()

def chngdir():
    clear_screen()
    print('Change directory'
          'Your current working directory is:\n   {}\n'.format(os.getcwd()))
    decide = input(str(
        '\nEnter directory to go to\n'
        '   use ".." to go level up\n'
        '   to change drive from top level use [Drive]:doubleslash\n'))
    try:
        os.chdir(decide)
    except FileNotFoundError:
        print('\nDirectory "{}" not found\n'.format(decide))
        input('Press ENTER to try again ...')
        chngdir()
    clear_screen()
    print('Your new working directory is:\n   {}\n'.format(os.getcwd()))
    chngdirdecide()

def chngdirdecide():
    decide = input(str(
        '\nRun again? (1)\nNew action. (2)\n'))
    options = {
        '1': chngdir,
        '2': filetool}
    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        input('Press ENTER to continue ...')
        chngdirdecide()






# def gofile():
#     file = input(str('Enter file name: '))
#     pass
#
#
# def makefile(fmode):
#     with open(txtfilename(), mode=fmode, encoding='utf-8') as f:
#         return f
#
#
# def makedir():
#     pass
#
#
# def startprogram():
#
#     filetool()
#
#     decision = input(
#         'Press:\n'
#         '   1   to work \n'
#         'N to work with another file\n'
#         'X to end')
#
#     if decision.lower() in ('yes', 'y', 'c', 'cont', 'continue', ''):
#         contwork()
#     elif decision.lower() in ('no', 'n', 'not', 'next', 'new'):
#         otherwork()
#     elif decision.lower() in ('exit', 'quit', 'x'):
#         endprog()
#     else:
#         print('Your ENTRY is NOT VALID, please try again ...')
#         endprog()
#
#
#
#
#
# def askfilehandle():
#     """
#     User input:
#
#     :return:
#     """
#
#     clear_screen()
#
#     decision = input(
#         'Press:\n'
#         'Y to continue with current file\n'
#         'N to work with another file\n'
#         'X to end')
#
#     if decision.lower() in ('yes', 'y', 'c', 'cont', 'continue', ''):
#         contwork()
#     elif decision.lower() in ('no', 'n', 'not', 'next', 'new'):
#         otherwork()
#     elif decision.lower() in ('exit', 'quit', 'x'):
#         endprog()
#     else:
#         print('Your ENTRY is NOT VALID, please try again ...')
#         endprog()
#
#
# def contwork():
#     """
#     continue working on current file
#
#     :return:
#     """
#
#
# def otherwork():
#     """
#     work on different file than current myfile
#
#     :return:
#     """
#
#
# def endprog():
#     """
#     handle end of the program
#     :return:
#     """
#     input('Thank you for using this program!\n\n'
#           'Press ENTER to EXIT')
#
#
# # user input file name
# def txtfilename():
#     """
#     get the name of the file and store as temporary variable for later use
#
#     :return: cwfile -- STR
#     """
#
#     global cwfile
#     cwfile = input(str('Enter file name: '))
#     test = a.split('.')
#     try:
#         if c == test[0] + '.txt':
#             print('Your new file is named {0} and is located:\n'
#                   '{1}'.format(cwfile, os.getcwd()))
#             return cwfile
#         else:
#             txtfilename()
#     except:
#         txtfilename()
#
#
# def multiinput():
#
#     try:
#         while True:
#             data = input()
#             if not data: break
#             yield data
#     except KeyboardInterrupt:
#         return
#
#
# def writetext():
#
#     print('Enter text:\n')
#     userinput = list(multiinput())
#     return userinput
#
#
# # create file
# def createfile():
#
#     with open(txtfilename(), mode='w', encoding='utf-8') as myfile:
#         return myfile
#
#
# def appendtofile():
#     global cwfile
#     with open(cwfile, mode='a', encoding='utf-8') as myfile:
#         for i in writetext():
#             myfile.write('{}\n'.format(i))
#             askfilehandle()


def main():
    """
    main runtime

    :return: 
    """
    set_window_size(cmd_width, cmd_height)
    clear_screen()
    print('          FILE HANDLING TOOL by s3icc0          \n')
    filetool()

main()
