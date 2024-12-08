from libqtile import widget, qtile
from theme_colors import ThemeColors
from qtile_extras import widget as extrawidgets
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
from libqtile.lazy import lazy

__all__ = ["WIDGET_DEFAULTS", "first_bar"]

theme_colors = ThemeColors()
catppuccin = theme_colors.CATPPUCCIN_MOCHA



WIDGET_DEFAULTS = {
    "font": "JetBrainsMono Nerd Font Bold",
    "fontsize": 16,
    "padding": 2,
    "background": catppuccin.get("base"),
    "foreground": catppuccin.get("text"),
}


DECORATION_GROUPBOX = {
    "decorations": [
        RectDecoration(
            colour=catppuccin.get("surface0"), 
            radius=10, 
            filled=True, 
            padding_y=4, 
            group=True
        )
    ],
    "padding": 10,
}


DECORATION_SPACER_1 = {
    "decorations": [
        RectDecoration(
            colour=catppuccin.get("surface0"), 
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
            colour=catppuccin.get("surface0"), 
            radius=10, 
            filled=True, 
            padding_y=4, 
            group=True
        )
    ],
    "padding": 0,
}


# TODO - Criar o calendario...
# def open_calendar():
#     qtile.cmd_spawn("gnome-calendar")

def open_rofi(*args, **kwargs):
    qtile.spawn("rofi -show drun")
    

def first_bar(primary: bool = False):
    widgets = [
        extrawidgets.Spacer(length=10),
        # widgets a esquerda
        extrawidgets.TextBox(
            text="󰣇",
            fontsize=24,
            padding=8,
            mouse_callbacks={"Button1": lazy.function(open_rofi)},
            foreground=catppuccin.get("mauve"),
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.CurrentLayout(
            foreground=catppuccin.get("green"),
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.WindowName(
            max_chars=20,
            foreground=catppuccin.get("flamingo"),
            # **DECORATION_GROUPBOX
        ),
        
        extrawidgets.Spacer(),
        
        # widgets no centro
        extrawidgets.GroupBox(
            highlight_method="text",
            inactive=catppuccin.get("surface2"),  # Cor dos grupos inativos
            active=catppuccin.get("text"),  # Cor dos grupos ativos
            this_current_screen_border=catppuccin.get("mauve"),  # Cor da borda do grupo ativo na tela atual
            # this_screen_border=catppuccin.get("blue"),  # Cor da borda do grupo ativo em outras telas
            # other_screen_border=catppuccin.get("surface0"),  # Cor da borda do grupo ativo em outras telas
            # other_current_screen_border=catppuccin.get("surface0"),  # Cor da borda do grupo ativo em outras telas
            **DECORATION_GROUPBOX
        ),
        
        extrawidgets.Spacer(),
        
        # widgets a direita
        extrawidgets.Volume(
            emoji=True,
            emoji_list=["", "", "", ""],
            foreground=catppuccin.get("yellow"),
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10, **DECORATION_SPACER_1),
        extrawidgets.DF(
            visible_on_warn=False,
            partition="/home",
            format=' ({r:.0f}%|',
            foreground=catppuccin.get("red"),
            **DECORATION_DF
        ),
        extrawidgets.DF(
            visible_on_warn=False,
            partition="/",
            format='{r:.0f}%)',
            foreground=catppuccin.get("red"),
            **DECORATION_DF
        ),
        extrawidgets.Memory(
            measure_mem='G', 
            format="󰍛 {MemUsed:.2f}GB",
            foreground=catppuccin.get("blue"),
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.Clock(
            # padding=8,
            format=" %d-%m-%Y %H:%M",
            foreground=catppuccin.get("sapphire"),
            # mouse_callbacks={"Button1": lazy.function(open_calendar)},
            **DECORATION_GROUPBOX
        ),
        extrawidgets.Spacer(length=10),
        extrawidgets.Systray(),
        extrawidgets.Spacer(length=10),
    ]
    return widgets
