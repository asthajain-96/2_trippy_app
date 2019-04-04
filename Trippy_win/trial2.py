import os
#import filter_selection

# create folder directory to save images
folder = r'\trippy'
cwd = os.getcwd()
print(folder)
print(cwd)
newpath = cwd+folder
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print('successful')
print(newpath)
