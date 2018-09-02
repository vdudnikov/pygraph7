# pygraph7

## Описание
Небольшая библиотека для хранения матриц в формате Graph7.

Формат Graph7 был разработан автором для хранения большого количества графов (то есть их матриц смежности) с минимальным объемом занимаемой памяти. В первую очередь была ориентация на уже давно известный формат Graph6. Однако у формата Graph6 есть некоторые недостатки:

  * можно хранить только один тип графов: простые графы (для хранения других типов используются другие форматы);
  * хранится избыточная информация о графах, а именно порядок графа;
  * нельзя хранить дополнительную информацию о ребрах (вес и т.п.);
  * для кодирования используются человеконечитаемые символы.

В связи с перечисленными недостатками было решено создать новый формат, который бы избавил от этих недостатков.

Эта библиотека является реализацией формата Graph7, а в ее основе лежит реализация на Си, доступная по адресу https://github.com/va-dudnikov/graph7.

Подробное описание формата будет добавлено позже.

## Установка

Установка через pip.

```bash
pip install pygraph7
```

Установка через github.

```bash
git clone https://github.com/va-dudnikov/pygraph7
cd pygraph7
git submodule init
git submodule update

python setup.py install
```

## Пример использования
```python
import graph7 as g7

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

encoded = g7.encode(mat) # Кодируем матрицу как int

print(encoded)
print(g7.decode(encoded) == mat)

encoded = g7.encode(mat, "float") # Кодируем матрицу как C-float

print(encoded)
print(g7.decode(encoded, "float") == mat)

encoded = g7.encode(mat, "double") # Кодируем матрицу как C-double

print(encoded)
print(g7.decode(encoded, "double") == mat)

# Вывод
# b'HAAQIDBAUGBwgJ'
# True
# b'HGAACAPwAAAEAAAEBAAACAQAAAoEAAAMBAAADgQAAAAEEAABBB'
# True
# b'HOAAAAAAAA8D8AAAAAAAAAQAAAAAAAAAhAAAAAAAAAEEAAAAAAAAAUQAAAAAAAABhAAAAAAAAAHEAAAAAAAAAgQAAAAAAAACJA'
# True
```

Больше примеров вы найдете в директории examples, которых будет достаточно для использования библиотеки.
