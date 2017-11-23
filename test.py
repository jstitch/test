def suma(arg1, arg2):
    return arg1 + arg2

if __name__ == "__main__":
    import sys
    try:
        print(suma(sys.argv[1], sys.argv[2]))
    except:
        sys.exit(1)

    sys.exit(0)
