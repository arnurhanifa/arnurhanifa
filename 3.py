def handshake(n):
    totalHandshake = 0
    for i in range(n):
        for j in range(i):
            totalHandshake = totalHandshake + 1
    return totalHandshake

print(handshake(3))