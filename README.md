
# Частотный анализ текста
Данный скрипт составит список самых часто встречающихся слов для любого текста, поданного на вход.

Скрипт принимает на вход путь до текстового файла и выводит в консоль десять самых популярных слов в этом файле в порядке убывания частоты.
Данный скрипт использует библиотеки:

 1. re (для новичков: https://tproger.ru/translations/regular-expression-python/)
  2. collections (документация: https://pythonworld.ru/moduli/modul-collections.html)
 3. sys (документация: https://pythonworld.ru/moduli/modul-sys.html)
Чтобы их импортировать необходимо написать следующее
```python
import re
import collections
import sys
```

# Быстрый старт
```bash
python 5_lang_frequency.py "your_text.txt"
```
# Пример вывода

```Самые популярные слова:
1) в встречается 277 раз(а)
2) и встречается 139 раз(а)
3) с встречается 125 раз(а)
4) ацп встречается 112 раз(а)
5) для встречается 107 раз(а)
6) на встречается 93 раз(а)
7) рисунок встречается 76 раз(а)
8) данных встречается 60 раз(а)
9) сигнала встречается 54 раз(а)
10) напряжение встречается 53 раз(а)
```

# Цели проекта

Данный код написан в ознакомительных целях в рамках обучения курса веб - разработчика  - [DEVMAN.org](https://devman.org)
