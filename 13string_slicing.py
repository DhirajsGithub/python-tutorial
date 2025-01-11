#slicing / selecting sub sequences
lang = "python"
#works like - [start argument : stope argument)       ---> start argument included stop argument is excluded
print(lang[1:4])
print(lang[-5:-2])

print(lang[1:])    #no stoping argument hence start argument to ending tak jayegi
print(lang[:])     #no start and stop argument hence puri string print ho jayegi
print(lang[0:78])  #insuuficent bigger stop argument hence stating argument se ending tak jayegi
print(lang[:3])   #no start argument agar waise hain to start argument 0 hi hoga