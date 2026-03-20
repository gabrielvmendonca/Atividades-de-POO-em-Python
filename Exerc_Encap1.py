class ControleTemperatura:
    def __init__(self,temperatura):
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if -50 <= valor <= 100:
            self.__temperatura = valor
        else:
            print(f"Valor {valor} inválido! A temperatura deve estar entre -50 e 100.")
            # Definimos um valor padrão ou mantemos o antigo em caso de erro
            self.__temperatura = 0

    def converter_para_fahrenheit(self):
        return (self.temperatura * 1.8) + 32
    
temp = ControleTemperatura(float(input("Digite um valor: ")))

print(f"Temperatura atual: {temp.temperatura}°C")
print(f"Em Fahrenheit: {temp.converter_para_fahrenheit()}°F")