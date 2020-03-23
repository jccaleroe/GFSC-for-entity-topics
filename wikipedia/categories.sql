with recursive r as (
    select c2.cat_id,
           c2.cat_title,
           (c2.cat_pages - c2.cat_subcats) - c2.cat_files         as num_pages,
           c2.cat_id                                              as gp,
           cast(concat(c1.cat_id, ',', c2.cat_id) as char(10000)) as path
    from category as c1
             join categorylinks as cl1 on cl1.cl_to = c1.cat_title
             join page as p1 on p1.page_id = cl1.cl_from
             join category as c2 on page_title = c2.cat_title
    where cl1.cl_to = 'Personas_por_actividad'
      and c1.cat_id != c2.cat_id
    union all
    select cr.cat_id,
           cr.cat_title,
           (cr.cat_pages - cr.cat_subcats) - cr.cat_files as num_pages,
           r.gp,
           concat(r.path, ',', cr.cat_id)
    from r
             join categorylinks as clr on cl_to = r.cat_title
             join page as pr on pr.page_id = clr.cl_from
             join category as cr on pr.page_title = cr.cat_title
    where r.cat_id != cr.cat_id
      and not find_in_set(cr.cat_id, r.path)
)
select r.cat_id, r.cat_title, sum(r.num_pages), r.gp
from r
group by r.gp;

