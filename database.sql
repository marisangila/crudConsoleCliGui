CREATE DATABASE filmes;

USE filmes;

CREATE TABLE filme(
    PK_filme INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_filme VARCHAR(45) NOT NULL,
    ano_lancamento_filme INT
);
