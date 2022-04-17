import shutil
import os
import psutil
import linux_utils
import subprocess
import fcntl
import struct
import json
from blkinfo import BlkDiskInfo



uname = os.uname()
total = str((shutil.disk_usage("/").total // (2**30))) + "GB"
used = str((shutil.disk_usage("/").used // (2**30))) + "GB"
free = str((shutil.disk_usage("/").free // (2**30))) + "GB"


path1 = "/home/paul/flash"
total1 = str((shutil.disk_usage(path1).total // (2**30))) + "GB"
used1 = str((shutil.disk_usage(path1).used // (2**30))) + "GB"
free1 = str((shutil.disk_usage(path1).free // (2**30))) + "GB"



a = psutil.disk_partitions()




def print_mounted_fs():
    c = 0
    for el in a:
        c = c + 1
        print(el)
        print(c)

#print(total, used, free)



#print(total1, used1, free1)

q = dir(os.path)


myblkd = BlkDiskInfo()
all_my_disks = myblkd.get_disks()
json_output = json.dumps(all_my_disks)

all_my_disks[0].pop("children",None)
all_my_disks


#print(type(all_my_disks[0]))
print(all_my_disks[0])


