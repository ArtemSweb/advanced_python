text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for i in text:
    result[i] = result.get(i, 0) + 1

#print по условиям задачи не нужно
print(result)
