def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    # Initialize prices and offers dictionaries
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20,
        'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40,
        'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40,
        'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21
    }
    
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'E': (2, 'B'),  # Buy 2 E, get one B free
        'F': (3, 20),   # Buy 3 F, pay for 2
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'N': (3, 'M'),  # Buy 3 N, get one M free
        'P': [(5, 200)],
        'Q': [(3, 80)],
        'R': (3, 'Q'),  # Buy 3 R, get one Q free
        'U': [(4, 120)], # Buy 3 U, get one U free (effectively 4 for 120)
        'V': [(3, 130), (2, 90)],
        'S': (3, 45),   # Buy any 3 of (S, T, X, Y, Z) for 45
        'T': (3, 45),
        'X': (3, 45),
        'Y': (3, 45),
        'Z': (3, 45)
    }

    group_offer= {'S': 20, 'T': 20, 'X': 17, 'Y': 20, 'Z': 21}

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

    # Apply BOGOF and other free item offers
    for sku, offer in offers.items():
        if isinstance(offer, tuple):
            offer_qty, free_sku = offer
            if sku in basket and free_sku in basket:
                free_count = basket[sku] // offer_qty
                if basket[free_sku] >= free_count:
                    basket[free_sku] -= free_count
                else:
                    basket[free_sku] = 0

    # Apply group offers for S, T, X, Y, Z
    group_count = sum(basket.get(sku, 0) for sku in group_offer)
    if group_count >= 3:
        total_groups = group_count // 3
        total += total_groups * 45
        total_items_to_remove = total_groups * 3
        for sku in sorted(group_offer, key=group_offer.get, reverse=True):
            while total_items_to_remove > 0 and basket.get(sku, 0) > 0:
                remove_count = min(basket[sku], total_items_to_remove)
                basket[sku] -= remove_count
                total_items_to_remove -= remove_count

    # Apply special pricing offers
    for sku, quantity in basket.items():
        if sku in offers and isinstance(offers[sku], list):
            for deal in offers[sku]:
                min_qty, deal_price = deal
                if quantity >= min_qty:
                    offer_count = quantity // min_qty
                    total += offer_count * deal_price
                    quantity -= offer_count * min_qty
            total += quantity * prices[sku]
        else:
            total += quantity * prices[sku]

    return total

# Test the updated checkout function
print(checkout("STX"))  # Expected: 45
print(checkout("STXSTX"))  # Expected: 90
print(checkout("SSS"))  # Expected: 45
print(checkout("AABBBCCCC"))  # Example test, should apply 3A for 130 and 2B for 45, no offer for C
print(checkout("AAA"))  # Expected: 130
print(checkout("AAAAA"))  # Expected: 200
print(checkout("AABBE"))  # Expected: 175
print(checkout("EEEEBB"))  # Expected: 160 (2E free 2B)
print(checkout("FFFF"))  # Expected: 20 (3 for 20, 1 free)
print(checkout("UUU"))  # Expected: 120 (3U, 1 free U)
print(checkout("VVVVV"))  # Expected: 220 (3V for 130 and 2V for 90)
print(checkout("XYZXYZ"))  # Expected: 90 (buy any 3 of (S,T,X,Y,Z) for 45)

