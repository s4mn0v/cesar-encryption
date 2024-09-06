import sys
import math
import unicodedata
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QSpinBox, QCheckBox
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRectF, QPointF

class CaesarWheel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shift = 0
        self.include_numbers = False
        self.include_special = False
        self.preserve_case = False
        self.setMinimumSize(300, 300)

    def setShift(self, shift):
        self.shift = shift
        self.update()

    def setOptions(self, include_numbers, include_special, preserve_case):
        self.include_numbers = include_numbers
        self.include_special = include_special
        self.preserve_case = preserve_case
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

        # Preparar fuentes
        font = QFont()
        font.setPointSize(10)
        painter.setFont(font)

        # Determinar qué caracteres incluir en la rueda
        chars = []
        if self.preserve_case:
            chars.extend([chr(i) for i in range(65, 91)])  # A-Z
            chars.extend([chr(i) for i in range(97, 123)])  # a-z
        else:
            chars.extend([chr(i) for i in range(65, 91)])  # A-Z
        
        if self.include_numbers:
            chars.extend([str(i) for i in range(10)])  # 0-9
        
        if self.include_special:
            chars.extend(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/'])

        total_chars = len(chars)

        for i, char in enumerate(chars):
            angle = 2 * math.pi * i / total_chars
            x_outer = center.x() + radius * math.cos(angle)
            y_outer = center.y() + radius * math.sin(angle)
            x_inner = center.x() + inner_radius * math.cos(angle)
            y_inner = center.y() + inner_radius * math.sin(angle)

            # Carácter exterior
            painter.setPen(Qt.GlobalColor.black)
            painter.drawText(QRectF(x_outer-10, y_outer-10, 20, 20), Qt.AlignmentFlag.AlignCenter, char)

            # Carácter interior (cifrado)
            painter.setPen(Qt.GlobalColor.red)
            if char.isalpha():
                if self.preserve_case:
                    ascii_offset = 65 if char.isupper() else 97
                    shifted_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
                else:
                    ascii_offset = 65
                    shifted_char = chr((ord(char.upper()) - ascii_offset + self.shift) % 26 + ascii_offset)
            elif char.isdigit() and self.include_numbers:
                shifted_char = str((int(char) + self.shift) % 10)
            else:
                shifted_char = char
            painter.drawText(QRectF(x_inner-10, y_inner-10, 20, 20), Qt.AlignmentFlag.AlignCenter, shifted_char)

        # Dibujar línea de referencia
        painter.setPen(QPen(Qt.GlobalColor.blue, 2))
        painter.drawLine(QPointF(center.x(), center.y() - radius), QPointF(center.x(), center.y() - inner_radius))

class CifradoCesarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cifrado César con Rueda Interactiva")
        self.setGeometry(100, 100, 600, 550)

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

        # Opciones de cifrado
        options_layout = QHBoxLayout()
        self.include_numbers = QCheckBox("Incluir números")
        self.include_special = QCheckBox("Incluir caracteres especiales")
        self.preserve_case = QCheckBox("Preservar mayúsculas/minúsculas")
        options_layout.addWidget(self.include_numbers)
        options_layout.addWidget(self.include_special)
        options_layout.addWidget(self.preserve_case)
        layout.addLayout(options_layout)

        # Conectar cambios de opciones a la actualización de la rueda
        self.include_numbers.stateChanged.connect(self.update_wheel_options)
        self.include_special.stateChanged.connect(self.update_wheel_options)
        self.preserve_case.stateChanged.connect(self.update_wheel_options)

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

    def update_wheel_options(self):
        self.caesar_wheel.setOptions(
            self.include_numbers.isChecked(),
            self.include_special.isChecked(),
            self.preserve_case.isChecked()
        )

    def caesar_cipher(self, text, shift, decrypt=False):
        result = ""
        if decrypt:
            shift = -shift

        for char in text:
            if char.isalpha():
                if self.preserve_case.isChecked():
                    ascii_offset = 65 if char.isupper() else 97
                    shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
                    result += chr(shifted)
                else:
                    ascii_offset = 65
                    shifted = (ord(char.upper()) - ascii_offset + shift) % 26 + ascii_offset
                    result += chr(shifted)
            elif char.isdigit() and self.include_numbers.isChecked():
                shifted = (int(char) + shift) % 10
                result += str(shifted)
            elif not char.isalnum() and self.include_special.isChecked():
                result += char
            elif unicodedata.category(char).startswith('L'):
                normalized = unicodedata.normalize('NFKD', char)
                base_char = normalized[0]
                if base_char.isalpha():
                    if self.preserve_case.isChecked():
                        ascii_offset = 65 if base_char.isupper() else 97
                        shifted = (ord(base_char) - ascii_offset + shift) % 26 + ascii_offset
                        result += chr(shifted)
                    else:
                        ascii_offset = 65
                        shifted = (ord(base_char.upper()) - ascii_offset + shift) % 26 + ascii_offset
                        result += chr(shifted)
                else:
                    result += char
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
