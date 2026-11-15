from models import Paciente, Medico, CitaMedica
from repository import CentroSaludRepository

def mostrar_menu():
    print("\n" + "="*40)
    print("   CENTRO DE SALUD - CHORRILLOS")
    print("="*40)
    print("1. Registrar Paciente")
    print("2. Registrar Médico")
    print("3. Programar Cita Médica")
    print("4. Listar Pacientes")
    print("5. Listar Médicos")
    print("6. Listar Citas Programadas")
    print("7. Salir")
    print("="*40)

def main():
    repo = CentroSaludRepository()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR NUEVO PACIENTE ---")
            dni = input("Ingrese DNI: ").strip()
            if repo.buscar_paciente(dni):
                print("[!] Error: Ya existe un paciente con ese DNI.")
                continue
            nombre = input("Ingrese Nombre completo: ").strip()
            try:
                edad = int(input("Ingrese Edad: ").strip())
            except ValueError:
                print("[!] Error: La edad debe ser un número entero.")
                continue
            historia = input("Ingrese Número de Historia Clínica (ej. HC-002): ").strip()
            antecedentes = input("Ingrese Antecedentes médicos: ").strip()

            nuevo_paciente = Paciente(dni, nombre, edad, historia, antecedentes)
            repo.agregar_paciente(nuevo_paciente)
            print("[Éxito] Paciente registrado correctamente.")

        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO MÉDICO ---")
            dni = input("Ingrese DNI: ").strip()
            nombre = input("Ingrese Nombre completo: ").strip()
            try:
                edad = int(input("Ingrese Edad: ").strip())
            except ValueError:
                print("[!] Error: La edad debe ser un número entero.")
                continue
            cmp = input("Ingrese Código CMP (ej. CMP-11223): ").strip()
            if repo.buscar_medico(cmp):
                print("[!] Error: Ya existe un médico con ese CMP.")
                continue
            especialidad = input("Ingrese Especialidad: ").strip()

            nuevo_medico = Medico(dni, nombre, edad, cmp, especialidad)
            repo.agregar_medico(nuevo_medico)
            print("[Éxito] Médico registrado correctamente.")

        elif opcion == "3":
            print("\n--- PROGRAMAR CITA MÉDICA ---")
            dni_paciente = input("Ingrese DNI del Paciente: ").strip()
            paciente = repo.buscar_paciente(dni_paciente)
            if not paciente:
                print("[!] Error: Paciente no encontrado. Regístrelo primero.")
                continue

            cmp_medico = input("Ingrese CMP del Médico: ").strip()
            medico = repo.buscar_medico(cmp_medico)
            if not medico:
                print("[!] Error: Médico no encontrado.")
                continue

            fecha = input("Ingrese Fecha (DD/MM/YYYY): ").strip()
            hora = input("Ingrese Hora (HH:MM): ").strip()

            nueva_cita = CitaMedica(fecha, hora, paciente, medico)
            repo.programar_cita(nueva_cita)
            print("[Éxito] Cita médica programada correctamente.")

        elif opcion == "4":
            print("\n--- LISTA DE PACIENTES REGISTRADOS ---")
            if not repo.pacientes:
                print("No hay pacientes registrados.")
            else:
                for p in repo.pacientes:
                    p.mostrar_info()

        elif opcion == "5":
            print("\n--- LISTA DE MÉDICOS REGISTRADOS ---")
            if not repo.medicos:
                print("No hay médicos registrados.")
            else:
                for m in repo.medicos:
                    m.mostrar_info()

        elif opcion == "6":
            print("\n--- CITAS MÉDICAS PROGRAMADAS ---")
            if not repo.citas:
                print("No hay citas programadas.")
            else:
                for c in repo.citas:
                    c.mostrar_detalles()

        elif opcion == "7":
            print("\nGracias por usar el sistema del Centro de Salud Chorrillos. ¡Hasta luego!")
            break
        else:
            print("[!] Opción inválida. Por favor, elija un número del 1 al 6.")

if __name__ == "__main__":
    main()