def is_power_of_six(n):
    # Base case: 1 is a power of 6 (6^0)
    if n == 1:
        return True
    
    # Check if n is divisible by 6
    if n % 6 != 0:
        return False
    
    # Check if the last digit of n is 6 or 1
    # (6^n always ends with 6 or 1)
    last_digit = n % 10
    if last_digit != 6 and last_digit != 1:
        return False
    
    # Recursive case: check if n/6 is a power of 6
    return is_power_of_six(n // 6)