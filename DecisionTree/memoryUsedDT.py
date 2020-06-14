import os
import psutil

from decisionTree  import my_DT_function

my_DT_function()
process = psutil.Process(os.getpid())
used_memory = process.memory_info().rss/1024/1024

print("Memorie folosita: %s Mb" % used_memory) 
