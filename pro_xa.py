xadrez = [
    ["_|"," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8" ],
    ["1|","TBE","CBE","BBE","RBA","RBE","BBD","CBD","TBD"],
    ["2|","PB1","PB2","PB3","PB4","PB5","PB6","PB7","PB8"],
    ["3|","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["4|","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["5|","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["6|","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["7|","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["8|","PP1","PP2","PP3","PP4","PP5","PP6","PP7","PP8"],
    ["9|","TPE","CPE","BPE","RP2","RP2","BPD","CPD","TPD"]
    ]

def ATTX():
    for i in xadrez:
        for j in i:
            print(j, end=" ")
        print()
    print()

def jogador1(p1, p2, escolhaP):
    linha = 1
    coluna = 1
    for linha in range (len(xadrez)):
        for coluna in range(len(xadrez[linha])):
            if xadrez[linha][coluna] == escolhaP:
                xadrez[linha][coluna] = "| |"
    xadrez[p1][p2] = escolhaP
    return ATTX()

def jogador2(p1, p2, escolhaP):
    linha = 1
    coluna = 1
    for linha in range (len(xadrez)):
        for coluna in range(len(xadrez[linha])):
            if xadrez[linha][coluna] == escolhaP:
                xadrez[linha][coluna] = "| |"
    xadrez[p1][p2] = escolhaP
    return ATTX()

ATTX()

escolhaP = input("Escolha a peça Jogador 1:")
p1, p2 = map(int, input("Escolha a posição para mover a peça [Linha][Coluna]: ").split())
jogador1(p1, p2, escolhaP)

escolhaP = input("Escolha a peça Jogador 2:")
p1, p2 = map(int, input("Escolha a posição para mover a peça  [Linha][Coluna]: ").split())
jogador2(p1, p2, escolhaP)


