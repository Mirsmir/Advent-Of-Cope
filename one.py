import re;
#regEx

data = list()
for _ in range(1000):
    data.append(input())    

total = 0

for index, line in enumerate(data):
    tens = re.search("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9",line).group()
    if tens=="one":
        tens = re.sub(tens,"1",tens)
    if tens=="two":
        tens= re.sub(tens,"2",tens)
    if tens=="three":
        tens = re.sub(tens,"3",tens)
    if tens=="four":
        tens = re.sub(tens,"4",tens)
    if tens=="five":
        tens = re.sub(tens,"5",tens)
    if tens=="six":
        tens = re.sub(tens,"6",tens)
    if tens=="seven":
        tens = re.sub(tens,"7",tens)
    if tens=="eight":
        tens = re.sub(tens,"8",tens)
    if tens=="nine":
        tens = re.sub(tens,"9",tens)
    print(tens)
    ones = re.search("one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9"[::-1],line[::-1]).group()
    if ones=="eno":
        ones = re.sub(ones,"1",ones)
    if ones=="owt":
        ones = re.sub(ones,"2",ones)
    if ones=="eerht":
        ones = re.sub(ones,"3",ones)
    if ones=="ruof":
        ones = re.sub(ones,"4",ones)
    if ones=="evif":
        ones = re.sub(ones,"5",ones)
    if ones=="xis":
        ones = re.sub(ones,"6",ones)
    if ones=="neves":
        ones = re.sub(ones,"7",ones)
    if ones=="thgie":
        ones = re.sub(ones,"8",ones)
    if ones=="enin":
        ones = re.sub(ones,"9",ones)
    print(ones)
    line=int(tens)*10 +int(ones)
    print(line)
    total+=int(line)
    data[index]=line
    
print(total)

# for line in data:
#     curr_num = 0
#     count=0
#     for char in line:
#             if char in checker: 
#                 curr_num += int(char)*10
#                 print(curr_num)
#                 break
#     for char in line[::-1]:
#             if char in checker: 
#                 curr_num += int(char)
#                 print(curr_num)
#                 break
#     total += curr_num

