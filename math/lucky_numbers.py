def lucky_numbers(n):
    survivor = 1
    delete_every = 2
    index = None
    sieve = list(range(1, n + 1))

    while len(sieve) >= delete_every:
        index = delete_every - 1
        while index < len(sieve):
            del sieve[index]
            index += (delete_every - 1)

        survivor_index = sieve.index(survivor) + 1
        survivor = sieve[survivor_index]
        delete_every = survivor

    return sieve

if __name__ == "__main__":
    number = input("Enter number: ")
    number = int(number)
    print("Lucky numbers:", *lucky_numbers(number))