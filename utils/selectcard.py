def selectcard(player, mesa):
    if len(mesa) >0:
        maiorcard = max(mesa, key=lambda item: item["nvl"])

        if maiorcard["time"] == player[0]["time"] or maiorcard["nvl"] > max(player, key=lambda item: item["nvl"])["nvl"]:
            return min(player, key=lambda item: item["nvl"])
        
        else:
            return max(player, key=lambda item: item["nvl"])
    else:
        return player[0]
    
    return