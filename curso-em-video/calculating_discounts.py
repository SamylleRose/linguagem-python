employee_salary = float(input('Qual é o salário do funcionario? R$ '))
increase = (employee_salary * 0.15) + employee_salary
print(f'Um funcionário que ganhava R${employee_salary:.2f}, com 15% de aumento, passa a receber R${increase:.2f}')