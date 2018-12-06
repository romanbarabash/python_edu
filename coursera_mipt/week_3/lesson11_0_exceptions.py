class ExceptionHandler:
    while True:
        try:
            raw = input("enter the number: ")
            number = int(raw)
        except ValueError:
            print("Incorrect input")
        except KeyboardInterrupt:
            print("exit")
            break
        finally:
            print("# program was executed")
