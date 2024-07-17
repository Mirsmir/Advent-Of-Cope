import re

data=list()
spec = "!@#$%^&*()-+?_=,<>/"

for _ in range(11):
    data.append(input())
    
#TODO:dont want to overextend past the line this TIME. (index out of bonds) 


nomera=list()

for row,line in enumerate(data): #2d array, column is the index of indiv number in each row, row is the line num
    #in this case u have each colmn multiplied by number of rows
    #row points to array of array of columns which points to an int object
    nums = list(re.finditer("\d+",row))
    # create object with span (ik i can make this shorter but i wont)
    for intestine in nums: #intestine as in col ajajja
        print(intestine.start(), " num pos")
        
        # op object and look at seperate index vals
    specials = list(re.finditer("[^\d\.]",row))#not integer or a dot THANK YOU CODING CLUB
    for intestine in specials:
        print(intestine.start()," special char")         


# row, intestine = 11, 10
# foo = []
#wjhajhawkjjkaw


# for i in range(row):
#     col = []
#     for j in range(intestine):
#         line = data[j]
#         print(j)
#         print(line)
#         col.append(line[j])
# foo.append(col)
# print(foo)
# for line in data:
#     nomera.append(re.findall("\d+",line))
    
# print(nomera) 

# for index,line in enumerate(data):
#     nomera = list()
#     nomera.append(re.findall("\d+",line))
#     # print(line)
#     for n in nomera:
#        startPos= line.find(n)
#        endPos = startPos+len(n)-1





