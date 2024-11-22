from libqtile.config import Screen
from libqtile.bar import Bar
from .qtile_widget_bars import first_bar
from theme_colors import ThemeColors

__all__ = ["SCREENS_BASE"]

theme_colors = ThemeColors()
catppuccin = theme_colors.CATPPUCCIN_MOCHA


SCREENS_BASE = [
    Screen(
        top=Bar(widgets=first_bar(primary=True), size=32, background=catppuccin.get("base")),
    ),
]
