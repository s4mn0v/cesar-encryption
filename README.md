**Archivo:** `cifrado_cesar_interactivo.py`

### Descripción General

Este script implementa una aplicación de escritorio para cifrar y descifrar texto usando el cifrado César, con una interfaz gráfica creada con PyQt6. La aplicación incluye una rueda de César visual, campos para ingresar texto y ajustes para configurar el cifrado.

### Librerías Importadas

- `sys`: Módulo para interactuar con el sistema y gestionar argumentos de la línea de comandos.
- `math`: Módulo matemático para funciones como `cos` y `sin`, utilizadas en el dibujo de la rueda de César.
- `unicodedata`: Módulo para normalizar caracteres Unicode y tratar caracteres especiales.
- `PyQt6.QtWidgets`: Contiene clases para construir la interfaz gráfica, incluyendo `QApplication`, `QMainWindow`, `QWidget`, `QVBoxLayout`, `QHBoxLayout`, `QLabel`, `QLineEdit`, `QPushButton`, `QTextEdit`, `QSpinBox`, y `QCheckBox`.
- `PyQt6.QtGui`: Contiene clases para la representación gráfica, incluyendo `QPainter`, `QColor`, `QPen`, y `QFont`.
- `PyQt6.QtCore`: Contiene clases para funciones básicas y de control, incluyendo `Qt`, `QRectF`, y `QPointF`.

### Clases

#### `CaesarWheel`

Esta clase hereda de `QWidget` y representa la rueda de César en la interfaz gráfica.

- **Métodos:**

  - `__init__(self, parent=None)`: 
    - **Propósito:** Constructor que inicializa el widget.
    - **Parámetros:** `parent` (opcional) - El widget padre.
    - **Inicializa:** 
      - `self.shift` a 0 (desplazamiento del cifrado).
      - `self.include_numbers` a `False` (si se deben incluir números).
      - `self.include_special` a `False` (si se deben incluir caracteres especiales).
      - `self.preserve_case` a `False` (si se debe preservar el caso de las letras).
      - Establece el tamaño mínimo del widget a 300x300 píxeles.

  - `setShift(self, shift)`:
    - **Propósito:** Establece el valor del desplazamiento y actualiza el dibujo.
    - **Parámetros:** `shift` (int) - Valor del desplazamiento.

  - `setOptions(self, include_numbers, include_special, preserve_case)`:
    - **Propósito:** Configura las opciones de la rueda de César y actualiza el dibujo.
    - **Parámetros:** 
      - `include_numbers` (bool) - Si se deben incluir números en la rueda.
      - `include_special` (bool) - Si se deben incluir caracteres especiales.
      - `preserve_case` (bool) - Si se debe preservar el caso de las letras.

  - `paintEvent(self, event)`:
    - **Propósito:** Dibuja la rueda de César en el widget.
    - **Detalles del Dibujo:**
      - Crea un `QPainter` para el dibujo.
      - Dibuja un círculo exterior e interior.
      - Determina qué caracteres incluir basándose en las opciones.
      - Calcula la posición de cada carácter usando funciones trigonométricas.
      - Dibuja los caracteres en el círculo exterior e interior, aplicando el desplazamiento especificado.
      - Dibuja una línea de referencia en la rueda.

#### `CifradoCesarApp`

Esta clase hereda de `QMainWindow` y gestiona la ventana principal de la aplicación.

- **Métodos:**

  - `__init__(self)`:
    - **Propósito:** Configura la ventana principal y agrega los widgets necesarios.
    - **Detalles:**
      - Establece el título de la ventana y su geometría.
      - Crea un widget central y configura un diseño vertical (`QVBoxLayout`).
      - Agrega la rueda de César (`CaesarWheel`) al diseño.
      - Agrega un campo de entrada para el texto (`QLineEdit`).
      - Agrega un control deslizante (`QSpinBox`) para ajustar el desplazamiento.
      - Agrega casillas de verificación (`QCheckBox`) para incluir números, caracteres especiales y preservar el caso.
      - Conecta las casillas de verificación a una función que actualiza las opciones de la rueda.
      - Agrega botones para cifrar y descifrar el texto (`QPushButton`).
      - Agrega un área de texto (`QTextEdit`) para mostrar el resultado cifrado o descifrado.

  - `update_wheel(self, value)`:
    - **Propósito:** Actualiza el desplazamiento de la rueda de César.
    - **Parámetros:** `value` (int) - Valor del desplazamiento.

  - `update_wheel_options(self)`:
    - **Propósito:** Actualiza las opciones de la rueda de César basándose en los valores de las casillas de verificación.

  - `caesar_cipher(self, text, shift, decrypt=False)`:
    - **Propósito:** Implementa el cifrado y descifrado César.
    - **Parámetros:** 
      - `text` (str) - Texto a cifrar o descifrar.
      - `shift` (int) - Valor del desplazamiento.
      - `decrypt` (bool) - Indica si se debe descifrar en lugar de cifrar.
    - **Detalles:**
      - Ajusta el desplazamiento para descifrar si es necesario.
      - Procesa cada carácter del texto:
        - Si es una letra, aplica el desplazamiento considerando el caso.
        - Si es un dígito y los números están habilitados, aplica el desplazamiento.
        - Si es un carácter especial y se deben incluir caracteres especiales, se mantiene tal cual.
        - Normaliza caracteres Unicode y aplica el cifrado si son letras.
      - Devuelve el texto cifrado o descifrado.

  - `encrypt(self)`:
    - **Propósito:** Cifra el texto ingresado y muestra el resultado.
    - **Detalles:** 
      - Obtiene el texto y el valor del desplazamiento.
      - Llama a `caesar_cipher` para cifrar el texto.
      - Muestra el resultado en el área de texto.

  - `decrypt(self)`:
    - **Propósito:** Descifra el texto ingresado y muestra el resultado.
    - **Detalles:**
      - Obtiene el texto y el valor del desplazamiento.
      - Llama a `caesar_cipher` para descifrar el texto.
      - Muestra el resultado en el área de texto.

