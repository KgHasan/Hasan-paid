import os, platform, time, sys
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.050)
xoss('\033[0;91m Checking Your Mobile...?');time.sleep(0.50)
time.sleep(10)
def Update():
    exit('\033[1;31m Commands On Update Please Wait For Update')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\033[0;92m Congratulations Your Device Support this Tools")
            time.sleep(5)
            xoss('\033[0;93m FOLLOW MY FB ACCOUNT')
            time.sleep(3)
            os.system('xdg-open https://www.facebook.com/copy.link.erorr404')
            from new3 import refat
            refat()
        elif bit == '32bit':
            xoss("\033[0;92m Congratulations Your Device Support This Tools")
            xoss('\033[0;93m JOIN MY FB GROUP')
            os.system('xdg-open https://facebook.com/groups/551365756758487/')
            from R4NDOM import refat
            refat()
        else:
            exit('\033[1;31m Connection & Network Error')
Run()
 
