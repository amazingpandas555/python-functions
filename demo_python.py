def calculate_average(numbers):
    """Return the arithmetic mean, or None if the list is empty."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))  # 20.0
