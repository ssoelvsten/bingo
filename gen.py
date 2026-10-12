import random

def __gen_card(history, yrotsih, rows, cols):
    '''
    Generate a card of size `rows*cols` with entries from `history` together
    with at what time rows are going to be filled.
    '''
    entries = [x for x in history]
    random.shuffle(entries)
    card = [entries[r*cols:r*cols+cols] for r in range(rows)]

    timings = [max([yrotsih[x] for x in xs]) for xs in card]
    timings.sort()

    return (card, timings)

def gen_cards(history, n, rows, cols):
    '''
    Generate `n` cards such that only one player wins each individual number of
    rows and never the same player wins twice.
    '''
    yrotsih = {}
    for i in range(len(history)):
        yrotsih[history[i]] = i

    card, timings = __gen_card(history, yrotsih, rows, cols)
    cards = [card]
    winners = [(t, 0) for t in timings]

    while True:
        card, timings = __gen_card(history, yrotsih, rows, cols)

        shadowings = sum([timings[i] < winners[i][0] for i in range(rows)])
        if shadowings > 1:
            continue

        winners = [(timings[i], len(cards)) if timings[i] < winners[i][0] else winners[i] for i in range(rows)]
        cards.append(card)

        if len(cards) < n:
            continue
        if len(set([i for (_, i) in winners])) is not len(winners):
            continue
        break

    return cards, winners
