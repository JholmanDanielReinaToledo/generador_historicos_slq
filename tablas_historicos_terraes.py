import os

def generar_triggers(schema, tablass):
    file = open("tabla_historico_terraes.txt", "w")
    for tabla in tablass:
        estructura = 'create table sghistorico.historico' + tabla + '(\n'
        estructura = estructura + ' like ' + schema + '.' + tabla + ',\n'
        estructura = estructura + ' fecha_modificacion timestamptz not null default now(),\n'
        estructura = estructura + ' usuario_modificacion bigint not null default sg_ciudadano.current_user_id() references sg_administracion.usuario(id),\n'
        estructura = estructura + ' operacion_ultima_modificacion varchar,\n'
        estructura = estructura + ' tramite_modificante varchar not null default sg_administracion.current_user_tramite(),\n'
        estructura = estructura + ' resolucion_modificante bigint not null default sg_administracion.current_user_resolucion() references sg_administracion.resolucion(id)\n'
        estructura = estructura + ' );\n'
        estructura = estructura + '\n'
        estructura = estructura + ' create index on sghistorico.historico' + tabla +'(usuario_modificacion);\n'
        estructura = estructura + ' create index on sghistorico.historico' + tabla +'(operacion_ultima_modificacion);\n'
        estructura = estructura + ' create index on sghistorico.historico' + tabla +'(resolucion_modificante);\n'
        file.write(estructura + os.linesep)
    file.close()

schema = 'sg_catastro'

tablas = [
    'zona_fisica_predio',
    'zona_geoeconomica_predio',
    'lindero_predio',
    'av_tablacalificacionconstruccion',
    'av_tipologiaconstruccion',
    'av_zonahomogeneafisicarural',
    'av_zonahomogeneafisicaurbana',
    'av_zonahomogeneageoeconomicarural',
    'av_zonahomogeneageoeconomicaurbana',
]

generar_triggers(schema, tablas)
