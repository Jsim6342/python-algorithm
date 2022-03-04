def solution(max_weight, specs, names):
    answer = 0
    
    # specs = dict(specs)
    dict_specs = {product:int(weight) for product, weight in specs}
    
    now_weight = 0
    for name in names:
        if now_weight - dict_specs[name] < 0:
            answer += 1
            now_weight = max_weight
        now_weight -= dict_specs[name]
    
    return answer

if __name__ == "__main__":
    max_weight = 300
    specs = [["toy","70"], ["snack", "200"]]
    names = ["toy", "snack", "snack"]
    print(solution(max_weight, specs, names))