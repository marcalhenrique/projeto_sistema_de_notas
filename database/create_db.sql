-- -----------------------------------------------------
-- Marçal Henrique Moreira
-- Discente em Engenharia de Computação pelo IFMG - Campus Bambuí
-- 2022
-- github.com/marcalhenrique
-- -----------------------------------------------------
-- Arquivo de criação do banco de dados Sistemas de Notas
-- -----------------------------------------------------


-- Criando as tabelas
create table if not exists aluno(

    id_aluno serial not null,
    nome_aluno varchar(100) not null,
    data_nascimento date not null,
    media float,

    constraint aluno_pk primary key (id_aluno)
);


create table if not exists professor(

    id_professor serial not null,
    nome_professor varchar(100) not null,
    area varchar(100),

    constraint professor_pk primary key (id_professor)
);


create table if not exists disciplina(

    id_disciplina serial not null,
    nome_disciplina varchar(100) not null,
    carga_horaria int not null,
    id_professor int not null,

    constraint disciplina_pk primary key (id_disciplina),
    constraint disciplina_fk_professor foreign key (id_professor) references professor(id_professor)
);


create table if not exists matriculado(

    id_disciplina int not null,
    id_aluno int not null,
    nota float,

    constraint matriculado_pk primary key (id_disciplina, id_aluno),
    constraint matriculado_fk_disciplina foreign key (id_disciplina) references disciplina(id_disciplina),
    constraint matriculado_fk_aluno foreign key (id_aluno) references aluno(id_aluno)
);


-- Inserindo alguns dados nas tabelas criadas
insert into professor(nome_professor, area) values 
('Marcos', 'Dados'),
('Samuel', 'Redes'),
('Gabriel', 'Sistemas'),
('Calebe', 'Eletronica');


insert into disciplina(nome_disciplina, carga_horaria, id_professor) values 
('Banco de Dados', 80, 1),
('Redes de Computadores', 80, 2),
('Sistemas Operacionais', 80, 3),
('Eletronica', 80, 4);


insert into aluno(nome_aluno, data_nascimento, media) values 
('Joao', '1990-01-01', 7.5),
('Maria', '1990-01-01', 8.5),
('Jose', '1990-01-01', 9.5),
('Pedro', '1990-01-01', 6.5);


insert into matriculado(id_disciplina, id_aluno, nota) values 
(1, 1, 7.5),
(1, 2, 8.5),
(1, 3, 9.5),
(1, 4, 6.5),
(2, 1, 7.5),
(2, 2, 8.5),
(2, 3, 9.5),
(2, 4, 6.5),
(3, 1, 7.5),
(3, 2, 8.5),
(3, 3, 9.5),
(3, 4, 6.5),
(4, 1, 7.5),
(4, 2, 8.5),
(4, 3, 9.5),
(4, 4, 6.5);


-- Consultas
select * from aluno;
select * from professor;
select * from disciplina;
