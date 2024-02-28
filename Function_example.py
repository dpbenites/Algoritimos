## vou contruir um exemplo de funcao utilizando uma bilbioteca 

# para acostumar a utilizar a biblioteca e exemplificar

import matplotlib.pyplot as plt 
import numpy as np  

def Plot_derivatives(n, c):
    ''' n é o grau da derivada
     c é uma constante

    f(x) = cX^n 
    f'(x) = cnX^n-1'''

    x = np.linspace(0, 10, 400)
    f = c * x**n
    df = c * n * x**(n-1)

    plt.xlabel('$X$')
    plt.ylabel('$y$')
    plt.plot(x, f, label=f'$y = {c}X^{n}$ ', color='red')
    plt.plot(x, df, label="$y' = dy/dx $", color='green')
    plt.legend()
    plt.grid(True)
    
    # Remova a linha abaixo, pois a função já faz as plotagens
    # return plt.plot()

# Chame a função para exibir os gráficos
Plot_derivatives(5, 2)
plt.show()  # Adicione essa linha para mostrar o gráfico
