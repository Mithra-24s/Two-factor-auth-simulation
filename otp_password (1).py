import random
from twilio.rest import Client

# Configuration
password = "secure123"
max_attempts = 5

# Twilio credentials (use environment variables in production)
account_sid = ""
auth_token = ""
twilio_number = "+"
user_phone_number = "+"

# Initialize variables
user_input = ""
attempts = 0

while user_input != password and attempts < max_attempts:
    try:
        user_input = input("Enter the password: ")
        attempts += 1

        if user_input == password:
            print("Generating OTP...")

            # Generate 6-digit OTP
            otp = str(random.randint(100000, 999999))

            try:
                # Send OTP using Twilio
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body=f"Your OTP is: {otp}",
                    from_=twilio_number,
                    to=user_phone_number
                )
                print("OTP sent. Please check your phone.")
            except Exception as e:
                print(f"Failed to send OTP: {e}")
                break

            try:
                # Prompt user to enter OTP
                entered_otp = input("Enter the OTP: ")
                if entered_otp == otp:
                    print("Logged in")
                else:
                    print("Incorrect OTP. Access denied.")
                break
            except Exception as e:
                print(f"Error while entering OTP: {e}")
                break

        elif attempts == max_attempts:
            print("Too many failed attempts. You are locked out.")
            break
        else:
            print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")

    except Exception as e:
        print(f"An error occurred: {e}")
        break
