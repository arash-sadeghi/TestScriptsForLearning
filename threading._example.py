'''Learning Multi Threading'''
import threading
import time 

def func(inp):
    global var
    var += 1
    print("[+] func started")
    print(f"[+] say {inp} and variable {var}")
    time.sleep(1)
    print("[+] func ended")


var = 20 #! this will be recieved by func

def main():
    # var = 10 #! this will not be recieved by func

    t1 = threading.Thread(target = func, args = ['gada'])
    t1.start()

    t2 = threading.Thread(target = func, args = ['gada2'])
    t2.start()

    t1.join()
    t2.join()

    print(f"[+] end of main {var}")

if __name__ == '__main__':
    t = time.time()
    main()
    print(f"[+] main took {time.time()-t} s")