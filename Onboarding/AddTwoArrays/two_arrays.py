N = int(input())

# Get the array
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
for i in range(N):
    sumArray.append(numArray1[i] + numArray2[i])

# Print the sumArray
print (*sumArray)
