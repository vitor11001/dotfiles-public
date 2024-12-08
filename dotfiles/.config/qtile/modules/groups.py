from libqtile.config import Group

__all__ = ["GROUPS_LIST"]


group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

GROUPS_LIST = [Group(name) for name in group_names]
