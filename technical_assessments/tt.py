#!/usr/bin/env python
import random

SIZE = 9

board = ['-' for _ in range(SIZE)]


def print_board():
    print('\n ' + '-' * 5)
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print(' ' + '-' * 5)
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print(' ' + '-' * 5)
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print(' ' + '-' * 5 + '\n')


def check_line(char, i, j, k):
    return char == board[i] == board[j] == board[k]


def check_lines(char):
    return any([check_line(char, 0, 1, 2),
                check_line(char, 3, 4, 5),
                check_line(char, 6, 7, 8),
                check_line(char, 0, 3, 6),
                check_line(char, 1, 4, 7),
                check_line(char, 2, 5, 8),
                check_line(char, 0, 4, 8),
                check_line(char, 6, 4, 2)])


def is_legal_move(idx):
    return not (board[idx] == 'x' or board[idx] == 'o')


def is_tie(moves):
    return moves == SIZE


def main():
    moves = 0
    while True:
        print_board()
        _input = input("Choise position: ")
        _input = int(_input)

        if is_legal_move(_input):
            board[_input] = 'x'
            moves += 1

        print_board()

        if check_lines('x'):
            print('Human win')
            break

        if is_tie(moves):
            print('Tie')
            break

        while True:
            random.seed()
            laptop = random.randint(0, 8)

            if is_legal_move(laptop):
                board[laptop] = 'o'
                moves += 1
                break

        print_board()

        if check_lines('o'):
            print('Computer win')
            break


if __name__ == '__main__':
    main()
