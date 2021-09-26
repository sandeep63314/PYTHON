# Enter your code here. Read input from STDIN. Print output to STDOUT
values = (input()).split()
l,b = int(values[0]),int(values[1])
if (l%2 != 0) and (l*3 == b):
    l1 = l//2
    str = '.|.'
    for i in range(l1):
        print(str.center(b,'-'))
        str = '.|.'+str+'.|.'
    print('WELCOME'.center(b,'-'))
    start = 3
    stop = len(str) - 3
    for i in range(l1):         
        print(str[start:stop].center(b,'-'))
        start += 3
        stop -= 3
