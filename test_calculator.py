"""
Unit-тесты для калькулятора.
Тестирует основные функции математических операций и расчетов.
"""

import unittest
import tkinter as tk
from main import CalculatorGUI, RectangleCalculatorGUI


class TestCalculatorLogic(unittest.TestCase):
    """Тесты для логики калькулятора."""
    
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.root = tk.Tk()
        self.calculator = CalculatorGUI(self.root)
        # Скрываем окно для тестирования
        self.root.withdraw()
    
    def tearDown(self):
        """Очистка после каждого теста."""
        self.root.destroy()
    
    def test_addition(self):
        """Тест сложения."""
        # Arrange
        self.calculator.entry.delete(0, tk.END)
        self.calculator.entry.insert(0, "2+3")
        
        # Act
        self.calculator.on_button_click("=")
        
        # Assert
        self.assertEqual(self.calculator.entry.get(), "5")
    
    def test_multiplication(self):
        """Тест умножения."""
        # Arrange
        self.calculator.entry.delete(0, tk.END)
        self.calculator.entry.insert(0, "3*4")
        
        # Act
        self.calculator.on_button_click("=")
        
        # Assert
        self.assertEqual(self.calculator.entry.get(), "12")
    
    def test_division_by_zero_error_handling(self):
        """Тест обработки ошибки деления на ноль."""
        # Arrange
        self.calculator.entry.delete(0, tk.END)
        self.calculator.entry.insert(0, "5/0")
        
        # Act
        self.calculator.on_button_click("=")
        
        # Assert
        self.assertEqual(self.calculator.entry.get(), "Ошибка")


class TestRectangleCalculator(unittest.TestCase):
    """Тесты для калькулятора прямоугольника."""
    
    def setUp(self):
        """Настройка перед каждым тестом."""
        self.root = tk.Tk()
        self.rectangle_calc = RectangleCalculatorGUI(self.root)
        # Скрываем окно для тестирования
        self.root.withdraw()
    
    def tearDown(self):
        """Очистка после каждого теста."""
        self.root.destroy()
    
    def test_calculate_area(self):
        """Тест расчета площади прямоугольника."""
        # Arrange
        self.rectangle_calc.length_entry.delete(0, tk.END)
        self.rectangle_calc.length_entry.insert(0, "5")
        self.rectangle_calc.width_entry.delete(0, tk.END)
        self.rectangle_calc.width_entry.insert(0, "3")
        
        # Act
        self.rectangle_calc.calculate_area()
        
        # Assert
        self.assertEqual(self.rectangle_calc.result_label.cget("text"), "Площадь: 15.0")
    
    def test_calculate_perimeter(self):
        """Тест расчета периметра прямоугольника."""
        # Arrange
        self.rectangle_calc.length_entry.delete(0, tk.END)
        self.rectangle_calc.length_entry.insert(0, "5")
        self.rectangle_calc.width_entry.delete(0, tk.END)
        self.rectangle_calc.width_entry.insert(0, "3")
        
        # Act
        self.rectangle_calc.calculate_perimeter()
        
        # Assert
        self.assertEqual(self.rectangle_calc.result_label.cget("text"), "Периметр: 16.0")


class TestMathematicalFunctions(unittest.TestCase):
    """Тесты для отдельных математических функций."""
    
    def test_rectangle_area_calculation(self):
        """Тест расчета площади прямоугольника."""
        # Arrange & Act & Assert
        def calculate_rectangle_area(length, width):
            return length * width
        
        self.assertEqual(calculate_rectangle_area(5, 3), 15)
        self.assertEqual(calculate_rectangle_area(2.5, 4.0), 10.0)
    
    def test_rectangle_perimeter_calculation(self):
        """Тест расчета периметра прямоугольника."""
        # Arrange & Act & Assert
        def calculate_rectangle_perimeter(length, width):
            return 2 * (length + width)
        
        self.assertEqual(calculate_rectangle_perimeter(5, 3), 16)
        self.assertEqual(calculate_rectangle_perimeter(2.5, 4.0), 13.0)


if __name__ == '__main__':
    # Создаем test suite
    suite = unittest.TestSuite()
    
    # Добавляем тесты
    suite.addTest(unittest.makeSuite(TestCalculatorLogic))
    suite.addTest(unittest.makeSuite(TestRectangleCalculator))
    suite.addTest(unittest.makeSuite(TestMathematicalFunctions))
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Выводим результаты
    print(f"\nРезультаты тестирования:")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешных: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Неудачных: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    if result.failures:
        print("\nНеудачные тесты:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")
    
    if result.errors:
        print("\nОшибки:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")
