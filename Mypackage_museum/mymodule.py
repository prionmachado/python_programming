def main():
    hello("name")
    goodbye("name")


def hello(name):
    name = name.capitalize()
    print(f"Hello, {name}")


def goodbye(name):
    name = name.capitalize()
    print(f"Goodbye, {name}")


if __name__ == "__main__":
    main() 
