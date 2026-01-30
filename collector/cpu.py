import time
target="cpu "
file_path="/proc/stat"
extracted_metrics=[]
def get_cpu():
    with open(file_path) as file:
        for line in file:
            if line.startswith(target):
                extracted_metrics=[int(val) for val in line.split()[1:]]
                total_time=sum(extracted_metrics,0)
                idle_time=extracted_metrics[3]
                return total_time,idle_time

t1, i1=get_cpu()
time.sleep(1)
t2, i2=get_cpu()

delta_total=t2-t1
delta_idle=i2-i1

cpu_usage=(delta_total-delta_idle)/delta_total * 100
print(cpu_usage,"%")


