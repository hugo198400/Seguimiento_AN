import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APP1.settings')
django.setup()

from Avances.models import Puntos, Fichas, Ala, AAA, CustomUser

def probar_relacion():
    # Recuperar o crear una instancia de Puntos
    punto, created = Puntos.objects.get_or_create(
        COD='P001',
        defaults={
            'id_ala': Ala.objects.first(),
            'id_aaa': AAA.objects.first(),
            'Sector': 'Sector 1',
            'COEN': 123,
            'MetaKm': 10.0,
            'AvanceKm': 5.0,
            'MetaVol': 100.0,
            'AvanceVol': 50.0,
            'Pinicio': '2025-01-01',
            'Pfinal': '2025-12-31',
            'PLazo': 365,
            'Estado': 'En Proceso',
            'id_user': CustomUser.objects.first(),
            'Estatus': 200
        }
    )

    # Crear una instancia de Fichas relacionada con el Punto
    ficha, created = Fichas.objects.get_or_create(
        COD_Ficha='F001',
        defaults={
            'COD_puntos': punto,
            'id_aaa': AAA.objects.first(),
            'id_ala': Ala.objects.first(),
            'sector': 'Sector 1',
            'descripcion': 'Descripción de la ficha',
            'departamento': 'Departamento 1',
            'provincia': 'Provincia 1',
            'distrito': 'Distrito 1',
            'cuenca': 'Cuenca 1',
            'Tipo': 'Tipo 1',
            'cuerpoAgua': 'Cuerpo de Agua 1',
            'MetaKm': 10.0,
            'MetaVol': 100.0,
            'Poblacion': 1000,
            'viviendas': 200,
            'AreaCultivo': 50.0,
            'Cultivo': 'Cultivo 1',
            'Este_I': 123.45,
            'Norte_I': 678.90,
            'Este_F': 123.45,
            'Norte_F': 678.90,
            'Zona': 'Zona 1',
            'margen': 'Margen 1',
            'Ptto': 100000.0,
            'link': 'http://example.com',
            'Observacion': 'Sin Observacion'
        }
    )

    # Verificar la relación inversa
    fichas_relacionadas = punto.fichas.all()

    # Imprimir las fichas relacionadas
    for ficha in fichas_relacionadas:
        print(ficha.COD_Ficha)

if __name__ == '__main__':
    probar_relacion()