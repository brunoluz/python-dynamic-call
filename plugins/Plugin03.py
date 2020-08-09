class Plugin03Class:
    def __init__(self, my_param=None):
        self.my_param = my_param

    def run(self):
        print(f"parametro: {self.my_param}")
