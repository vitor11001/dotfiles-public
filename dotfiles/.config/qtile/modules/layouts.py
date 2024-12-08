from libqtile import layout
from themes import CatppuccinMocha

__all__ = ["LAYOUT_MAP", "FLOAT_LAYOUT"]


theme_colors = CatppuccinMocha()

layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": theme_colors.mauve,
    "border_normal": theme_colors.base,    
}


FLOAT_LAYOUT: dict = {
    "border_width": 3,
    "border_focus": theme_colors.mauve,
    "border_normal": theme_colors.base,
} # used as default for some programs, see 'floating_layout' in config.py


LAYOUT_MAP: list = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
]
