# 19. Count vowels in a given string.

s = "education"
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print(count)