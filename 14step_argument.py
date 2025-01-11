#step argument
firstName = "Harshal"
print(firstName[0:4:1])               #[start:stop:step]
print(firstName[::1])
print(firstName[ ::2])                  # will start from 0th indexing and continue from there
print(firstName[::3])
print(firstName[1::2])
print(firstName[::-1])      #0 se start ho rahi hai and end tak ja rahi with -1 step toh reversehi hogayegi
print(firstName[-1::-1])    #same as above