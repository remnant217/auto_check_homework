import csv

with open('spo_python_sem1_task1.csv', 'w') as csv_file:
    fieldnames = ['input', 'output']
    data = [
        {'input': '2\n2', 'output': '4'},
        {'input': '3\n9', 'output': '12'},
        {'input': '-3\n-9', 'output': '-12'}
    ]

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)