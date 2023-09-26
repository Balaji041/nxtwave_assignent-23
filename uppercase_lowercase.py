def get_lower_and_upper_case_letters(word):
    # Complete this function
    upper=""
    lower=""
    for i in word:
        if i.isupper():
            upper+=i
        else:
            lower+=i
    return upper+"\n"+lower


word = input()
# Call the get_lower_and_upper_case_letters function
print(get_lower_and_upper_case_letters(word))

"""
input:PreMium
output:
PM
reium
"""
