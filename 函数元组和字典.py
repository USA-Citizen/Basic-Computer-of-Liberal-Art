def breakfast(food, *talk, **factor):
    print(f'Would you like some {food} for breakfast, sir?')
    print(f'Sorry, what I dislike most is just the very {food}, madam.')
    for sentence in talk: # 元组不需要加*
        print(sentence)
    for i in range(40):
        print('-', end = '')
    for key in factor: # 字典不需要加**
        print(f'{key} : {factor[key]}')

breakfast('cheese',
'On, your flavour is so ridiculous.',
'It\'s ridiculous that no one has ever understood me.',
place='plane',
time='yesterday') # 字典的键不能是表达式