import sys

sys.stdout.reconfigure(encoding='utf-8')

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print("João gastou mais que Pedro")
elif total_pedro > total_joao:
    print("João gastou mais que Pedro")
elif total_joao := total_pedro:
    print("Os dois gastaram o mesmo valor")
    