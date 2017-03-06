import socket
import subprocess

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
s.connect(("ctf.upml.tech", 1337))

possibles = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

figs = {}
for char in possibles:
    sw = subprocess.Popen("figlet "+char, shell=True, stdout=subprocess.PIPE).stdout.read()
    figs[char] = sw

def name_char(char):
    char = '\n'.join(char)+'\n'
    for poss in possibles:
        works = figs[poss]
        if char == works:
            # print poss, repr(works)
            return poss

    return input().strip()

def solve(prob):
    tokens = []
    i = 0
    while i < len(prob[2]):
        spaces = True
        for h in range(len(prob)):
            if prob[h][i] != ' ':
                spaces = False
                break

        if spaces:
            character = []
            for h in range(len(prob)):
                character.append(prob[h][:i])
                prob[h] = prob[h][i+1:]
            tokens.append(character)
            i = 0
        else:
            i = i+1
    tokens.append(prob)

    ans = ""
    for c in tokens:
        if c[0] == '':
            continue
        this = name_char(c)
        ans += this

    return ans

solved = 0
while solved < 100:
    prob = s.recv(10000)

    prob = prob.split('\n')
    prob = prob[3:-2]

    ans = solve(prob)

    s.send(ans + "\n")

    solved += 1

fin = s.recv(10000)
print(fin)
