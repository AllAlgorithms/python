def generate_lucky_number_sequence(end):
    
    #create a list of all odd numbers up to the final number
    sequence = [*range(1, end+1, 2)]

    #remove every xth number from the list where x = the nth element of the sequence
    n = 1
    while len(sequence) > sequence[n]:
        number_to_delete = sequence[n]
        del sequence[number_to_delete-1::number_to_delete]
        n = n + 1

    return sequence

print(generate_lucky_number_sequence(int(input("Please enter the upper bound of the lucky number sequence: "))))
