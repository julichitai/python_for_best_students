""""""""""""""""""""
"""РАБОТА С JSON """
""""""""""""""""""""
import json


""" СЕРИАЛИЗАЦИЯ """
model = {
    'model': 'Classifier',
    'version': 1.8,
    'classes': ['cat', 'dog', 'pigeon'],
    'metrics': [100, 89, 90, 67, 99]
}

with open('model.json', 'w') as file:
    json.dump(model, fp=file)


""" ОТЛИЧИЯ DUMP ОТ DUMPS """
print(json.dumps(model))


""" ДЕСЕРИАЛИЗАЦИЯ """
with open('model.json', 'r') as file:
    model = json.load(file)

print(model)
print(sum(model['metrics']) / len(model['metrics']))


""" ОТЛИЧИЯ LOAD ОТ LOADS """
print(json.loads(
    '{"model": "Classifier", "version": 1.8, "classes": ["cat", "dog", "pigeon"], "metrics": [100, 89, 90, 67, 99]}'
))
