def binary(num, n):
    return format(num & ((1 << n) - 1), f"0{n}b")


def booths_multiplication(multiplicand, multiplier):
    n = max(
        abs(multiplicand).bit_length() + 1,
        abs(multiplier).bit_length() + 1,
        2
    )

    mask = (1 << n) - 1

    M = multiplicand
    Q = multiplier & mask
    A = 0
    Q_1 = 0

    print("\nInitial Values:")
    print("M =", binary(M, n))
    print("A =", binary(A, n))
    print("Q =", binary(Q, n))
    print("Q-1 =", Q_1)

    for i in range(n):
        print(f"\nStep {i + 1}")

        Q0 = Q & 1

        if Q0 == 0 and Q_1 == 1:
            A = A + M
            print("Operation: A = A + M")

        elif Q0 == 1 and Q_1 == 0:
            A = A - M
            print("Operation: A = A - M")

        else:
            print("Operation: No operation")

        A = A & mask

        print("Before shift:")
        print("A =", binary(A, n))
        print("Q =", binary(Q, n))
        print("Q-1 =", Q_1)

        # Arithmetic right shift of A, Q, Q-1
        new_Q_1 = Q & 1
        Q = ((A & 1) << (n - 1)) | (Q >> 1)

        # Preserve the sign bit of A
        sign_bit = A & (1 << (n - 1))
        A = (A >> 1) | sign_bit

        Q_1 = new_Q_1

        print("After shift:")
        print("A =", binary(A, n))
        print("Q =", binary(Q, n))
        print("Q-1 =", Q_1)

    result_bits = binary(A, n) + binary(Q, n)
    result = int(result_bits, 2)

    if result & (1 << (2 * n - 1)):
        result -= 1 << (2 * n)

    print("\nFinal Binary Product:", result_bits)
    print("Final Decimal Product:", result)


m = int(input("Enter multiplicand: "))
q = int(input("Enter multiplier: "))

booths_multiplication(m, q)