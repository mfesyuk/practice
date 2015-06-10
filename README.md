Тема проекта:

Распознавание кондуитов

I.	Формулировка задачи.

Распознать табличные значения кондуита по фотографии и записать их в файл.

II.	Входные/выходные данные.

1)	Входные данные: изображение кондуита в формате jpg и текстовый файл «groupeng.txt» с именами и фамилиями учащихся.

2)	Выходные данные: файл формата csv с именами и фамилиями учащихся и задачами, решенными данными участниками соответственно. Под фамилией каждого человека расположены плюсы (если в кондуите на этом месте стоял +) и минусы (если в кондуите на этом месте ничего не было) в том порядке, в котором они были изображены в таблице.

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

4)	В одной папке с программой должен находиться файл с названием «groupeng.txt», в котором должны быть записаны каждые с новой строчки имена и фамилии учащихся на английском языке

5)	Кондуит должен удовлетворять следующим условиям:

a)	9 столбцов и 11 строчек:

•	в первой строчке со второго столбца по девятый записаны номера задач с 1 по 8

•	в первом столбце со второй строчки по одиннадцатую записаны фамилии и имена учеников

•	в первом столбце в первой строчке пусто

•	если ученик из списка в первом столбце сдал задачу, то на пересечении строчки, содержащей его фамилию и имя, и столбца, содержащего номер задачи, стоит +

b)	по углам таблицы с внешней стороны находятся черные квадраты

c)	соотношения размеров таблицы должно быть следующим:

•	ширина к длине относится как 11:39

•	ширина строк одинаковая

•	первый столбец по длине относится ко всей длине таблицы как 9:39

•	столбцы со второго по девятый равны по длине и относятся к общей длине таблицы как 5:52

•	длины сторон черных квадратов по углам таблицы равны и относятся к общей ширине таблицы как 1:11

IV.	Описание кода.

Программа поделена на несколько блоков, каждый из которых выполняет определенные функции, описываемые ниже:

1)	Загрузка изображения (4-5 строчки)

2)	Обработка изображения, а именно изменения размера и бинаризация (7-19 строчки)

3)	Создание двумерного массива, где каждому 0 соответствует белый пиксель на изображении, а каждой 1 – черный (21-26 
строчки)

4)	Нахождение четырех черных квадратов, расположенных по углам таблицы, с помощью уже созданного двумерного массива (28-134 строчки)

5)	Произведение перспективной трансформации изображения с целью выравнивания таблицы по ее углам, найденным в предыдущем пункте, углы таблицы располагаются ровно по углам полученного изображения (136-142 строчки)

6)	Создание нового двумерного массива по правилам, описанным в п.3 (144-149 строчки)

7)	Нахождение x-координат для вертикальных и y-координат для горизонтальных линий, разделяющих ячейки таблицы (152-184 строчки)

8)	Создание двумерного массива, состоящего из 10 строчек по количеству учеников и 8 столбцов по количеству задач и заполненного плюсами и минусами в соответствии с принятым на вход изображением (186-201 строчки)

9)	Считываение имен и фамилий учащихся из файла «groupeng.txt» и запись их в выходной файл «conduit.csv» вместе с + и – , записываемыми в соответствии с кондуитом, изображение которого было передано на вход программе (203-216 строчки)

V. Руководство пользователя.

1) загрузить фотографию кондуита в формате jpg в папку, содержащую данную программу

2) создать в этой же папке файл "groupeng.txt" с именами и фамилиями учащихся на английском языке (потом исправлю на русский), каждый ученик с новой строчки

3) установить программу Python 2.7.4, библиотеку Open CV 3.0.0

4) написать в cmd путь к папке, в которой содержится данная программа

5) в следующей строке в cmd написать C:\Python27\python.exe scantabl.py photo.jpg

6) после выполнения программы в папке появится файл "conduit.csv" с именами и фамилиями учащихся и + и - под ними в зависимомти от того, стоял ли плюс в соответствующей ячейке в кондуите на згружаемом изображении
