# Четем списъка с дрехи от входа и го съхраняваме като списък от цели числа.
clothes = list(map(int, input().split()))
# Четем капацитета на стелажа от входа.
rack_capacity = int(input())

racks_used = 1  # Започваме с първия стелаж.
current_rack_load = 0

# Обхождаме всеки елемент (дреха) от списъка с дрехи.
for piece in clothes:
    if current_rack_load + piece <= rack_capacity:
        # Ако текущият стелаж може да побере дрехата, я добавяме към него.
        current_rack_load += piece
    else:
        # Ако текущият стелаж е препълнен, стартираме нов стелаж и добавяме дрехата там.
        racks_used += 1
        current_rack_load = piece

# Извеждаме броя на използваните стелажи.
print(racks_used)
