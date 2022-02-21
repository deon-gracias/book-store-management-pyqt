from PySide2 import *

from Custom_Widgets.Widgets import *

# GUI
from book_store.ui.book_store_ui import *

# Main Window
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        loadJsonStyle(self, self.ui) # Applying Json Stylesheet

        self.add_listeners() # Adding listeners

        self.show() # Show Window
    
    @QtCore.Slot()
    def switchView(self, index):
        views = {0: "Inventory", 1: "Billing", 2: "Analytics"}
        self.ui.header_title.setText(views[index])
        self.ui.main.setCurrentIndex(index)

    def add_listeners(self):
        self.ui.inventory_nav_btn.clicked.connect(lambda: self.switchView(0))
        self.ui.billing_nav_btn.clicked.connect(lambda: self.switchView(1))
        self.ui.analytics_nav_btn.clicked.connect(lambda: self.switchView(2))
