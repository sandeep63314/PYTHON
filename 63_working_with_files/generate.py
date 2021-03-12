alphabets = ['A','B','c','d','e','f','g','h','i','J','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

unicode = [int((val * (val + 1))/2) for val in [ord(l) for l in alphabets]]

print(unicode)
print(unicode[9])

alphabets = [chr(ch) for ch in [int((val * (val + 1))/2) for val in [ord(l) for l in alphabets]]]

print(alphabets)

print(ord(alphabets[14]))
