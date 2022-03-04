def solution(s):
    stack = []
    for word in s:
        if stack:
            while stack and word > stack[-1]:
                stack.pop()
            stack.append(word)
        else:
            stack.append(word)
    
    return ''.join(stack)

if __name__ == "__main__":
    s = "xyb"
    print(solution(s))