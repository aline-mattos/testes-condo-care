import unittest
from datetime import datetime
from reserva import verificar_reserva

class TestVerificarReserva(unittest.TestCase):
    def test_data_no_passado(self):
        data_reserva = datetime(2023, 11, 1)
        resultado = verificar_reserva(data_reserva)
        self.assertEqual(resultado, "A reserva não pode ser feita no passado.")
        print("Resultado do Teste 1 - Particionamento por Equivalência:\n"
              "Testando: Data de reserva no passado \n"
              "Data atual: 07/11/2023\n"
              "Entrada: 01/11/2023\n"
              "Saída: A reserva não pode ser feita no passado.\n")

    def test_data_valida_no_futuro(self):
        data_reserva = datetime(2023, 12, 15)
        resultado = verificar_reserva(data_reserva)
        self.assertEqual(resultado, "Reserva feita com sucesso.")
        print("Resultado do Teste 2 - Particionamento por Equivalência:\n"
              "Testando: Data de reserva no futuro \n"
              "Data atual: 07/11/2023\n"
              "Entrada: 15/12/2023\n"
              "Saída: Reserva feita com sucesso.\n")


    def test_limite_intervalo_90_dias(self):
        data_reserva = datetime(2024, 2, 6)
        resultado = verificar_reserva(data_reserva)
        self.assertEqual(resultado, "Reserva feita com sucesso.")
        print("Resultado do Teste 1 - Análise de Valor Limítrofe:\n"
              "Testando: Data de reserva no limite do intervalo de 90 dias \n"
              "Data atual: 07/11/2023\n"
              "Entrada: 06/02/2024\n"
              "Saída: Reserva feita com sucesso.\n")

    def test_apos_limite_intervalo_90_dias(self):
        data_reserva = datetime(2024, 2, 8)
        resultado = verificar_reserva(data_reserva)
        self.assertEqual(resultado, "A reserva não pode ser feita com mais de 90 dias de antecedência.")
        print("Resultado do Teste 2 - Análise de Valor Limítrofe:\n"
              "Testando: Data de reserva no limite após 90 dias \n"
              "Data atual: 07/11/2023\n"
              "Entrada: 08/02/2024\n"
              "Saída: A reserva não pode ser feita com mais de 90 dias de antecedência.\n")

    def test_data_valida_no_presente(self):
        data_reserva = datetime(2023, 11, 8)
        resultado = verificar_reserva(data_reserva)
        self.assertEqual(resultado, "Reserva feita com sucesso.")
        print("Resultado do Teste 3 - Análise de Valor Limítrofe:\n"
              "Testando: Data um dia após o começo do intervalo de 90 dias \n"
              "Data atual: 07/11/2023\n"
              "Entrada: 08/11/2023\n"
              "Saída: Reserva feita com sucesso.\n")

if __name__ == '__main__':
    unittest.main()