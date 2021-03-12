# A variable local to a parent function can be used inside a inner function using keyword 'nonlocal'
lives = 3

print(f'Local variable of __main__ program is {lives}')

def death_game():
    global lives
    live = lives

    def over():
        nonlocal live
        live -= 1
        return live

    lives = over()
    return lives


print(f'Value after use of nonlocal variable is {death_game()}')
print(f'Value of local variable in __main__ program after use of nonlocal variable {lives}')
