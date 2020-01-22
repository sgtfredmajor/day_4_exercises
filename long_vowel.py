# The code will provide the user with the ability to 
# added capitallize vowels to cover words that that been capitalized 
vowels = "aeiouAEIOU"
# added a string to prompt the user to input data
user_input = input("Enter a word or words that contain double vowels: ")
new_text = ""

n = 0
#while n is less that the length of the user input
while n < len(user_input):
    if user_input[n] in vowels and (n+1) < len(user_input):
        if user_input[n] == user_input[n+1]:
            new_text = new_text + (user_input[n] * 5)
        else:
            new_text = new_text + user_input[n]
    else:
        new_text = new_text + user_input[n]
    n = n+1

print(new_text)