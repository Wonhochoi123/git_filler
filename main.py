# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from random import randint
for i in range(1,2):
    for j in range(0,randint(1,10)):
        d=str(i)+" days ago"
        with open('file.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="'+d+'" -m "commit"')
os.system('git push -u origin main')