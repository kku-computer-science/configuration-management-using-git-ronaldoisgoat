#!/usr/bin/env python3

def quick_sort(items):
    """Return a new list sorted with quick sort."""
    if len(items) < 2:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    mid = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def read_ints():
    """Read space-separated integers from one line."""
    raw = input("Enter numbers (e.g. 1 7 8 12 23):\n> ").strip()
    if not raw:
        return []
    try:
        return [int(x) for x in raw.split()]
    except ValueError:
        print("Invalid input: please enter integers only.\n")
        return read_ints()


def main():
    while True:
        choice = input(
            "Select sort type:\n"
            "1. Quick Sort\n"
            "2. Bubble Sort (not implemented)\n"
            "3. End Program\n"
            "> "
        ).strip()

        if choice == "1":
            numbers = read_ints()
            sorted_numbers = quick_sort(numbers)
            print(f"Result: {sorted_numbers}\n")
        elif choice == "2":
            print("Bubble Sort is not implemented yet.\n")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
