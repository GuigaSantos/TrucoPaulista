from utils.shuffle import shuffle
from utils.selectplayer import selectplayer
from utils.selectcard import selectcard


pointt1 = 0
pointt2 = 0
rodada = 1
firstp = "p1"




while  pointt1 < 12 and pointt2 < 12:
    vira, listplayer = shuffle()

    lista = {
        "p1": listplayer[0],
        "p2": listplayer[1],
        "p3": listplayer[2],
        "p4": listplayer[3]
    }


    
    print(f"\n\nRODADA: {rodada}")

    rodadat2 = 0
    rodadat1 = 0
    for q in range(3):
        print("\n\n")
        print(f"placar : Rodada [{rodadat1}]x[{rodadat2}] | Partida [{pointt1}]x[{pointt2}]")

        print(f"O vira é: {vira["nome"]} de {vira["naipe"]}")

        print(f"Sua mão:")
        maop1 = lista["p1"]
        for x in range(len(maop1)):
            print(f"  [{x+1}]: {maop1[x]["nome"]} de {maop1[x]["naipe"]}  ", end="")
        print("\n")

        mesa = []

        for i in selectplayer(firstp):


            if i == "p1":

                while True:
                    try:
                        select = int(input("Qual carta jogar?"))
                        if select <= len(maop1) and select >= 1:
                            break
                        else:
                            print("formatação incorreta")
                    except ValueError:
                        print("formatação incorreta")

                carta = lista[i].pop(select - 1)
                mesa.append(carta)
                print(f"O jogador {i} jogou a carta {carta["nome"]} de {carta["naipe"]}")
                    
            else:
                carta = selectcard(lista[i], mesa)
                lista[i].remove(carta)
                print(f"O jogador {i} jogou a carta {carta["nome"]} de {carta["naipe"]}")
                mesa.append(carta)


        maiornvl = max(hnvl["nvl"] for hnvl in mesa)
        melado = [hcards for hcards in mesa if hcards["nvl"] == maiornvl]
        timesmelados = [tms["time"] for tms in melado]

        if len(set(timesmelados)) > 1:
            print("Essa rodada foi melada pelas cartas: ", end="")
            for i in melado:
                print(f"{i["nome"]} de {i["naipe"]} ", end="")
            print("")
            rodadat1 += 1
            rodadat2 += 1
        else:
            highcard = melado[0]
            firstp = highcard["player"]

            print(f"Vencedor dessa rodada foi: {firstp} com a carta {highcard["nome"]} de {highcard["naipe"]}")

            if highcard["time"]:
                rodadat1 += 1
            else:
                rodadat2 += 1

        if rodadat1 == 2 or rodadat2 == 2:
            break
        

    if rodadat1 > rodadat2:
        pointt1 += 1
    elif rodadat1 < rodadat2:
        pointt2 += 1
        

    
    rodada += 1