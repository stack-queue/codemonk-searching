num_testcases = int(input())

testcases = []

for i in range(num_testcases):
    testcases.append(input())

vowels = ['a', 'e', 'i', 'o', 'u']

for testcase in testcases:
    count = 0
    testcase_lower = testcase.lower()
    for vowel in vowels:
        count += testcase_lower.count(vowel)
    print(count)
