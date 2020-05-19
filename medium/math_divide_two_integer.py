def divide(dividend, divisor):
    """
    二分查找

    正负数的判断中，这样判断更简单。

    const isNegative = dividend > 0 !== divisor > 0;

    """
    result, dvd, dvs = 0, abs(dividend), abs(divisor)
    while dvd >= dvs:
        print('tst')
        inc = dvs
        i = 0
        while dvd >= inc:
            dvd -= inc
            result += 1 << i
            inc <<= 1
            i += 1
    if (dividend > 0) == (divisor > 0):
        return result
    else:
        return -result

print(divide(-12, 3))