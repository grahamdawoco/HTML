dfa = open("dfa.txt")
input = open("input.txt")
output = open("output.txt","w")
lines = dfa.readlines()
i=0
for line in lines:
    lines[i]=line.rstrip().split(",")
    i=i+1
print (lines)
states=lines[0]
alphabet=lines[1]
initial=lines[2]
finals=lines[3]
rules=lines[4:]
#numstates = len(states)
#lenalph = len(alphabet)
#numrules=numstates*lenalph

lines1 =input.readlines()
j=0
#print(lines1)
for line in lines1:
    line=line.rstrip()
    lines1[j]=list(line)
    j=j+1
print(lines1)

for line in lines1:
    currentstate = initial
    print(initial)
    print(currentstate[0])
    for element in line:
        for rule in rules:
            print(initial)
            if rule[0] == currentstate[0] and rule[1] == element:
                currentstate = rule[2]
                print(initial)
                break
    if currentstate in finals:
        print('accept')
        output.write('accept\n')
    else:
        print('reject')
        output.write('reject\n')
dfa.close()
input.close()
output.close()