import_anual = float(input("Introdueix l'import anual: "))
irpf = 0

# Comprovar si hi ha impost a pagar
if import_anual <= 0:
    print("La taxa d'IRPF és: 0")
else:
    # Càlcul del tram 1
    if import_anual > 12450:
        irpf += (12450 * 0.19)
    else:
        irpf += (import_anual * 0.19)

    # Càlcul del tram 2
    if import_anual > 20200:
        irpf += ((20200 - 12450) * 0.24)
    elif import_anual > 12450:
        irpf += ((import_anual - 12450) * 0.24)

    # Càlcul del tram 3
    if import_anual > 35200:
        irpf += ((35200 - 20200) * 0.30)
    elif import_anual > 20200:
        irpf += ((import_anual - 20200) * 0.30)

    # Càlcul del tram 4
    if import_anual > 60000:
        irpf += ((60000 - 35200) * 0.37)
    elif import_anual > 35200:
        irpf += ((import_anual - 35200) * 0.37)

    # Càlcul del tram 5
    if import_anual > 300000:
        irpf += ((300000 - 60000) * 0.45)
    elif import_anual > 60000:
        irpf += ((import_anual - 60000) * 0.45)

    # Càlcul del tram 6
    if import_anual > 300000:
        irpf += ((import_anual - 300000) * 0.47)

    print(f"La taxa d'IRPF és: {irpf}")
