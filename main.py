# INF601 - Advanced Programming in Python

# Nathan Birkes

# Mini Project 2

import helpers as hf


def main() -> None:

    fake_data = hf.get_fake_data(30)

    hf.create_charts(fake_data)

if __name__ == "__main__":
    main()