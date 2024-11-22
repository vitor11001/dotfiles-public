from libqtile import layout
from theme_colors import ThemeColors

theme_colors = ThemeColors()
catppuccin = theme_colors.CATPPUCCIN_MOCHA


layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": catppuccin.get("mauve"),
    "border_normal": catppuccin.get("base"),    
}


FLOAT_LAYOUT: dict = {
    "border_width": 3,
    "border_focus": catppuccin.get("mauve"),
    "border_normal": catppuccin.get("base"),
} # used as default for some programs, see 'floating_layout' in config.py


LAYOUT_MAP: list = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
]
