from time import sleep
from threading import *


class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.5)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(0.5)
            
t1=hello()
t2=hi()
#To create two dofferent methods instaed of calling run method call start method
#t1.run()
#t2.run()
t1.start()
sleep(0.2)
t2.start()
print("bye")