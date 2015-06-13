Тема проекта:

Распознавание кондуитов

I.	Формулировка задачи.

Распознать табличные значения кондуита по фотографии и создать аналогичный кондуит в Excel.

II.	Входные/выходные данные.

1)	Входные данные: изображение кондуита в формате jpg и текстовый файл «groups.txt», которрый состоит из определенного числа групп учащихся по 10 человек (перед списком каждой группы должен в отдельной строке стоять ее номер, а под ним уже должны быть написаны фамилии и имена учащихся данной группы с новой строчки каждый в том порядке, в котором они находятся в распознваемом кондуите)

2)	Выходные данные: таблица в Excel полностью аналогичная той, которая была дана на вход в качестве изображения.

III.	Требования к программе.

1)	На устройстве, использующем данную программу, должны быть установлены следующие программы:

a)	Python 2.7.4

b)	OpenCV 3.0.0

c)	NumPy 1.9.2

2)	Фотография должна быть сделана при следующих условиях:

a)	Лист с кондуитом правильно ориентирован по отношению к камере

b)	Угол наклона камеры по отношению к листу с кондуитом не превышает 30 градусов

c)	Освещение в комнате, где производится фотографирование, равномерное (теней на фотографии не должно быть видно)

3)	Изображение должно быть сохранено в той же папке, что и программа, в формате jpg

4)	В одной папке с программой должен находиться файл с названием «groups.txt»

5)	Кондуит должен удовлетворять следующим условиям:

a)	9 столбцов и 11 строчек:

•	в первой строчке со второго столбца по девятый записаны номера задач с 1 по 8

•	в первом столбце со второй строчки по одиннадцатую записаны фамилии и имена учеников

•	в первом столбце в первой строчке число вертикальных линий (можно проводить ручкой), параллельных линиям сетки, должно соответствовать номеру группы в файле "groups.txt"

•	если ученик из списка в первом столбце сдал задачу, то на пересечении строчки, содержащей его фамилию и имя, и столбца, содержащего номер задачи, стоит +

b)	по углам таблицы с внешней стороны находятся черные квадраты

c)	соотношения размеров таблицы должно быть следующим:

•	ширина к длине относится как 11:39

•	ширина строк одинаковая

•	первый столбец по длине относится ко всей длине таблицы как 9:39

•	столбцы со второго по девятый равны по длине и относятся к общей длине таблицы как 5:52

•	длины сторон черных квадратов по углам таблицы равны и относятся к общей ширине таблицы как 1:11

6) данные в таблицу должны заноситься черной (желательно гелевой) ручкой

IV.	Описание кода.

Программа поделена на несколько блоков, каждый из которых выполняет определенные функции, описываемые ниже:

1)	Загрузка изображения (5-6 строчки)

2)	Обработка изображения, а именно изменения размера и бинаризация (7-21 строчки)

3)	Создание двумерного массива, где каждому 0 соответствует белый пиксель на изображении, а каждой 1 – черный (23-28 
строчки)

4)	Нахождение четырех черных квадратов, расположенных по углам таблицы, с помощью уже созданного двумерного массива (30-137 строчки)

5)	Произведение перспективной трансформации изображения с целью выравнивания таблицы по ее углам, найденным в предыдущем пункте, углы таблицы располагаются ровно по углам полученного изображения (139-146 строчки)

6)	Создание нового двумерного массива по правилам, описанным в п.3 (148-153 строчки)

7)	Нахождение x-координат для вертикальных и y-координат для горизонтальных линий, разделяющих ячейки таблицы (155-189 строчки)

8)	Создание двумерного массива, состоящего из 10 строчек по количеству учеников и 8 столбцов по количеству задач и заполненного плюсами и минусами в соответствии с принятым на вход изображением (191-206 строчки)

9) Нахождение номера группы по количеству проведенных вертикальных линий в отведенном для этого поле (208-220 строчки)

10)	Считываение имен и фамилий учащихся из файла «groups.txt» и запись их в выходной файл «conduit.csv» вместе с + и – , записываемыми в соответствии с кондуитом, изображение которого было передано на вход программе (222-238 строчки)

V. Руководство пользователя.

1) загрузить фотографию кондуита в формате jpg в папку, содержащую данную программу

2) создать в этой же папке файл "groups.txt" с именами и фамилиями учащихся, каждый ученик с новой строчки

3) установить программу Python 2.7.4, библиотеку Open CV 3.0.0 и NumPy 1.9.2

4) написать в cmd путь к папке, в которой содержится данная программа

5) в следующей строке в cmd написать C:\Python27\python.exe scantabl.py photo.jpg 

6) после выполнения программы в папке появится файл "conduit.csv" с кондуитом, аналогичным тому, чье изображение было передано на вход
