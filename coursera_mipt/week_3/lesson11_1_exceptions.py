class ExceptionsRaiser:
    try:
        raw = input("enter the number: ")
        if not raw.isdigit():
            raise ValueError
    except ValueError:
        print("incorrect input")
