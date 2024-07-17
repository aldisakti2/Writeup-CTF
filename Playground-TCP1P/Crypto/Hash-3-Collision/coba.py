def find_characters(target_sum):
    # Dynamic programming table to store strings summing to each possible value up to target_sum
    dp = [""] * (target_sum + 1)
    
    # ASCII printable characters range from 32 to 126
    for i in range(32, 127):
        char = chr(i)
        for j in range(target_sum, i - 1, -1):
            if j == i or (dp[j - i] != "" and len(dp[j]) == 0):
                dp[j] = dp[j - i] + char
                print(dp)
    
    return dp[target_sum] if dp[target_sum] != "" else None

target_sum = 16779507
result = find_characters(target_sum)

if result:
    print("Possible string:", result)
else:
    print("No possible string found")

