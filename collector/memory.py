import time
filepath="/proc/meminfo"
    
            
def get_memstats():
    total_mem=0
    availmem=0
    with open(filepath) as file:
        for line in file:
            if line.startswith("MemTotal: "):
                total_mem=int(line.split(":")[1].replace("kB","").strip())
            if line.startswith("MemAvailable: "):
                availmem=int(line.split(":")[1].replace("kB","").strip())
            if total_mem>0 and availmem>0:
                break
    return total_mem,availmem
        

while True:
# snapshot1
    total_mem,availmem=get_memstats()
    total_mem/=1024*1024
    availmem/=1024*1024
    actual_mem=total_mem-availmem
    ram_usage=(actual_mem/total_mem)*100
    print(round(ram_usage,2),"%")
    time.sleep(2)


