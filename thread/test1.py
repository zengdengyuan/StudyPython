
#@function:The startup thread does not open the lock
#@time:2019-3-20
import threading
import time

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        print("Staring" +self.name)
        print_time(self.name,self.counter,3)
        print("Stoping"+self.name)


def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print(threadName+' '+time.ctime(time.time()))
        counter-=1

threads =[]
thread1 =   myThread(1,"thread-1",1)
thread2 =   myThread(2,"thread-2",2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("Exiting Main Thread")
