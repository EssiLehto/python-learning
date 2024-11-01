message = "Hello you beautiful person!"
print(message)

response = input("How are you doing? Please respond your feeling [great, fine, okay, not good]: ")

edited_response = response.lower()

print ("You said you are doing", edited_response)

if edited_response == "fine":
    print("I´m happy to hear that.")
elif edited_response == "not good":
    print("I´m sorry to hear that.")
elif edited_response == "okay":
    print("I´m neutral to hear that")
elif edited_response == "great":
    print("I´m delighted to hear that!")
else: 
    print("I don´t know how to respond to that.")