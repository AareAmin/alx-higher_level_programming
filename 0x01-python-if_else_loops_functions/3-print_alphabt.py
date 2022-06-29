#!/usr/bin/python3
for letter in range(ord('a'), ord('b') + 1):
    if letter != ord('e') and letter != ord('q'):
        print('{:c}'.format(letter), end='')
