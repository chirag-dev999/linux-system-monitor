# process.py
filepath = "/proc/loadavg"

def get_processes():
    with open(filepath) as f:
        running, total = f.readline().split()[3].split("/")
    return running, total
