# cpu.py
file_path = "/proc/stat"

_prev = (None, None)

def get_cpu():
    with open(file_path) as f:
        for line in f:
            if line.startswith("cpu "):
                vals = [int(v) for v in line.split()[1:]]
                return sum(vals), vals[3]
    return None, None

def get_cpu_usage():
    global _prev
    t1, i1 = _prev
    t2, i2 = get_cpu()
    _prev = (t2, i2)
    if t1 is None or t2 is None:
        return 0.0
    delta_total = t2 - t1
    delta_idle  = i2 - i1
    return round((delta_total - delta_idle) / delta_total * 100, 1)
