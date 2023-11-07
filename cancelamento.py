from datetime import datetime

def verificar_cancelamento(data_reserva, tipo_salao, cancelamento_data):
    # Preços de reserva para cada tipo de salão
    precos_salao = {
        "quiosque": 60.00,
        "salao_pequeno": 80.00,
        "salao_grande": 100.00
    }

    # Verifica se o tipo de salão é válido
    if tipo_salao not in precos_salao:
        return "Tipo de salão inválido."

    # Calcula a diferença de dias entre a data da reserva e a data atual
    diferenca_dias = (cancelamento_data - data_reserva).days

    if diferenca_dias < 0:
        return "Reserva cancelada com sucesso. Nenhum ônus será aplicado."

    elif diferenca_dias == 0:
        # Reserva cancelada no mesmo dia da reserva
        taxa_cancelamento_atrasado = 40.00
        return f"Cancelamento no dia da reserva. Será cobrada uma taxa de R$ {taxa_cancelamento_atrasado:.2f}."

    else:
        # Reserva não cancelada
        taxa_salao = precos_salao[tipo_salao]
        return f"Reserva não cancelada. Será cobrada uma taxa de R$ {taxa_salao:.2f}."
