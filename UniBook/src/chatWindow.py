from PySide6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget, QPushButton, QLineEdit

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the central widget and layout
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Create QTextBrowser for chat display
        self.chat_display = QTextBrowser(self.central_widget)
        self.layout.addWidget(self.chat_display)

        # Create QLineEdit for typing messages
        self.input_field = QLineEdit(self.central_widget)
        self.layout.addWidget(self.input_field)

        # Create QPushButton to send message
        self.send_button = QPushButton("Send", self.central_widget)
        self.layout.addWidget(self.send_button)

        # Connect button to send message
        self.send_button.clicked.connect(self.send_message)

        # Set the central widget
        self.setCentralWidget(self.central_widget)

        # Display some initial messages in the chat display
        self.display_message("User1", "Hello, how are you?")
        self.display_message("User2", "I'm good, thanks for asking!")

    def send_message(self):
        message = self.input_field.text()
        if message:
            # Display the user's message in the chat
            self.display_message("You", message)
            # Clear the input field
            self.input_field.clear()

    def display_message(self, user, message):
        # Format the message to show the user and the message
        formatted_message = f"<b>{user}:</b> {message}<br>"
        self.chat_display.append(formatted_message)  # Append the message to QTextBrowser


if __name__ == "__main__":
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()
