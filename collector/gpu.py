import subprocess
import time

while True:
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=utilization.gpu,temperature.gpu", "--format=csv,noheader,nounits"],
        stdout=subprocess.PIPE,
        text=True
    )
    gpu_util, temp = result.stdout.strip().split(", ")
    print(f"GPU Load: {gpu_util}%, Temp: {temp}°C")
    time.sleep(2)
