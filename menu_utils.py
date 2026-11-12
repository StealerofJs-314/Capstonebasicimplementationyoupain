from input_utils import read_int


def choose_option(title, options, prompt="Enter a number: "):
    while True:
        print(f"\n{title}")
        for option in sorted(options):
            print(f"{option}. {options[option]}")
        choice = read_int(prompt)
        if choice in options:
            return choice
        print("Invalid option. Please choose one of the displayed options.")
