diffs = [
        14893,
        19951,
        22199,
        16579,
        17141,
        12083
        ]

z_stops = [[0], [0], [0], [0], [0], [0]]

rounds = 0
while True:
    if (rounds % 1000 == 0):
        print(z_stops)
        sets = [set(x) for x in z_stops]
        u = set.intersection(*sets)
        if len(u) > 1:
            print(u)
    for i in range(len(diffs)):
        diff = diffs[i]
        z_stops[i].append(z_stops[i][-1] + diff)  
        if rounds % 2 == 1:
            diffs[i] *= 2
        rounds += 1

        # 12927600769609



