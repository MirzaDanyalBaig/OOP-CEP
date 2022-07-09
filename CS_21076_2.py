import csv
from csv import writer

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from abc import ABCMeta, abstractmethod

class DataHandler:
    dialog = None

    def set_data(self, filename, data_list):
        with open(filename, "a", newline="") as f:
            writer_object = writer(f)
            writer_object.writerow(data_list)
            f.close()

    def data_collection(self, *args, credentials_filename=None, login_filename=None, user_id=None):
        signup_list = []
        login_list = [args[3].text, args[4].text]

        if credentials_filename == "admin_credentials.csv" and login_filename == "admin_login_credentials.csv":
            login_list.append(args[6].text)

        for credentials in args:
            # print(credentials.text)
            if credentials.text == "":
                credentials.text = "-"
            signup_list.append(credentials.text)

        signup_list.insert(0, user_id)
        login_list.insert(0, user_id)
        # print(customer_credentials)
        # print(customer_login_credentials)
        self.set_data(credentials_filename, signup_list)
        self.set_data(login_filename, login_list)

    def verify(self, password, password_2):
        if password.text == "" and password_2.text == "":
            return False
        elif password_2.text == password.text:
            return True
        else:
            return False

    def show_dialog_box(self):
        if not self.dialog:
            self.dialog = MDDialog(title="Incorrect Passwords",
                                   text="Passwords are not filled or do not match. Please enter again!",
                                   buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def get_data(self, filename=None):
        with open(filename) as f:
            reader_obj = csv.reader(f)
            for i in reader_obj:
                return i


d1 = DataHandler()
d1.get_data("customer_credentials.csv")
