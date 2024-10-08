# Итоговая контрольная работа по блоку специализация.

## Задание

1. Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

2. Создать директорию, переместить файл туда.

3. Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

4. Установить и удалить deb-пакет с помощью dpkg.

5. Выложить историю команд в терминале ubuntu

6. Нарисовать диаграмму, в которой есть класс родительский класс, домашние
животные и вьючные животные, в составы которых в случае домашних
животных войдут классы: собаки, кошки, хомяки, а в класс вьючные животные
войдут: Лошади, верблюды и ослы).

7. В подключенном MySQL репозитории создать базу данных “Друзья
человека”

8. Создать таблицы с иерархией из диаграммы в БД

9. Заполнить низкоуровневые таблицы именами(животных), командами
которые они выполняют и датами рождения

10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.

11.Создать новую таблицу “молодые животные” в которую попадут все
животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
до месяца подсчитать возраст животных в новой таблице

12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
прошлую принадлежность к старым таблицам.

13.Создать класс с Инкапсуляцией методов и наследованием по диаграмме.

14. Написать программу, имитирующую работу реестра домашних животных.

## В программе должен быть реализован следующий функционал:

14.1 Завести новое животное

14.2 определять животное в правильный класс

14.3 увидеть список команд, которое выполняет животное

14.4 обучить животное новым командам

14.5 Реализовать навигацию по меню

15.Создайте класс Счетчик, у которого есть метод add(), увеличивающий̆
значение внутренней̆int переменной̆на 1 при нажатие “Завести новое
животное” Сделайте так, чтобы с объектом такого типа можно было работать в
блоке try-with-resources. Нужно бросить исключение, если работа с объектом
типа счетчик была не в ресурсном try и/или ресурс остался открыт. Значение
считать в ресурсе try, если при заведения животного заполнены все поля.


## Решение

### Создание файлов и наполнение их контентом
1. Откроем терминал.

2. Для создания файла Домашние животные и заполнения его содержимым выполним следующие команды:
```
    echo -e "Собаки\nКошки\nХомяки" > Домашние_животные.txt
```
3. Для создания файла Вьючные животные и заполнения его содержимым выполним такие команды:
```
    echo -e "Лошади\nВерблюды\nОслы" > Вьючные_животные.txt
 ```   
### Объединение файлов и просмотр содержимого
4. Для объединения файлов используем команду cat:
```
    cat Домашние_животные.txt Вьючные_животные.txt > Всех_животные.txt
```    
5. Чтобы просмотреть содержимое объединённого файла, выполним:
```
    cat Всех_животные.txt
 ```   
### Переименование файла и перемещение в новую директорию
6. Для переименования файла:
```
    mv Всех_животные.txt Друзья_человека.txt
 ```   
7. Создадим новую директорию:
```
    mkdir Мои_файлы
```    
8. Переместим файл в созданную директорию:
```
    mv Друзья_человека.txt Мои_файлы/
 ```   
### Подключение дополнительного репозитория MySQL и установка пакета
9. Добавим репозиторий MySQL:
```
    sudo apt-get install wget

    wget https://repo.mysql.com/mysql-apt-config_0.8.17-1_all.deb

    sudo dpkg -i mysql-apt-config_0.8.17-1_all.deb

    sudo apt-get update
```
10. Установим любой пакет из репозитория, например MySQL Server:
```
    sudo apt-get install mysql-server
 ```   
### Установка и удаление deb-пакета с помощью dpkg
11. Для установки пакета, например, htop, сначала скачайте его:
```
    wget http://mirrors.kernel.org/ubuntu/pool/universe/h/htop/htop_3.0.5-7build1_amd64.deb

    sudo dpkg -i htop_3.0.5-7build1_amd64.deb
  ```  
12. Для удаления пакета:
```
    sudo dpkg -r htop
```
### Сохранение истории команд
13. Чтобы сохранить историю команд в файл, выполните:
```
    history > история_команд.txt
```
### Диаграмма классов
Ниже представлена диаграмма классов для иерархии животных.

```
+--------------------+
| Животные     |
+--------------------+
     ||
     ||
+-------------------+   +------------------+
| Домашние животные |   | Вьючные животные |
+-------------------+   +------------------+
     ||               ||
 +------+-----+         +------+-----+
 |      |         |      |
+-------+  +-------+     +-------+  +-------+
| Собаки |  | Кошки |     | Лошади |  | Ослы |
+-------+  +-------+     +-------+  +-------+
      |
     +-------+
     | Хомяки |
     +-------+
```

