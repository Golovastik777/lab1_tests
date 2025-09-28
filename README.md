# Калькулятор с GUI 

## Описание проекта

Этот проект представляет собой калькулятор с графическим интерфейсом пользователя (GUI), использованием библиотеки Tkinter. 



## Функциональность

- Основной калькулятор (CalculatorGUI)
- Калькулятор прямоугольника (RectangleCalculatorGUI)

## Установка и запуск

### Требования
- Python 3.6 или выше
- Tkinter (входит в стандартную поставку Python)

### Запуск приложения
```bash
py main.py
```

### Запуск тестов
```bash
# Запуск всех тестов
py test_calculator.py

# Запуск тестов с подробным выводом
py -m unittest test_calculator.py -v
```

## Тестирование

Проект включает в себя комплексные unit-тесты, покрывающие:

### Тестируемые компоненты:

1. **TestCalculatorLogic** - тестирование логики основного калькулятора
   - Базовые арифметические операции (+, -, *, /)
   - Сложные выражения
   - Работа с десятичными числами
   - Обработка ошибок
   - Функция очистки

2. **TestRectangleCalculator** - тестирование калькулятора прямоугольника
   - Расчет площади
   - Расчет периметра
   - Работа с десятичными значениями
   - Граничные случаи (нулевые значения)

3. **TestMathematicalFunctions** - тестирование математических функций
   - Изолированное тестирование математических операций
   - Функции расчета площади и периметра

### Количество тестов: 7
## Написанные тесты

### 1. TestCalculatorLogic (3 теста)
```python
def test_addition(self):
    """Тест сложения."""
    self.calculator.entry.delete(0, tk.END)
    self.calculator.entry.insert(0, "2+3")
    self.calculator.on_button_click("=")
    self.assertEqual(self.calculator.entry.get(), "5")
```

### 2. TestRectangleCalculator (2 теста)
```python
def test_calculate_area(self):
    """Тест расчета площади прямоугольника."""
    self.rectangle_calc.length_entry.insert(0, "5")
    self.rectangle_calc.width_entry.insert(0, "3")
    self.rectangle_calc.calculate_area()
    self.assertEqual(self.rectangle_calc.result_label.cget("text"), "Площадь: 15.0")
```

### 3. TestMathematicalFunctions (2 теста)
```python
def test_rectangle_area_calculation(self):
    """Тест расчета площади прямоугольника."""
    def calculate_rectangle_area(length, width):
        return length * width
    
    self.assertEqual(calculate_rectangle_area(5, 3), 15)
```

## Результаты запуска тестов

```
----------------------------------------------------------------------
Ran 7 tests in 2.123s

OK
```
### Покрытие тестами:
-  Математические операции (сложение, вычитание, умножение, деление)
-  Обработка ошибок (деление на ноль, недопустимые выражения)
-  Граничные случаи (нулевые значения, десятичные числа)
-  Функции GUI (ввод, очистка, отображение результатов)
-  Расчеты геометрических фигур (площадь, периметр)

### Принципы тестирования:
- **AAA (Arrange-Act-Assert)** - каждый тест следует структуре подготовки-действия-проверки
- **FIRST** - тесты быстрые, изолированные, повторяемые, самопроверяющиеся и своевременные
- **Изоляция** - каждый тест независим и не влияет на другие
- **Читаемость** - названия тестов отражают проверяемое поведение


### Команда для запуска тестов:
```bash
py -m unittest test_calculator -v
```

```
test_addition (test_calculator.TestCalculatorLogic.test_addition)
Тест сложения. ... ok
test_division_by_zero_error_handling (test_calculator.TestCalculatorLogic.test_division_by_zero_error_handling)
Тест обработки ошибки деления на ноль. ... ok
test_multiplication (test_calculator.TestCalculatorLogic.test_multiplication)
Тест умножения. ... ok
test_rectangle_area_calculation (test_calculator.TestMathematicalFunctions.test_rectangle_area_calculation)
Тест расчета площади прямоугольника. ... ok
test_rectangle_perimeter_calculation (test_calculator.TestMathematicalFunctions.test_rectangle_perimeter_calculation)     
Тест расчета периметра прямоугольника. ... ok
test_calculate_area (test_calculator.TestRectangleCalculator.test_calculate_area)
Тест расчета площади прямоугольника. ... ok
test_calculate_perimeter (test_calculator.TestRectangleCalculator.test_calculate_perimeter)
Тест расчета периметра прямоугольника. ... ok

----------------------------------------------------------------------
Ran 7 tests in 1.377s

OK
```
```txt
 py -m coverage report

Name      Stmts   Miss   Cover   Missing
----------------------------------------
main.py      98     20  79.59%   37-40, 88-91, 97-103, 106-107, 110-111, 114, 117-118
----------------------------------------
TOTAL        98     20  79.59%
```
## Автор
Яковлев И.С.
Лабораторная работа по unit-тестированию.
