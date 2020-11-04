from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from libreria_20B.libreria import Libreria
from libreria_20B.libro import Libro

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.libreria = Libreria()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.monstrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_titulo)

    @Slot()
    def buscar_titulo(self):
        titulo = self.ui.buscar_lineEdit.text()
        encontrado = False
        for libro in self.libreria:
            if titulo == libro.titulo:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                titulo_widget = QTableWidgetItem(libro.titulo)
                autor_widget = QTableWidgetItem(libro.autor)
                publicado_widget = QTableWidgetItem(str(libro.publicado))
                editorial_widget = QTableWidgetItem(libro.editorial)

                self.ui.tabla.setItem(0, 0, titulo_widget)
                self.ui.tabla.setItem(0, 1, autor_widget)
                self.ui.tabla.setItem(0, 2, publicado_widget)
                self.ui.tabla.setItem(0, 3, editorial_widget)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'El libro con título "{titulo}" no fue encontrado'
            )
        


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(4)
        headers = ["Título", "Autor", "Publicado", "Editorial"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.libreria))

        row = 0
        for libro in self.libreria:
            titulo_widget = QTableWidgetItem(libro.titulo)
            autor_widget = QTableWidgetItem(libro.autor)
            publicado_widget = QTableWidgetItem(str(libro.publicado))
            editorial_widget = QTableWidgetItem(libro.editorial)

            self.ui.tabla.setItem(row, 0, titulo_widget)
            self.ui.tabla.setItem(row, 1, autor_widget)
            self.ui.tabla.setItem(row, 2, publicado_widget)
            self.ui.tabla.setItem(row, 3, editorial_widget)

            row += 1

    @Slot()
    def action_abrir_archivo(self):
        # print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.libreria.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.libreria.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        # self.libreria.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.libreria))

    @Slot()
    def click_agregar(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_final(libro)

        # print(titulo, autor, publicado, editorial)
        # self.ui.salida.insertPlainText(titulo + autor + str(publicado) + editorial)
    @Slot()
    def click_agregar_inicio(self):
        titulo = self.ui.titulo_lineEdit.text()
        autor = self.ui.autor_lineEdit.text()
        publicado = self.ui.publicado_spinBox.value()
        editorial = self.ui.editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_inicio(libro)