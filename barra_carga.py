import itertools
import threading
import time
import sys

done = False
contador = 0
#here is the animation
def animate():
    #for c in itertools.cycle(['|', '/', '-', '\\']):
    global contador
    for c in itertools.cycle(['.', '..', '...', '   ']):
        if done:
            break
        contador +=1
        #sys.stdout.write('                      ')
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
#t.start()

#long process here
#time.sleep(10)
#donee = 1
#print(donee)
#t.run()
