'''
@author: Monkey Coders
@version: 1

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad

Mineria de datos.
    inegi: https://www.inegi.org.mx/
    conapo: https://datos.gob.mx/busca/dataset/proyecciones-de-la-poblacion-de-mexico-y-de-las-entidades-federativas-2016-2050/resource/a31f9dbb-4f65-47da-ba44-50eb44a9ad25
    impi: https://datos.gob.mx/busca/dataset/informacion-estadistica-de-invenciones-signos-distintivos-y-proteccion-a-la-propiedad-intelectu
    sectur: https://www.datatur.sectur.gob.mx

Crecimiento poblacional:
    1. Extraer la poblacion total por entidad federativa
    2. Extraer la natalidad total por entidad federativa
    3. Extraer la mortalidad total por entidad federativa
    4. Calcular la natalidad 2010 hasta la actualidad (Angie)
    5. Calcular la mortalidad 2010 hasta el actualidad (Angie)
    6. Con los datos de mortalidad y natalidad calcular la poblacion total hasta 2018   
    7. Sacar la prediccion de la poblacion 2019

Crecimiento economico:
    Factores del crecimiento economico:
    - numero de empresas registradas
    - numero de patentes registradas
    - valor agregado bruto por empresa
'''
from classes.conexionDB import ConexionDB
from classes.csvScanner import CsvScanner
from classes.controlador import ControladorDatos

