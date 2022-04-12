import shutil
import os

uname = os.uname()
total = str((shutil.disk_usage("/").total // (2**30))) + "GB"
used = str((shutil.disk_usage("/").used // (2**30))) + "GB"
free = str((shutil.disk_usage("/").free // (2**30))) + "GB"










