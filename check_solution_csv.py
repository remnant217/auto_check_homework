import csv
import subprocess
import sys

def run_solution_csv(file_name: str):
    with open(file_name, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for num_test, row in enumerate(csv_reader, start=1):
            input = row['input']
            output = row['output']
            
            try:
                result = subprocess.run(
                    args=[sys.executable, 'solution.py'],
                    input=input,
                    text=True,
                    capture_output=True,
                    check=True
                ).stdout.strip()

                if result != output:
                    return f'Ошибка в тесте #{num_test}\nВвод:\n{input}\nОжидаемый вывод:\n{output}\nПолученный вывод:\n{result}'
                
            except subprocess.CalledProcessError as e:
                only_error= e.stderr[e.stderr.find('line'):]
                return f'При запуске программы возникла ошибка: {only_error}'

        return 'Все тесты пройдены!'

print(run_solution_csv(file_name='spo_python_sem1_task1.csv'))