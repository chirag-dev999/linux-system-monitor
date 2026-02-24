# gpu.py — NVIDIA via nvidia-smi
import subprocess

def get_gpu_temp():
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
        stdout=subprocess.PIPE,
        text=True   )
    return float(result.stdout.strip())
