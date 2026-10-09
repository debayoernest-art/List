
import random



def create_list():
    numbers = []

    for i in range(10):
        numbers.append(random.randint(1, 50))

    return numbers



def get_length(numbers):
    count = 0

    for number in numbers:
        count += 1

    return count



def sum_even_positions(numbers):
    total = 0

    for i in range(1, get_length(numbers), 2):
        total += numbers[i]

    return total



def sum_odd_positions(numbers):
    total = 0

    for i in range(0, get_length(numbers), 2):
        total += numbers[i]

    return total



def multiply_third_positions(numbers):
    product = 1

    for i in range(2, get_length(numbers), 3):
        product *= numbers[i]

    return product



def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / get_length(numbers)



def get_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest



def get_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest



def matching_strings(words):
    result = []

    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            result.append(word)

    return result



def sequential_list():
    numbers = []

    for number in range(1, 16):
        numbers.append(number)

    return numbers


def sum_every_third(numbers):
    total = 0

    for i in range(2, get_length(numbers), 3):
        total += numbers[i]

    return total



def sum_first_middle_last(numbers):
    count = get_length(numbers)

    if count == 0:
        return None

    first = numbers[0]
    last = numbers[-1]
    middle_index = count // 2

    if count % 2 == 1:
        middle = numbers[middle_index]
    else:
        middle = (numbers[middle_index - 1] + numbers[middle_index]) / 2

    return first + middle + last




my_numbers = create_list()

print("Random list:", my_numbers)
print("Length:", get_length(my_numbers))
print("Sum at even positions:", sum_even_positions(my_numbers))
print("Sum at odd positions:", sum_odd_positions(my_numbers))
print("Product at every third position:", multiply_third_positions(my_numbers))
print("Average:", calculate_average(my_numbers))
print("Largest element:", get_largest(my_numbers))
print("Smallest element:", get_smallest(my_numbers))
print("Sum of every third element:", sum_every_third(my_numbers))

print("\nSequential list:", sequential_list())

words = ["madam", "abc", "181", "dad", "xy", "bb"]
matches = matching_strings(words)

print("Matching strings:", matches)
print("Number of matching strings:", get_length(matches))

test_list = [10, 20, 30, 40, 50]
print("Sum of first, middle and last:", sum_first_middle_last(test_list))

test_list2 = [10, 20, 30, 40, 50, 60]
print("Sum with two middle elements:", sum_first_middle_last(test_list2))
