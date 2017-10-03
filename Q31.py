import time
import psutil
import sys
## Prerequesit are time and PSUTIL libraries

def update():
    i=1
    val=eval(raw_input("Enter the time in second till which you want to see the result:->"))
    while (val>0):
        time.sleep(5)
        print("i=:",i)
        val1=psutil.cpu_count()
        #total no. of cpu core in your system
        val2 = round(psutil.cpu_percent(),1)
        # val2 have the percentage of cpu utilization
        val3=psutil.virtual_memory();
        #RAM usage in the system
        val4=psutil.disk_usage('/');
        # disk usage in the system
        print('CPU CORE:',val1)
        print('CPU USAGE:',val2)
        print('RAM Usage:',val3)
        print('Disk USage:',val4)
        print'--------------------------'
        val=val-5
        i=i+1


update()

