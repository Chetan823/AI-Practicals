MAX, MIN = 1000, -1000

def alphabeta(depth, nodeIndex, maximisingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximisingPlayer:
        best = MIN

        for i in range(0,2):
            val = alphabeta(depth+1, nodeIndex*2+1, False, values, alpha, beta)
            best = max[best, val]
            alpha = max[alpha, best]

            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range (0,2):
            val = alphabeta(depth+1, nodeIndex*2+1, True, values, alpha, beta)
            best = min[best, val]
            beta = min[beta, best]

            if alpha <= beta:
                break

        return best


values = [3,5,6,9,1,2,0,-1]
print("The optimal values are:", alphabeta(0, 0, True, values, MIN, MAX))
