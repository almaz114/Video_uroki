import sys
import os
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

main_path = "D:\\Видео уроки\\"
path_1 = "D:\\Видео уроки\\1 Видео по сборке электробусов"  # путь к Раздел 1

# Установите свой путь vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv                          # !!!

path_2 = "C:\\Users\\Almaz\\PycharmProjects\\Video_Player\\movies"  # путь к Разделу 2   # !!! +++
path_3 = "C:\\Users\\Almaz\\PycharmProjects\\Video_Player"  # путь к Разделу 3

path_1_1 = ""               # пути к папкам подраздела 1
path_1_2 = ""
path_1_3 = ""
path_1_4 = ""
path_1_5 = ""
xxx = "I:\oldje"

path_2_1 = ""               # пути к папкам подраздела 2
path_2_2 = ""
path_2_3 = ""
path_2_4 = ""
path_2_5 = ""


def hhmmss(ms):
    # s = 1000
    # m = 60000
    # h = 360000
    s = round(ms / 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Раздел 1')
        self.setMinimumWidth(930)
        self.setMinimumHeight(450)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 531, 151))
        self.label.setMinimumSize(QtCore.QSize(140, 150))
        self.label.move(225, 50)
        self.label.setObjectName("label")
        self.label.setText("ВЫБЕРИТЕ РАЗДЕЛ ВИДЕОУРОКОВ")
        self.label.setFont(QFont('Arial', 22))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 211, 81))
        # self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: green;}')
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.move(70, 190)
        self.pushButton.setText("СБОРКА АВТОБУСОВ")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 100, 250, 81))  # 250 - ширина кнопки
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.move(330, 190)
        self.pushButton_2.setText("МОНТАЖ  \n ЭЛЕКТРООБОРУДОВАНИЯ")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 100, 250, 81))  # 250 - ширина кнопки
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.move(630, 190)
        self.pushButton_3.setText("УСТАНОВКА ДВЕРНЫХ \n СИСТЕМ (CAMOZZI)")


class Window1_1(QWidget):  # Окно № 1   Раздел 1.1   Сборка автобусов
    def __init__(self):
        super(Window1_1, self).__init__()
        self.setWindowTitle('Сборка автобусов')
        self.setMinimumWidth(930)
        self.setMinimumHeight(450)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 531, 151))
        self.label.setMinimumSize(QtCore.QSize(140, 150))
        self.label.move(255, 50)
        self.label.setObjectName("label")
        self.label.setText("ВЫБЕРИТЕ ПОДРАЗДЕЛЫ")
        self.label.setFont(QFont('Arial', 22))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 245, 81))
        # self.pushButton.setStyleSheet('QPushButton {background-color: #A3C1DA; color: green;}')
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.move(70, 190)
        self.pushButton.setText("1.1 Монтаж тягового \n электрооборудования 6282")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 100, 290, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.move(330, 190)
        self.pushButton_2.setText("1.2 Монтаж элементов  \n интерьера электробуса 6282")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 100, 250, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.move(630, 190)
        self.pushButton_3.setText("1.3 Монтаж элементов \n экстерьера 6282")

        # self.button = QPushButton(self)
        # self.button.setText('show_window_2')
        # self.button.show()


class Window2(QWidget):  # Окно № 2
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        self.setMinimumWidth(270)
        self.setMinimumHeight(250)
        self.button = QPushButton(self)
        self.button.setText('Показать панель управления воспроизведением')
        self.button.show()


class ViewerWindow(QMainWindow):  # класс для работы с окном № 2
    # если state is True то по идее запускается окно № 2
    state = pyqtSignal(bool)

    def closeEvent(self, e):
        # Emit the window state, to update the viewer toggle button.
        self.state.emit(False)  # класс для работы с окном № 2


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):  # получаем имя файла fileName
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())

            print(media.canonicalUrl().fileName())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):  # получаем кол-во записей в playlist-e
        # print(self.playlist.mediaCount())
        return self.playlist.mediaCount()