### Создание базы данных и таблиц в MySQL
1. Создание базы данных “Друзья человека”:
```
      CREATE DATABASE Друзья_человека;
```
2. Создание таблиц с иерархией из диаграммы:
```
    USE Друзья_человека;

    CREATE TABLE Животные (
        id INT AUTO_INCREMENT PRIMARY KEY,
        название VARCHAR(50)
    );

    CREATE TABLE Домашние_животные (
        id INT AUTO_INCREMENT PRIMARY KEY,
        животное_id INT,
        название VARCHAR(50),
        FOREIGN KEY (животное_id) REFERENCES Животные(id)
    );

    CREATE TABLE Вьючные_животные (
        id INT AUTO_INCREMENT PRIMARY KEY,
        животное_id INT,
        название VARCHAR(50),
        FOREIGN KEY (животное_id) REFERENCES Животные(id)
    );

    CREATE TABLE Собаки (
        id INT AUTO_INCREMENT PRIMARY KEY,
        домашнее_животное_id INT,
        имя VARCHAR(50),
        команды TEXT,
        дата_рождения DATE,
        FOREIGN KEY (домашнее_животное_id) REFERENCES Домашние_животные(id)
    );

    CREATE TABLE Кошки (
        id INT AUTO_INCREMENT PRIMARY KEY,
        домашнее_животное_id INT,
        имя VARCHAR(50),
        команды TEXT,
        дата_рождения DATE,
        FOREIGN KEY (домашнее_животное_id) REFERENCES Домашние_животные(id)
    );

    CREATE TABLE Хомяки (
        id INT AUTO_INCREMENT PRIMARY KEY,
        домашнее_животное_id INT,
        имя VARCHAR(50),
        команды TEXT,
        дата_рождения DATE,
        FOREIGN KEY (домашнее_животное_id) REFERENCES Домашние_животные(id)
    );

    CREATE TABLE Лошади (
        id INT AUTO_INCREMENT PRIMARY KEY,
        вьючное_животное_id INT,
        имя VARCHAR(50),
        команды TEXT,
        дата_рождения DATE,
        FOREIGN KEY (вьючное_животное_id) REFERENCES Вьючные_животные(id)
    );

    CREATE TABLE Ослы (
        id INT AUTO_INCREMENT PRIMARY KEY,
        вьючное_животное_id INT,
        имя VARCHAR(50),
        команды TEXT,
        дата_рождения DATE,
        FOREIGN KEY (вьючное_животное_id) REFERENCES Вьючные_животные(id)
    );
```
3. Заполнение низкоуровневых таблиц:
```
    INSERT INTO Животные (название) VALUES ('Домашние животные'), ('Вьючные животные');

    INSERT INTO Домашние_животные (животное_id, название) VALUES 
    (1, 'Собаки'), 
    (1, 'Кошки'), 
    (1, 'Хомяки');

    INSERT INTO Вьючные_животные (животное_id, название) VALUES 
    (2, 'Лошади'), 
    (2, 'Ослы');

    -- Заполнение Собаки
    INSERT INTO Собаки (домашнее_животное_id, имя, команды, дата_рождения) VALUES 
    (1, 'Шарик', 'Сидеть, Лежать', '2023-01-15'), 
    (1, 'Бобик', 'Апорт, Фас', '2022-05-10');

    -- Заполнение Кошки
    INSERT INTO Кошки (домашнее_животное_id, имя, команды, дата_рождения) VALUES 
    (2, 'Мурка', 'Ко мне, Лапу', '2021-11-25'), 
    (2, 'Барсик', 'Ко мне', '2023-07-09');

    -- Заполнение Хомяки
    INSERT INTO Хомяки (домашнее_животное_id, имя, команды, дата_рождения) VALUES 
    (3, 'Хома', 'Кубарем', '2021-09-13');

    -- Заполнение Лошади
    INSERT INTO Лошади (вьючное_животное_id, имя, команды, дата_рождения) VALUES 
    (1, 'Буцефал', 'Вперёд', '2019-03-25'), 
    (1, 'Торнадо', 'Назад', '2020-12-12');

    -- Заполнение Ослы
    INSERT INTO Ослы (вьючное_животное_id, имя, команды, дата_рождения) VALUES 
    (2, 'Барон', 'Вперёд', '2020-04-22'), 
    (2, 'Тошка', 'Стоять', '2021-08-30');
```
4. Удаление верблюдов (верблюды отсутствуют в исходной таблице):
```
    -- Так как таблица верблюдов не была создана, этот шаг можно пропустить.
```
5. Объединение таблиц лошадей и ослов в одну таблицу:
```
    CREATE TABLE Лошади_и_Ослы AS 
    SELECT id, вьючное_животное_id, имя, команды, дата_рождения FROM Лошади 
    UNION 
    SELECT id, вьючное_животное_id, имя, команды, дата_рождения FROM Ослы;
```
6. Создание новой таблицы "молодые животные":
```
    CREATE TABLE Молодые_животные AS
    SELECT *, 
    TIMESTAMPDIFF(MONTH, дата_рождения, CURDATE()) AS возраст_в_месяцах
    FROM (
        SELECT id, имя, команды, дата_рождения, 'Собаки' AS вид FROM Собаки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Кошки' AS вид FROM Кошки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Хомяки' AS вид FROM Хомяки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Лошади' AS вид FROM Лошади UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Ослы' AS вид FROM Ослы
    ) AS все_животные
    WHERE дата_рождения BETWEEN CURDATE() - INTERVAL 3 YEAR AND CURDATE() - INTERVAL 1 YEAR;
```
7. Объединение всех таблиц в одну:
```
    CREATE TABLE Все_животные AS
    SELECT * FROM (
        SELECT id, имя, команды, дата_рождения, 'Собаки' AS вид FROM Собаки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Кошки' AS вид FROM Кошки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Хомяки' AS вид FROM Хомяки UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Лошади' AS вид FROM Лошади UNION ALL
        SELECT id, имя, команды, дата_рождения, 'Ослы' AS вид FROM Ослы
    ) AS все_животные;
```
### Написать программу, имитирующую работу реестра домашних животных.

Решение данной задачи и поставленных дополнительных условий можно найти в данном репозитории в папке Animals. Там находятся несколько файлов с кодами на языке Python. Папка предназначена для использования в качестве проекта PyCharm. Данная среда разработки доступна на любых платформах, однако код может быть запущен и без неё. В процессе написания программ я учёл все условия, в чём можно будет убедиться, обратившись к папке Animals.
