# Our price table and offers: 
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+




def checkout(skus):
    
    # Dictionary of item prices
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
        'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90, 'M': 15, 'N': 40,
        'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 30, 'T': 20, 'U': 40,
        'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z': 50
    }

    # Dictionary of special offers
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': (2, 'B'),  # Buy 2 E, get one B free
        'F': (3, 20),   # Buy 3 F, pay for 2
        'H': [(10, 80), (5, 45)],
        'K': [(2, 150)],
        'N': (3, 'M'),  # Buy 3 N, get one M free
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': (3, 'Q'),  # Buy 3 R, get one Q free
        'U': (4, 120),  # Buy 3 U, get one U free (effectively 4 for 120)
        'V': [(3, 130), (2, 90)]
    }
    
    
    # Count the occurrences of each SKU in the basket
    basket = {}
    for sku in skus:
        if sku not in prices:
            return -1
        if sku in basket:
            basket[sku] += 1
        else:
            basket[sku] = 1

    total = 0


    for sku, offer in offers.items():
        if isinstance(offer, tuple):
            offer_qty, free_sku = offer
            if sku in basket and free_sku in basket:
                free_sku_count = basket[sku]//offer_qty
                if basket[free_sku] > free_sku_count:
                    basket[free_sku] -= free_sku_count
                else:
                    basket[free_sku] = 0

   # Apply special pricing offers
    for sku, offer in offers.items():
        if isinstance(offer, list):
            quantity = basket.get(sku, 0)
            for min_qty, offer_price in sorted(offer, reverse=True):
                if quantity >= min_qty:
                    offer_count = quantity // min_qty
                    total += offer_count * offer_price
                    quantity -= offer_count * min_qty
            total += quantity * prices[sku]
        elif isinstance(offer, tuple) and sku in basket:
            total += basket[sku] * prices[sku]

    # Add prices for items without special offers
    for sku, quantity in basket.items():
        if sku not in offers:
            total += quantity * prices[sku]
    print (total)
    return total

checkout('UUUU')