games = {'monster hunter', 'tekken', 'genshin impact'}
characters = {'hunter', 'Jin', 'Aether'}

games.add('Star Rail')
print(games)

games.clear()
print(games)

games = {'monster hunter', 'tekken', 'genshin impact'}
x = games.copy()
print(x)

games = {'monster hunter', 'tekken', 'genshin impact'}
x = games.difference({'tekken', 'genshin impact'})
print(x)

games.difference_update({'tekken'})
print(games)

games = {'monster hunter', 'tekken', 'genshin impact'}
games.discard('tekken')
print(games)

games = {'monster hunter', 'tekken', 'genshin impact'}
common = games.intersection({'tekken', 'monster hunter'})
print(common)

games.intersection_update({'tekken', 'monster hunter'})
print(games)

print(games.isdisjoint(characters))

print({'tekken'}.issubset(games))

print(games.issuperset({'monster hunter'}))

games = {'monster hunter', 'tekken', 'genshin impact'}
games.pop()
print(games)

characters.remove('Jin')
print(characters)

games = {'monster hunter', 'tekken', 'genshin impact'}
diff = games.symmetric_difference({'tekken', 'genshin impact'})
print(diff)

games.symmetric_difference_update({'monster hunter', 'genshin impact'})
print(games)

combined = games.union(characters)
print(combined)

games.update(characters)
print(games)