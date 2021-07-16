from multiprocessing import Pool, cpu_count
import time

runtime = 60*2

def stress_test(x):
    timeout = time.time() + runtime  # runtime in seconds
    while True:
        if time.time() > timeout: break
        else: 1.01 * 100
            
def run_stress_test():
    print("running stress test")
    pool = Pool(processes=cpu_count())
    pool.map(stress_test, range(cpu_count()))
    pool.close()
    pool.join()
            
if __name__ == "__main__":
    run_stress_test()
