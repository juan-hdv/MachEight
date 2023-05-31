"""
Finds pairs of integers from a list that sum to a given value. The function 
will take as input the list of numbers as well as the target sum.​Sample output 
is shown below. The algorithm must be faster than O(n^2)
Assume that:
 - All input values are integers.
 - There aren't any repeat values in the list.​

> app 1,9,5,0,20,-4,12,16,7 12
+ 12,0
+ 5,7
+ 16,-4
"""


def match_pairs_sum_to_value(numbers: int, value: int):
    result = []
    differences = dict()
    for n in numbers:
        num = differences.get(n)
        if num is not None:
            result.append((num, n))
        differences[value - n] = n
        # print(f"{n}, diff={num} differenbces={differences}")
    return result


def format_pairs(result: list):
    return "\n".join([f"+ {t[0]},{t[1]}" for t in result]) + "\n"


def run_test_swite():
    assert match_pairs_sum_to_value([], 1) == []
    assert match_pairs_sum_to_value([1], 1) == []
    assert match_pairs_sum_to_value([1, 9, 5, 0, 20, -4, 12, 16, 7], 12) == [(0, 12), (-4, 16), (5, 7)]
    assert match_pairs_sum_to_value([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 20) == [(8, 12), (6, 14), (4, 16), (2, 18), (0, 20)]
    assert match_pairs_sum_to_value([1, 2, 3, 4, 5], 6) == [(2, 4), (1, 5)]
    assert match_pairs_sum_to_value([10, 20, 30, 40], 60) == [(20, 40)]
    assert match_pairs_sum_to_value([5, 10, 15, 20, 25], 30) == [(10, 20), (5, 25)]
    assert match_pairs_sum_to_value([2, 4, 6, 8, 10], 16) == [(6, 10)]
    assert match_pairs_sum_to_value([1, 2, 3, 4, 5], 10) == []
    assert match_pairs_sum_to_value([1, 2, 3, 4, 5], 10) == []
    assert match_pairs_sum_to_value([-1, -2, -3, -4, -5], -9) == [(-4, -5)]
    assert match_pairs_sum_to_value([1, 3, 5, 7, 9], 4) == [(1, 3)]


if __name__ == "__main__":
    option = input("1. Manualy input a new data example\n2. Run test swite\n> ")
    if option == "1":
        str_list = input("Comma separated list of numbers: ").split(",")
        numbers = [int(n) for n in str_list]
        value = int(input("Value to match with pair sum: "))
        result = match_pairs_sum_to_value(numbers, value)
        print(format_pairs(result))
    elif option == "2":
        run_test_swite()
        print("All test passed!\n")
    else:
        print("Good bye. Try again ...\n")
