-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema geektext_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema geektext_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `geektext_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `geektext_db` ;

-- -----------------------------------------------------
-- Table `geektext_db`.`author`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`author` (
  `author_id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(100) NULL DEFAULT NULL,
  `lastname` VARCHAR(100) NULL DEFAULT NULL,
  `bio` VARCHAR(255) NULL DEFAULT NULL,
  `pub` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`author_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `geektext_db`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`books` (
  `isbn` VARCHAR(17) NOT NULL,
  `title` VARCHAR(255) NULL DEFAULT NULL,
  `descp` VARCHAR(255) NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NULL DEFAULT NULL,
  `author_id` INT NULL DEFAULT NULL,
  `genre` VARCHAR(100) NULL DEFAULT NULL,
  `pub` VARCHAR(100) NULL DEFAULT NULL,
  `year` INT NULL DEFAULT NULL,
  `copiessold` INT NULL DEFAULT NULL,
  PRIMARY KEY (`isbn`),
  INDEX `authorid_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `author_id`
    FOREIGN KEY (`author_id`)
    REFERENCES `geektext_db`.`author` (`author_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `geektext_db`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `geektext_db`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`ratings` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NULL DEFAULT NULL,
  `comment` VARCHAR(255) NULL DEFAULT NULL,
  `rating` INT NOT NULL,
  `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `isbn` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`rating_id`),
  INDEX `user_id1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id1`
    FOREIGN KEY (`user_id`)
    REFERENCES `geektext_db`.`user` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `geektext_db`.`shoppingcart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`shoppingcart` (
  `cart_id` INT NOT NULL AUTO_INCREMENT,
  `isbn` VARCHAR(13) NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  INDEX `isbn_idx` (`isbn` ASC) VISIBLE,
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `isbn`
    FOREIGN KEY (`isbn`)
    REFERENCES `geektext_db`.`books` (`isbn`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `geektext_db`.`user` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `geektext_db`.`wishlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geektext_db`.`wishlist` (
  `list_id` INT NOT NULL AUTO_INCREMENT,
  `isbn` VARCHAR(13) NULL DEFAULT NULL,
  `user_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`list_id`),
  INDEX `isbn1_idx` (`isbn` ASC) VISIBLE,
  INDEX `user_id2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `isbn1`
    FOREIGN KEY (`isbn`)
    REFERENCES `geektext_db`.`books` (`isbn`),
  CONSTRAINT `user_id2`
    FOREIGN KEY (`user_id`)
    REFERENCES `geektext_db`.`user` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
