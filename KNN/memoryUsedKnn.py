import os
import psutil

from knn  import my_knn_function


my_knn_function()
process = psutil.Process(os.getpid())
used_memory = process.memory_info().rss/1024/1024

print("Memorie folosita: %s Mb" % used_memory) 
