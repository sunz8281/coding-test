def solution(people, limit):
    cnt = 0
    left, right = 0, len(people)-1
    people.sort()
    while left<right:
        if people[left] + people[right] > limit:
            cnt += 1
            right -= 1
        else:
            cnt += 1
            left += 1
            right -= 1
    if left == right: cnt += 1
    return cnt