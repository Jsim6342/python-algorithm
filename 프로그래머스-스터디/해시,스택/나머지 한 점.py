def solution(v):
    answer = []

    x_dictionary = dict()
    y_dictionary = dict()
    
    for x, y in v:
        
        # x좌표 카운트
        if x not in x_dictionary:
            x_dictionary[x] = 1
        else:
            x_dictionary[x] += 1
            
        # y좌표 카운트
        if y not in y_dictionary:
            y_dictionary[y] = 1
        else:
            y_dictionary[y] += 1
        
    # x, y 좌표 원소 중 1개만 카운트 된 원소를 answer에 append
    for key, value in x_dictionary.items():
        if value == 1:
            answer.append(key)
    for key, value in y_dictionary.items():
        if value == 1:
            answer.append(key)

    return answer

if __name__ == "__main__":
    v = [[1,4],[3,4],[3,10]]
    print(solution(v))