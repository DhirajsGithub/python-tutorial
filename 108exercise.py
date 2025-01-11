# with open('108index.html', 'r') as rf:
#     with open('108output.txt','a') as wf:
#         for line in rf.readlines():
#             if '<a href=' in line:
#                 pos = line.find("<a href=")
#                 pos_1 = line.find('\"',pos)
#                 pos_2 = line.find("\"", pos_1+1)
#                 link = (f'{line[pos_1+1 : pos_2]}\n')
#                 wf.write(link)

# above code will give one link at a time, it will fail to give if there exist multiple link in a line 


with open('108index.html', 'r') as rf:
    with open('108output.txt', 'a') as wf:
        page = rf.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else :
                pos_1 = page.find('\"', pos)
                pos_2 = page.find('\"', pos_1+1)
                link = page[pos_1+1: pos_2]
                wf.write(link + '\n')
                page = page[pos_2:]
                