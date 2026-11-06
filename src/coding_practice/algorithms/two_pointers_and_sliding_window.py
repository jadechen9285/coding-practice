


def sol(nums): 
    """Problem 2.3.1 — Remove Duplicates from Sorted Array
    # 1. ROLES:  fast keeping check on the each right side new element, slow can be replace by the curnent num state
    # 2. KEEP:   if cur_num != nums[fast]: count += 1 and cur_num get updated to the fast num
    # 3. PROVE:  since the list is sorted in ascending, so the slow(cur num) once is checked can be discard and not be worry again.
    """
    slow = 0

    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            nums[slow+1] = nums[fast]
            slow += 1

    return slow + 1

def sol2(nums): 
    """Remove Duplicates from Sorted Array II
    # 1. ROLES:  fast keeping check on the each right side new element, slow keeps the first appear of the number
    # 2. KEEP:   if cur_num != nums[fast] and count < 2: nums[slow + 2] = nums[fast], slow += 1, count = 0 reset else: count += 1
    # 3. PROVE:  since the list is sorted in ascending, slow will keep track of the first appear number, fast check the duplication, 
    # once pass, slow index can be discard and move forward.
    """

    slow = 0
    for fast in range(len(nums)):
        if slow < 2 or nums[fast] != nums[slow-2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow 


def is_happy(n): 
    """Problem 2.3.3 — Happy Number
    """
    slow = n
    fast = n
    # each turn: slow follows 1 arrow, fast follows 2
    # stop when they're on the same card
    # return whether that card is 1

    def next_num(n):
        # return the sum of squares of n's digits
        # 19 → 82, 82 → 68, 2 → 4
        digit = [int(c) for c in str(n)]
        return sum([d**2 for d in digit])

    ## or 
    # def next_num(n):
    #     total = 0
    #     while n > 0:
    #         d = n % 10        # last digit
    #         total += d * d
    #         n //= 10          # drop last digit
    #     return total

    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))

        if slow == fast:
            break 

    return slow == 1
