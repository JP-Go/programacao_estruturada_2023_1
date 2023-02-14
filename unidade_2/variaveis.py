# Variaveis
print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Em 2025 você terá",2025 - nascimento,"anos")

# Desafio 1
print("#" * 20)
birth_year = int(input('Em que ano você nasceu?: '))
future_year = int(input('Para qual ano você quer saber sua idade?: '))
age = future_year - birth_year

print('Você terá', age, 'anos em', future_year)

# Desafio 2
print("#" * 20)
age = int(input('Quantos anos você tem?: '))
print('Se você fosse um cachorro, você teria', age * 7, 'anos')
print('''
      'O'______'
        ||   ||
      ''')
