def linear_search(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def sort_numbers(numbers):
    return sorted(numbers)

def display_numbers(numbers):
    print("Sorted numbers--> ", numbers)

def main():
    num_inputs = int(input("How many numbers do you want to enter? "))

    
        