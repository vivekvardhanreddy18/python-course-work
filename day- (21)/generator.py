def reels():
    data = ['reel1', 'reel2', 'reel3', 'reel4', 'reel5']
    for i in data:
        yield i

res = reels()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))