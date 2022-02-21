import sys

# GUI
from Custom_Widgets.Widgets import QApplication
from book_store.ui.book_store_ui import *
from book_store.main_window import MainWindow

# Database Connection
from book_store.utils.db_conn import BookStoreDb

# Execute App
def run():

    # Connect To Database
    db = BookStoreDb()

    # Launch GUI
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())