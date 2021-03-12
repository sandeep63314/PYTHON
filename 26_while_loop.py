# while loop is used to loop over a given condition
print("Print 'A'")
ctr = 6
size = ctr
blk = ' ' * ctr
str = blk + '*'
print(str)
while 0 < ctr:
    ctr -= 1
    blk = ' ' * ctr
    str = blk + '*'
    diff = size - ctr
    if ctr == size / 2:
        str += ('*' * diff) + ('*' * (diff - 1)) + '*'
        print(str)
        continue
    else:
        str += (' ' * diff) + (' ' * (diff - 1)) + '*'
        print(str)

print("Print 'B'")
ctr = 0
len = 10
while ctr < 7:
    if ctr % 3 == 0:
        str = '*' * len
        print(str)
    else:
        str = '*' + (' ' * (len + 1)) + '*'
        print(str)
    ctr += 1

print("Print 'C'")
ctr = 0
len = 10
while ctr < 7:
    if ctr % 6 == 0:
        str = '*' * len
        print(str)
    elif ctr in [1, 5]:
        str = '*' + (' ' * (len + 1)) + '*'
        print(str)
    else:
        print('*')
    ctr += 1

print("Print 'D'")
ctr = 0
mid = int(size / 2)
blk = 2
str = '*'
print(str)
while ctr < 5:
    if ctr < mid:
        blk += 3
        str = '*' + (' ' * blk) + '*'
        print(str)
    else:
        blk -= 3
        str = '*' + (' ' * blk) + '*'
        print(str)
    ctr += 1
else:
    str = '*'
print(str)

print("Print 'E'")
ctr = 0
while ctr < 7:
    if ctr % 3 == 0:
        str = '*' * 13
        print(str)
    else:
        str = '*'
        print(str)
    ctr += 1

print("Print 'F")
ctr = 7
start = ctr
mid = int(ctr / 2)
while ctr > 0:
    if ctr in [start, mid + 1]:
        print('*' * 13)
    else:
        print('*')
    ctr -= 1

print('Print \'G\'')
length = 13
height = 7
length_mid = int(length / 2)
height_mid = int(height / 2)
l_mid = length_mid
while height > 0:
    if height > (height_mid + 1):
        if l_mid < 0:
            l_mid = 0
        if (height % 6) == 1:
            str = (' ' * length_mid) + ('*' * (length - length_mid))
            print(str)
        else:
            l_mid -= 2
            str = (' ' * (l_mid)) + '*'
            print(str)
    elif height == (height_mid + 1):
        str = '*' + (' ' * (length_mid - 1)) + ('*' * (length - length_mid))
        l_mid -= 2
        print(str)
    else:
        if (height % 6) == 1:
            str = (' ' * length_mid) + ('*' * (length - length_mid))
            print(str)
        else:
            l_mid += 2
            str = (' ' * (l_mid)) + '*' + (' ' * (length - l_mid - 2)) + '*'
            print(str)
    height -= 1

print("Print 'H'")
height = 7
mid = round(height / 2)
while height > 0:
    if height == mid:
        str = ('*' * 13)
        height -= 1
        print(str)
    str = '*' + (' ' * 11) + '*'
    print(str)
    height -= 1

print("Print 'I'")
height = 0
length = 13
len_mid = int(length / 2)
while height < 7:
    if (height % 6) == 0:
        str = '*' * length
        print(str)
    else:
        str = (' ' * len_mid) + '*'
        print(str)
    height += 1

print("Print 'J'")
height = 6
length = 13
height_mid = int(height / 2)
len_mid = round(length / 2) + 1
blank = len_mid
ctr = 0
print('*' * 13)

while height > 0:
    if height > height_mid:
        print((' ' * (len_mid - 1)) + '*')
    else:
        blank = blank - 2
        str = ((' ' * ctr) + '*') + (' ' * blank) + ('*' + (' ' * ctr))
        ctr += 1
        print(str)
    height -= 1