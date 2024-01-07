import sys
import requests
from ui import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        all_oil_req = requests.get("http://api.herolights.net:8080/all_oil")
        all_oil_json = all_oil_req.json()

        # print(all_oil_json)
        # set number of rows to number of items in data
        self.ui.oil_output_table.setRowCount(len(all_oil_json["data"]))

        self.add_oil_to_table(all_oil_json)

        self.show()

    def add_oil_to_table(self, all_oil_json):
        row = 0
        for oil in all_oil_json["data"]:
            self.ui.oil_output_table.setItem(row, 0, QTableWidgetItem(str(oil["Year"])))
            self.ui.oil_output_table.setItem(
                row,
                1,
                QTableWidgetItem(oil["Make"] if oil["Make"] != None else "None"),
            )
            self.ui.oil_output_table.setItem(
                row,
                2,
                QTableWidgetItem(oil["Model"] if oil["Model"] != None else "None"),
            )
            self.ui.oil_output_table.setItem(
                row,
                3,
                QTableWidgetItem(oil["Series"] if oil["Series"] != None else "None"),
            )
            self.ui.oil_output_table.setItem(
                row, 4, QTableWidgetItem(str(oil["EngineSizeLiters"]))
            )
            self.ui.oil_output_table.setItem(row, 5, QTableWidgetItem(oil["Oil"]))
            self.ui.oil_output_table.setItem(
                row, 6, QTableWidgetItem(str(oil["Quarts"]))
            )
            self.ui.oil_output_table.setItem(
                row, 7, QTableWidgetItem(str(oil["NAPA_Filter"]))
            )

            row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
