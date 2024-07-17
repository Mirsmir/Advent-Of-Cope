import re

data=list()
for _ in range(100):
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    data.append(input())
    
# n=0
# checker = [(str(n) in range(50))]
# print(checker)

# r1=0
# r2=50
# def checker(r1, r2):
#     return tuple(range(r1, r2))

game=0
total=0
green=0
red=0
blue=0
for indexe,line in enumerate(data):
    game+=1
    line=((str(str(line)[str(line).find(":")+len(":"):])))
    # im so funny
    data[indexe]=line
    over = False
    print(line) 
    print('game ' + str(game))
    green=0
    blue=0
    red=0
    
    
    bigBlock=line.split(";")
    # set=re.sub("'"," ",(str(str(bigBlock)[str(bigBlock).find("['")+len("['"):str(bigBlock).find("']")])))  
    
    
    for index,poo in enumerate(bigBlock): 
        bigBlock=line.split(";")
        print(bigBlock[index])       
        subset= str(bigBlock[index]).split(",")
        print('total',total)
        
        for dune, _ in enumerate(subset): 
            subset= str(bigBlock[index]).split(",")
            print(subset[dune])
            num=0
            
            color=re.search("green|red|blue",subset[dune]).group()
            match color:
                
                case "green":
                    num = re.search("\d+",subset[dune]).group()
                    if green<int(num):
                        green=int(num)
                    print(green)
                                       
                case "blue":
                    num=int(re.search("\d+",subset[dune]).group())
                    if blue<num:
                        blue=num
                    print(blue)
                                                           
                case "red":
                    num=int(re.search("\d+",subset[dune]).group())
                    if red<num:
                        red=num
                    print(red)
            power=red*blue*green
        print('power: ',power)
    total+=power
       
        
         
print('total:', total)

                    







