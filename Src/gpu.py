# gpu.py — NVIDIA via nvidia-smi
import subprocess

def get_gpu_usage():
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
        stdout=subprocess.PIPE, text=True
    )
    return float(result.stdout.strip())
