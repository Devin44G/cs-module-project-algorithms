'''
Input: an integer
Returns: an integer
'''


# def eating_cookies(n):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


def eating_cookies(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100
    cache = {i: 0 for i in range(num_cookies + 1)}
    print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")
