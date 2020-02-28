def solution(N):
    results = ['Codility', 'Test', 'Coders']
    dividers = [2, 3, 5]

    for num in range(1, N + 1):
        current_print = ""
        for i, divider in enumerate(dividers):
            if num % divider:
                current_print += results[i]

        if not current_print:
            print(num)
        else:
            print(current_print)
