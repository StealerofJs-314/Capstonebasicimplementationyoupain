from datetime import datetime
import os


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_positive_int(prompt):
    while True:
        value = read_int(prompt)
        if value > 0:
            return value
        print("Please enter a positive number.")


def read_text(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("Please enter a value.")


def read_future_datetime():
    while True:
        date_text = read_text("Event date (YYYY-MM-DD, e.g. 2026-12-26): ")
        time_text = read_text("Event time (HH:MM, 24-hour): ")
        try:
            event_datetime = datetime.strptime(
                f"{date_text} {time_text}", "%Y-%m-%d %H:%M"
            )
        except ValueError:
            print("Enter a valid date and time (YYYY-MM-DD and 24-hour HH:MM).")
            continue
        if event_datetime <= datetime.now():
            print("Please enter a future date and time.")
            continue
        return event_datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")
