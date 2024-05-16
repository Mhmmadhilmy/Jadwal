import csv
from datetime import datetime, timedelta

def create_schedule(employees, start_date, days):
    schedule = []
    current_date = start_date
    day_of_week = current_date.weekday()

    for i in range(days):
        for employee in employees:
            schedule.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'day': current_date.strftime('%A'),
                'employee': employee,
                'shift': 'Morning' if day_of_week < 5 else 'Weekend Shift'
            })
        current_date += timedelta(days=1)
        day_of_week = (day_of_week + 1) % 7

    return schedule

def save_schedule_to_csv(schedule, filename):
    keys = schedule[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(schedule)

if __name__ == '__main__':
    employees = ['Alice', 'Bob', 'Charlie', 'David']
    start_date = datetime.strptime('2023-05-01', '%Y-%m-%d')
    days = 14  # Generate schedule for 2 weeks

    schedule = create_schedule(employees, start_date, days)
    save_schedule_to_csv(schedule, 'employee_schedule.csv')

    print('Schedule generated and saved to employee_schedule.csv')
