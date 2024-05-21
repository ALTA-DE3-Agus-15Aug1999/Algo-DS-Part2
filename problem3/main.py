def playing_domino(cards, deck):
    hasil = []
    for domino in cards:
        if deck[0] in domino:
            hasil.append(domino)
        elif deck[1] in domino:
            hasil.append(domino)
    return hasil[0] if hasil else []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []