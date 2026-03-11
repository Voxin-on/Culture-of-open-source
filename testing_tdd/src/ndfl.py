def calculate_ndfl_tax(income):
    tiers=[(0.0,0.0,0.13),
           (2_400_000.0,312_000,0.15),
           (5_000_000.0,702_000.0,0.18)
           ]
    for start,additive,rate in tiers[::-1]:
        if income>start:
            return additive +(income-start)*rate
    return