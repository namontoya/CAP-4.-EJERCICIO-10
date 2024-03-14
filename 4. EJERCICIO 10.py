#Capitulo 3. Ejercicio resuelto 10

NI = input("Ingrese el número de inscripción: ")
NOM = input("Ingrese los nombres: ")
PAT = float(input("Ingrese el patrimonio: "))
EST = float(input("Ingrese el estrato social: "))
PAGMAT = 50000

if (PAT > 2000000) and (EST > 3):
    PAGMAT = PAGMAT + 0.03 * PAT

print(f"EL ESTUDIANTE CON NÚMERO DE INSCRIPCION {NI} Y NOMBRE {NOM} DEBE PAGAR ${PAGMAT}") 
