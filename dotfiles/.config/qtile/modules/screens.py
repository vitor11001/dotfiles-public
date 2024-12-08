from libqtile.config import Screen
from libqtile.bar import Bar
from .bars import top_bar
from themes import CatppuccinMocha

__all__ = ["SCREENS_BASE"]

theme_colors = CatppuccinMocha()


SCREENS_BASE = [
    Screen(
        top=Bar(widgets=top_bar(), size=32, background=theme_colors.base),
    ),
]
