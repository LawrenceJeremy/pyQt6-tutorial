import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Static Grid Example")
window.setGeometry(200, 200, 500, 300)

# QLayouts
grid = QGridLayout()

# Widgets
grid.addWidget(QLabel("Label 1"), 0, 0)  # Upper-left

# Show display
window.setLayout(grid)
window.show()

# out
sys.exit(app.exec())
