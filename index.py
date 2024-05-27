import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
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

        self.show()

    @Slot()
    def saveNote(self):
        note = QLabel(f"""
data: {self.window.calendarWidget.selectedDate().toString("yyyy-MM-dd")}
opis dnia:
{self.window.textEdit.toPlainText()}
""")
        note.setWordWrap(True)
        note.setFixedSize(200,200)
        self.window.scrollAreaLayout.addWidget(note)

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())