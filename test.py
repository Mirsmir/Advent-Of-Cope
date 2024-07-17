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
    # to add an end:    str(line).rfind("'")
    data[indexe]=line
    over = False
    print(line) 
    print('game ' + str(game))
    
    
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
                    num = re.search("1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |13|14|15|16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |27 |28 |29 |30 |31 |32 |33 |34 ",subset[dune]).group()
                    if num>green:
                        green=num
                    print(green)
                    if green>13:
                        over=True
                        break
                   
                case "blue":
                    blue=0
                    num=re.search("1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |27 |28 |29 |30 |31 |32 |33 |34 ",subset[dune]).group()
                    blue+=int(num)
                    print(blue)
                    if blue>14:
                        over=True
                        break
                                       
                case "red":
                    red=0
                    num=re.search("1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |27 |28 |29 |30 |31 |32 |33 |34 ",subset[dune]).group()
                    red+=int(num)
                    print(red)
                    if red>12:
                        over=True
                        break
        print(over)
    if over == False:
        total+=game
        
        
            
            
          
    
  
print('total:', total)
