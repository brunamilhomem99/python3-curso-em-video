# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocados.
# O programa deve mostrar:
# A) Apenas os 5 primeiros colocados;
# B) Os últimos 4 colocados da tabela;
# C) Uma lista com os times em ordem alfabética;
# D) Em que posição na tabela está o Botafogo. (adaptado para a colocação de 2023)

colocados = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Internacional', 'Fluminense', 'Corinthians', 'Athletico-PR',
             'Atlético', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino',
             'Coritiba', 'Cuiabá', 'Grêmio', 'Vasco', 'Bahia')

print('Cinco primeiros colocados: ')
for c in range(0, 5):
    print(colocados[c])

print('\n4 últimos colocados: ')
for c in colocados[16:]:
    print(c)

print('\nTimes em ordem alfabética: ')
for c in sorted(colocados):
    print(c)

position_botafogo = colocados.index('Botafogo')
print(f'\nPosição do time Botafogo: {position_botafogo}º')


