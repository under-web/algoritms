from collections import deque


def binary_search(s_list, item):
    """Бинарный поиск по отсортированному списку O(log n)"""
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
    """Функция поиска наименьшего элемента массива"""
    smalllest = arr[0]
    smalllest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smalllest:
            smalllest = arr[i]
            smalllest_index = i
    return smalllest_index


def selection_sort(arr):
    """Функция сортировки выбором O(n**2)"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def quick_sort(array):
    """Функция быстрой сортировки O(n log n)"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


def person_is_seller(name):
    return name[-1] == 'm'


def algo_graphs(name):
    """ Функция реализующая графы"""

    graph = {}
    search_queue = deque()
    search_queue += graph[name]
    searcher = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searcher:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searcher.append(person)
    return False


# алгоритм Декстры со взвешенными графами
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если это узел с наименьшей стоимостью из виденных и он еще не был обработан
            lowest_cost = cost  # ...он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # найти узел с наименьшей стоимостью среди необработанных
while node is not None:  # если обработаны все узлы, цикл while завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]  # если к соседу можно быстрее
        if costs[n] > new_cost:  # добраться через текущий узел...
            costs[n] = new_cost  # обновить стоимость для этого узла
            parents[n] = node  # этот узел становится новым родителем для соседа
    processed.append(node)  # узел помечается как обработанный
    node = find_lowest_cost_node(costs)  # найти следующий узел для обработки и повторить цикл

if __name__ == '__main__':
    spisok = [3, 3, 45, 6, 67, 8, 4, 34, 23, 6, 6, 7, 8]
    # with open('Юла телефоны.txt', 'r', encoding='utf-8') as file:
    #     target_list = file.readlines()
    # h = list(set(target_list))
    # h.sort()
    # print('Позиция в списке {}'.format(binary_search(h, 79271201015)))
    # print(quick_sort(spisok))
