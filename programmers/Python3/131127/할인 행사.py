def solution(want, number, discount):
    cart = dict(zip(want, number))
    for i in range(10):
        if discount[i] in want: cart[discount[i]] -= 1
    
    answer = 0
    for key, value in cart.items():
        if value>0: break
    else: answer += 1
    for i in range(len(discount)-10):
        if discount[i] in want: cart[discount[i]] += 1
        if discount[i+10] in want: cart[discount[i+10]] -= 1
        
        for key, value in cart.items():
            if value>0: break
        else: answer += 1
    return answer