call get_em_all('Abogados,Personajes_ficticios_por_actividad,Activistas,Ocupaciones_del_automóvil,Personas_relacionadas_con_la_astronáutica,Arquitectos,Archiveros,Árbitros,Anticuarios,Agrimensores,Aviadores,Bibliotecarios,Bomberos,Bufones,Cancilleres_mayores_del_rey,Carpinteros,Celebridades,Científicos,Cocineros,Coleccionistas,Comenderos,Confesores_reales,Contadores,Criminales,Críticos,Damas_de_compañía,Decanos,Decoradores,Delineantes,Ocupaciones_del_deporte,Dietistas,Diplomáticos,Directores_artísticos,Dirigentes,Documentalistas,Ecologistas,Educadores,Personalidades_electorales,Funcionarios_administrativos,Escribas,Enólogos,Enfermeros,Empresarios,Espías,Estudiantes,Exploradores,Fabricantes_de_instrumentos_científicos,Filósofos,Funcionarios_postales,Gastrónomos,Impostores,Ingenieros,Inventores,Jardineros,Joyeros,Jueces,Juristas,Justicias_mayores_de_la_Casa_del_Rey,Libreros,Maquilladores,Marinos,Marmolistas,Mayordomos_mayores_del_rey,Mercaderes,Militares,Mnemonistas,Modelos,Nobles,Notarios,Oradores,Religiosos,Retóricos,Sindicalistas,Toreros,Taxidermistas,Tipógrafos,Titiriteros,Trabajadores_sociales,Verdugos,Vexilólogos,Vidrieros,Personas_relacionadas_con_el_vino,Personas_deificadas,Personas_relacionadas_con_la_Organización_de_las_Naciones_Unidas,Ocupaciones_de_la_televisión,Pedagogos,Peluqueros,Periodistas,Políticos,Publicistas,Pseudocientíficos,Ocupaciones_de_los_videojuegos,Ocupaciones_de_la_medicina_alternativa,Especialistas_en_política,Personas_relacionadas_con_la_energía,Escritores,Apicultores,Impresores,Restauradores,Tapiceros,Trabajadores_sexuales,Cortesanas_y_prostitutas,Mineros,Ocupaciones_artísticas,Demonólogos,Comerciantes_de_pieles,Estudiosos_y_académicos,Mayordomos_mayores_de_la_reina,Constructores,Personas_relacionadas_con_el_pico_petrolero,Camareros_mayores_del_rey,Empleados_por_empresa,Capellanes_mayores_del_rey,Prostitutos_y_gigolós,Tejedores,Orfebres,Alfareros_y_ceramistas,Hombres_por_actividad,Abanderados,Corredores_de_bolsa,Médicos,Deportistas,Perfumistas,Agentes_por_servicio_de_inteligencia,Cazatormentas,Secretarios_generales_de_organizaciones_internacionales,Psicometristas,Conferencistas,Humoristas,Familias_por_profesión,Prestamistas,Pregoneros,Policías,Bármanes,Latifundistas,Mediáticos,Personas_relacionadas_con_la_ciencia_ficción,Investigadores,Funcionarios,Toneleros,Personas_en_la_industria_del_sexo,Teóricos,Presidentes_de_organizaciones_internacionales,Personas_implicadas_en_negocios,Subastadores,Telegrafistas,Traductores,Personas_por_periodo_y_actividad,Personas_por_nacionalidad_y_actividad,Personas_por_actividad_y_país,Personas_por_actividad_y_periodo,Personas_por_continente_y_actividad,Personas_por_actividad_y_siglo,Personas_por_actividad_y_localidad,Causas_de_muerte_por_actividad,Personas_LGBT_por_actividad,Mujeres_por_actividad,Categorías_de_personas_por_actividad,Personas_por_localidad_y_actividad,Cristianos_por_actividad,Judíos_por_actividad,Musulmanes_por_actividad,Cantantes,Editores,Directores_de_moda,Modistas,Nutricionistas,Farmacéuticos,Odontólogos,Bioquímicos,Músicos,Artistas')
drop procedure if exists get_em_all;
delimiter  //
create procedure get_em_all(var varchar(3100))
BEGIN
    DECLARE title varchar(150);

    WHILE var != ''
        DO
            SET title = convert(SUBSTRING_INDEX(var, ',', 1) using utf8);

            with recursive r as (
                select c2.cat_id,
                       c2.cat_title,
                       (c2.cat_pages - c2.cat_subcats) - c2.cat_files        as num_pages,
                       cast(concat(c2.cat_id, ',', c1.cat_id) as char(1000)) as path,
                       1                                                     as level
                from category as c1
                         join categorylinks as cl1 on cl1.cl_to = c1.cat_title
                         join page as p1 on p1.page_id = cl1.cl_from
                         join category as c2 on page_title = c2.cat_title
                where convert(cl1.cl_to using utf8) = title
                  and c1.cat_id != c2.cat_id
                union all
                select cr.cat_id,
                       cr.cat_title,
                       (cr.cat_pages - cr.cat_subcats) - cr.cat_files as num_pages,
                       concat(cr.cat_id, ',', r.path),
                       r.level + 1
                from r
                         join categorylinks as clr on cl_to = r.cat_title
                         join page as pr on pr.page_id = clr.cl_from
                         join category as cr on pr.page_title = cr.cat_title
                where r.level <= 10
                  and r.cat_id != cr.cat_id
                  and not find_in_set(cr.cat_id, r.path)
            )
            select sum(r.num_pages), title
            from r;

            IF LOCATE(',', var) > 0 THEN
                SET var = SUBSTRING(var, LOCATE(',', var) + 1);
            ELSE
                SET var = '';
            END IF;
        END WHILE;
END;
//
delimiter ;


call get_ids('Educadores,Ocupaciones_del_deporte,Deportistas,Religiosos,Músicos,Críticos,Activistas,Dirigentes,Nobles,Militares,Especialistas_en_política,Políticos,Escritores,Ocupaciones_artísticas,Estudiantes,Filósofos,Artistas,Retóricos,Científicos,Apicultores');
drop procedure if exists get_ids;
delimiter  //
create procedure get_ids(var varchar(3100))
BEGIN
    DECLARE title varchar(150);

    WHILE var != ''
        DO
            SET title = convert(SUBSTRING_INDEX(var, ',', 1) using utf8);

            select cat_id from category where cat_title = convert(title using utf8);

            IF LOCATE(',', var) > 0 THEN
                SET var = SUBSTRING(var, LOCATE(',', var) + 1);
            ELSE
                SET var = '';
            END IF;
        END WHILE;
END;
//
delimiter ;
