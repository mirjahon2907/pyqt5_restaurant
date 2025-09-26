from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QCheckBox, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Restaurant")

        self.v_main_lay = QVBoxLayout()
        self.h_lbl_lay = QHBoxLayout()

        self.h_btn1_lay = QVBoxLayout()
        self.h_btn2_lay = QVBoxLayout()
        self.h_btn3_lay = QVBoxLayout()
        self.h_btn4_lay = QVBoxLayout()
        self.buttons_lay = QHBoxLayout()

        self.lbl = QLabel("MENU")

        self.l1 = QLabel("1-meal")
        self.l2 = QLabel("2-meal")
        self.l3 = QLabel("Sweets")
        self.l4 = QLabel("Drinks")

        self.first_1 = QCheckBox("Sho'rva -> 35000")
        self.first_2 = QCheckBox("Mastava -> 32000")
        self.first_3 = QCheckBox("Chuchvara -> 25000")

        self.second_1 = QCheckBox("Palov -> 25000")
        self.second_2 = QCheckBox("Manti -> 30000")
        self.second_3 = QCheckBox("Lag'mon -> 28000")

        self.Sweets_1 = QCheckBox("Halva -> 15000")
        self.Sweets_2 = QCheckBox("Chak-chak -> 22000")
        self.Sweets_3 = QCheckBox("Napaleon -> 45000")

        self.Drinks_1 = QCheckBox("Coca-cola -> 10000")
        self.Drinks_2 = QCheckBox("Fanta -> 12000")
        self.Drinks_3 = QCheckBox("Sprite -> 8000")

        self.lst_of_checks = [self.l1,self.first_1, self.first_2, self.first_3,
                            self.l2,
                            self.second_1, self.second_2, self.second_3,
                            self.l3,
                            self.Sweets_1, self.Sweets_2, self.Sweets_3,
                            self.l4,
                            self.Drinks_1, self.Drinks_2, self.Drinks_3]

        self.h_lbl_lay.addStretch()
        self.h_lbl_lay.addWidget(self.lbl)
        self.h_lbl_lay.addStretch()
        self.v_main_lay.addLayout(self.h_lbl_lay)
    
        self.Total_lbl = QLabel("")
        self.v_main_lay.addWidget(self.Total_lbl)

        for i in self.lst_of_checks:
            self.v_main_lay.addWidget(i)

        self.btn_buy = QPushButton("Buy")
        self.btn_buy.clicked.connect(self.buy)
        self.btn_buy.hide()

        self.btn_next = QPushButton("Next")
        self.btn_next.clicked.connect(self.Next)

        self_btn_exit = QPushButton("Exit")
        self_btn_exit.clicked.connect(self.close)

        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.back)
        self.btn_back.hide()


        self.buttons_lay.addStretch()
        self.buttons_lay.addWidget(self_btn_exit)
        self.buttons_lay.addWidget(self.btn_next)
        self.buttons_lay.addWidget(self.btn_back)
        self.buttons_lay.addWidget(self.btn_buy)
        self.buttons_lay.addStretch()

        self.v_main_lay.addLayout(self.buttons_lay)


        self.setLayout(self.v_main_lay)

    def exit(self):
        self.close()

    def Next(self):
        bought_items = []
        self.sum = 0
        count = 0
        self.btn_buy.show()
        self.btn_back.show()
        self.btn_next.hide()
        self.lbl.setText("")
        
        for i in self.lst_of_checks:
            if isinstance(i, QCheckBox) and i.isChecked():
                count += 1
                price = int(i.text().split("->")[-1])
                self.sum += price
                bought_items.append(i.text())
            else:
                i.hide()
        if count < 4:
            for i in self.lst_of_checks:
                if isinstance(i, QCheckBox) and i.isChecked():
                    i.hide()
            self.lbl.setText("You have to choose at least 5 items to complete order!")
            self.btn_buy.hide()
            self.btn_back.show()
            self.btn_next.hide()
        else:
            self.Total_lbl.setText(f"Total Check: {self.sum} UZS")



    def buy(self):
        QMessageBox.information(self, "Success", f"Purchase successful! Total amount: {self.sum} UZS")
        self.sum = 0
        self.Total_lbl.setText("")
        self.lbl.setText("MENU")
        self.btn_buy.hide()
        self.btn_back.hide()
        self.btn_next.show()
        for i in self.lst_of_checks:
            if isinstance(i, QCheckBox) and i.isChecked():
                i.setChecked(False)
            i.show()

    def back(self):
        self.btn_buy.hide()
        self.btn_back.hide()
        self.btn_next.show()
        self.Total_lbl.hide()
        self.lbl.setText("MENU")
        for i in self.lst_of_checks:
            if isinstance(i,QCheckBox) and i.isChecked():
                i.setChecked(False)
            i.show()


app = QApplication([])
W = MyWindow()
W.show()
app.exec_()
