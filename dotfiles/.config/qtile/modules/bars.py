from libqtile import widget, qtile
from qtile_extras import widget as extrawidgets
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy
from themes import CatppuccinMocha

__all__ = ["top_bar"]


theme_colors = CatppuccinMocha()


WIDGET_DEFAULTS = {
    "font": "JetBrainsMono Nerd Font Bold",
    "fontsize": 16,
    "padding": 2,
    "background": theme_colors.base,
    "foreground": theme_colors.text,
}


DECORATION_GROUPBOX = {
    "decorations": [
        RectDecoration(
            colour=theme_colors.surface0, 
            radius=10, 
            filled=True, 
            padding_y=4, 
            group=True
        )
    ],
    "padding": 10,
}


DECORATION_SPACER = {
    "decorations": [
        RectDecoration(
            colour=theme_colors.surface0, 
            radius=10, 
            filled=True, 
            padding_y=4, 
            group=True
        )
    ],
    "padding": 0,
}


DECORATION_DF = {
    "decorations": [
        RectDecoration(
            colour=theme_colors.surface0, 
            radius=10, 
            filled=True, 
            padding_y=4, 
            group=True
        )
    ],
    "padding": 0,
}


def open_rofi(*args, **kwargs):
    qtile.spawn("rofi -show drun")


def top_bar():
    widgets = [
        extrawidgets.Spacer(length=10),
        # widgets a esquerda
        extrawidgets.TextBox(
            text="󰣇",
            fontsize=24,
            padding=8,
            mouse_callbacks={"Button1": lazy.function(open_rofi)},
            foreground=theme_colors.mauve,
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.CurrentLayout(
            foreground=theme_colors.green,
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.WindowName(
            max_chars=20,
            foreground=theme_colors.flamingo,
            # **DECORATION_GROUPBOX
        ),
        
        extrawidgets.Spacer(),
        
        # widgets no centro
        extrawidgets.GroupBox(
            highlight_method="text",
            inactive=theme_colors.surface2,  # Cor dos grupos inativos
            active=theme_colors.text,  # Cor dos grupos ativos
            this_current_screen_border=theme_colors.mauve,  # Cor da borda do grupo ativo na tela atual
            # this_screen_border=theme_colors.get("blue"),  # Cor da borda do grupo ativo em outras telas
            # other_screen_border=theme_colors.get("surface0"),  # Cor da borda do grupo ativo em outras telas
            # other_current_screen_border=theme_colors.get("surface0"),  # Cor da borda do grupo ativo em outras telas
            **DECORATION_GROUPBOX
        ),
        
        extrawidgets.Spacer(),
        
        # widgets a direita
        extrawidgets.Volume(
            emoji=True,
            emoji_list=["", "", "", ""],
            foreground=theme_colors.yellow,
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10, **DECORATION_SPACER),
        extrawidgets.DF(
            visible_on_warn=False,
            partition="/home",
            format=' ({r:.0f}%|',
            foreground=theme_colors.red,
            **DECORATION_DF
        ),
        extrawidgets.DF(
            visible_on_warn=False,
            partition="/",
            format='{r:.0f}%)',
            foreground=theme_colors.red,
            **DECORATION_DF
        ),
        extrawidgets.Memory(
            measure_mem='G', 
            format="󰍛 {MemUsed:.2f}GB",
            foreground=theme_colors.blue,
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.Clock(
            # padding=8,
            format="  %d-%m-%Y %H:%M",
            foreground=theme_colors.sapphire,
            # mouse_callbacks={"Button1": lazy.function(open_calendar)},
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.Systray(),
        extrawidgets.Spacer(length=10),
    ]
    return widgets
