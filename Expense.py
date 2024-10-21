import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QTableWidget, QTableWidgetItem, 
    QLineEdit, QLabel, QPushButton, QMenuBar, QMenu, QMessageBox
)
from PyQt5.QtCore import Qt

class DatabaseManager:
    def __init__(self, db_name='expenses.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    expense_name TEXT UNIQUE NOT NULL,
                    price REAL NOT NULL
                )
            ''')

    def insert_expense(self, expense_name, price):
        with self.connection:
            try:
                self.connection.execute('''
                    INSERT INTO expenses (expense_name, price) VALUES (?, ?)
                ''', (expense_name, price))
            except sqlite3.IntegrityError:
                raise ValueError(f"Expense '{expense_name}' already exists.")

    def delete_expense(self, expense_name):
        with self.connection:
            self.connection.execute('''
                DELETE FROM expenses WHERE expense_name = ?
            ''', (expense_name,))

    def fetch_expenses(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT expense_name, price FROM expenses')
        return cursor.fetchall()

    def close(self):
        self.connection.close()


class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)

        # Initialize the Database Manager
        self.db_manager = DatabaseManager()

        # Create a central widget and set it as the central widget of the QMainWindow
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Create a menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        
        file_menu = QMenu("File", self)
        edit_menu = QMenu("Edit", self)
        help_menu = QMenu("Help", self)
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(edit_menu)
        menu_bar.addMenu(help_menu)

        # Create the top panel for input fields and add button
        top_panel = QHBoxLayout()
        layout.addLayout(top_panel)

        # Create labels and text fields for "Expense" and "Price"
        expense_label = QLabel("Expense:")
        self.expense_input = QLineEdit()
        self.expense_input.setFixedWidth(150)

        price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.price_input.setFixedWidth(100)

        # Create the button to add expenses
        add_button = QPushButton("Add Expense")
        add_button.clicked.connect(self.add_expense)

        # Create the button to delete expenses
        delete_button = QPushButton("Delete Expense")
        delete_button.clicked.connect(self.delete_expense)

        # Add widgets to the top panel
        top_panel.addWidget(expense_label)
        top_panel.addWidget(self.expense_input)
        top_panel.addWidget(price_label)
        top_panel.addWidget(self.price_input)
        top_panel.addWidget(add_button)
        top_panel.addWidget(delete_button)

        # Create the table to display expenses
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Expense", "Price"])
        layout.addWidget(self.table)

        # Create the bottom panel for displaying the total
        total_label = QLabel("Total:")
        self.total_value = QLabel("0.00")
        total_layout = QHBoxLayout()
        total_layout.addWidget(total_label)
        total_layout.addWidget(self.total_value)
        layout.addLayout(total_layout)

        # Load initial data from the database
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from the database and populate the table."""
        expenses = self.db_manager.fetch_expenses()
        self.table.setRowCount(0)  # Clear existing rows
        for expense_name, price in expenses:
            self.add_expense_to_table(expense_name, price)
        self.update_total()

    def add_expense(self):
        """Add a new expense to the database and table."""
        expense_name = self.expense_input.text().strip()
        price_text = self.price_input.text().strip()

        if not expense_name or not price_text:
            QMessageBox.warning(self, "Input Error", "Please enter both expense name and price.")
            return

        try:
            price = float(price_text)
            self.db_manager.insert_expense(expense_name, price)
            self.add_expense_to_table(expense_name, price)

            # Clear input fields
            self.expense_input.clear()
            self.price_input.clear()
            self.update_total()
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def add_expense_to_table(self, expense_name, price):
        """Add expense to the table."""
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(expense_name))
        self.table.setItem(row_position, 1, QTableWidgetItem(str(price)))

    def delete_expense(self):
        """Delete an expense from the database and the table."""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Selection Error", "Please select an expense to delete.")
            return
        
        expense_name = self.table.item(selected_row, 0).text()
        self.db_manager.delete_expense(expense_name)
        self.table.removeRow(selected_row)
        self.update_total()

    def update_total(self):
        """Calculate and update the total price."""
        total = 0.0
        for row in range(self.table.rowCount()):
            price_item = self.table.item(row, 1)
            if price_item:
                total += float(price_item.text())
        self.total_value.setText(f"{total:.2f}")

    def closeEvent(self, event):
        """Handle the window close event."""
        self.db_manager.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())