class MainWindow(QMainWindow, Ui_MainWindow):  # Главное окно программы
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.error.connect(self.erroralert)
        self.player.play()
        # Setup the playlist.
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        test = None  # ? -------

        # Add viewer for video playback, separate floating window.
        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)  # второе окно ко-е видео воспроизводит
        self.player.setVideoOutput(videoWidget)  # основное окно с кнопками

        # Connect control buttons/slides for media player.
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        # кнопка при нажатии на ко-й откроется новое окно
        self.viewButton.toggled.connect(self.toggle_viewer)
        # self.viewer.state.connect(self.viewButton.setChecked) # ??? где сама функция

        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)
        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)  # QListView - содержащий список файлов
        self.playlist.currentIndexChanged.connect(self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()  # работа с листом списком видеофайлов
        selection_model.selectionChanged.connect(self.playlist_selection_changed)
        # selection_model.clear()
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        # self.open_file_action.triggered.connect(self.open_file)
        # загрузка списка файлов при нажатии на Button в окне управления
        # self.pushButton.clicked.connect(self.open_spisok)
        # -- загрузка списка файлов -- #
        self.pushButton.clicked.connect(
            lambda ch, path_new=path_3: self.open_spisok(path_new)
        )  # откроем список файлов,  path_new - параметр
        # -- Очистка списка -- #
        self.pushButton_2.clicked.connect(self.clear_spisok)

        # -- вовзрат в основной раздел -- #
        self.pushButton_3.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.close_viewer)
        self.pushButton_3.clicked.connect(self.show_window_1)
        self.setAcceptDrops(True)  # актвность drag & drop метода

    def show_window_1(self):  # функция вызова окна (Основной раздел)
        self.w1 = Window1()
        self.w1.show()

        self.w1.pushButton.clicked.connect(self.show_Window1_1)  # Открываем раздел 1
        self.w1.pushButton.clicked.connect(self.w1.hide)  # скрываем основной раздел
        # !!! vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.w1.pushButton_2.clicked.connect(
            lambda: self.show_main_window('2'))  # Открываем раздел 2                        # !!! +++ 2
        # передаем условный номер раздела ->^                                                    # !!!
        self.w1.pushButton_2.clicked.connect(self.w1.hide)

        self.w1.pushButton_3.clicked.connect(
            lambda: self.show_main_window('3'))
        # передаем условный номер раздела ->^
        self.w1.pushButton_3.clicked.connect(self.w1.hide)

    # !!! ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def show_main_window(self, section=0):  # функция вызова окна управления               #  +++ section
        # !!!
        # ?        self.window = MainWindow()               # !!! ЭТОГО ДЕЛАТЬ НЕ НАДО так как мы и так находимся
        # ?       self.window.show()                        # !!!                      в классе MainWindow

        # print(f'section ---> {section}')
        if section == '1.2':  # +++
            self.open_spisok(xxx)

        if section == '2':  # +++
            self.open_spisok(path_2)  # +++
            # ------------>> ^^^^^^
        # ...
        if section == '3':
            self.open_spisok(path_3)
            print(f'section ---> {section}')

        self.show()  # +++

    def show_Window1_1(self):
        print("откроем окно раздел 1_1")
        self.w1_1 = Window1_1()
        self.w1_1.show()

        self.w1_1.pushButton.clicked.connect(
            lambda: self.show_main_window('1.1'))
        self.w1_1.pushButton.clicked.connect(self.w1_1.hide)  # скрываем основной раздел

        self.w1_1.pushButton_2.clicked.connect(
            lambda: self.show_main_window('1.2'))  # Открываем раздел 2                        # !!! +++ 2
        # передаем условный номер раздела ->^                                                    # !!!
        self.w1_1.pushButton_2.clicked.connect(self.w1_1.hide)

        self.w1_1.pushButton_3.clicked.connect(
            lambda: self.show_main_window('1.3'))
        # передаем условный номер раздела ->^
        self.w1_1.pushButton_3.clicked.connect(self.w1_1.hide)


    def show_window_2(self):  # функция вызова второго окна
        self.w2 = Window2()
        self.w2.show()
        # при нажатии на Button показываем главное окно упрвления
        self.w2.button.clicked.connect(self.show_main_window)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(QMediaContent(url))
            print(" url :" + str(url))
            print("QMediaContent url :" + str(QMediaContent(url)))

        self.model.layoutChanged.emit()

        # If not playing, seeking to first of newly added + play.
        if self.player.state() != QMediaPlayer.PlayingState:
            i = self.playlist.mediaCount() - len(e.mimeData().urls())
            self.playlist.setCurrentIndex(i)
            print("i :" + str(i))
            self.player.play()

    def open_spisok(self, path_new):                # загрузки файлов в список mediaplayer
        self.playlist.clear()                       # очишаем список
        print("очишаем список playlist перед заполнением")
        files = os.listdir(path_new)                # список имен файлов в папке path
        print("files: " + str(files))               # список файлов с абсолютным путем
        for f in files:
            fullname = os.path.join(path_new, f)  #
            print("fullname :" + fullname)
            print(type(fullname))

            self.playlist.addMedia(
                QMediaContent(QUrl.fromLocalFile(fullname)))  # добавляем в список файлы видео (пути к файлам)

            self.model.layoutChanged.emit()

    def clear_spisok(self):
        self.playlist.clear()  # очишаем список
        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        self.timeSlider.setMaximum(duration)
        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))
        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:  # если state - True
            self.viewer.show()
        else:
            self.viewer.hide()

    def erroralert(self, *args):
        print(args)

    def close_viewer(self):
        print("Закрываем окно просмотра видео (viewer)")
        self.viewer.close()

    # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def closeEvent(self, event):
        self.show_window_1()
        self.hide()
        event.ignore()


# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("Kiosk Media Player")
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(45, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(12, 100, 238))
    palette.setColor(QPalette.Highlight, QColor(12, 115, 228))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }"
    )

    window = MainWindow()
    #    window.show()                             # !!! ЭТОГО ДЕЛАТЬ НЕ НАДО
    window.show_window_1()  # показываем окно № 1 Основной раздел
    #    print("скроем главное окно")
    #    window.hide()  # скроем главное окно       # !!! ЭТОГО ДЕЛАТЬ НЕ НАДО
    sys.exit(app.exec_())