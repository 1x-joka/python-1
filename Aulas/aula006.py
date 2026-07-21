# ============= CORES NO TERMINAL =============
# -> ANSI (escape sequence) = tudo dentro de ANSI começa com \código, no caso das cores o padrão é \033['style'; 'text'; 'background'; m
    # style: 0 (normal), 1 (bold), 4 (underline), 7 (inverte as cores da letra com o fundo)
    # text: 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (roxo), 36 (ciano), 37 (cinza)
    # background: 40 (branco), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (azul), 45 (roxo), 46 (ciano), 47 (cinza)

print('\033[7;31;43mHello Word!\033[m')