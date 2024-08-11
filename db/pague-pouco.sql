CREATE SCHEMA IF NOT EXISTS `pague_pouco` DEFAULT CHARACTER SET utf8 ;
USE `pague_pouco`;

CREATE TABLE IF NOT EXISTS `Cliente`(
  `idCliente` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nomeCliente` VARCHAR(100) NOT NULL,
  `dtNasc` DATE,
  `telefone` CHAR(11) NOT NULL,
  `cpf` CHAR(11),
  `endereco` VARCHAR(200)
  );
  
CREATE TABLE IF NOT EXISTS `Farmaceutico` (
  `idFarmaceutico` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nomeFarmaceutico` VARCHAR(45) NOT NULL,
  `crf` CHAR(5) NOT NULL,
  `localRegistro` CHAR(2) NOT NULL,
  `telefone` CHAR(11) NOT NULL
  );

CREATE TABLE IF NOT EXISTS `Venda` (
  `idVenda` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `DataVenda` DATETIME NOT NULL,
  `idCliente` INT NOT NULL,
  `idFarmaceutico` INT NOT NULL,
  FOREIGN KEY(`idCliente`) REFERENCES `Cliente`(`idCliente`) ON DELETE CASCADE,
  FOREIGN KEY(`idFarmaceutico`) REFERENCES `Farmaceutico`(`idFarmaceutico`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `Produto` (
  `idProduto` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nomeProduto` VARCHAR(100) NOT NULL,
  `dtValidade` DATE NOT NULL,
  `qtdeEstoque` SMALLINT NOT NULL,
  `valorVenda` FLOAT NOT NULL,
  `composto` VARCHAR(45) NOT NULL,
  `valorCusto` FLOAT
);

CREATE TABLE IF NOT EXISTS `VendaProduto` (
  `idVendaProduto` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `qtdeVendida` TINYINT NULL,
  `idProduto` INT NOT NULL,
  `idVenda` INT NOT NULL,
  FOREIGN KEY(`idProduto`) REFERENCES `Produto`(`idProduto`) ON DELETE CASCADE,
  FOREIGN KEY(`idVenda`) REFERENCES `Venda`(`idVenda`) ON DELETE CASCADE
);