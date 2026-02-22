from multiprocessing import Process, cpu_count
import time

def counter(number):
    while number > 0:
        number -= 1
        time.sleep(0.1)


def spawn_processes(num_processes):
    processes = [Process(target=counter, args=(1000,)) for _ in range(num_processes)]
    for process in processes:
        process.start()
        print(f"test {process.pid}.")
    for process in processes:
        process.join()
        print(f"test {process.pid} is klaar.")

def main():
    num_processors = cpu_count()
    num_processes = num_processors * 200
    spawn_processes(num_processes)


if __name__ == "__main__":
    main()
    print("geslaagt")