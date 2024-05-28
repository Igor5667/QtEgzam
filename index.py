import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QComboBox, QButtonGroup
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

exampleText = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Corrupti magni facere fuga aliquid error iure tenetur. Cum quae aliquid, id accusamus beatae quibusdam tempora maiores obcaecati omnis culpa, quas voluptatum dolore vel eaque vero velit illo labore iusto? Ratione blanditiis natus a nam sapiente eveniet."

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        self.window = loader.load(r"c:\Users\igido\Desktop\MyProjects\QtEgzam\untitled.ui", self)
        self.setWindowTitle("Egzam1")

        #connect signals
        self.window.saveNoteButtton.clicked.connect(self.saveNote)

        #initialize button groups
        self.poczGroup = QButtonGroup(self)
        self.poczGroup.addButton(self.window.bdPoczRadio)
        self.poczGroup.addButton(self.window.dPoczRadio)
        self.poczGroup.addButton(self.window.uPoczRadio)
        self.poczGroup.addButton(self.window.zPoczRadio)

        self.konGroup = QButtonGroup(self)
        self.konGroup.addButton(self.window.bdKonRadio)
        self.konGroup.addButton(self.window.dKonRadio)
        self.konGroup.addButton(self.window.uKonRadio)
        self.konGroup.addButton(self.window.zKonRadio)
        self.show()

    @Slot()
    def saveNote(self):



        note = QLabel(f"""
data: {self.window.calendarWidget.selectedDate().toString("yyyy-MM-dd")}
opis dnia:
{self.window.textEdit.toPlainText()}
poczucie na początku: {self.poczGroup.checkedButton().text()}
poczucie na koncu: {self.konGroup.checkedButton().text()}
aktywnosc w ciagu dnia: {self.window.comboBox.currentText()}
""")
        note.setWordWrap(True)
        note.setFixedSize(200,200)
        self.window.scrollAreaLayout.addWidget(note)

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())