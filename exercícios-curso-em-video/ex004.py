# getting input from user
value = input('Digite algo: ')

# analyzing the input
print('O tipo primitivo do seu input é:', type(value))
print('\033[31mSó tem espaços?\033[m', value.isspace())
print('\033[32mÉ alfanumérico?\033[m', value.isalnum())
print('\033[33m]É um número?\033[m', value.isnumeric())
print('\033[34mÉ alfabético?\033[m', value.isalpha())
print('\033[35mEstá em maiúsculo?\033[m', value.isupper())
print('\033[36mEstá em minúsculo?\033[m', value.islower())
print('\033[30mEstá capitalizada?\033[m', value.istitle())
