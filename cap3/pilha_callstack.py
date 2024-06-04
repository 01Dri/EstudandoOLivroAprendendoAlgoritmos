# Primeiro, vamos entender um pouco sobre pilhas?

# Pilha: É uma estrutura de dados parecida com uma pilha de pratos, onde você coloca um prato em cima do outro.
# Ou seja, você tem um prato da cor preta e, em seguida, adiciona um prato dar cor cinza em cima.
# PILHA:
# - PRATO_CINZA -> Novos itens sempre são inseridos no topo da pilha.
# - PRATO_PRETO

# As operações típicas de uma pilha são "push" (insere um novo elemento no topo da pilha) e "pop" (remove o elemento do topo da pilha).

# Callstack: É uma pilha na memória onde são armazenadas todas as chamadas de funções, veja o exemplo abaixo:

def hello():
    name = "Diego"
    print("Hello " + name)
    hello2(name)
    print("Byeee!")

def hello2(name):
    print("How are you " + name)

# Quando a função "hello" é chamada:
# PILHA
# - hello()

# Dentro da função hello, a chamada print é feita:
# PILHA
# - print("Hello Diego")
# - hello() -> Parcialmente completa, aguardando conclusão da chamada print

# Após a conclusão de print, ele é removido do topo da pilha:
# PILHA
# - hello()

# A próxima linha chama hello2(name):
# PILHA
# - hello2("Diego")
# - hello() -> Parcialmente completa, aguardando conclusão da chamada hello2

# Dentro de hello2, a chamada print é feita:
# PILHA
# - print("How are you Diego")
# - hello2("Diego") -> Parcialmente completa, aguardando conclusão da chamada print
# - hello() -> Parcialmente completa, aguardando conclusão da chamada hello2

# Após a conclusão de print, ele é removido do topo da pilha:
# PILHA
# - hello2("Diego")
# - hello() -> Parcialmente completa, aguardando conclusão da chamada hello2

# A função hello2 é concluída e removida da pilha:
# PILHA
# - hello()

# Voltando para hello, a próxima linha é print("Byeee!"):
# PILHA
# - print("Byeee!")
# - hello() -> Parcialmente completa, aguardando conclusão da chamada print

# Após a conclusão de print, ele é removido do topo da pilha:
# PILHA
# - hello()

# Finalmente, a função hello é concluída e removida da pilha:
# PILHA
# (vazia)