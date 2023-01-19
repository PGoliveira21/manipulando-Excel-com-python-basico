#funçoes
def faixaIdade(idad):
    if idad <= 12:
        return 'criança'
    elif idad <= 18:
        return 'adolescente'
    elif idad <= 80:
        return 'adulto'
    else:
        return 'idoso'