from matplotlib import pyplot as plt

dias = [1, 3, 6, 8, 11, 13, 17, 22]
temp_max = [22, 20, 25, 15, 30, 23, 17, 27]
temp_min = [17, 15, 18, 10, 22, 20, 8, 18]

plt.title("Temperaturas Máximas e Mínimas de Bertolândia em Outubro")

plt.xlabel("Dias")
plt.ylabel("Temperatura (°C)")

plt.grid(True)

plt.plot(dias, temp_max, linestyle='--', marker='o', label="Temperatura Máxima")
plt.plot(dias, temp_min, color='#9407F2', linewidth=5, label="Temperatura Mínima")

plt.legend(loc="best")

plt.axis([6, 18, 5, 35])

# plt.savefig("NomeDaImagem")
plt.show()