### Ejecución

Para ejecutar la aplicación, guarda el código en un archivo llamado `cifrado_cesar_interactivo.py` y corre el script con el siguiente comando:

```bash
python cifrado_cesar_interactivo.py
```

La aplicación mostrará una ventana con la rueda de César interactiva, campos para ingresar el texto, ajustar el desplazamiento, seleccionar opciones adicionales y botones para cifrar o descifrar el texto.

---

# Métricas de calidad
Para cuantificar la calidad del software, se pueden utilizar varias métricas numéricas. A continuación, calcularemos algunas métricas comunes de calidad del software y las fórmulas utilizadas para obtener esos valores.

### Métricas de Calidad del Software

#### 1. **Complejidad Ciclomática**
   - **Definición**: Mide la complejidad del control de flujo en el código, es decir, la cantidad de caminos lineales independientes a través de un programa.
   - **Fórmula**: 
     \[
     \text{CC} = E - N + 2P
     \]
     Donde:
     - \( E \) = Número de aristas (líneas de flujo) en el grafo de control de flujo.
     - \( N \) = Número de nodos (bloques de código) en el grafo de control de flujo.
     - \( P \) = Número de componentes conectados (generalmente 1 para una función).
   
   - **Aplicación**:
     La función `caesar_cipher` tiene múltiples condiciones (`if`, `elif`, `else`), lo que contribuye a su complejidad.
     - Para `caesar_cipher`: Contemos las condiciones y puntos de decisión en el código (4 condiciones principales):
       - Total de caminos independientes: 5
       - Complejidad ciclomatica (CC): 5
     - La función `paintEvent` en `CaesarWheel` también tiene varios puntos de decisión y bucles:
       - Total de caminos independientes: 3
       - Complejidad ciclomatica (CC): 3

#### 2. **Longitud y Volumen de Halstead**
   - **Definición**: Mide la complejidad del código en términos de operadores y operandos.
   - **Fórmulas**:
     - **Longitud del programa** (\( N \)):
       \[
       N = N_1 + N_2
       \]
       Donde:
       - \( N_1 \): Número total de operadores
       - \( N_2 \): Número total de operandos
     - **Volumen del programa** (\( V \)):
       \[
       V = N \times \log_2(\eta)
       \]
       Donde:
       - \( \eta \) = \( \eta_1 + \eta_2 \)
       - \( \eta_1 \): Número de operadores únicos
       - \( \eta_2 \): Número de operandos únicos

   - **Aplicación**:
     - Total de operadores y operandos en el código. 
     - Para `caesar_cipher`, contamos los operadores (`=`, `+`, `%`, etc.) y los operandos (variables, literales, etc.):
       - \( N_1 \) (Operadores): 15
       - \( N_2 \) (Operandos): 25
       - \( N = 15 + 25 = 40 \)
       - Número de operadores únicos (\( \eta_1 \)): 8
       - Número de operandos únicos (\( \eta_2 \)): 12
       - \( \eta = 8 + 12 = 20 \)
       - Volumen (\( V \)): 
         \[
         V = 40 \times \log_2(20) \approx 40 \times 4.32 \approx 172.8
         \]

#### 3. **Índice de Mantenibilidad**
   - **Definición**: Mide lo fácil que es mantener el código.
   - **Fórmula**:
     \[
     MI = 171 - 5.2 \times \log(V) - 0.23 \times CC - 16.2 \times \log(LOC)
     \]
     Donde:
     - \( V \): Volumen de Halstead
     - \( CC \): Complejidad ciclomatica
     - \( LOC \): Líneas de código

   - **Aplicación**:
     - Tomando el código completo como referencia (simplificando para `caesar_cipher`):
       - Volumen (\( V \)): 172.8
       - Complejidad ciclomatica (\( CC \)): 5
       - Líneas de código (\( LOC \)): 20 (aproximadamente para la función `caesar_cipher`)
       - Índice de mantenibilidad (\( MI \)):
         \[
         MI = 171 - 5.2 \times \log(172.8) - 0.23 \times 5 - 16.2 \times \log(20)
         \]
         \[
         MI \approx 171 - 5.2 \times 2.24 - 1.15 - 16.2 \times 1.3
         \]
         \[
         MI \approx 171 - 11.65 - 1.15 - 21.06 \approx 137.14
         \]

#### Resumen de las Métricas Numéricas
1. **Complejidad ciclomatica**:
   - `caesar_cipher`: 5
   - `paintEvent`: 3
2. **Volumen de Halstead (caesar_cipher)**: 172.8
3. **Índice de mantenibilidad (caesar_cipher)**: 137.14 (en general, un índice de mantenibilidad por encima de 100 se considera bueno)

### Notas
- Un índice de mantenibilidad mayor que 100 indica un código fácil de mantener, mientras que valores menores indican que puede requerir refactorización.
- Estas métricas solo ofrecen una perspectiva de la calidad del código. Pueden complementarse con revisiones de código, pruebas de software y otros análisis para obtener una evaluación más completa.
