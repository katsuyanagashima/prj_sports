CREATE DATABASE IF NOT EXISTS prj_sports CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'kyodo'@'%' IDENTIFIED BY 'kyodo1234';
GRANT ALL PRIVILEGES ON prj_sports.* TO 'kyodo'@'%';

FLUSH PRIVILEGES;
