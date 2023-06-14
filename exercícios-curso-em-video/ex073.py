# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocados.
# O programa deve mostrar:
# A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o Botafogo. (adaptado para a colocação de 2023)

cyan = '\033[36m'
purple = '\033[35m'
blue = '\033[34m'
yellow = '\033[33m'
green = '\033[32m'
reset = '\033[m'

colocados = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR',
             'Atlético', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino',
             'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia')

print(f'Lista de times do Brasileirão: {cyan}{colocados}{reset}')

print('Cinco primeiros colocados: ')
for c in range(0, 5):
    print(f'{purple}{colocados[c]}{reset}')

print('\n4 últimos colocados: ')
for c in colocados[16:]:
    print(f'{blue}{c}{reset}')

print('\nTimes em ordem alfabética: ')
for c in sorted(colocados):
    print(f'{yellow}{c}{reset}')

print(f'\nPosição do time Botafogo: {green}{colocados.index("Botafogo") +1}º{reset}')
