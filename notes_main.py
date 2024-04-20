from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QRadioButton, QListWidget, QInputDialog, QFormLayout 
import json
app = QApplication([])
notes = {
    'Добро пожаловать!' : {
        'текст' : 'Это самое лучшее приложение для заметок в мире!', 
        'теги' : ['добро', 'инструкция']
    }
}
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)
btn_s = QPushButton('Сохранить заметку')
btn_d = QPushButton('Удалить заметку')
btn_c = QPushButton('Создать заметку')
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
btn_add = QPushButton('Добавить к заметке')
btn_del = QPushButton('Открепить от заметки')
btn_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(btn_c)
row_1.addWidget(btn_d)
row_2 = QVBoxLayout()
row_2.addWidget(btn_s)
col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(btn_add)
row_3.addWidget(btn_del)
row_4 = QHBoxLayout()
row_4.addWidget(btn_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки: ')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def show_noteI():
    key = list_notes.selectedItems()[0]/text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print('Тег для удаления не выбран!')

def search_tag():
    print(btn_search.text())
    tag = field_tag.text()
    if btn_search.text() == 'Искать заметку по тегу' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        btn_search.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(btn_search.text())
    elif btn_search.text() == 'Сбросить поиск':
        field_tag.clear()
        field_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        btn_search.setText('Искать заметку по тегу')
        print(btn_search.text())
    else:
        pass

btn_c.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
btn_s.clicked.connect(save_note)
btn_d.clicked.connect(del_note)
btn_add.clicked.connect(add_tag)
btn_del.clicked.connect(del_tag)
btn_search.clicked.connect(search_tag)

notes_win.show()
with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)

app.exec_()