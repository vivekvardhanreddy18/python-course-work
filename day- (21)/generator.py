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
    

# def factors(num):
#     for i in range(1, num + 1):
#         if num % i == 0:
#             yield i

# res = factors(12)
# for i in res:
#     print(i)

# print(next(res))  # This will raise StopIteration since the generator is exhausted


# def primenobetween(num2):
#     for i in range(0, num2 + 1):
#         if i > 1:
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j == 0:
#                     break
#             else:
#                 yield i

# res = primenobetween(0, 50)
# for i in res:
#     print(i)    
