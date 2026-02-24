# memory.py
filepath = "/proc/meminfo"

def get_memory_usage():
    total, avail = 0, 0
    with open(filepath) as f:
        for line in f:
            if line.startswith("MemTotal:"):
                total = int(line.split()[1])
            elif line.startswith("MemAvailable:"):
                avail = int(line.split()[1])
            if total and avail:
                break
    return round((total - avail) / total * 100, 1)
