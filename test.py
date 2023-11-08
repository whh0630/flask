import matplotlib.pyplot as plt
from collections import Counter
import random
import json


def test_check_ym():
    items = []
    with open("lotto.json", "r") as file:
        items = json.load(file)
        
    
    groups = []
    for item in items:
        arr = [item['drwtNo1'], item['drwtNo2'], item['drwtNo3'], item['drwtNo4'], item['drwtNo5'], item['drwtNo6']]
        groups.append(arr)
    # print(groups)

    all_numbers = [number for group in groups for number in group]
    number_counts = Counter(all_numbers)
    print(number_counts)

    for idx in range(1, 46):
        print(number_counts[idx])


#------------------------------------------------------------------------------------------------------------

def pyplot_test0():
    dice_numbers = [1, 2, 3, 4, 5, 6]
    probability = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    
    plt.bar(dice_numbers, probability, align='center', alpha=0.7)
    plt.xlabel('주사위 눈')
    plt.ylabel('확률')
    plt.title('주사위 확률 분포')
    plt.xticks(dice_numbers)
    plt.show()

def pyplot_test1():
    
    items = []
    with open("lotto.json", "r") as file:
        items = json.load(file)
    # print(items)

    groups = []
    for item in items:
        arr = [item['drwtNo1'], item['drwtNo2'], item['drwtNo3'], item['drwtNo4'], item['drwtNo5'], item['drwtNo6']]
        groups.append(arr)
    # print(groups)

    all_numbers = [number for group in groups for number in group]
    number_counts = Counter(all_numbers)
    print(number_counts)

    new_numbers = generate_lotto_numbers_based_on_data(number_counts)
    print(new_numbers)

    numbers, counts = zip(*number_counts.items())
    plt.bar(numbers, counts)
    plt.xlabel('로또 번호')
    plt.ylabel('빈도')
    plt.title('로또 번호 빈도 분석')
    plt.xticks(numbers)
    # plt.show()
    
def generate_lotto_numbers_based_on_data(number_counts):
    # check most number 
    most_common_numbers = [number for number, count in number_counts.most_common(6)]

    # select number
    remaining_numbers = [number for number in range(1, 46) if number not in most_common_numbers]
    random.shuffle(remaining_numbers)
    additional_numbers = remaining_numbers[:6]

    return most_common_numbers + additional_numbers


if __name__ == '__main__':
    # pyplot_test0()
    # pyplot_test1()
    test_check_ym()