import sys
import os


def main():
    plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
    sys.path.append(plugins_dir)

    plugin01 = __import__("Plugin01")
    print(plugin01.execute())

    plugin02 = __import__("Plugin02")
    print(plugin02.execute("p01", "p02"))


if __name__ == '__main__':
    main()
