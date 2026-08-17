def build_lcs_table(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create DP table with extra row and column
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                # Characters differ
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    return dp


def reconstruct_lcs(seq1, seq2, dp):
    i = len(seq1)
    j = len(seq2)

    lcs_result = []

    # Walk backwards through the table
    while i > 0 and j > 0:

        if seq1[i - 1] == seq2[j - 1]:
            lcs_result.append(seq1[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    # Reverse because we reconstructed backwards
    lcs_result.reverse()

    return lcs_result


def lcs(seq1, seq2):
    dp = build_lcs_table(seq1, seq2)

    result = reconstruct_lcs(seq1, seq2, dp)

    return result, dp[len(seq1)][len(seq2)]


def print_dp_table(seq1, seq2, dp):
    print("\nDP Table:")

    print("    ", end="")
    for char in seq2:
        print(char, end=" ")
    print()

    for i in range(len(dp)):
        if i == 0:
            print("  ", end="")
        else:
            print(seq1[i - 1], end=" ")

        for value in dp[i]:
            print(value, end=" ")

        print()


# Main program
seq1 = "ABCBDAB"
seq2 = "BDCABA"

result, length = lcs(seq1, seq2)

print("Sequence 1:", seq1)
print("Sequence 2:", seq2)

print_dp_table(seq1, seq2, build_lcs_table(seq1, seq2))

print("\nLongest Common Subsequence:", "".join(result))
print("Length:", length)