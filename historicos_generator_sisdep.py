import os

def generar_triggers(schema, tablass):
    file = open("historicos_sisdep.txt", "w")
    for tabla in tablass:
        estructura = 'create table sisdep_archivo.' + tabla + '(\n'
        estructura = estructura + ' like ' + schema + '.' + tabla + ',\n'
        estructura = estructura + ' operation varchar,\n'
        estructura = estructura + ' CONSTRAINT fk_id_usuario_edita FOREIGN KEY (id_usuario_edita)\n'
        estructura = estructura + ' REFERENCES sisdep_administracion.usuario(id)\n'
        estructura = estructura + ');'

        funcion = 'create or replace function sisdep_archivo.tgghistorico'+tabla+'_func() returns trigger as $$'
        funcion = funcion + ' begin\n'
        funcion = funcion + "  insert into sisdep_archivo."+tabla+"(\n"
        funcion = funcion + "  columnas\n"
        funcion = funcion + "  ) values (\n"
        funcion = funcion + "  old.columas,\n"
        funcion = funcion + "  tg_op\n"
        funcion = funcion + "  );\n"
        funcion = funcion + "   if(tg_op in ('DELETE', 'delete')) then\n"
        funcion = funcion + '       return old;\n'
        funcion = funcion + '   else\n'
        funcion = funcion + '       return new;\n'
        funcion = funcion + '   end if;\n'
        funcion = funcion + ' end;\n'
        funcion = funcion + '$function$;\n'

        trigger = 'CREATE TRIGGER historico BEFORE DELETE OR UPDATE ON ' + schema + '.' + tabla + '\n'
        trigger = trigger + '   FOR EACH ROW EXECUTE PROCEDURE sisdep_archivo.tgghistorico' + tabla + '_func();'

        file.write(estructura + os.linesep)
        file.write(funcion + os.linesep)
        file.write(trigger + os.linesep)
    file.close()

schema = 'sisdep_ventero'

tablas = [
    'persona',
    'ventero'
    ]

generar_triggers(schema, tablas)