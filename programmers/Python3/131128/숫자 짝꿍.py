def solution(X, Y):
    x, y = sorted(str(X)), sorted(str(Y))
    i, j = 0, 0
    numbers = []
    while True:
        try:
            while x[i] > y[j]: j+=1
            while x[i] < y[j]: i+=1
            if x[i]==y[j]:
                numbers.append(x[i])
                i, j = i+1, j+1
        except:
            answer = ''.join(numbers[::-1])
            if not answer:
                return "-1"
            if answer[0]=="0": return "0"
            return answer
    