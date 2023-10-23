# Четем имената на децата, разделени с интервали, и ги съхраняваме в списък.
children = input().split()
# Четем n-тото хвърляне.
n = int(input())

# Започваме с начален индекс 0.
index = 0

# Правим цикъл, докато има повече от едно дете в списъка.
while len(children) > 1:
    # Пресмятаме новия индекс, който трябва да се изключи от играта.
    index = (index + n - 1) % len(children)
    # Изваждаме имената на децата, които напускат играта, и ги отпечатваме.
    removed_child = children.pop(index)
    print(f"Removed {removed_child}")

# Накрая остава едно дете в списъка, което става победител.
winner = children[0]
print(f"Winner is {winner}")
