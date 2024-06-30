def checkout(skus):
    # Define prices and offers
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F':10}
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': (2, 'B'),  # Buy 2 E, get one B free
        'F': (2,'F')
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

    # Apply BOGOF offers first
    if 'E' in basket:
        e_count = basket['E']
        if 'B' in basket:
            free_b_count = e_count // 2
            if basket['B'] > free_b_count:
                basket['B'] -= free_b_count
            else:
                basket['B'] = 0

    # apply BTGOF
    if 'F' in basket:
        f_count = basket['F']
        f_count_by3 = f_count//3
        basket['B'] = basket['B']-f_count_by3

    # Apply special offers and calculate total
    for sku, count in basket.items():
        if sku in offers and sku != 'E':
            item_offers = offers[sku]
            item_offers.sort(reverse=True, key=lambda x: x[0])  # Apply largest offer first
            for qty, price in item_offers:
                if count >= qty:
                    offer_count = count // qty
                    total += offer_count * price
                    count %= qty
            total += count * prices[sku]
        else:
            total += count * prices[sku]
    print (total)
    return total

checkout('F')




