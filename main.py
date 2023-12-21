import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QLabel
from PyQt6.QtCore import Qt
import csv

class ElementInfoDialog(QDialog):
    def __init__(self, element_info):
        super().__init__()

        self.setWindowTitle('Информация об элементе')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout(self)

        label = QLabel(element_info)
        layout.addWidget(label)

        self.setLayout(layout)

class Table(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Таблица Менделеева')
        self.setGeometry(100, 100, 800, 400)

        # Создаем объект QTableWidget с 8 строками и 18 колонками (как в таблице Менделеева)
        self.table_widget = QTableWidget(self)
        self.table_widget.setRowCount(12)
        self.table_widget.setColumnCount(14)

      
        periods = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
        self.table_widget.setHorizontalHeaderLabels(periods)
        self.table_widget.setVerticalHeaderLabels(
            ["1", "2", "3", "4.1", "4.2", "5.1", "5.2", "6.1", "6.2", "7", "Лантаноиды", "Актиноиды"])

       
        with open('periodic_table.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 5:
                    symbol = row[0]
                    full_name = row[1]
                    group = row[2]
                    period = row[3]
                    mass = row[4]

                    item = QTableWidgetItem(symbol)
                    item.setData(Qt.ItemDataRole.ToolTipRole, f"Полное название: {full_name}, Масса: {mass}")
                    self.table_widget.setItem(int(period) - 1, int(group) - 1, item)

        
        layout = QVBoxLayout(self)
        layout.addWidget(self.table_widget)

        self.setLayout(layout)

        
        self.table_widget.itemClicked.connect(self.showElementDetails)

    def showElementDetails(self, item):
        element_info = item.data(Qt.ItemDataRole.ToolTipRole)
        dialog = ElementInfoDialog(element_info)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    window.show()
    sys.exit(app.exec())
