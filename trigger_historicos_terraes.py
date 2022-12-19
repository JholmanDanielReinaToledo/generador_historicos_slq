import os

def generar_triggers(tablass):
    file = open("triggers_historicos_terrates.txt", "w")
    for tabla in tablass:
        estructura = 'create or replace function sg_historico.historico_' + tabla + '_funcion() returns trigger as $$\n'
        estructura = estructura + 'begin\n'
        estructura = estructura + '  insert into sg_historico.historico_' + tabla + '(\n'
        estructura = estructura + '    t_id,\n'
        estructura = estructura + '    operacion_ultima_modificacion\n'
        estructura = estructura + '  ) values (\n'
        estructura = estructura + '    old.t_id,\n'
        estructura = estructura + '    tg_op\n'
        estructura = estructura + '  );\n'
        estructura = estructura + "  if(tg_op in ('DELETE', 'delete')) then\n"
        estructura = estructura + '     return old;\n'
        estructura = estructura + '     else\n'
        estructura = estructura + '        return new;\n'
        estructura = estructura + '     end if;\n'
        estructura = estructura + 'end;\n'
        estructura = estructura + '$$ language plpgsql strict security definer;\n'
        estructura = estructura + '\n'
        estructura = estructura + '\n'
        estructura = estructura + 'create trigger tgg_historico_' + tabla + '\n'
        estructura = estructura + '  before update or delete\n'
        estructura = estructura + '  on sg_catastro.' + tabla + '\n'
        estructura = estructura + '  for each row\n'
        estructura = estructura + '  execute procedure sg_historico.historico_' + tabla + '_funcion();\n'
        estructura = estructura + '\n'
        estructura = estructura + '\n'
        file.write(estructura + os.linesep)
    file.close()

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
generar_triggers(tablas)
