import time
file_path="/sys/class/drm/card2/device/gpu_busy_percent"
while True:
    with open(file_path) as file:
        print(file.read().strip(),"%")
        time.sleep(1)