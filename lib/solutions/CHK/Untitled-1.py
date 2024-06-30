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
for sku, offer in offers.items():
    if isinstance(offer, tuple):
        print(offer)