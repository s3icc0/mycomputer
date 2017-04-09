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
        '   1   List files\n'
        '   3   Change directory\n'
        '   4   Enter known filename\n'
        '   5   Create new file only\n'
        '   6   Create new file and edit\n'
        '   7   Create new directory\n'
        '   8   Create new directory and change directory\n'))

    options = {
        '1': lstdecide
#         '3': chngdir,
#         '4': gofile,
#         '5': lambda: makefile(fmode='w'),
#         '6': lambda: makefile(fmode='a'),
#         '7': mkdir,
#         '8': mkdirc
}

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
        '2': lstdir,
        '3': lstall}

    if decide in options.keys():
        options[decide]()
    else:
        print('Your ENTRY is NOT VALID, please try again ...')
        lstfiles()

def lstfiles():

    print('Listing files in: {}'.format(os.getcwd()))

    print(filename for filename in os.listdir(os.getcwd()))


def lstall():

    print('Listing files and directories in: {}'.format(os.getcwd()))

    for item in os.listdir(os.getcwd()):
        print(item)


def lstdir():

    print('Listing directories in: {}'.format(os.getcwd()))
    i for i in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(
            os.getcwd(), name))


# cwdir()

lstdir()
