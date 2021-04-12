def binary_search(s_list, item):
    """Бинарный поиск по отсортированному списку"""
    low = 0
    high = len(s_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = s_list[mid]
        if guess == item:
            return mid
        elif int(guess) > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    # spisok = [3, 3, 45, 6, 67, 8, 4, 34, 23, 6, 6, 7, 8]
    with open('Юла телефоны.txt', 'r', encoding='utf-8') as file:
        target_list = file.readlines()
    h = list(set(target_list))
    h.sort()
    print('Позиция в списке {}'.format(binary_search(h, 79271201015)))
