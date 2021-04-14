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


def find_smallest(arr):
    """Функция поискаа наименьшего элемента массива"""
    smalllest = arr[0]
    smalllest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smalllest:
            smalllest = arr[i]
            smalllest_index = i
    return smalllest_index

def selection_sort(arr):
    """Функция сортировки выбором"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    spisok = [3, 3, 45, 6, 67, 8, 4, 34, 23, 6, 6, 7, 8]
    # with open('Юла телефоны.txt', 'r', encoding='utf-8') as file:
    #     target_list = file.readlines()
    # h = list(set(target_list))
    # h.sort()
    # print('Позиция в списке {}'.format(binary_search(h, 79271201015)))
    print(selection_sort(spisok))