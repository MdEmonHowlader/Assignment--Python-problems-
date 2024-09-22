input_string=input("Enter String: ")
vowel_count = 0
v="aeiouAEIOU"
for i in input_string:
    if i in v:
        vowel_count+=1
print("Total Vowel: ", vowel_count)