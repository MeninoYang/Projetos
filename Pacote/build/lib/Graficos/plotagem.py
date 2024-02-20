import matplotlib.pyplot as plt

def plotar_grafico(x, y, titulo, xlabel, ylabel):
    plt.plot(x, y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()