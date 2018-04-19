def largest(bot, top):
    z = []
    for x in range(bot, top):
        for y in range(bot, top):
            if str(x*y) == str(x*y)[::-1]:
                z.append(x*y)
    return z

z = largest(100,999)
print(max(z))
