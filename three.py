import re

data=list()
for _ in range(11):
    data.append(input())
    spec = "!@#$%^&*()-+?_=,<>/"

# we can try to rearrange the data to form both rows and columns
# then check if any of those slots have a special character

# nvmd, we're gunna look at the index of the number in line X, 
# after searching for special characters on the index +- the numbers first and last indexes
# then we go back to the index of the previous line and then line right after
# (index +- 1), and we look at the same indexes as the number in line X
# only now were looking for the special characters 


total=0

for indexData,line in enumerate(data):
    # pos=0
    # numIndx=0
    # lenght=0
    # print(line)
    pos=list()
    data[indexData]=line
    
    
    nums=re.findall("\d+",line)
    # print(nums)

    for poo,smallNum in enumerate(nums):
        # print(nums[poo])
        nums[poo]=smallNum
        length=len(smallNum)
        numIndx=line.find(smallNum)
        # print(numIndx,':',length+numIndx-1)   
        # poo will be used to see what index of the list (nums)
        # was found at what index of data line 
                        
        for index,char in enumerate(line):
            if char in spec:
                pos.append(index)
                # print(pos)
                for position in pos:
                    # print(position,char,'position')  
                    print()
    
                if position == length+numIndx or position == numIndx-1:
                    # print('WOO, ITS A SPECIAL NUM')
                    # print(smallNum)
                    total+=int(smallNum)
                    # print('TOTAL',total)
               
print('total: ',total)

numbers=list()


    # donc, on doit faire comme ca: we will have a function that will num with a variable argument (specifically the num)
    # then we will have for loop that calls that function but increments the num everytime
    # we will then have a correspponding index to look at based on what column we should be lookimg at
    # then we will do for loop in range 3, index of line before and after, and we will create a list 
        
    # that has a range of the length +1 on either side of the num.

# indexCalc(data,position,length,numbers,start,end)
def indexCalc(line,end,position,length,number):    
    
    print(line)
    print(number,'number')
    length=len(number)
    position=line.find(str(number))
    print(position,':',position+length-1)
    end=position+length-1

    print(end,'end index')
    return position,end,length



def dataFind(data,position,end,index,spec):
    print(data)
    currentLine=data[index]
    previousLine=data[index-1]
    futureLine=data[index+1]
    coolNum=False
    print(end)
            
    if line[end-1] or line[position+1] or previousLine[position+1] or previousLine[end-1] or futureLine[position+1] or futureLine[end-1] in spec: 
        coolNum=True
    elif currentLine[end-1] or currentLine[position+1] in spec:
        coolNum=True
        


for index, line in enumerate(data):

    nomera=list()
    numbers=re.findall("\d+",line)
    nomera.append(numbers)
    
    for indexNomera,numbers in enumerate(nomera):

        for number in numbers:
            start=0
            end=0
            end=str((indexCalc(line,end,position,number,data))[1:2].replace(',',''))[1:-1]
            #start at 1, which is where ( is, then step backwards where ) is.
            position=str((indexCalc(line,end,position,number,data))[:1:].replace(',',''))[1:-1]
            print(position,':',end)
            print(dataFind(data,position,int(end),length,index,spec))
            # print(str(line[index-1]).split(position, end))
            
            
            #make an array that stores the specified indexes of the the line before and after the line 
            # in question, then check if there a special char in the array. 
            
    
    
        

           


    






    