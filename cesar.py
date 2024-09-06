import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QSpinBox
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRectF, QPointF

class CaesarWheel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shift = 0
        self.setMinimumSize(300, 300)

    def setShift(self, shift):
        self.shift = shift
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center = QPointF(self.rect().center())
        radius = min(self.width(), self.height()) / 2 - 10

        # Dibujar círculo exterior
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.drawEllipse(center, radius, radius)

        # Dibujar círculo interior
        inner_radius = radius * 0.7
        painter.drawEllipse(center, inner_radius, inner_radius)

        # Dibujar letras
        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)

        for i in range(26):
            angle = 2 * math.pi * i / 26
            x_outer = center.x() + radius * math.cos(angle)
            y_outer = center.y() + radius * math.sin(angle)
            x_inner = center.x() + inner_radius * math.cos(angle)
            y_inner = center.y() + inner_radius * math.sin(angle)

            # Letra exterior
            painter.setPen(Qt.GlobalColor.black)
            painter.drawText(QRectF(x_outer-10, y_outer-10, 20, 20), Qt.AlignmentFlag.AlignCenter, chr(65 + i))

            # Letra interior (cifrada)
            painter.setPen(Qt.GlobalColor.red)
            shifted_char = chr(65 + (i + self.shift) % 26)
            painter.drawText(QRectF(x_inner-10, y_inner-10, 20, 20), Qt.AlignmentFlag.AlignCenter, shifted_char)

        # Dibujar línea de referencia
        painter.setPen(QPen(Qt.GlobalColor.blue, 2))
        painter.drawLine(QPointF(center.x(), center.y() - radius), QPointF(center.x(), center.y() - inner_radius))

class CifradoCesarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cifrado César con Rueda")
        self.setGeometry(100, 100, 600, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Rueda de César
        self.caesar_wheel = CaesarWheel()
        layout.addWidget(self.caesar_wheel)

        # Input
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Texto:"))
        self.input_text = QLineEdit()
        input_layout.addWidget(self.input_text)
        layout.addLayout(input_layout)

        # Shift
        shift_layout = QHBoxLayout()
        shift_layout.addWidget(QLabel("Desplazamiento:"))
        self.shift_spinbox = QSpinBox()
        self.shift_spinbox.setRange(0, 25)
        self.shift_spinbox.valueChanged.connect(self.update_wheel)
        shift_layout.addWidget(self.shift_spinbox)
        layout.addLayout(shift_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.encrypt_button = QPushButton("Cifrar")
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button = QPushButton("Descifrar")
        self.decrypt_button.clicked.connect(self.decrypt)
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        layout.addLayout(button_layout)

        # Output
        layout.addWidget(QLabel("Resultado:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

    def update_wheel(self, value):
        self.caesar_wheel.setShift(value)

    def caesar_cipher(self, text, shift, decrypt=False):
        result = ""
        if decrypt:
            shift = -shift
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
                result += chr(shifted)
            else:
                result += char
        return result

    def encrypt(self):
        text = self.input_text.text()
        shift = self.shift_spinbox.value()
        encrypted = self.caesar_cipher(text, shift)
        self.output_text.setText(encrypted)

    def decrypt(self):
        text = self.input_text.text()
        shift = self.shift_spinbox.value()
        decrypted = self.caesar_cipher(text, shift, decrypt=True)
        self.output_text.setText(decrypted)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CifradoCesarApp()
    window.show()
    sys.exit(app.exec())