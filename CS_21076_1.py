# Imported files required to run the script
from kivy.config import Config

# These module functions will always be placed on top otherwise there properties won't execute.
Config.set("graphics", "width", "1080")
Config.set("graphics", "height", "640")
Config.set('graphics', 'resizable', False)
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from CS_21076_2 import DataHandler
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty


# The main container class developed to provide the single interface to all contained classes.
class GUI:
    # This class displays introduction screen of  application.
    class IntroWindow(Screen):
        pass

    # This class displays login screen of customer. Here customer can sign in to application.
    class CustomerLoginWindow(Screen):
        pass

    # This class displays signup screen of customer to user. Here user can register as a customer.
    class CustomerSignUpWindow(Screen, DataHandler):
        count = 0

        @classmethod
        def set_id(cls):
            cls.customer_id = f"C{cls.count}"
            return cls.customer_id
        count += 1

        def data_saver(self, *args):
            self.data_collection(*args, credentials_filename="customer_credentials.csv",
                                 login_filename="customer_login_credentials.csv", user_id=self.set_id())

    # This class displays profile screen of customer. Here customer can see his credentials.
    class CustomerProfileWindow(Screen, DataHandler):
        grid = ObjectProperty(None)
        cred_list = ["Name:", "Email Address:", "Password:", "Phone Number:", "Credit Card Number:", "Gender:", "Date of Birth:"]

        def on_grid(self, *args):
            self.data_list = self.get_data(filename="customer_credentials.csv")
            if self.data_list[1] == "-":
                self.data_list[1] = ""
            if self.data_list[2] == "-":
                self.data_list[2] = ""
            self.grid.add_widget(MDLabel(text=f"{self.cred_list[0]} {self.data_list[0]} {self.data_list[1]} {self.data_list[2]}", font_name="time_new_romans.ttf", font_size=18))
            for i in range(1, len(self.cred_list)):
                self.grid.add_widget(MDLabel(text=f"{self.cred_list[i]} {self.data_list[i+2]}",font_name="time_new_romans.ttf", font_size=18))

    # This class displays product screen to customer. Here customer can view and add the products to his cart.
    class ProductWindow(Screen, DataHandler):
        pass

    # This class is used to extend properties of MDCard class, and develop the better variant of display cards to show our products.
    class ElementCard(MDCard, DataHandler):
        label = "For timekeeping, Finland follows Eastern European Time (EET) during its winter as standard time and Eastern European Summer Time (EEST) in the summer as daylight saving time. EET is two hours ahead of Coordinated Universal Time and EEST is three hours ahead. Finland adopted EET in 1921, and daylight saving time in its current form from 1981. Up to the 19th century, each locality used its own solar time, which could vary in Finland by up to 31 minutes. In 1862, a mean time was adopted as a single time zone for railway scheduling. Daylight saving time was first attempted in 1942, abandoned as not useful, and introduced again in 1981 to align with neighbouring countries. In 2017, the Finnish parliament voted to call on the European Union to abolish daylight saving time. Finland's time zone is maintained by the VTT Technical Research Centre of Finland and the Centre for Metrology and Accreditation, using an atomic clock and hydrogen monitors. The 24-hour clock notation is used in Finland."

        def bottom_sheet(self, image, price, rate, label):
            # for i in
            bottom_sheet = Factory.ContentCustomSheet()
            bottom_sheet.image = image
            bottom_sheet.price = price
            bottom_sheet.rate = rate
            bottom_sheet.label = label
            self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
            self.custom_sheet.open()

    # This class displays shopping cart screen of customer. Here user can see all his orders, change or remove them,
    # as well as check them out for completion of purchase processes.
    class CurrentCartWindow(Screen):
        pass

    # This class displays complete shopping history of customer.
    class ShoppingHistoryWindow(Screen):
        pass

    # This class display all orders and information regrading them to customer.
    class AfterCheckoutWindow(Screen):
        pass

    # This class displays login screen of administrator. Here administrator can sign in to application.
    class AdminLoginWindow(Screen):
        pass

    # This class displays signup screen of administrator to user. Here user can register as an administrator.
    class AdminSignUpWindow(Screen, DataHandler):
        def data_saver(self, *args):
            self.data_collection(*args, credentials_filename="admin_credentials.csv",
                                 login_filename="admin_login_credentials.csv")

    # This class displays action screen of administrator. Here administrator can see various actions he can perform, regarding the application.
    class AdminWindow(Screen):
        pass

    # This class displays profile screen of customer. Here customer can see his credentials.
    class AdminProfileWindow(Screen, DataHandler):
        grids = ObjectProperty(None)

        def on_grids(self, *args):
            for i in self.get_data(filename="admin_credentials.csv"):
                self.grids.add_widget(MDLabel(text=f"{i}"))

    # This class displays profile screen of customer to administrator. Here administrator can see the customer's credentials.
    class AdminCustomerInfoWindow(Screen):
        pass

    # This class displays product screen to administrator. Here administrator can update stock as well as perform different actions regarding products.
    class AdminProductViewWindow(Screen):
        pass

    # This class manages the flow, as well as transitions between different screens.
    class Manager(ScreenManager):
        pass

    # This class is used to build and initiate the application.
    class ShoppingApp(MDApp):
        def build(self):
            kv = Builder.load_file("CS_21076_4.kv")
            return kv


app = GUI().ShoppingApp().run()
