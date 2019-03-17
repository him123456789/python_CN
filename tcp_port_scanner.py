import socket
from datetime import datetime
import threading
from queue import Queue

print_lock=threading.Lock()


host=input("Enter Host Address To Scan : ")
ip=socket.gethostbyname(host)


print("-"*80)
print("      Please wait,Scanning The Host--------->",ip)
print("-"*80)

t1=datetime.now()

def scan(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((ip,port))
        if result==0:
            print("\nPort %d Is Open--------->"%(port))
            sock.close()
        else:
            print("\nPort %d Is Close :-("%(port))

    except:
        pass



def threader():
    while True:
        worker=q.get()
        scan(worker)
        q.task_done()

q=Queue()

for x in range(99):
    t=threading.Thread(target=threader)
    t.deamon=True
    t.start()

for worker in range(1,100):
    q.put(worker)

q.join()


t2=datetime.now()


total=t2-t1
print("Total Scanning Time:",total)
