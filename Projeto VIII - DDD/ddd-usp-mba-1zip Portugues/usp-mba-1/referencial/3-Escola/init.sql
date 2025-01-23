-- Criar tabela "alunos"
CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefone VARCHAR(15) NOT NULL
);

-- Criar tabela "cursos"
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    descricao TEXT
);

-- Criar tabela "matriculas"
CREATE TABLE IF NOT EXISTS matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(id),
    curso_id INT REFERENCES cursos(id)
);

-- Criar 50 alunos com nomes reais
INSERT INTO alunos (nome, email, telefone) VALUES
('Ana Beatriz', 'ana.beatriz@email.com', '(11) 90001-0001'),
('Carlos Eduardo', 'carlos.eduardo@email.com', '(11) 90002-0002'),
('Mariana Oliveira', 'mariana.oliveira@email.com', '(11) 90003-0003'),
('Lucas Silva', 'lucas.silva@email.com', '(11) 90004-0004'),
('Gabriela Santos', 'gabriela.santos@email.com', '(11) 90005-0005'),
('João Pedro', 'joao.pedro@email.com', '(11) 90006-0006'),
('Fernanda Costa', 'fernanda.costa@email.com', '(11) 90007-0007'),
('Ricardo Almeida', 'ricardo.almeida@email.com', '(11) 90008-0008'),
('Julia Mendes', 'julia.mendes@email.com', '(11) 90009-0009'),
('Matheus Rocha', 'matheus.rocha@email.com', '(11) 90010-0010'),
('Camila Barbosa', 'camila.barbosa@email.com', '(11) 90011-0011'),
('Bruno Martins', 'bruno.martins@email.com', '(11) 90012-0012'),
('Larissa Lima', 'larissa.lima@email.com', '(11) 90013-0013'),
('André Carvalho', 'andre.carvalho@email.com', '(11) 90014-0014'),
('Letícia Ramos', 'leticia.ramos@email.com', '(11) 90015-0015'),
('Felipe Gonçalves', 'felipe.goncalves@email.com', '(11) 90016-0016'),
('Isabela Souza', 'isabela.souza@email.com', '(11) 90017-0017'),
('Thiago Araújo', 'thiago.araujo@email.com', '(11) 90018-0018'),
('Rafaela Duarte', 'rafaela.duarte@email.com', '(11) 90019-0019'),
('Marcelo Ferreira', 'marcelo.ferreira@email.com', '(11) 90020-0020'),
('Bianca Cruz', 'bianca.cruz@email.com', '(11) 90021-0021'),
('Daniel Borges', 'daniel.borges@email.com', '(11) 90022-0022'),
('Luana Nunes', 'luana.nunes@email.com', '(11) 90023-0023'),
('Gustavo Vieira', 'gustavo.vieira@email.com', '(11) 90024-0024'),
('Nicole Pereira', 'nicole.pereira@email.com', '(11) 90025-0025'),
('Rafael Correia', 'rafael.correia@email.com', '(11) 90026-0026'),
('Patrícia Monteiro', 'patricia.monteiro@email.com', '(11) 90027-0027'),
('Victor Henrique', 'victor.henrique@email.com', '(11) 90028-0028'),
('Alice Figueiredo', 'alice.figueiredo@email.com', '(11) 90029-0029'),
('Pedro Lucas', 'pedro.lucas@email.com', '(11) 90030-0030'),
('Juliana Santana', 'juliana.santana@email.com', '(11) 90031-0031'),
('Diego Andrade', 'diego.andrade@email.com', '(11) 90032-0032'),
('Renata Batista', 'renata.batista@email.com', '(11) 90033-0033'),
('Caio Moreira', 'caio.moreira@email.com', '(11) 90034-0034'),
('Sabrina Ribeiro', 'sabrina.ribeiro@email.com', '(11) 90035-0035'),
('Fernando Teixeira', 'fernando.teixeira@email.com', '(11) 90036-0036'),
('Elaine Cardoso', 'elaine.cardoso@email.com', '(11) 90037-0037'),
('Vinícius Prado', 'vinicius.prado@email.com', '(11) 90038-0038'),
('Manuela Melo', 'manuela.melo@email.com', '(11) 90039-0039'),
('Eduardo Lima', 'eduardo.lima@email.com', '(11) 90040-0040'),
('Livia Martins', 'livia.martins@email.com', '(11) 90041-0041'),
('Rodrigo Barros', 'rodrigo.barros@email.com', '(11) 90042-0042'),
('Vanessa Pires', 'vanessa.pires@email.com', '(11) 90043-0043'),
('Samuel Queiroz', 'samuel.queiroz@email.com', '(11) 90044-0044'),
('Carolina Matos', 'carolina.matos@email.com', '(11) 90045-0045'),
('Leandro Coelho', 'leandro.coelho@email.com', '(11) 90046-0046'),
('Aline Silva', 'aline.silva@email.com', '(11) 90047-0047'),
('Henrique Sampaio', 'henrique.sampaio@email.com', '(11) 90048-0048'),
('Paula Dias', 'paula.dias@email.com', '(11) 90049-0049'),
('Maurício Farias', 'mauricio.farias@email.com', '(11) 90050-0050');

INSERT INTO cursos (nome, codigo, descricao) VALUES
('Desenvolvimento Web', 'WEB101', 'Curso de introdução ao desenvolvimento web.'),
('Inteligência Artificial', 'AI202', 'Curso introdutório sobre inteligência artificial.'),
('Banco de Dados SQL', 'DB303', 'Curso de gerenciamento de banco de dados relacionais.'),
('Desenvolvimento Mobile', 'MOB404', 'Curso sobre criação de aplicativos móveis.'),
('Segurança da Informação', 'SEC505', 'Curso sobre práticas de segurança na tecnologia.');

-- Matricular alunos em 5 turmas (cada turma com 10 alunos)
INSERT INTO matriculas (aluno_id, curso_id) VALUES
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1);

-- Turma 2: Curso de Inteligência Artificial (AI202)
INSERT INTO matriculas (aluno_id, curso_id) VALUES
(11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2);

-- Turma 3: Curso de Banco de Dados SQL (DB303)
INSERT INTO matriculas (aluno_id, curso_id) VALUES
(21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3), (28, 3), (29, 3), (30, 3);

-- Turma 4: Curso de Desenvolvimento Mobile (MOB404)
INSERT INTO matriculas (aluno_id, curso_id) VALUES
(31, 4), (32, 4), (33, 4), (34, 4), (35, 4), (36, 4), (37, 4), (38, 4), (39, 4), (40, 4);