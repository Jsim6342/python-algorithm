from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return [x for x in result][0]

if __name__ == "__main__":
    participate = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participate, completion))