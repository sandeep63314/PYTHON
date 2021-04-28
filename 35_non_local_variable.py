# A variable local to a parent function can be used inside a inner function using keyword 'nonlocal'
lives = 3

print(f'Local variable of __main__ program is {lives}')

def death_game():
    global lives
    live = 5

    def over():
        nonlocal live
        live -= 1
        return live

    lives -= 1
    return over(),lives

a,b = death_game()
print(f'Value after use of nonlocal variable is {a}')
print(f'Value of global variable after use of death_game() is {b}')