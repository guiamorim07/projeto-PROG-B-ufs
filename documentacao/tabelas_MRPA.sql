
DROP TABLE IF EXISTS laudo, medicao, exame, template_laudo, status_medicao, medico, paciente CASCADE;

CREATE TABLE paciente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo VARCHAR(1),
    cpf VARCHAR(11) UNIQUE
);

CREATE TABLE medico (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    crm VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE status_medicao (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(30) NOT NULL
);

CREATE TABLE exame (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER NOT NULL,
    medico_id INTEGER NOT NULL,
    data_exame DATE NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    FOREIGN KEY (medico_id) REFERENCES medico(id)
);

CREATE TABLE medicao (
    id SERIAL PRIMARY KEY,
    exame_id INTEGER NOT NULL,
    pressao_sistolica INTEGER NOT NULL,
    pressao_diastolica INTEGER NOT NULL,
    frequencia_cardiaca INTEGER,
    classificacao_pa VARCHAR(50),
    status_medicao_id INTEGER NOT NULL,
    FOREIGN KEY (exame_id) REFERENCES exame(id),
    FOREIGN KEY (status_medicao_id) REFERENCES status_medicao(id)
);

CREATE TABLE template_laudo (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    conteudo TEXT NOT NULL,
    padrao BOOLEAN DEFAULT FALSE
);

CREATE TABLE laudo (
    id SERIAL PRIMARY KEY,
    exame_id INTEGER NOT NULL,
    template_laudo_id INTEGER NOT NULL,
    data_geracao TIMESTAMP NOT NULL,
    caminho_pdf VARCHAR(255),
    FOREIGN KEY (exame_id) REFERENCES exame(id),
    FOREIGN KEY (template_laudo_id) REFERENCES template_laudo(id)
);