preamble = '''
<html>
  <head>
    <style>
      body {
        font-family: Arial, Helvetica, sans-serif;
      }
      table {
        border: solid black 0.15rem;
        border-collapse: collapse;

        font-size: 1.5em;
        font-family: inherit;
        font-weight: bold;

        margin-bottom: 10rem;
      }
      tr {
      }
      td {
        width: 10rem;
        height: 10rem;
        text-align: center;

        padding: 1rem;
        border: solid gray 0.1rem;
      }

      div.id {
        width: 100%;
        text-align: right;
      }

      @media print {
        .break {
          break-after: page;
        }
      }
      @media screen {
        table {
        }
      }
    </style>
  </head>
  <body>
'''
postamble = '  </body>\n</html>\n'

def __card_to_html(card, n = None):
    html = ''
    if n is not None:
        html += '<div class="id">{0}</div>'.format(n)
    html += '    <table>\n'
    for row in card:
        html += '      <tr>\n'
        html += '\n'.join('        <td>{0}</td>'.format(x) for x in row)
        html += '      </tr>\n'
    html += '    </table>\n'
    return html

def card_to_html(card, n = None):
    '''
    Create the HTML for a single Bingo card.
    '''
    return preamble + __card_to_html(card, n) + postamble

def cards_to_html(cards):
    '''
    Create the HTML for a collection of Bingo cards.
    '''
    html = preamble
    for i in range(len(cards)):
        html += __card_to_html(cards[i], i+1)
        if i % 2 == 1:
            html += '<div class="break"></div>'

    html += postamble
    return html
