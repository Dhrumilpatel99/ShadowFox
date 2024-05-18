# 2. Create basic mobile phone functionalities in the classes like:
# make_call, recieve_call, take_a_picture, etc.

class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False, front_camera="5MP", rear_camera="8MP", ram="2GB", storage="16GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self):
        print("Making a call...")

    def receive_call(self):
        print("Receiving a call...")

    def take_a_picture(self):
        print("Taking a picture...")

class Apple(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False, front_camera="5MP", rear_camera="12MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="4G/5G", dual_sim=True, front_camera="8MP", rear_camera="16MP", ram="3GB", storage="32GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model


iphone_12 = Apple("iPhone 12")
galaxy_s21 = Samsung("Galaxy S21")

iphone_12.make_call()
galaxy_s21.take_a_picture()
