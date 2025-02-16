import os
import multiprocessing
import subprocess

def generate_load():
    # Generates load by creating an infinite loop
    while True:
        pass

if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()

    processes = []
    for _ in range(cpu_count):
        p = multiprocessing.Process(target=generate_load)
        p.start()
        processes.append(p)

    # Optionally, to keep the main script running indefinitely
    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
