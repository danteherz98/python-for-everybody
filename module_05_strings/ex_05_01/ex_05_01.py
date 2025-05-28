total = 0 
count = 0
while True:
    user_input = input("Enter a number or done when finish: ")
    if user_input == "done":
        break
    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid number. Please enter an int or done.")

if count > 0:
    average = total / count
    print(f"Total: {total}, Count: {count}, Average: {average}")
else:
    print("No numbers were entered.")

          