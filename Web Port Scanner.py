import socket
from threading import Thread
from queue import Queue
import time
print("-"*70)
print("Port Scanner by CodeWithKashif")
print("-"*70)
host = input("Enter Ip: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
try:
    host = socket.gethostbyname(host)
except:
    print("Name resolution failed")
    exit()
print("Scanning ..........Please Wait!")
def start_scan():
    while q.not_empty:
        port = q.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = s.connect_ex((host, port))
        if not connection:
            print(f"[+]Open Port {port}")
        s.close()
        q.task_done()
t1 = time.time()
q = Queue()
for i in range(start_port, end_port+1):
    q.put(i)
for i in range(1000):
    t = Thread(target=start_scan)
    t.start()
q.join()
t2 = time.time()
print(f"Scan Completed in {t2-t1} Seconds........")
