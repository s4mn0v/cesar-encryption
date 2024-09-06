# Cifrado César con Rueda

Este proyecto es una aplicación de escritorio para cifrado y descifrado de texto utilizando el cifrado César, implementado en Python con la biblioteca PyQt6. La aplicación presenta una interfaz gráfica que incluye una representación visual de la rueda de César, un campo de entrada para el texto, controles para ajustar el desplazamiento del cifrado, y botones para cifrar y descifrar el texto.

## Requisitos

- Python 3.x
- PyQt6

Puedes instalar PyQt6 con pip si aún no lo tienes:
```bash
pip install PyQt6
```

## Descripción del Código

### Clases

#### `CaesarWheel`

Una clase personalizada que hereda de `QWidget` y se encarga de dibujar la rueda de César en la interfaz gráfica.

- **Métodos Principales:**
  - `__init__(self, parent=None)`: Constructor de la clase. Inicializa el objeto y establece el tamaño mínimo del widget.
  - `setShift(self, shift)`: Establece el desplazamiento del cifrado y actualiza el widget.
  - `paintEvent(self, event)`: Dibuja la rueda de César con las letras y el desplazamiento especificado.

#### `CifradoCesarApp`

La clase principal que hereda de `QMainWindow` y crea la interfaz de usuario de la aplicación.

- **Métodos Principales:**
  - `__init__(self)`: Constructor de la clase. Configura la ventana principal y agrega los widgets necesarios.
  - `update_wheel(self, value)`: Actualiza el desplazamiento de la rueda de César.
  - `caesar_cipher(self, text, shift, decrypt=False)`: Implementa el cifrado y descifrado César.
  - `encrypt(self)`: Cifra el texto ingresado y muestra el resultado.
  - `decrypt(self)`: Descifra el texto ingresado y muestra el resultado.

## Uso

1. Ejecuta el script.
2. La aplicación mostrará una ventana con una rueda de César, un campo de entrada para texto, un control deslizante para el desplazamiento, y botones para cifrar y descifrar el texto.
3. Ingresa el texto en el campo correspondiente y ajusta el desplazamiento.
4. Haz clic en el botón "Cifrar" para cifrar el texto o en el botón "Descifrar" para descifrarlo. El resultado se mostrará en el área de texto inferior.

## Ejecución

Para ejecutar la aplicación, guarda el código en un archivo llamado, por ejemplo, `cifrado_cesar.py` y corre el script con Python:

```bash
python cifrado_cesar.py
```

¡Disfruta cifrando y descifrando mensajes con tu nueva aplicación de cifrado César!
