import os
import psutil

from logisticRegression  import my_function


my_function()
process = psutil.Process(os.getpid())
used_memory = process.memory_info().rss/1024/1024

print("Memorie folosita: %s Mb" % used_memory) 
