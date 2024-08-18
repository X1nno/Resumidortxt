from os import system
system("cls")

import nltk
nltk.download('punkt')
nltk.download('stopwords')

import tkinter as tk
from tkinter import scrolledtext
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def resumir_texto():
    texto = input_text.get("1.0", tk.END)
    
    stop_words = set(stopwords.words("english"))
    palabras = word_tokenize(texto)
    
    frecuencia = {}
    for palabra in palabras:
        if palabra.lower() not in stop_words:
            if palabra.lower() in frecuencia:
                frecuencia[palabra.lower()] += 1
            else:
                frecuencia[palabra.lower()] = 1
                
    valor_oracion = {}
    oraciones = sent_tokenize(texto)
    
    for oracion in oraciones:
        for palabra in oracion.lower().split():
            if palabra in frecuencia:
                if len(oracion.split(' ')) < 30:
                    if oracion in valor_oracion:
                        valor_oracion[oracion] += frecuencia[palabra]
                    else:
                        valor_oracion[oracion] = frecuencia[palabra]
    
    resumen = []
    umbral = sum(valor_oracion.values()) / len(valor_oracion)
    
    for oracion in oraciones:
        if oracion in valor_oracion and valor_oracion[oracion] > (1.2 * umbral):
            resumen.append(oracion)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ' '.join(resumen))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resumidor de Texto")
ventana.geometry("800x600")

# Crear el cuadro de texto para la entrada
input_label = tk.Label(ventana, text="Texto para resumir:")
input_label.pack(pady=10)
input_text = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=10)
input_text.pack(pady=10)

# Botón para resumir el texto
resumir_button = tk.Button(ventana, text="Resumir", command=resumir_texto)
resumir_button.pack(pady=10)

# Crear el cuadro de texto para la salida (resumen)
output_label = tk.Label(ventana, text="Resumen:")
output_label.pack(pady=10)
output_text = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=10)
output_text.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
