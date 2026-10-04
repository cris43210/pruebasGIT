"""
Analizador de Fortaleza de Contrasenas
Curso: Programacion II (IC010404) - Semana 1
Escuela Profesional de Ingenieria en Ciberseguridad - UNAS

Programa de demostracion para el laboratorio de configuracion del IDE.
Permite evaluar la fortaleza de una contrasena y verificar si aparece
en una lista de contrasenas filtradas/comunes (uso defensivo y educativo).
"""

import re

# Lista negra simple de contrasenas comunes (fines educativos)
CONTRASENAS_COMUNES = [
    "123456", "password", "qwerty", "abc123", "admin123", "12345678",
]


def calcular_puntaje(contrasena):
    """Calcula un puntaje de 0 a 5 segun criterios basicos de seguridad."""
    criterios = {
        "longitud": len(contrasena) >= 8,
        "mayuscula": bool(re.search(r"[A-Z]", contrasena)),
        "minuscula": bool(re.search(r"[a-z]", contrasena)),
        "numero": bool(re.search(r"[0-9]", contrasena)),
        "especial": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)),
    }
    puntaje = sum(1 for cumple in criterios.values() if cumple)
    return puntaje, criterios


def esta_en_lista_negra(contrasena, lista_negra):
    """Verifica si la contrasena aparece en la lista de contrasenas comunes."""
    return contrasena.lower() in lista_negra


def clasificar_fortaleza(puntaje):
    """Traduce el puntaje numerico a una categoria legible."""
    if puntaje <= 2:
        return "Debil"
    elif puntaje <= 4:
        return "Moderada"
    else:
        return "Fuerte"

def contras(abc):
    abc = "contrasenaDEVELOP"
    return True

def main():
    contrasenas_prueba = [
        "123456",
        "PASSWORD",
        "Password1",
        "C1b3rS3g#2026",
    ]

    print("=== Analizador de Fortaleza de Contrasenas ===\n")

    for contrasena in contrasenas_prueba:
        puntaje, criterios = calcular_puntaje(contrasena)
        fortaleza = clasificar_fortaleza(puntaje)
        en_lista_negra = esta_en_lista_negra(contrasena, CONTRASENAS_COMUNES)

        print(f"Contrasena: {contrasena}")
        print(f"  Puntaje: {puntaje}/5  ->  Fortaleza: {fortaleza}")
        if en_lista_negra:
            print("  ALERTA: la contrasena aparece en la lista de filtraciones comunes")
        print("-" * 50)


if __name__ == "__main__":
    main()
