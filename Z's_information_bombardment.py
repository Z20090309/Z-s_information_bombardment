from pynput.keyboard import Key,Controller
from os import system as zzk
import time


zzk('cls')
print('--------------')
print('|            |')
print('--------    /')
print('       /   /')
print('      /   /')
print('     /   /')
print('    /   /')
print('   /   /')
print('  /   /')
print(' /   /')
print('/   ------------')
print('|              |')
print('----------------')
print('Big handsome guy \'Z\' is here!')
print('about this:')
print('It can realize the information bombardment function of QQ or WeChat.')
print('(As long as you press the enter key to send a message, you can use the software)')
print('Once you have entered the content and the number of times,\n you need to move the mouse cursor to the dialog box and click on the input box.')
print('Let\'s get started!')
keyboard = Controller()
a = str(input('Please enter your content:'))
ci = int(input('Please enter the number of times:'))
print('There are 5 seconds left before the program starts.')
for i in range(5):
    print(5-i)
    time.sleep(1)
for i in range(ci):
    keyboard.type(a)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)