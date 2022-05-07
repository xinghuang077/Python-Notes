#  https://levelup.gitconnected.com/10-interesting-python-programs-with-code-b676181a2d1a
#  A python program to shut down your computer.
#  Note: Make sure to save and close all documents before executing this program. After running this program which will cause the computer to shut down, the unsaved data might be lost.

import os
shutdown = input("Do you want to shutdown your computer (yes / no): ")
if shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print('Shutdown is not requested')                                               