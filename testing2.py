import os

print('Listing directories in: {}'.format(os.getcwd()))
for i in os.listdir(os.getcwd()):
    if os.path.isdir(os.path.join(os.getcwd(), i)):
        print(i)