if __name__ == "__main__":
    #Contenedores de informacion
    poblacion_2010 = []
    natalidad_2010_2017 = []
    mortalidad_2010_2017 = []
    poblacion_2018_2019 = []
    patentes_2010_2018 = []
    unidades_economicas_2013_2018 = []
    turistas_2010_2018 = []
    pib_mexico_1993_2018 = []
    pib_entidades_2010_2017 = []
    exportaciones_entidades_2010_2018 = []

    #Utilidades
    scanner = CsvScanner()
    database = ConexionDB()
    controlador = ControladorDatos()

    #Base de datos
    database.limpiar_tablas_postgres()
    database.crear_tablas_postgres()

    '''
        Poblacion 2010.
        Datos: @inegi
    '''
    poblacion_2010 = scanner.leer_poblacion_2010(
        'inegi_data/pob_entidades/Poblacion_01.csv')
    '''
        Natalidad 2011 - 2017.
        Datos: @inegi
    '''
    natalidad_2010_2017 = scanner.leer_natalidad_2010_2017(
        'inegi_data/pob_entidades/Natalidad_01.csv')
    '''
        Moratlidad 2011 - 2017.
        Datos: @inegi
    '''
    mortalidad_2010_2017 = scanner.leer_mortalidad_2010_2017(
        'inegi_data/pob_entidades/Mortalidad_01.csv')
    '''
        Proyecciones de poblacion 2018.
        Datos: @conapo
    '''
    poblacion_2018_2019 = scanner.leer_poblacion_2018_2019(
        'conapo_data/pob_ini_proyecciones.csv')
    '''
        Patentes registradas por entidad federativa 2015 - 2018
        Datos: @impi
    '''
    patentes_2010_2018 = scanner.leer_patentes_2010_2018(
        'impi_data/patentes.csv')
    '''
        Unidades economicas registradas en cada entidad federativa 2013 - 2018
        Datos: @denue
    '''
    unidades_economicas_2013_2018 = scanner.leer_unidades_economicas_2013_2018(
        'inegi_data/neg_entidades/negocios.csv')
    '''
        Turistas registrados en cada entidad federativa 2010 - 2018
        Datos: @sectur
    '''
    turistas_2010_2018 = scanner.leer_turistas_2010_2018(
        'sectur_data/turismo_entidades.csv')
    '''
        PIB de Mexico 2010 - 2018
        Datos: @inegi
    '''
    pib_mexico_1993_2018 = scanner.leer_pib_mexico_1993_2018(
        'inegi_data/pib_mexico/pib_mexico.csv')
    '''
        PIB por entidad federativa y actividad economica 2010 - 2017
        Datos: @inegi
    '''
    #EN DESARROLLO
    pib_entidades_2010_2017 = scanner.leer_pib_entidades_2010_2017(
        ['inegi_data/pib_entidades/pibe_entidad_ags.csv', 'inegi_data/pib_entidades/pibe_entidad_bc.csv',
         'inegi_data/pib_entidades/pibe_entidad_bcs.csv', 'inegi_data/pib_entidades/pibe_entidad_camp.csv',
         'inegi_data/pib_entidades/pibe_entidad_coah.csv', 'inegi_data/pib_entidades/pibe_entidad_col.csv',
         'inegi_data/pib_entidades/pibe_entidad_chis.csv',  'inegi_data/pib_entidades/pibe_entidad_chih.csv',
         'inegi_data/pib_entidades/pibe_entidad_cdmx.csv', 'inegi_data/pib_entidades/pibe_entidad_dgo.csv',
         'inegi_data/pib_entidades/pibe_entidad_gto.csv', 'inegi_data/pib_entidades/pibe_entidad_gro.csv',
         'inegi_data/pib_entidades/pibe_entidad_hgo.csv', 'inegi_data/pib_entidades/pibe_entidad_jal.csv',
         'inegi_data/pib_entidades/pibe_entidad_mex.csv', 'inegi_data/pib_entidades/pibe_entidad_mich.csv',
         'inegi_data/pib_entidades/pibe_entidad_mor.csv', 'inegi_data/pib_entidades/pibe_entidad_nay.csv',
         'inegi_data/pib_entidades/pibe_entidad_nl.csv','inegi_data/pib_entidades/pibe_entidad_oax.csv', 
         'inegi_data/pib_entidades/pibe_entidad_pue.csv', 'inegi_data/pib_entidades/pibe_entidad_qr.csv', 
         'inegi_data/pib_entidades/pibe_entidad_qro.csv','inegi_data/pib_entidades/pibe_entidad_slp.csv', 
         'inegi_data/pib_entidades/pibe_entidad_sin.csv','inegi_data/pib_entidades/pibe_entidad_son.csv', 
         'inegi_data/pib_entidades/pibe_entidad_tab.csv','inegi_data/pib_entidades/pibe_entidad_tamps.csv', 
         'inegi_data/pib_entidades/pibe_entidad_tlax.csv', 'inegi_data/pib_entidades/pibe_entidad_ver.csv',
          'inegi_data/pib_entidades/pibe_entidad_yuc.csv','inegi_data/pib_entidades/pibe_entidad_zac.csv']
          )
    '''
        Indicador Trimestral de Actividad Económica Estatal 2010 T1 - 2018 T3
        Datos: @ITAEE
    '''
    '''
        Exportaciones de mexico por entidad federativa 2010 - 2018 
        Datos: @ADUANA
    '''
    exportaciones_entidades_2010_2018 = scanner.leer_exportaciones_entidades_2010_2018('inegi_data/exp_entidades/exportaciones.csv')
    '''
        Gastos en consumo de electricidad por municipio 2010 - 2018 
        Datos: @CFE
    '''
    '''
        Transacciones bancarias por municipio en cajeros automaticos 2010 - 2018 
        Datos: @CNBV
    '''

    #controladores
    controlador.controlador_poblacion_2010(database, poblacion_2010)
    #controlador.controlador_poblacion_2010_2017(database, poblacion_2010, natalidad_2010_2017, mortalidad_2010_2017)
    #controlador.controlador_poblacion_2018_2019(database, poblacion_2018_2019)
    #controlador.controlador_patentes_2010_2018(database, patentes_2010_2018)
    #controlador.controlador_unidades_economicas_2013_2018(database, unidades_economicas_2013_2018)
    #controlador.controlador_turistas_2010_2018(database, turistas_2010_2018)
    controlador.controlador_pib_mexico_1993_2018(database, pib_mexico_1993_2018)
    #controlador.controlador_poblacion_mexico_2010_2019(database, poblacion_2010, natalidad_2010_2017, mortalidad_2010_2017, poblacion_2018_2019)
    #controlador.controlador_exportaciones_entidades_2010_2018(database, exportaciones_entidades_2010_2018)
    '''
    NOTA:
        Insertar unidades economicas de todo mexico 2010 - 2018 
    '''