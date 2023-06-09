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

    while True:
        numbers = []
        for _ in range(num_inputs):
            num = int(input("Enter a number: "))
            numbers.append(num)

        sorted_numbers = sort_numbers(numbers)
        display_numbers(sorted_numbers)

        search_choice = input("Choose search method:\n1. Linear search\n2. Binary search\nEnter your choice: ")

        if search_choice == "1":
            while True:
                target = int(input("Enter a number to perform a linear search: "))
                if isinstance(target, int):
                    index = linear_search(numbers, target)
                    if index != -1:
                        print("(linear search) Number found at index: ", index)
                    else:
                        print("Number not found.")
                    break
                else:
                    break

        elif search_choice == "2":
            while True:
                target = int(input("Enter a number to perform a binary search: "))
                if isinstance(target, int):
                    index = binary_search(sorted_numbers, target)
                    if index != -1:
                        print("(binary search) Number found at index: ", index)
                    else:
                        print("Number not found.")
                    break
                else:
                    break

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break
        num_inputs = int(input("How many numbers do you want to enter? "))

        
if __name__ == "__main__":
    main()
