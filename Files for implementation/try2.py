a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
dic = {1: [10, 20], 2: 40, 3: 'foo'}

print([dic.get(n, n) for n in a])



