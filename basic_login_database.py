users = []
temp_user = 'user_'
user_count = 0
while True:
    new_user = input('Register new user? [y/n]: ').rstrip().lower()
    if new_user == 'y':
            user_id = temp_user + str(user_count)
            user_count += 1
            user_details = {}
            user_details['user_id'] = user_id
            first_name = input('Enter first name: ').title()
            user_details['first_name'] = first_name
            last_name = input('Enter last name: ').title()
            user_details['last_name'] = last_name
            dob = input('Enter DOB (dd/mm/yyyy): ')
            user_details['dob'] = dob
            users.append(user_details)
            del user_details
            print(f'Thank you for registration your user id is {user_id}')
    elif new_user == 'n':
          old_user_id = input('Enter your user ID: ')
          print('Fetching details...')
          if old_user_id == 'sudo':
               print(users)
               continue
          for user in users:
                if user['user_id'] == old_user_id:
                    print(f"Full Name: {user['first_name']} {user['last_name']}")
                    print(f"DOB: {user['dob']}")
                    feedback = input('Thank you for using our system wanna give feedback: ')
                    if feedback != '':
                        user['feedback'] = feedback
                        print('Thank you for your feedback')
                        continue
                else:
                     print('User not found wanna register?')
                     continue
    else:
         print('Try again flat earth brainer!')
         continue