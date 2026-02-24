import time

filepath = "/proc/loadavg"

def get_proc():
    with open(filepath) as file:
        line = file.readline()
        running, total = line.split()[3].split("/")
    return running, total

while True:
    running, total = get_proc()
    print("running processes:", running)
    print("total processes:", total)
    print()
    time.sleep(2)
