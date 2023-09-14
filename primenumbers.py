from time import sleep
# Get user input for the range with error handling
while True:
  try:
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    break  # Exit the loop if both inputs are valid integers
  except ValueError:
    print("Invalid input. Please enter a valid integer.")

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      return False
  return True

prime_numbers = []
for num in range(lower_bound, upper_bound + 1):
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers in the range from", lower_bound, "to", upper_bound, "are:")
print(prime_numbers)
sleep(3)

menu = input("Press a to run program again.  Press q to quit:  ")

while True:
  if menu == 'q':
    print("Goodbye")
    sleep(3)
    break
  elif menu == 'a':
    # Allow the user to run the program again
    while True:
      try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        break  # Exit the loop if both inputs are valid integers
      except ValueError:
        print("Invalid input. Please enter a valid integer.")

    prime_numbers = []
    for num in range(lower_bound, upper_bound + 1):
      if is_prime(num):
        prime_numbers.append(num)

    print("Prime numbers in the range from", lower_bound, "to", upper_bound, "are:")
    print(prime_numbers)

    sleep(3)

    menu = input("Press 'a' to run the program again. Press 'q' to quit: ")
  else:
    print("Invalid input. Please enter 'a' or 'q'.")
