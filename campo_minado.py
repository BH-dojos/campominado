def resolve_campo_minado(campo_minado):
    linha = campo_minado[0]
    solucao = ''
    for casa in linha:
        if casa == '*':
            solucao += '*'
        elif len(linha)>1 and linha[1] == '*':
            solucao += '1'
        elif casa == '.':
            solucao += '0'


    return [solucao]