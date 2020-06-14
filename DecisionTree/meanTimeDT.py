from decisionTree  import my_DT_function

sum=0
nr_iterations=10

for index in range  (0,nr_iterations):
   sum=sum+my_DT_function()

medie = sum/nr_iterations
print("Medie executie: %s" % medie)