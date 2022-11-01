import os 
import threading
from Campo_bot import CampoBot
from Adm_bot import AdmBot
import time
def main():
    print("\n" * os.get_terminal_size().lines)
    print(30*"-")
    print("Inciando Bots de Campo e ADM")
    print(30*"-")
    while True:
        time.sleep(10)
        t1 = threading.Thread(target=CampoBot)
        t2 = threading.Thread(target=AdmBot)
        t1.start()
        t2.start()
        t1.join()
        t2.join()


if __name__ == "__main__":
    main()