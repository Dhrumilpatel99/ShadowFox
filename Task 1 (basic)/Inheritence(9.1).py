class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False, front_camera="5MP", rear_camera="8MP", ram="2GB", storage="16GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

class Apple(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False, front_camera="5MP", rear_camera="12MP", ram="4GB", storage="64GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model, screen_type="Touch Screen", network_type="4G/5G", dual_sim=True, front_camera="8MP", rear_camera="16MP", ram="3GB", storage="32GB"):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

# Example usage:
iphone_12 = Apple("iPhone 12")
galaxy_s21 = Samsung("Galaxy S21")

print("iPhone 12:")
print("Screen Type:", iphone_12.screen_type)
print("Network Type:", iphone_12.network_type)
print("Dual SIM Support:", iphone_12.dual_sim)
print("Front Camera:", iphone_12.front_camera)
print("Rear Camera:", iphone_12.rear_camera)
print("RAM:", iphone_12.ram)
print("Storage:", iphone_12.storage)
print("Model:", iphone_12.model)
print()

print("Galaxy S21:")
print("Screen Type:", galaxy_s21.screen_type)
print("Network Type:", galaxy_s21.network_type)
print("Dual SIM Support:", galaxy_s21.dual_sim)
print("Front Camera:", galaxy_s21.front_camera)
print("Rear Camera:", galaxy_s21.rear_camera)
print("RAM:", galaxy_s21.ram)
print("Storage:", galaxy_s21.storage)
print("Model:", galaxy_s21.model)
