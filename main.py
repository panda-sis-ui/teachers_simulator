import sys
import os
import json
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QMessageBox

# Импорты UI классов
from menu import Ui_menu_window                 # главное меню
from rules import Ui_rules_window               # правила
from uchitelhouse import Ui_uchitelhouse_window # учительская
from problems import Ui_problems_window         # список ситуаций
from pages_max import Ui_pages_window           # страница ситуации
from result import Ui_result_window             # результаты

# Главное меню
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_menu_window()
        self.ui.setupUi(self)
        # Подключение сигналов
        self.ui.new_game.clicked.connect(self.new_game)
        self.ui.rules.clicked.connect(self.rules_show)
        self.ui.exit_game.clicked.connect(self.exit)

    def new_game(self):
        """Открытие окна Учительская"""
        self.hide()  # Скрываем главное меню
        teacher_home = TeacherHome()
        teacher_home.accepted.connect(self.show)  # Показываем главное меню при успешном закрытии
        teacher_home.rejected.connect(self.show)  # Показываем главное меню при отмене
        teacher_home.exec_()

    def rules_show(self):
        """Открытие окна правил."""
        rules_window = Rules()
        self.hide()  # Скрываем главное меню
        rules_window.accepted.connect(self.show)  # Показываем главное меню при успешном закрытии
        rules_window.rejected.connect(self.show)  # Показываем главное меню при отмене
        rules_window.exec_()

    def exit(self):
        """Выход из программы."""
        QApplication.quit()


