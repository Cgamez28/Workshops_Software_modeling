from datetime import datetime
from users import Client
from machines import Machine

class PurchaseManager:
    """
    This class represents the purchase manager.
    """
    def __init__(self, client: Client, machine: Machine):
        self.client = client
        self.machine = machine

    def finalize_purchase(self):
        """
        This method allows to finalize the purchase.
        """
        with open("purchase.txt", "a") as file:
            file.write(f"Date: {datetime.now()}\n")
            file.write(f"Client: {self.client._name}\n")
            file.write(f"Adress: {self.client.__addresses}\n")
            file.write(f"Phone: {self.client.__phones}\n")
            file.write(f"Email: {self.client._email}\n")
            file.write(f"Arcade machine material: {self.machine.material}\n")
            file.write("Games:\n")
        
        print("The purchase has been finalized.")
