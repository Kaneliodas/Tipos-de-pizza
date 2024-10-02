#Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza.
#Modifique seu laço for para mostrar uma frase usando o nome da pizza em
#vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha
#na saída contendo uma frase simples como Gosto de pizza de pepperoni.
#• Acrescente uma linha no final de seu programa, fora do laço for, que informe
#quanto você gosta de pizza. A saída deve ser constituída de três ou mais
#linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo, Eu realmente adoro pizza!
Pizza = ['Chocolate', 'carne de sol', 'calabresa']
for pizzas in Pizza: print("Eu gosto de pizza de " + pizzas)
print("A minha pizza favorita é pizza de "+ Pizza[1])



#Pate 2:
#Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
#Então faça o seguinte: • Adicione uma nova pizza à lista original.
#• Adicione uma pizza diferente à lista friend_pizzas.
#• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
#favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
#Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize
#um laço for para exibir a segunda lista. Certifique-se de que cada pizza
#nova esteja armazenada na lista apropriada

friend_pizzas = Pizza[:]

Pizza.append('sushi')
friend_pizzas.append('frango')
for pizzas in Pizza: print("Eu gosto de pizza de " + str(pizzas))

for a in friend_pizzas: print("\nEle gosta de pizza de " + str(a))

