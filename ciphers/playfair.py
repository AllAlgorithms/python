#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# @Author: Gleydson Rodrigues

# ./playfair.py [encrypt/decrypt] key message


alphabet = "abcdefghijlmnopqrstuvwxyz".upper()

def vetorize(text):
    listText = []
    for letter in text:
        listText.append(letter)
    return listText

def normalizeMessage(text):
    newText = []
    text = text.upper()
    text = text.replace(" ", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    pos = 0
    while pos < len(text) - 1:
        firstLetter = text[pos]
        secondLetter = text[pos + 1]
        if firstLetter == secondLetter:
            if firstLetter == "X":
                newText.append(firstLetter)
                newText.append("Z")
                pos += 1
            else:
                newText.append(firstLetter)
                newText.append("X")
                pos += 1
        else:
            newText.append(firstLetter)
            newText.append(secondLetter)
            pos += 2
    if pos < len(text):
        if text[-1] == "X":
            newText.append(text[pos])
            newText.append("Z")
        else:
            newText.append(text[pos])
            newText.append("X")
    return newText

def createMatrix():
    matrix = []
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append("")
    return matrix

def mountGrid(matrix, key, alphabet):
    alphabet = vetorize(alphabet)
    line, column, pos = 0, 0, 0
    for letter in key:
        line = pos / 5
        column = pos % 5
        if letter in alphabet:
            alphabet.remove(letter)
            matrix[line][column] = letter
            pos += 1     
    while len(alphabet) > 0:
        line = pos / 5
        column = pos % 5
        matrix[line][column] = alphabet.pop(0)
        pos += 1
    return matrix

def getIndex(letter, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return [i, j]

def encrypt(message, key):
    matrix = mountGrid(createMatrix(), key, alphabet)
    message = normalizeMessage(message)
    messageEncrypted = ""
    pos, line, column = 0, 0, 1
    while pos < len(message) - 1:
        firstLetter = message[pos]
        secondLetter = message[pos + 1]
        indexFirstLetter = getIndex(firstLetter, matrix)
        indexSecondLetter = getIndex(secondLetter, matrix)
        if indexFirstLetter[line] == indexSecondLetter[line]:
            messageEncrypted += matrix[indexFirstLetter[line]][(indexFirstLetter[column] + 1) % 5]
            messageEncrypted += matrix[indexSecondLetter[line]][(indexSecondLetter[column] + 1) % 5]
        elif indexFirstLetter[column] == indexSecondLetter[column]:
            messageEncrypted += matrix[(indexFirstLetter[line] + 1) % 5][indexFirstLetter[column]]
            messageEncrypted += matrix[(indexSecondLetter[line] + 1) % 5][indexSecondLetter[column]]
        else:
            messageEncrypted += matrix[indexFirstLetter[line]][indexSecondLetter[column]]
            messageEncrypted += matrix[indexSecondLetter[line]][indexFirstLetter[column]]
        pos += 2
    return messageEncrypted

def decrypt(messageEncrypted, key):
    matrix = mountGrid(createMatrix(), key, alphabet)
    messageDecrypted = ""
    pos, line, column = 0, 0, 1
    while pos < len(messageEncrypted):
        firstLetter = messageEncrypted[pos]
        secondLetter = messageEncrypted[pos + 1]
        indexFirstLetter = getIndex(firstLetter, matrix)
        indexSecondLetter = getIndex(secondLetter, matrix)
        if indexFirstLetter[line] == indexSecondLetter[line]:
            messageDecrypted += matrix[indexFirstLetter[line]][(indexFirstLetter[column] - 1) % 5]
            messageDecrypted += matrix[indexSecondLetter[line]][(indexSecondLetter[column] - 1) % 5]
        elif indexFirstLetter[column] == indexSecondLetter[column]:
            messageDecrypted += matrix[(indexFirstLetter[line] - 1) % 5][indexFirstLetter[column]]
            messageDecrypted += matrix[(indexSecondLetter[line] - 1) % 5][indexSecondLetter[column]]
        else:
            messageDecrypted += matrix[indexFirstLetter[line]][indexSecondLetter[column]]
            messageDecrypted += matrix[indexSecondLetter[line]][indexFirstLetter[column]]
        pos += 2
    return messageDecrypted

def help():
    print(
        "./playfair.py [encrypt/decrypt] key message"
    )

def main():
    params = sys.argv[1:]
    if len(params) == 0:
        help()
    elif params[0] == "encrypt":
        key = params[1].upper()
        message = params[2:]
        print(encrypt("".join(x for x in message).upper(), key))
    elif params[0] == "decrypt":
        key = params[1].upper()
        message = params[2:]
        print(decrypt("".join(x for x in message).upper(), key))
    else:
        help()

if __name__ == "__main__":
    main()