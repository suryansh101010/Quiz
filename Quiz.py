#one-width space
import random
import curses
from curses import wrapper
import keyboard
import time
import subprocess
keyboard.press_and_release('Win+d') 
time.sleep(1)
keyboard.press_and_release('Alt+Tab')
time.sleep(0.5)
keyboard.press_and_release('Win+up')
time.sleep(0.5)
keyboard.press_and_release('Win+up')
time.sleep(0.5)
keyboard.press_and_release('Win+down')
time.sleep(0.5)
keyboard.press_and_release('Win+up')
time.sleep(0.5)
strq = ""
hint = False
def formatfile(file):
    with open(file,'r') as g:
        text = g.read()
    text = text.replace(f'Q1. {strq}','')
    text = text.replace(' ','')
    text = text.replace(' ',' ')
    text = text.replace('',' ')
    text = text.replace('\n','')
    text = text.replace('01','')
    text = text.replace('02','\n')
    text = text.replace('03','\n')
    text = text.replace('04','\n')
    text = text.replace('05','\n')
    text = text.replace('06','\n')
    text = text.replace('07','\n')
    text = text.replace('08','\n')
    text = text.replace('09','\n')
    text = text.replace('10','\n')
    text = text.replace('11','\n')
    text = text.replace('12','\n')
    text = text.replace('13','\n')
    text = text.replace('14','\n')
    text = text.replace('15','\n')
    text = text.replace('16','\n')
    text = text.replace('17','\n')
    text = text.replace('18','\n')
    text = text.replace('19','\n')
    text = text.replace('20','\n')
    text = text.replace('ProgramCommands:OutputofCode:','')
    with open('file2.py','w') as e:
        e.write(text)
    output = subprocess.check_output('python file2.py', shell=True)
    output = output.decode('utf-8')
    return output
def get_screen_content(stdscr):
    content = ""
    rows, cols = stdscr.getmaxyx()
    rows -= 1
    for row in range(rows):
        for col in range(cols):
            content += chr(stdscr.inch(row+1, col) & 0xFF)
    return content
def check(debug):
    debug = debug.lower()
    if "next" in debug:
        next = True
    elif "previous" in debug:
        prev = True
    elif "hint" in debug:
        global hint
        hint = True
    elif "quit" in debug or "exit" in debug:
        e = True
def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    # If the value is not found, you can return None or raise an exception
    return None
