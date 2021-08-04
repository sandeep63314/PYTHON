import difflib
import sys
s = []
t = []
source = open('sourceFile.txt','r')
target = open('targetFile.txt','r')
diff = (difflib.unified_diff(source.readlines(),target.readlines(),fromfile='source',tofile = 'target'))
#sys.stdout.writelines(diff)
for line in diff:
    if line[:3] == '---':
        continue
    elif line[:3] == '+++':
        continue
    elif line[:2] == '@@':
        continue
    elif line[0] == '-':
        s.append('Source:' + line[1:])
    elif line[0] == '+':
        t.append('Target:' + line[1:])

with open('fileDifference.txt','w+') as d:
    for x, y in list(zip(s, t)):
        d.write(x.strip() + '\n')
        d.write(y.strip() + '\n')
print('Completed!!!Check delta change in fileDifference.txt')