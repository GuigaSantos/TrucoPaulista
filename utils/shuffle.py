import copy
import random
from .cards import cards

pesomanilha = {
    "ouros": 11,
    "espadas": 12,
    "copas": 13,
    "paus": 14,
}

ordem = ["p1", "p2", "p3", "p4"]

def shuffle():
    listplayer = []

    newcards = copy.deepcopy(cards)
    random.shuffle(newcards)
    vira = newcards.pop()

    if vira["nvl"] == 10:
        manilha = 1
    else:
        manilha = vira["nvl"] + 1

    for i in range(4):
        p = []
        for _ in range(3):
            carta = newcards.pop()
            carta["player"] = ordem[i]

            if (i+1)%2 == 0:
                carta["time"] = 0
                
            elif not (i+1)%2 == 0:
                carta["time"] = 1
                

            if carta["nvl"] == manilha:
                carta["nvl"] = pesomanilha[carta["naipe"]] 

            p.append(carta)
                


        listplayer.append(p)


    return vira, listplayer
