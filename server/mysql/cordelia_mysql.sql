DROP DATABASE IF EXISTS `cordelia_courses`;
CREATE DATABASE `cordelia_courses`;
USE `cordelia_courses`;

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
    `id` VARCHAR(70) NOT NULL PRIMARY KEY,
    `name` VARCHAR(70) NOT NULL,
    `last_name` VARCHAR(70) NOT NULL,
    `google_code` VARCHAR(100),
    `password` VARCHAR(100),
    `email` VARCHAR(120) NOT NULL,
    `last_item_check` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `description` VARCHAR(255) NOT NULL,
    `teacher_name` VARCHAR(120) NOT NULL,
    `course_data` VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `accesses`;
CREATE TABLE `accesses` (
    `product_id` INT NOT NULL PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `course_id` INT UNSIGNED NOT NULL,
    CONSTRAINT `fk_course_id` FOREIGN KEY (`course_id`) REFERENCES `courses`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `purchases`;
CREATE TABLE `purchases` (
    `customer_id` VARCHAR(70) NOT NULL,
    `access_id` INT NOT NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `purchase_id` VARCHAR(100) GENERATED ALWAYS AS (CONCAT(`customer_id`, `access_id`)) STORED,
    CONSTRAINT `fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_access_id` FOREIGN KEY (`access_id`) REFERENCES `accesses` (`product_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `opinions`;
CREATE TABLE `opinions` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `customer_id` VARCHAR(70) NOT NULL,
    `course_id` INT UNSIGNED NOT NULL,
    `class_id` VARCHAR(10) NOT NULL,
    `username` VARCHAR(70) NOT NULL,
    `body` VARCHAR(255) NOT NULL,
    `isodate` VARCHAR(255) NOT NULL,
    CONSTRAINT `fk_customer_id_opinions` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_course_id_opinions` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



/* GET COURSES BOUGHT BY A CUSTOMER BY CUSTOMER EMAIL */
-- SELECT * FROM `courses` WHERE `id` IN (SELECT `accesses`.`course_id` FROM `purchases`, `accesses` WHERE `accesses`.`product_id`=`purchases`.`access_id` AND `purchases`.`customer_id`=(SELECT `id` FROM `customers` WHERE `email`='theronin115@gmail.com'));

/* 
    INSERTING INITIAL DATA
 */


INSERT INTO `courses`(`id`, `name`, `description`, `teacher_name`, `course_data`) VALUES (1, 'Serie Tendencias O/I 2022', 'Curso donde aprenderás las tendencias de la temporada actual, para sentirte actualizada y a la moda', 'Cordelia Ruiz', './entitys_data/courses/st_io_2022');

INSERT INTO `accesses`(`product_id`, `name`, `course_id`) VALUES (0, 'special-access', 1);
INSERT INTO `accesses`(`product_id`, `name`, `course_id`) VALUES (25230, 'Acceso limitado a la serie Tendencias O/I 2022', 1);
INSERT INTO `accesses`(`product_id`, `name`, `course_id`) VALUES (25229, 'Acceso ilimitado a la serie Tendencias O/I 2022', 1);
