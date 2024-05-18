# 5.Make some objects of Samsung class with different properties
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

# Create objects of the Apple class with different properties
iphone_11 = Apple("iPhone 11", rear_camera="12MP", ram="4GB", storage="128GB")
iphone_XR = Apple("iPhone XR", rear_camera="12MP", ram="3GB", storage="64GB")

# Display the properties of each object
print("iPhone 11 Specs:")
print("Model:", iphone_11.model)
print("Screen Type:", iphone_11.screen_type)
print("Network Type:", iphone_11.network_type)
print("Dual SIM Support:", iphone_11.dual_sim)
print("Front Camera:", iphone_11.front_camera)
print("Rear Camera:", iphone_11.rear_camera)
print("RAM:", iphone_11.ram)
print("Storage:", iphone_11.storage)
print()

print("iPhone XR Specs:")
print("Model:", iphone_XR.model)
print("Screen Type:", iphone_XR.screen_type)
print("Network Type:", iphone_XR.network_type)
print("Dual SIM Support:", iphone_XR.dual_sim)
print("Front Camera:", iphone_XR.front_camera)
print("Rear Camera:", iphone_XR.rear_camera)
print("RAM:", iphone_XR.ram)
print("Storage:", iphone_XR.storage)
