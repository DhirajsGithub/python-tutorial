with open('109love_story.txt', 'r') as rf:
# with open ('109love_story.txt','r', encoding= 'UTF-8') as rf:        # for any windows user or any ohter text editor
    print(rf.encoding)    #-----> UTF-8
    data = rf.read()
    print(data)


# reading a large file with small chunks !
# with open ('109large.txt', 'r') as largef:
#     data = largef.read()
#     print(data)
with open('109large.txt', 'r') as largef:
    data = largef.read(100)
    while len(data) > 0:
        print(data)
        data = largef.read(100)