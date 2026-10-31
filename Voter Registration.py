print("Voter Registration")

candidate_name = ["Alice", "Bob", "Charlie"]  # candidates a registered voter can choose from
voter_info = []  # stores a dictionary for each registered voter


def is_valid_voter_id(voter_id):
    # Valid if it is at least 5 characters long and only letters/numbers
    return voter_id.isalnum() and len(voter_id) >= 5


# Step 1: Check age and register the voter
registered = False
while not registered:
    age = input("Please enter your age: ")
    if not age.isdigit():
        print("Invalid input. Please enter a valid number for age.")
        continue

    age = int(age)
    if not 18 <= age <= 120:
        print("Sorry, you are not eligible to register to vote. You must be at least 18 years old.")
        break  # not eligible, so stop instead of looping forever

    print("You are eligible to register to vote!")
    voter_id = input("Please enter your voter ID (at least 5 letters/numbers): ")
    while not is_valid_voter_id(voter_id):
        print("Invalid voter ID. It must be at least 5 characters long and contain only letters and numbers.")
        voter_id = input("Please enter your voter ID (at least 5 letters/numbers): ")

    voter_info.append({"age": age, "voter_id": voter_id})
    print("Registration successful! Your information has been saved.")
    registered = True

# Step 2: Choose a candidate (only for registered voters)
if registered:
    candidate = input("Please enter the name of the candidate you want to vote for: ")
    while candidate not in candidate_name:
        print("Invalid candidate name. Please choose from: " + ", ".join(candidate_name))
        candidate = input("Please enter the name of the candidate you want to vote for: ")
    print(f"You have successfully registered to vote for {candidate}.")

# Step 3: Confirm exit
exit_confirmation = ""
while exit_confirmation not in ("yes", "no"):
    exit_confirmation = input("Are you sure you want to exit the voter registration system? (yes/no): ").strip().lower()
    if exit_confirmation not in ("yes", "no"):
        print("Invalid input. Please enter 'yes' or 'no'.")

if exit_confirmation == "yes":
    print("Thank you for using the voter registration system. Goodbye!")
else:
    print("Continuing with the voter registration system.")

print(voter_info)
