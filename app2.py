import sys
import pathlib
import os
import pkgutil


def main():
    plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
    sys.path.append(plugins_dir)

    loaded_mod = __import__("Plugin03")
    loaded_class = getattr(loaded_mod, "Plugin03Class")

    # Create an instance of the class
    instance = loaded_class()
    setattr(instance, "my_param", "valor atribuido dinamicamente")
    instance.run()


if __name__ == '__main__':
    main()