def main(scr):
    DQ = {'Write a Python program to print "Hello, World!".':'use the print() function and put a string i.e. text between " as an arguement to the function.',
         'Write a Python program to calculate the sum of two numbers, 5 and 3.':'use the print() function and put 5+3 as an arguement.',
         'Write a Python program to find the square root of a given number, 9.':'use the ** operator and take the power as 0.5 .',
         'Write a Python program to check if a number is even or odd.':'use %(mod) operator.',
         'Write a Python program to concatenate (Join and Print) two strings, "Hello" and "World!".':'use print function and add the strings in the arguement as such print("str1" + "str2").',
         'Write a Python program to convert Celsius to Fahrenheit. Assume the temperature in Celsius is 30.[°F = (°C × 9/5) + 32]':'use two variables. One is 30 One is the formula with C as the first var.',
         'Write a Python program to generate a random number between 1 and 10.':'use random.randint().',
         'Write a Python program to find the maximum of three numbers: 7, 4, and 9.':'use max() function.',
         'Write a Python program to count the number of characters in a string: "Hello, Python!".':'use len() function.',
         'Write a Python program to check if a given string is a palindrome: "radar".':'use "example string"[::-1]'
         }
    LQ = list(DQ.keys())
    temp = []
    LQS = []
    prev = []
    i = 0
    while i < 5:
        r = random.randint(0,4)
        if r in temp:
            pass
        else:
            temp.append(r)
            LQS.append(LQ[r])
            i += 1
    try:
        time.sleep(1)
        scr.clear()
        str = "Press any key to start or press esc to exit" #First screen
        middle_x = int(round((curses.COLS/2)-20)) #x coord
        horz = int(middle_x - len(str)/20)
        vert = int(round((curses.LINES/2)-2)) #y coord
        scr.addstr(vert,horz,f"{str}")
        str = "(What just happened was making sure your window was maximized for optimal experience.)"
        middle_x = int(round((curses.COLS/2)-31-9)) #x coord
        horz = int(middle_x - len(str)/20)
        vert = int(round((curses.LINES/2)-2)) #y coord
        scr.addstr(vert+1,horz,f"{str}")
        scr.refresh()
        inp = scr.getch()
    except Exception as e:
        print("Please resize the terminal to a larger size and run the program again.")
        exit()
    if inp == 27:
        exit() #exit on esc
    else: #countinue on any other key
        while True:
            scr.clear()
            r = random.randint(0,len(LQS)-1)
            strq = LQS[r]
            LQS.pop(r)
            prev.append(strq)
            scr.addstr(0,0,f"Q1. {strq}")
            for i in range(20):
                if i < 9:
                    scr.addstr(i+2,0,f"0{i+1}")
                else:
                    scr.addstr(i+2,0,f"{i+1}")
            scr.addstr(23,0,'Program Commands: ')
            scr.addstr(24,0,'Output of Code:')
            scr.refresh()
            scr.move(2,3)
            countx = 3
            county = 2
            content = ""
            e = False
            c = ""
            debug = ""
            h = get_key_from_value(DQ, strq)
            while True:
                try:
                    if hint: scr.addstr(1,0,h)
                    if county == 23 and countx < 18 :
                        countx = 18
                    scr.move(county,countx)
                    o = scr.getch()
                    if o == 27:
                        e = True
                    elif o == 8:
                        if countx > 3:
                            countx -= 1
                            scr.addstr(county,countx," ")
                            scr.move(county,countx)
                        else:
                            county -= 1
                            scr.move(county,countx)
                    elif o == 32:
                        scr.addstr(county,countx,' ')
                        countx += 1 
                        scr.move(county,countx)
                    elif o == 9:
                        scr.addstr(county,countx,' ')
                        scr.addstr(county,countx+1,' ')
                        scr.addstr(county,countx+2,' ')
                        scr.addstr(county,countx+3,' ')
                        countx += 4
                        scr.move(county,countx)
                    elif o == 10:
                        if county < 22:  
                            if county == 21:
                                county = 23
                                scr.move(county,countx)
                            else:
                                county += 1
                                countx = 3
                                scr.move(county,countx)
                    elif o == 259: #up
                        if county > 2:
                            county -= 1
                            scr.move(county,countx)
                    elif o == 260: #left
                        if countx > 3:
                            countx -= 1
                            scr.move(county,countx)
                        else:
                            county -= 1
                            scr.move(county,countx)
                    elif o == 258: #down
                        if county < 22:  
                            if county == 21:
                                county = 23
                                scr.move(county,countx)
                            else:
                                county += 1
                                scr.move(county,countx)
                    elif o == 261:
                        countx += 1
                        scr.move(county,countx)
                    else:
                        if county == 23:
                            c = chr(o)
                            debug = debug + c
                            scr.addstr(county,countx,c)
                            countx += 1 
                            scr.move(county,countx)
                        else:    
                            c = chr(o)
                            scr.addstr(county,countx,c)
                            countx += 1 
                            scr.move(county,countx)
                    check(debug)
                except Exception as e:
                    scr.clear()
                    print(e,"line 111")
                    exit()
                if e:
                    content = get_screen_content(scr)
                    with open('C:\\Users\\Suryansh\\Documents\\coding\\School\\file.txt','w') as l:
                        l.write(content)
                    a = formatfile('C:\\Users\\Suryansh\\Documents\\coding\\School\\file.txt')
                    print(a)
                    scr.addstr(25,0,a)
                    scr.getch()
                    scr.clear()
                    exit()
try:
    wrapper(main)
except:
    pass