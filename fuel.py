def calc_fraction():
    while True:
        try:
            fraction = input("Fraction:").strip()
            a,b = fraction.split("/")
            a = int(a)
            b = int(b)
            if a>b:
                continue
            if b==0:
                continue

            fraction = (a/b) * 100

            if fraction<=1:
                print("E")
            elif fraction>=99:
                print("F")
            else:
                print(f"{round(fraction)}%")
            break

        except ValueError:
            continue
        except ZeroDivisionError:
            continue
calc_fraction()
