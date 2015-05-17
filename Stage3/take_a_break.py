import webbrowser
import time

loops = 0 

while loops < 3:
    time.sleep(3)
    webbrowser.open("http://google.com")
    print "Loop " + str(loops + 1) + " started at " + time.ctime()
    loops += 1
