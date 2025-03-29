def valida_inteiro(mensagem, mínimo, máximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print(f"Digite um valor entre {mínimo} e {máximo}")
        except ValueError:
            print("Você deve digitar um número inteiro")