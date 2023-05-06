import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import UI
from PyQt5.QtCore import QPoint, QCoreApplication, QTimer
import json
import os


class UI(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Это нужно для инициализации нашего дизайна
        self.setupUi(self)

        # убираем рамку windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.Button_exit.clicked.connect(QCoreApplication.instance().quit)
        self.Button_result.clicked.connect(self.Button_result_func)

        QTimer.singleShot(100, self.data_load)

    def Button_result_func(self):
        mass = int(self.lineEdit_mass.text())
        time_h = int(self.lineEdit_time_h.text())
        time_m = int(self.lineEdit_time_m.text())
        price_fl = float(self.lineEdit_price_fl.text())
        price_energy = float(self.lineEdit_price_energy.text())
        price_printer = float(self.lineEdit_price_printer.text())
        power = int(self.lineEdit_power.text())
        ratio = float(self.lineEdit_ratio.text())

        result = int(((mass / 1000 * price_fl) + (power / 1000 * price_energy * ((time_m / 60) +
                     time_h)) + (((time_m / 60 + time_h)) * (price_printer/365/8))) * 3 * ratio)
        self.label_result_output.setText(str(result)+' руб')

        data = {
            "price_fl": price_fl,
            "price_energy": price_energy,
            "price_printer": price_printer,
            "power": power,
            "ratio": ratio
        }
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)

    def data_load(self):
        if (os.path.isfile('data.json')) != True:
            data = {
                "price_fl": 1500,
                "price_energy": 4,
                "price_printer": 20000,
                "power": 300,
                "ratio": 1
            }
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=2)

        with open('data.json', 'r') as f:
            data_dict = json.load(f)

        self.lineEdit_price_fl.setText(str(data_dict.get('price_fl')))
        self.lineEdit_price_energy.setText(str(data_dict.get('price_energy')))
        self.lineEdit_price_printer.setText(
            str(data_dict.get('price_printer')))
        self.lineEdit_power.setText(str(data_dict.get('power')))
        self.lineEdit_ratio.setText(str(data_dict.get('ratio')))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def main():
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    window = UI()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
