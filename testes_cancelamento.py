import unittest
from datetime import datetime
from cancelamento import verificar_cancelamento

class TestVerificarCancelamento(unittest.TestCase):
    def test_cancelamento_sem_multa(self):
        data_reserva = datetime(2023, 12, 15)
        tipo_salao = "quiosque"
        cancelamento_data = datetime(2023, 12, 13)
        resultado = verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data)
        self.assertEqual(resultado, "Reserva cancelada com sucesso. Nenhum ônus será aplicado.")
        print("Resultado do Teste 3 - Particionamento por Equivalência:\n"
              "Testando: Cancelar reserva sem multa\n"
              "Data reservada: 15/12/2023\n"
              "Tipo de salão: Quiosque (R$ 60,00)\n"
              "Entrada (cancelamento): 13/12/2023\n"
              "Saída: Reserva cancelada com sucesso. Nenhum ônus será aplicado.\n")


    def test_cancelamento_com_multa_24h(self):
        data_reserva = datetime(2023, 12, 15)
        tipo_salao = "quiosque"
        cancelamento_data = datetime(2023, 12, 15)
        resultado = verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data)
        self.assertEqual(resultado, "Cancelamento no dia da reserva. Será cobrada uma taxa de R$ 40.00.")
        print("Resultado do Teste 4 - Particionamento por Equivalência:\n"
              "Testando: Cancelar reserva com multa (reserva e cancelamento no mesmo dia)\n"
              "Data reservada: 15/12/2023\n"
              "Tipo de salão: Quiosque (R$ 60,00)\n"
              "Entrada (cancelamento): 15/12/2023\n"
              "Saída: Cancelamento no dia da reserva. Será cobrada uma taxa de R$ 40.00.\n")

    def test_cancelamento_com_multa_salaog(self):
        data_reserva = datetime(2023, 12, 15)
        tipo_salao = "salao_grande"
        cancelamento_data = datetime(2023, 12, 20)
        resultado = verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data)
        self.assertEqual(resultado, "Reserva não cancelada. Será cobrada uma taxa de R$ 100.00.")
        print("Resultado do Teste 5 - Particionamento por Equivalência:\n"
              "Testando: Não cancelamento da reserva de Salão Grande (data de cancelamento depois da reservada)\n"
              "Data reservada: 15/12/2023\n"
              "Tipo de salão: Salão Grande (R$ 100,00)\n"
              "Entrada (cancelamento): 20/12/2023\n"
              "Saída: Reserva não cancelada. Será cobrada uma taxa de R$ 100.00.\n")

    def test_cancelamento_com_multa_salaop(self):
        data_reserva = datetime(2023, 12, 15)
        tipo_salao = "salao_pequeno"
        cancelamento_data = datetime(2023, 12, 20)
        resultado = verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data)
        self.assertEqual(resultado, "Reserva não cancelada. Será cobrada uma taxa de R$ 80.00.")
        print("Resultado do Teste 6 - Particionamento por Equivalência:\n"
              "Testando: Não cancelamento da reserva de Salão Pequeno (data de cancelamento depois da reservada)\n"
              "Data reservada: 15/12/2023\n"
              "Tipo de salão: Salão Pequeno (R$ 80,00)\n"
              "Entrada (cancelamento): 20/12/2023\n"
              "Saída: Reserva não cancelada. Será cobrada uma taxa de R$ 100.00.\n")

    def test_cancelamento_com_multa_quiosque(self):
        data_reserva = datetime(2023, 12, 15)
        tipo_salao = "quiosque"
        cancelamento_data = datetime(2023, 12, 20)
        resultado = verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data)
        self.assertEqual(resultado, "Reserva não cancelada. Será cobrada uma taxa de R$ 60.00.")
        print("Resultado do Teste 7 - Particionamento por Equivalência:\n"
              "Testando: Não cancelamento da reserva de Quiosque (data de cancelamento depois da reservada)\n"
              "Data reservada: 15/12/2023\n"
              "Tipo de salão: Quiosque (R$ 60,00)\n"
              "Entrada (cancelamento): 20/12/2023\n"
              "Saída: Reserva não cancelada. Será cobrada uma taxa de R$ 60.00.\n")

if __name__ == '__main__':
    unittest.main()
