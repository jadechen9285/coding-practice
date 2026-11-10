


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


def max_volwels(s, k):
    """Problem 2.4.1 — Maximum Number of Vowels in a Substring of Given Length

    # 1. WINDOW: what running value describes the current block? 
    # -> it contains the k consecutive letter of the string (k-substring), check the number of the vowels given this substring
    # 2. SLIDE:  how does that value change when one enters and one leaves? 
    # -> new letter enters, the leftest one needs to leave
    # 3. PROVE:  why does the update give the same result as recomputing? 
    # ->each time we minus the character it leaves (check if it is vowels) and plus the one it enters (check if it is vowels), 
    # using the sliding windows strategy, it go through all the combos
    """

    def count_vowels(s):
        return sum([c in vowels for c in s])

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = count_vowels(s[:k])
    best = count

    for i in range(k, len(s)):
        count = count + count_vowels(s[i]) - count_vowels(s[i-k])
        best = max(count, best)

        if best == k :
            return best

    return best 

def find_all_anagrams(s, p):
    """Problem 2.4.2 — Find All Anagrams in a String

    """
    k = len(p)
    if k > len(s):
        return []

    need = {}
    for c in p:
        need[c] = need.get(c, 0) + 1

    window = {}
    for c in s[:k]:                       # first window
        window[c] = window.get(c, 0) + 1

    res = []
    if window == need:
        res.append(0)

    for i in range(k, len(s)):
        enter = s[i]
        leave = s[i-k]

        window[enter] = window.get(enter, 0) + 1

        window[leave] -= 1
        if window[leave] == 0:
            del window[leave]

        if window == need:
            res.append(i-k+1)

    return res


def maximum_sum_of_unique_subarray(nums, k):
    """Problem 2.4.3 — Maximum Sum of Distinct Subarrays With Length K
    # 1. WINDOW: what running value describes the current block? 
    # -> it contains the k consecutive number for the list of nums, 
    # 2. SLIDE:  how does that value change when one enters and one leaves? 
    # -> new number enters, the leftest one needs to leave, each time check for uniqness 
    # 3. PROVE:  why does the update give the same result as recomputing? 
    # -> once we check the initated window, we just need to check the newest enter after getting rid of the one left, 
    # this way, we remove duplicate work and stay in O(n) of time, further we iterate all possibilities 
    """

    window = {}
    best = 0

    for num in nums[:k]:
        window[num] = window.get(num, 0) + 1

    window_sum = sum(nums[:k])

    if len(window) == k: # unique
        best = max(best, window_sum)

    for i in range(k, len(nums)):
        enter = nums[i]
        leave = nums[i-k]
        window_sum = window_sum - leave + enter
        window[enter] = window.get(enter, 0) + 1
        window[leave] = window.get(leave, 0) - 1

        if window[leave] == 0:
            del window[leave]

        if len(window) == k:
            best = max(best, window_sum)

    return best 