CREATE DATABASE db_feedback;
USE db_feedback;

CREATE TABLE tb_comentarios(
	cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    comentario TEXT NOT NULL,
    data_hora DATETIME NOT NULL
);