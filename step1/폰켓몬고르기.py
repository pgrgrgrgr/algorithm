def solution(nums):
    if len(nums) == len(set(nums)):
        answer = int(len(nums)/2)
    elif len(nums) > len(set(nums)):
        if len(set(nums)) < len(nums)/2:
            answer = len(set(nums))
        else:
            answer = int(len(nums)/2)
    return answer

solution([3,3,3,2,2,4])