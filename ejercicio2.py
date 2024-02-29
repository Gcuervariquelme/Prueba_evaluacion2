class Dialogo:
    def __init__(self, texto_original):
        self.texto_original = texto_original

    def dividir_en_frases(self):
        return self.texto_original.split("#")

    def formatear_frases(self, frases):
        frases_formateadas = [frase.capitalize() + "." for frase in frases]
        frases_formateadas[0] = frases_formateadas[0].replace(".", "...")
        return frases_formateadas

    def unir_frases(self, frases_formateadas):
        return "\n\n".join(frases_formateadas)

def main():
    texto_original = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

    dialogo = Dialogo(texto_original)
    frases = dialogo.dividir_en_frases()
    frases_formateadas = dialogo.formatear_frases(frases)
    dialogo_formateado = dialogo.unir_frases(frases_formateadas)

    print(dialogo_formateado)

if __name__ == "__main__":
    main()
