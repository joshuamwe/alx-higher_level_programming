#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]

    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
        print(".")
    else:
        print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")


