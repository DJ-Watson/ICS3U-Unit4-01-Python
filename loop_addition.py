#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program loops a number to add


def main():
    loopn = 0
    answer = 0

    # input
    intc = input("enter addition loop count: ")
    print("")

    # process and output
    try:
        numinput = int(intc)
        if numinput > 0:
            while loopn <= numinput:
                answer += loopn
                loopn += 1
            print(answer)
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
