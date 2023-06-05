image-- MySQL Script generated by MySQL Workbench
-- Sun Aug 16 09:55:24 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema webhw
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema webhw
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `webhw` DEFAULT CHARACTER SET utf8 ;
USE `webhw` ;

-- -----------------------------------------------------
-- Table `webhw`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `webhw`.`user` ;

CREATE TABLE IF NOT EXISTS `webhw`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
   `name` VARCHAR(45) NOT NULL, 
  `email` VARCHAR(45) NULL DEFAULT NULL,
   `phone` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(45) NULL DEFAULT NULL,
  `create_time` datetime,
  PRIMARY KEY (`iduser`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `webhw`.`item`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `webhw`.`item` ;

CREATE TABLE IF NOT EXISTS `webhw`.`item` (
  `iditem` INT NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `price` DECIMAL(5) NULL DEFAULT NULL,
  `image` TEXT,
  `image2` TEXT,
  `image3` TEXT,
  `image4` TEXT,
  `species` int,
  `desc` VARCHAR(45) NULL DEFAULT NULL,
  `time` datetime,
  PRIMARY KEY (`iditem`))
ENGINE = InnoDB;

-- ----------------------------------------------------
-- Table `webhw`.`order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `webhw`.`order` ;

CREATE TABLE IF NOT EXISTS `webhw`.`order` (
  `idorder` INT NOT NULL,
  `iduser` INT NULL DEFAULT NULL,
  `iditem` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idorder`),
  INDEX `orderitem_idx` (`iditem` ASC) VISIBLE,
  INDEX `itemuser_idx` (`iduser` ASC) VISIBLE,
  CONSTRAINT `orderitem`
    FOREIGN KEY (`iditem`)
    REFERENCES `webhw`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `orderuser`
    FOREIGN KEY (`iduser`)
    REFERENCES `webhw`.`user` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
INSERT INTO `webhw`.`order` VALUES (1,1,1);
CREATE TABLE `webhw`.`order_item` (
        _id INTEGER NOT NULL AUTO_INCREMENT,
        orderid INTEGER,
        itemid INTEGER,
        count FLOAT NOT NULL,
        PRIMARY KEY (_id),
        FOREIGN KEY(orderid) REFERENCES `order` (idorder) ON DELETE cascade,
        FOREIGN KEY(itemid) REFERENCES item (iditem)
)ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `webhw`.`cart`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `webhw`.`cart` ;

CREATE TABLE IF NOT EXISTS `webhw`.`cart` (
  `idorder` INT NOT NULL,
  `iduser` INT NULL DEFAULT NULL,
  `iditem` INT NULL DEFAULT NULL,
  `count` DECIMAL(2) NULL DEFAULT NULL,
  PRIMARY KEY (`idorder`),
  INDEX `orderitem_idx` (`iditem` ASC) VISIBLE,
  INDEX `itemuser_idx` (`iduser` ASC) VISIBLE,
  CONSTRAINT `cartitem`
    FOREIGN KEY (`iditem`)
    REFERENCES `webhw`.`item` (`iditem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `cartuser`
    FOREIGN KEY (`iduser`)
    REFERENCES `webhw`.`user` (`iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `webhw`.`image`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `webhw`.`image` ;

CREATE TABLE IF NOT EXISTS `webhw`.`image` (
  `idimage` INT NOT NULL,
  `url` VARCHAR(255) NULL DEFAULT NULL,
  `iditem` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idimage`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

