import time, threading

def walk_dog(name):
    time.sleep(8)
    print(f"Walking my dog {name}")

def take_out_trash():
    time.sleep(4)
    print("Taking out the trash")

def clean_house():
    time.sleep(5)
    print("Cleaning the house")

chore1 = threading.Thread(target=walk_dog, args=("Scooby doo",))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=clean_house)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are done.")
