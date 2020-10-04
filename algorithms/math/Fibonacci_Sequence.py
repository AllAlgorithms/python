# Fibonacci Sequence

if __name__ == '__main__':
    f = [0, 1]
    index1=0
    index2=1
    fibonacci_len = 10 # Lenght of Fibonacci Sequence
    for n in range(fibonacci_len):
        val = f[index1+n]+f[index2+n]
        f.append(val)
    f.pop(0)
    print f
