def solution(numbers):
    sorted_list = sorted(numbers)
    list_len = len(sorted_list)
    for i in range(list_len - 2):
        print(sorted_list[i])
        print(sorted_list[i+2])
        print(sorted_list[i+1])
        print(i)
     

solution([10, 2, 5, 1, 8, 20])