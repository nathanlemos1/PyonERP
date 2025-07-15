CREATE DATABASE IF NOT EXISTS pyonerp;
USE pyonerp;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARBINARY(255) NOT NULL,
    papel INT NOT NULL
);

CREATE TABLE papeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE permissoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE papel_permissao (
    papel_id INT,
    permissao_id INT,
    PRIMARY KEY (papel_id, permissao_id),
    FOREIGN KEY (papel_id) REFERENCES papeis(id),
    FOREIGN KEY (permissao_id) REFERENCES permissoes(id)
);

INSERT INTO papeis (nome) VALUES ('admin'), ('usuario');
INSERT INTO permissoes (nome) VALUES ('usuario_ver'), ('usuario_criar');
INSERT INTO papel_permissao (papel_id, permissao_id) VALUES 
(1, 1), (1, 2);

--- INSERT INTO usuarios (nome, email, senha, papel) 
--- VALUES ('Admin', 'admin@pyonerp.com', 
---        '$2b$12$suZwjVe6LXdENt/TVfdE3eBu89T77bQWyW7PgQf3lK/RqrdqSnsty', 1)

--- INSERT INTO usuarios (nome, email, senha, papel)
--- VALUES ('Admin', 'usuario1@pyonerp.com', '$2b$12$vvkkMyrmFE5XwcNqNnefV.oRxAPWbRgZ.kQ/VVvl0T7CnIQ2fhnSq', 2);