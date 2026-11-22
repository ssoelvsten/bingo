import argparse
import random
from pathlib import Path
import sys

from gen import gen_cards
from html import card_to_html, cards_to_html

################################################################################
# Argument Parsing
################################################################################

parser = argparse.ArgumentParser(
    prog="gen",
    description='Generate (Un)fair Bingo Cards.',
)
parser.add_argument('history', metavar='path', type=str,
                    help='file name to use as the draw history')
parser.add_argument('count', metavar='n', type=int,
                    help='number of cards to generate')
parser.add_argument('--rows', metavar='n', type=int, default=3,
                    help='number of rows')
parser.add_argument('--columns', metavar='n', type=int, default=5,
                    help='number of columns')
parser.add_argument('--theme', type=str, default=None,
                    help='theme [XMas] to apply to visual outputs')
parser.add_argument('--min', metavar='n', type=int, default=0,
                    help='minimum number of turns to win first row')
parser.add_argument('--max', metavar='n', type=int, default=sys.maxsize,
                    help='maximum number of turns to win all rows')

args = parser.parse_args()

with open(args.history, 'r') as file:
    history = [x for x in file.read().split('\n') if len(x) > 0]

################################################################################
# Generate bingo cards
################################################################################
cards, winners = gen_cards(history, args.count, args.rows, args.columns, args.min, args.max)

print("Generated {0} cards".format(len(cards)))

print("\nWinners:")
for (t,i) in winners:
    print("  {0:4d} @ t = {1}".format(i,t))

################################################################################
# Write cards to file(s)
################################################################################
Path("./out").mkdir(parents=True, exist_ok=True)

for i in range(len(cards)):
    with open('./out/{0}.txt'.format(i+1), 'w') as file:
        for xs in cards[i]:
            file.writelines("\n".join(xs))
            file.write("\n")

    with open('./out/{0}.html'.format(i+1), 'w') as file:
        file.write(card_to_html(cards[i]))

with open('./out.html', 'w') as file:
    file.write(cards_to_html(cards, args.theme))
