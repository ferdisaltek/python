def solution(numbers):
    sorted_list = sorted(numbers)
    list_len = len(sorted_list)
    for i in range(list_len - 2):
        if sorted_list[i] > sorted_list[i + 2] - sorted_list[i + 1]:
            return 1
    
    return 0

solution([10, 2, 5, 1, 8, 20])