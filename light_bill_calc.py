rooms = []
temp_room = 'room_'
count = 1

def unit_calc(current_reading, previous_reading):
    used_unit = current_reading - previous_reading
    return used_unit

def bill_calc(unit, price):
    bill = unit * price
    return bill

total_bill = int(input('\nTotal Bill: '))
motor_current_reading = int(input('\nEnter motor current reading: '))
motor_previous_reading = int(input('Enter motor previous reading: '))
motor_unit = unit_calc(motor_current_reading, motor_previous_reading)
total_unit = motor_unit

while count <= 5:
    room_no = temp_room + str(count)
    print(f'\nEnter {room_no} details:')
    temp_details = {}
    temp_details['room_no'] = room_no
    current_reading = int(input('Current reading: '))
    temp_details['current_reading'] = current_reading
    previous_reading = int(input('Previous reading: '))
    temp_details['previous_reading'] = previous_reading
    temp_details['unit'] = unit_calc(current_reading, previous_reading)
    rooms.append(temp_details)
    del temp_details
    count += 1

for room in rooms:
    total_unit += room['unit']

price_per_unit = total_bill / total_unit
print(f'\nPrice per unit is: {price_per_unit}')

empty_room = int(input('\nHow many rooms are empty: '))
motor_bill_per_room = (price_per_unit * motor_unit)/(5-empty_room)
print(f"\nMotor used {motor_unit} unit's so per room Rs {motor_bill_per_room}")

for room in rooms:
    temp_unit = room['unit']
    temp_room_no = room['room_no']
    print(f"\n{temp_room_no} has used {temp_unit} unit's so light bill Rs {bill_calc(temp_unit, price_per_unit)} + motor bill Rs {motor_bill_per_room}; Total bill Rs {bill_calc(temp_unit, price_per_unit) + motor_bill_per_room}")