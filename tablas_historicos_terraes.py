import os

def generar_triggers(schema, tablass):
    file = open("tabla_historico_terraes.txt", "w")
    for tabla in tablass:
        estructura = 'create table sg_historico.historico_' + tabla + '(\n'
        estructura = estructura + ' like ' + schema + '.' + tabla + ',\n'
        estructura = estructura + ' fecha_modificacion timestamptz not null default now(),\n'
        estructura = estructura + ' usuario_modificacion bigint not null default sg_ciudadano.current_user_id() references sg_administracion.usuario(id),\n'
        estructura = estructura + ' operacion_ultima_modificacion varchar,\n'
        estructura = estructura + ' tramite_modificante varchar not null default sg_administracion.current_user_tramite(),\n'
        estructura = estructura + ' resolucion_modificante bigint not null default sg_administracion.current_user_resolucion() references sg_administracion.resolucion(id)\n'
        estructura = estructura + ' );\n'
        estructura = estructura + '\n'
        estructura = estructura + ' create index on sg_historico.historico_' + tabla +'(usuario_modificacion);\n'
        estructura = estructura + ' create index on sg_historico.historico_' + tabla +'(operacion_ultima_modificacion);\n'
        estructura = estructura + ' create index on sg_historico.historico_' + tabla +'(resolucion_modificante);\n'
        file.write(estructura + os.linesep)
    file.close()

schema = 'sg_catastro'

tablas = [
    'cc_barrio',
    'cc_centropoblado',
    'cc_corregimiento',
    'cc_limitemunicipio',
    'cc_localidadcomuna',
    'cc_manzana',
    'cc_metodooperacion',
    'cc_nomenclaturavial',
    'cc_nomenclaturavial_tipo_via',
    'cc_perimetrourbano',
    'cc_sectorrural',
    'cc_sectorurbano',
    'cc_vereda',
]

generar_triggers(schema, tablas)
