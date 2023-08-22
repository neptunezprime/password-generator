print ('welcome to tip calculator.')
bill = float(input('what was the total bill?\n'))
tip = int(input('what percentage of tip would you like to give? 10, 12, or 15?\n'))
people= int(input('how many people to split the bill?'))
tip_percentage = tip / 100
total_1 = tip_percentage * bill
total_2 = bill + total_1
bill_per_person = total_2 / people
total_3 = round(bill_per_person, 2)
total_3 = "{:.2f}".format(bill_per_person)
print(f"each person should pay ${total_3}")
