# BSU_7sem_Database
## Exchanges reference
1. Exchange Id (integer)
2. Exchange Name (text)
3. Formation Date (date)
4. Location (text)
5. Revenue (float)
## Companies reference:
1. Company Id (integer)
2. Company Name (text)
3. Formation Date (date)
4. Exchange Traded (reference to Exchanges)
5. Employees Number (integer)

Создание базы данных, а также добавление туда первых данных можно увидеть в файле step2_create_table_add_values.txt. Сейчас продемонстрирую то, как работает вебсайт. Запустив скрипт, мы попадаем на главную страницу:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/33881042-af44-4de8-abc2-cfcbd7d2461a)

Нажав на кнопку Companies в меню слева, мы попадаем на страницу, где отображается таблица companies, а также вспомогательные блоки, позволяющие производить некоторые операции над данной таблицей. Далее будут продемонстрированы данные операции.
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/5ca2b84c-7da4-43b1-bd16-2df01000a977)

Если мы хотим удалить строку, то нужно выбрать опцию delete напротив неё, нажать на кнопку Edit data внизу и обновить страницу. Строка будет удалена:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/fccb62c2-cd25-4488-a4ef-6615b5b76d87)
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/e9a09b9f-bcd1-41ea-ab84-28082f3c9b86)

Сортировка доступна как по дате, так и по остальным атрибутам (на первом фото -- сортировка по дате, на втором -- по числу сотрудников):
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/ccb4f870-897e-491d-b161-260dcf0cb90f)
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/4a4a8218-1b90-4fd1-80f5-268fb3fa0c02)

Данные в таблице можно изменять путём ввода нового значения в нужное поле и нажатия кнопки Edit data (например, изменим число сотрудников в Transocean Ltd с 6601 на 6602):
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/06dbf9b1-e93d-4219-bffc-50efefa06677)

Также есть возможность изменить Exchange, на которой торгуются акции компании. Для этого нужно выбрать опцию change_exchange напротив соответствующей компании, выбрать внизу Exchange из выпадающего списка (содержащего все используемые в таблице Exchange БЕЗ ПОВТОРЕНИЙ) и нажать кнопку change (например, изменим Exchange для компании ZTE с SSE на NYSE). Как было:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/ff453fd5-8b66-40e1-9797-b46b18b0ed16)
Что нужно сделать, чтобы изменить Exchange:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/136b33c7-abb5-4a56-b5b3-22cd5db1b566)
Как стало:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/2c6cee7a-6043-4588-9504-83aec0d18893)

Также есть возможность добавить новые данные, введя нужные данные и нажав кнопку Add data:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/d1e96324-d8de-45d9-9088-e4ee491dafe6)

Кстати, изменять даты можно с помощью удобного всплывающего календаря:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/02ab4e87-b9a9-41b0-a018-a5740d1d77fa)

Добавили две новые компании: Yandex и EPAM:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/36a0b992-14eb-4a88-b7d6-2cbe608faca4)

Вот так выглядит вкладка Exchanges:
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/ee288d3a-ecef-4ebd-b453-35d85f266e1a)
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/84d9683a-9b4b-4b7c-959b-26bd438513dc)

Функционал: можно точно так же изменять данные, а так же добавлять новые (принцип тот же). Единственное, что для атрибута Exchage size значение можно выбирать (как при изменении данных, так и при добавлении новых) из всплывающего списка вариантов (1, 2, 3):
![image](https://github.com/nikitastruhalsky/BSU_7sem_Database/assets/70744513/e83d5c5f-b7ba-48f4-9bd4-e217ab2ce6b5)

На этом всё!
