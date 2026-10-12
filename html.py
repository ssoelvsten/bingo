def __preamble(columns, style):
    html =  '''
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
'''
    html += 'width: {0}vw;'.format(100 / columns)
    html += 'height: {0}vw;'.format(60 / columns)

    html += '''
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
    '''

    if style == "xmas":
        html += '''
      table {
        border-color: .0e7445;
        border-width: 0.2rem;

        margin-bottom: 0;
      }
      td {
        border-color: #0e7445;
        border-width: 0.2rem;
        color: #d72026;
      }
      div.id {
        text-align: center;
        color: #d72026;
      }
      img {
        width: 100%;
      }
      img.bot {
        margin-bottom: 8rem;
      }
'''

    html += '''
    </style>
  </head>
<body>
    '''
    return html

def __postamble():
    return '  </body>\n</html>\n'

def __card_to_html(card, n = None, style = None):
    html = ''

    if n is not None:
        html += '<div class="id">{0}</div>'.format(n)

    if style == "xmas":
        html += '<img class="top" src="./assets/xmas-top.svg" />'

    html += '    <table>\n'
    for row in card:
        html += '      <tr>\n'
        html += '\n'.join('        <td>{0}</td>'.format(x) for x in row)
        html += '      </tr>\n'
    html += '    </table>\n'

    if style == "xmas":
        html += '<img class="bot" src="./assets/xmas-bot.svg" />'

    return html

def card_to_html(card, n = None, style = None):
    '''
    Create the HTML for a single Bingo card.
    '''
    return __preamble(len(card[0]), style) + __card_to_html(card, n, style) + __postamble()

def cards_to_html(cards, style = None):
    '''
    Create the HTML for a collection of Bingo cards.
    '''
    html = __preamble(len(cards[0][0]), style)
    for i in range(len(cards)):
        html += __card_to_html(cards[i], i+1, style)
        html += '<div class="break"></div>'

    html += __postamble()
    return html
