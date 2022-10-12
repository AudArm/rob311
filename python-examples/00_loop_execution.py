import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ

if __name__ == "__main__":
    start = time.time()
    t = 0.0
    count = 0

    # Print "ROB311 @UM-ROBOTICS" for 5 seconds @200Hz


    for t in range(EXEC_TIME):
        for i in range(200):
            print("ROB311 @UM-ROBOTICS")
            count = count + 1
            time.sleep(DT - 0.0001511005)

        print(time.time())
    print(time.time()-start)
    print(count)



