create database loja_simples; -- cria o banco de dados / schema

use loja_simples; -- seleciona o BD para o uso

-- cria a tabela eventos de acordo com o modelo logico
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    data_nasc DATE,
    sexo ENUM('M','F'),
    email VARCHAR(100),
    telefone VARCHAR(11)
);


CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100),
    descricao VARCHAR(150),
    data_cadastro DATE,
    preco_produto DECIMAL(10,2),
    estoque INT NOT NULL
);

CREATE TABLE venda (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    data_venda DATE NOT NULL,
    valor_venda DECIMAL(10,2) NOT NULL,
    dia_horario DATETIME NOT NULL,

    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

