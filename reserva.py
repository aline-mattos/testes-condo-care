from datetime import datetime

def verificar_reserva(data_reserva):
    # Obtenha a data atual
    data_atual = datetime.now()

    # Verifica se a data da reserva está no passado
    if data_reserva < data_atual:
        return "A reserva não pode ser feita no passado."

    # Calcula a diferença de dias entre a data da reserva e a data atual
    diferenca_dias = (data_reserva - data_atual).days

    # Verifica se a reserva está dentro do intervalo de 0 a 90 dias
    if 0 <= diferenca_dias <= 90:
        return "Reserva feita com sucesso."

    # Verifica se a reserva está a mais de 90 dias no futuro
    if diferenca_dias > 90:
        return "A reserva não pode ser feita com mais de 90 dias de antecedência."

    # Se nenhuma das condições anteriores for atendida, retorna uma mensagem de erro
    return "Ocorreu um erro ao fazer a reserva."