# Правила
class Rules(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_rules_window()
        self.ui.setupUi(self)
        # Кнопка "выход"
        self.ui.go_menu.clicked.connect(self.exit)
        self.ui.label_2.setText("Правила и описание приложения")

    def exit(self):
        """Закрытие окна 'правил', открытие Главного меню."""
        self.close()


# Учительская
class TeacherHome(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_uchitelhouse_window()
        self.ui.setupUi(self)
        self.ui.tosituations.clicked.connect(self.go_situations)
        self.ui.tomainmenu.clicked.connect(self.go_menu)
        #self.ui.personalinfo.setText("Дорогу педагогу!")
        self.set_image()

    def set_image(self):
        """Устанавливает изображение на label."""
        image_path = "../images/foto.png"
        print(image_path)  # Для отладки: проверяем путь к изображению
        # Очищаем label перед установкой нового изображения
        self.ui.img_label.clear()
        if os.path.exists(image_path):  # Проверяем существование файла
            pixmap = QPixmap(image_path)  # Создаем объект QPixmap
            self.ui.img_label.setPixmap(pixmap)  # Устанавливаем изображение на label
            self.ui.img_label.setScaledContents(True)  # Масштабируем изображение под размер label
        else:
            print(f"Ошибка: файл изображения не найден по пути {image_path}")

    def go_situations(self):
        """Переход к выбору ситуаций."""
        self.accept()  # Скрываем текущее окно
        problems_window = Problems()
        problems_window.exec_()  # Открываем окно Problems модально

    def go_menu(self):
        self.accept()
        menu.show()


# Окно с выбором ситуации
class Problems(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_problems_window()
        self.ui.setupUi(self)
        self.current_situation = None  # Текущая выбранная ситуация
        # Подключение сигналов
        self.ui.back.clicked.connect(self.back_menu)
        self.add_situations_to_list()
        self.ui.list_Problems.itemClicked.connect(self.SitChoise)

    def add_situations_to_list(self):
        """Добавление элементов в список ситуаций."""
        self.ui.list_Problems.clear()
        directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Ситуации")
        if not os.path.exists(directory):
            QMessageBox.critical(self, "Ошибка", "Папка 'Ситуации' не найдена")
            return
        for file_name in os.listdir(directory):
            if file_name.endswith('.json'):
                self.ui.list_Problems.addItem(file_name.rsplit('.json', 1)[0])

    def SitChoise(self):
        """Обработка выбора ситуации."""
        selected_item = self.ui.list_Problems.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Ошибка", "Выберите ситуацию из списка")
            return
        file_name = f"{selected_item.text()}.json"
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Ситуации", file_name)
        # Проверка существования файла
        if not os.path.exists(file_path):
            QMessageBox.critical(self, "Ошибка", f"Файл {file_name} не найден")
            return
        try:
            # Чтение и парсинг JSON-файла
            with open(file_path, 'r', encoding='utf-8') as file:
                self.current_situation = json.load(file)  # Загрузка JSON-файла
            # Проверка структуры JSON (минимальная валидация)
            if not isinstance(self.current_situation, dict) or "Описание" not in self.current_situation:
                QMessageBox.critical(self, "Ошибка", f"Файл {file_name} содержит некорректную структуру данных")
                return
            # Открытие окна с ситуацией
            self.accept()
            page_problems = PageProblems(self.current_situation,selected_item.text())
            page_problems.exec_()
        except IOError as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось прочитать файл {file_name}: {e}")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Ошибка", f"Некорректный формат JSON в файле {file_name}: {e}")

    def back_menu(self):
        """Возврат в учительскую."""
        self.accept()


# Решаем ситуацию
class PageProblems(QDialog):
    MAX_RECURSION_DEPTH = 10  # Максимальная глубина рекурсии
    def __init__(self, file_situation, namedirimages, depth=0):
        super().__init__()
        self.ui = Ui_pages_window()
        self.ui.setupUi(self)
        self.namedirimages = namedirimages
        self.situation = file_situation
        self.depth = depth  # Текущая глубина рекурсии
        # Подключение сигналов
        self.ui.ToTeachersClass.clicked.connect(self.ToTeacherHome)
        self.display_variants()
        self.ui.text_situation.setText(self.situation.get("Результат", "Нет результата"))
        # Установка изображения
        self.set_image()

    def set_image(self):
        """Устанавливает изображение на label."""
        image_path = os.path.join(f'../images/{self.namedirimages}', self.situation.get("Картинка", ""))
        print(image_path)  # Для отладки: проверяем путь к изображению
        # Очищаем label перед установкой нового изображения
        self.ui.img_label.clear()
        if os.path.exists(image_path):  # Проверяем существование файла
            pixmap = QPixmap(image_path)  # Создаем объект QPixmap
            self.ui.img_label.setPixmap(pixmap)  # Устанавливаем изображение на label
            self.ui.img_label.setScaledContents(True)  # Масштабируем изображение под размер label
        else:
            print(f"Ошибка: файл изображения не найден по пути {image_path}")

    def handle_variant(self, selected_variant):
        if selected_variant.get("Варианты"):
            # Если есть подварианты, создаем новую ситуацию
            new_situation = {
                "Описание": self.situation.get("Описание", ""),
                "Результат": selected_variant.get("Результат", ""),
                "Варианты": selected_variant.get("Варианты", []),
                "Картинка": selected_variant.get("Картинка", "")
            }
            self.close()
            page_problems = PageProblems(new_situation, self.namedirimages, depth=self.depth + 1)
            page_problems.exec_()
        else:
            # Если вариантов больше нет, открываем окно с результатом
            self.open_result(selected_variant)

    def display_variants(self):
        """Отображение вариантов ответов."""
        variants = self.situation.get("Варианты", [])
        buttons = [self.ui.var1, self.ui.var2, self.ui.var3, self.ui.var4, self.ui.var5, self.ui.var6]
        # Скрываем все кнопки
        for btn in buttons:
            btn.hide()
        # Отображаем доступные варианты
        for i, variant in enumerate(variants[:6]):  # Максимум 6 кнопок
            if i < len(buttons):
                buttons[i].setText(variant.get("Описание", "Нет описания"))
                buttons[i].show()
                # Подключаем сигналы
                try:
                    buttons[i].clicked.disconnect()
                except TypeError:
                    pass  # Если сигнал не был подключен
                buttons[i].clicked.connect(lambda checked, v=variant: self.handle_variant(v))
            else:
                buttons[i].deleteLater()

    def open_result(self, result_text):
        print("Переданный результат:", result_text)  # Отладочный вывод
        self.close()  # Скрываем текущее окно
        result_window = Result(result_text,self.namedirimages)
        result_window.accepted.connect(lambda: menu.show())  # Подключаем сигнал
        result_window.exec_()

    def ToTeacherHome(self):
        """Возврат в учительскую."""
        """Закрытие окна Result и открытие главного меню."""
        self.close()  # Закрываем текущее окно
        menu.show()    # Отображаем главное меню


# Результат
class Result(QDialog):
    def __init__(self, variant, namedirimages):
        super().__init__()
        self.ui = Ui_result_window()
        self.ui.setupUi(self)
        self.variant = variant
        self.namedirimages = namedirimages
        # Подключение сигналов
        self.ui.ToTeachersClass.clicked.connect(self.ToTeachersClass)  # Новый метод для перехода в главное меню
        # Отображение результата
        self.display_result()
        self.set_image()
        
        

    def set_image(self):
        """Устанавливает изображение на label."""
        image_path = os.path.join(f'../images/{self.namedirimages}', self.variant.get("Картинка", ""))
        print(image_path)  # Для отладки: проверяем путь к изображению
        # Очищаем label перед установкой нового изображения
        self.ui.img_label.clear()
        if os.path.exists(image_path):  # Проверяем существование файла
            pixmap = QPixmap(image_path)  # Создаем объект QPixmap
            self.ui.img_label.setPixmap(pixmap)  # Устанавливаем изображение на label
            self.ui.img_label.setScaledContents(True)  # Масштабируем изображение под размер label
        else:
            print(f"Ошибка: файл изображения не найден по пути {image_path}")

    def display_result(self):
        try:
            if hasattr(self.ui, 'text_result'):
                result_description = self.variant.get("Результат", "Нет описания")
                self.ui.text_result.setText(f"{result_description}")
            else:
                print("Ошибка: виджет result_text не найден")
        except Exception as e:
            print(f"Ошибка при отображении результата: {e}")
            QMessageBox.critical(self, "Ошибка", "Не удалось отобразить результат")

    def ToTeachersClass(self):
        """Закрытие окна Result и открытие главного меню."""
        self.accept()  # Закрываем текущее окно
        menu.show()    # Отображаем главное меню

def main():
    app = QApplication(sys.argv)
    exit_code = 0
    try:
        # Создание и отображение главного меню
        global menu
        menu = Menu()
        menu.show()
        # Запуск главного цикла приложения
        exit_code = app.exec_()
    except Exception as e:
        # Обработка ошибок
        QMessageBox.critical(None, "Ошибка", f"Произошла ошибка: {e}")
        exit_code = 1
    finally:
        sys.exit(exit_code)


if __name__ == '__main__':
    main()