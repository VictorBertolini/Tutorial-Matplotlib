# Tutorial Matplotlib

## Configuração inicial 

### Instalação
```shell
pip install matplotlib
```

## Código Básico
Para fins didáticos, utilizarei x e y criados com valores aleatórios. Sendo para cada x um y correspondente.
```python
x = [1, 3, 6, 8, 11, 13, 17, 22]
y = [10, 20, 25, 15, 30, 23, 17, 27]
``` 

E então precisa 'plotar' o gráfico, ou seja, adicionar esse gráfico formado com esses valores ao escopo

```python
plt.plot(x, y)
``` 

E então, mostra-se na tela a figura gerada:

```python
plt.show()
```

Assim, teremos: 

![Gráfico Básico](/images/Gráfico%20-%20Codigo%20Basico.png)

## Adicionando Labels 
Para facilitar a compreensão do gráfico, coloca-se título e o que cada eixo representa:

```python
plt.title("Temperaturas de Bertolândia em Outubro")

plt.xlabel("Dias")
plt.ylabel("Temperatura (°C)")
```

Melhorando muito mais a visualização e entendimento das informações contidas nele:

![Gráfico - Labels](/images/Gráfico%20-%20Labels.png)


## Adicionando um novo dado para comparação
Lembra que comentei do `plot()`? Que você colocaria no gráfico os dados e depois mostraria na tela com o `show()`? 

Agora colocaremos isso em prática!

Vamos alterar algumas coisas, vamos trocar alguns dados e nomes de algumas variáveis:

```python
dias = [1, 3, 6, 8, 11, 13, 17, 22]
temp_max = [22, 20, 25, 15, 30, 23, 17, 27]
temp_min = [17, 15, 18, 10, 22, 20, 8, 18]

plt.title("Temperaturas Máximas e Mínimas de Bertolândia em Outubro")
```

E agora vamos adicionar tanto as temperaturas máximas quanto as mínimas com o `plot()` e mostrar o resultado:

```python 
plt.plot(dias, temp_max)
plt.plot(dias, temp_min)
plt.show()
```

![Gráfico Max e min](/images/Gráfico%20-%20Temperaturas%20Max%20e%20Min.png)


## Adicionando Grid 

Para adicionar um grid (fundo quadriculado) para melhorar a visualização pode-se usar:

```python
plt.grid(True)
```
![Gráfico com Grid](/images/Gráfico%20-%20Grid.png)


## Estilização das linhas

### Linestyle
Coloca-se no .plot
```python
plt.plot(dias, temp_max, linestyle='--')
```
![Gráfico linestyle](/images/Gráfico%20-%20Linestyle.png)

### Marker
```python
plt.plot(dias, temp_max, linestyle='--', marker='o')
```
![Gráfico marker](/images/Gráfico%20-%20Marker.png)

### Cor
```python
plt.plot(dias, temp_min, color='#9407F2')
```

![Gráfico Cor](/images/Gráfico%20-%20Cor.png)

### Linewidth
```python
plt.plot(dias, temp_min, color='#9407F2', linewidth=5)
```
![Gráfico linewidth](/images/Gráfico%20-%20Linewidth.png)

## Legend
### Como usar 
Existem diversas formas de colocar o legend, mas a melhor delas é deixar um label no `plot()`

```python
plt.plot(dias, temp_max, linestyle='--', marker='o', label="Temperatura Máxima")
plt.plot(dias, temp_min, color='#9407F2', linewidth=5, label="Temperatura Mínima")

plt.legend()
```

![Gráfico Legend](/images/Gráfico%20-%20Legend.png)


### Mudando a posição do legend
Mas também pode-se colocar a legenda em diferentes locais da tela usando o parâmetro `loc`

E você pode usar diversas localizações como:

`best` (O próprio programa decide o melhor local)

`upper right`

`upper left`

`lower left`

`lower right`

`right`

`center left`

`center right`

`lower center`

`upper center`

`center`

E usa-se assim:
```python
plt.legend(loc="best")
```

## Definir intervalo do gráfico
```python
#       ([Xmin, Xmax, Ymin, Ymax])
plt.axis([6, 18, 5, 35])
```
![Gráfico com Intervalo](/images/Gráfico%20-%20Intervalo.png)

E pode-se também modificar apenas um dos eixos com `xlim()` e `ylim()`
```python
plt.xlim([6, 18])
plt.ylim([5, 35])
```
Quando se faz apenas do X, o próprio matplot decide os melhores valores para colocar nos limites de y, e a inversa também ocorre o mesmo.

## Salvar o Gráfico 
Ao invés de dar um `show()` para mostrar o gráfico, pode-se salvar a imagem com:

```python
plt.savefig(<file name>)
```
E irá aparecer junto aos arquivos




