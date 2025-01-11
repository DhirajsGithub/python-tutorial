#define a function take any no of lists containig numbers return average of the first element of each list
# argument = ([1,2,3,4],[2,4,6],[5,6,8,5],[1,2])

# take a reference for two lists
# def avg_finder(l1,l2):
#     merging_two = zip(l1,l2)
#     average = []
#     for pair in merging_two :
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg_finder([1,2,3,4],[2,4,6]))

# def avg_finder (*args):
#     merginig_all = zip(*args)
#     average = []
#     for pair in merginig_all:
#         average.append(sum(pair)/len(pair))
#     return average

# print(avg_finder([1,2,3],[2,4,6],[5,6,8],[1,2,7]))


#above code in one line
avg_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder([1,2,3],[2,4,6],[5,6,8],[1,2,7]))