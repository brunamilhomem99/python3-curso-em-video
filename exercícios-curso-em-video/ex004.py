# getting input from user
value = input('Digite algo: ')

# analyzing the input
print('O tipo primitivo do seu input é:', type(value))
print('Só tem espaços?', value.isspace())
print('É alfanumérico?', value.isalnum())
print('É um número?', value.isnumeric())
print('É alfabético?', value.isalpha())
print('Está em maiúsculo?', value.isupper())
print('Está em minúsculo?', value.islower())
print('Está capitalizada?', value.istitle())
