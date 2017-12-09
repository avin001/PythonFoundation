def box(width, height, symbol = '*'):
    """Print a box made up of asterisks or some other character.
    width: width of the box in characters, must be at least 2
    height: height of box in linex, must be at least 2
    symbol: a single character string used to draw the box edges
    """
    print(symbol * width) # print top edge of the box
    # print sides of the box
    for _ in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)
    print(symbol * width) # print bottom edge of the box


box(7, 5)
box(7, 5, '#')
box(4, 4, '$')
