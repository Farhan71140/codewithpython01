str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("✅ They are anagrams.")
else:
    print("❌ They are not anagrams.")