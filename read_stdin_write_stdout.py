# Read different types of data from standard input, process them as shown in output format and print the answer to standard output.

# Input format:
# First line contains integer N.
# Second line contains string S.

# Output format:
# First line should contain N x 2.
# Second line should contain the same string S.

# Constraints:
# 0 ≤ N ≤ 10
# 1 ≤ |S| ≤ 15 where |S| = length of string S

# Time Limit: 1.0 sec(s) for each input file.
# Memory Limit: 256 MB
# Source Limit: 1024 KB

number = int(raw_input())
string = raw_input()

print "%d\n" % (number*2)
print "%s\n" % string
