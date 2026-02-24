import multiprocessing
import time

def burn_cpu():
    while True:
        pass

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)

    time.sleep(10)  # Run for 10 seconds

    for p in processes:
        p.terminate()

    print("Finished safely.")
