# def reels():
#     data = ['reel1', 'reel2', 'reel3', 'reel4', 'reel5']
#     for i in data:
#         yield i

# res = reels()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

# def countdown():
#     yield 5
#     yield 4
#     yield 3
#     yield 2
#     yield 1

# res = countdown()
# for i in res:
#     print(i)
    

def factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            yield i

res = factors(12)
for i in res:
    print(i)

print(next(res))  # This will raise StopIteration since the generator is exhausted
