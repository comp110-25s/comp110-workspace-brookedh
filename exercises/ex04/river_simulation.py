"""Module to stimulate daily life in a river ecosystem!"""

from river import River


def main():
    my_river = River(num_fish=10, num_bears=2)

    # Stimulate one week in the river
    my_river.one_river_week()

    # View the river's state after one week
    my_river.view_river()

if __name__ = "__main__":
    main()