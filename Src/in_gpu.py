# in_gpu.py — integrated GPU via sysfs
file_path = "/sys/class/drm/card2/device/gpu_busy_percent"

def get_ingpu_usage():
        with open(file_path) as f:
            return float(f.read().strip())

