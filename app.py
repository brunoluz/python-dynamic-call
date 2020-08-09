import sys
import pathlib
import os


def main():
    current_dir = pathlib.Path(__file__).parent.absolute()
    sys.path.append(os.path.join(current_dir, "plugins"))

    plugin01 = __import__("Plugin01")
    print(plugin01.execute())

    plugin02 = __import__("Plugin02")
    print(plugin02.execute("p01", "p02"))


if __name__ == '__main__':
    main()
