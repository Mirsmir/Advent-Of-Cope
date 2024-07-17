import re

data=list()
nomera =list()
positions =list()

for _ in range(11):
    data.append(input())
    
spec ="!@#$%^&*()-+?_=,<>/"

def indexCalc(line,data):
    print(line)

    
for numerate,line in enumerate(data):
    data[numerate]=line
    num =re.findall("\d+",line)
    nomera.append(num) #num is the individual number in each line, nomera is the array of nums

print(nomera) #full list
index=0
        
def indexFinder(nomera, data,index,positions):
    
    for index,nums in enumerate(nomera):
        line2=data[index]
        print(index,"index")
        print(line2, "line")
        print(nums,"list in array from that one line")
        
        for num in nums:
            print(num)
            position= line2.find(num)
            print(position,"pos")
            if line2[position-1] in spec:
                print("yes")
            endPosition = position+len(num)-1
            print(endPosition,"endPos")
            if line2[endPosition+1] in spec:
                print("yes")
                
            
            positions.append([position,endPosition])

    return (position,endPosition,index,positions)
    
indexFinder(nomera, data, index, positions)       

print(positions)

def specFinder(positions,data):
        for index,things in enumerate(positions):
            for pos in things:
                print(pos)
                print(line)
                print(line[pos])
                if line[pos] in spec:
                    print("yes")
                else:
                    print("no")


# def arrayMaker(data,num,nomera):
#     lineLen=len(line2)
#     for index,num in enumerate(nomera):
#         for jim in num:
#             line2=data[index]
#             print(line2)
#             print(jim,"jim")
#             pos= line2.find(jim)
#             print(pos)
#             foo=list()
            
#             print(line2[pos])
            
#             while pos>=lineLen:

#                 foo.append(line2[pos-1])  
#                 foo.append(data[index-1][pos+len(jim)])              
                
#             print(foo,jim)
            
# arrayMaker(data,num,nomera)
            


              
        
    
# specFinder(positions,data)

