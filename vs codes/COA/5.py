def restoring_division(dividend, divisor):

    if divisor == 0:
        print("Error: Divisor cannot be zero")
        return

    if dividend < 0 or divisor < 0:
        print("Error: Enter unsigned integers only")
        return

    n = max(dividend.bit_length(), divisor.bit_length())

    A = 0
    Q = dividend
    M = divisor

    print(f"\nInitial: A={A:0{n}b}, Q={Q:0{n}b}, M={M:0{n}b}")

    for i in range(n):

        # Left shift A and Q together
        A = (A << 1) | ((Q >> (n - 1)) & 1)
        Q = (Q << 1) & ((1 << n) - 1)

        print(f"\nStep {i + 1}:")
        print(f"Shift Left AQ: A={A:0{n}b}, Q={Q:0{n}b}")

        # Subtract M
        A = A - M

        if A < 0:
            A = A + M
            print(f"A < M -> Restore A={A:0{n}b}, Q={Q:0{n}b}")
        else:
            Q = Q | 1
            print(f"A >= M -> A={A:0{n}b}, Q={Q:0{n}b}")

    print(f"\nResult: Quotient = {Q}, Remainder = {A}")


dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

restoring_division(dividend, divisor)