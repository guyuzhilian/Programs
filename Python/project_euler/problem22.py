# -*- coding:utf-8 -*-
#   author: Administrator
#   date: 2015-07-28 19:53

def main():
    name_list = [name.strip('"') for name in open("p022_names.txt").read().split(",")]
    name_list.sort()

    sum = 0
    for rank, name in enumerate(name_list):
        alphabetical_value = 0
        for char in name:
            alphabetical_value += ord(char) - ord('A') + 1

        print(rank, name, alphabetical_value)
        sum += (rank + 1) * alphabetical_value

    print(sum)

if __name__ == "__main__":
    main()