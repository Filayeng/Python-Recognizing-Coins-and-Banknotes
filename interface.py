import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from madeni_para_tanimlama import Madeni_Para_Tanimlayici
from banknot_tanimlama import Banknot_Tanimlayici


class ParaTanimlayici(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Money Recognition Application')
        self.setGeometry(100, 100, 600, 180)  # Increased window height to fit larger buttons

        # Layout for placing buttons and labels
        layout = QVBoxLayout()

        # Buttons for coin and banknote recognition
        self.madeni_para_buton = QPushButton('Coin Recognition', self)
        self.madeni_para_buton.clicked.connect(self.madeni_para_resmi_yukleme)
        self.madeni_para_buton.setStyleSheet("font-size: 20px; padding: 15px;")  # Enlarged button
        layout.addWidget(self.madeni_para_buton)

        self.banknot_buton = QPushButton('Banknote Recognition', self)
        self.banknot_buton.clicked.connect(self.banknot_resmi_yukleme)
        self.banknot_buton.setStyleSheet("font-size: 20px; padding: 15px;")  # Enlarged button
        layout.addWidget(self.banknot_buton)

        # Spacer to push the "Total" label to the center
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Label to display the total result or message, with red and larger font
        self.toplam_para = QLabel('Total : 0TL', self)
        self.toplam_para.setStyleSheet("font-size: 30px; color: red;")  # Larger and red text
        self.toplam_para.setAlignment(Qt.AlignCenter)  # Center the text horizontally
        layout.addWidget(self.toplam_para)

        # Label for displaying the image
        self.img_screen = QLabel(self)
        layout.addWidget(self.img_screen)

        # Set layout for the window
        self.setLayout(layout)

    def madeni_para_resmi_yukleme(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.bmp *.jpeg)')
        print(file_name)
        if file_name:
            self.process_image(file_name, 'coin')

    def banknot_resmi_yukleme(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', '', 'Images (*.png *.jpg *.bmp *.jpeg)')
        if file_name:
            self.process_image(file_name, 'banknote')

    def process_image(self, image_path, image_type):
        if image_type == 'coin':
            tanimlayici = Madeni_Para_Tanimlayici()
            tanimlayici.tanimalama_Fonksiyonu(image_path)
            self.toplam_para.setText("Toplam : " + str(tanimlayici.total) + " TL")

        elif image_type == 'banknote':
            tanimlayici = Banknot_Tanimlayici()
            tanimlayici.tanimalama_Fonksiyonu_B(image_path)
            self.toplam_para.setText("Toplam : " + str(tanimlayici.total) + " TL")

        image = tanimlayici.last_image
        if image is not None:
            # Convert image to RGB format for displaying in QLabel
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, _ = image_rgb.shape
            bytes_per_line = 3 * width
            q_image = QImage(image_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

            self.img_screen.setPixmap(QPixmap(q_image))

    def recognize_objects(self, image, image_type):
        if image_type == 'coin':
            # Simulate recognizing coins
            return 5  # Assume 5 coins found
        elif image_type == 'banknote':
            # Simulate recognizing banknotes
            return 2  # Assume 2 banknotes found
        return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParaTanimlayici()
    window.show()
    sys.exit(app.exec_())

