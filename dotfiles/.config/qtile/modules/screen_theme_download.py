import sys
from os.path import expanduser, exists, normpath, getctime
from subprocess import run
from os import system, listdir, makedirs
from datetime import datetime
from libqtile import layout, qtile, hook, bar, core
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import send_notification
from qtile_extras import widget
from shutil import which
from json import dump, load
from .groups import GROUPS_LIST


catppuccin_mocha = {
    'foreground': '#cdd6f4',
    'background': '#1e1e2e',
    'alt_background': '#181825',
    'disabled': '#313244',
    'accent': '#89b4fA',
}
theme = catppuccin_mocha


class WidgetTweaker:
    def __init__(self, func):
        self.format = func

#  _____           
# | __  | ___  ___ 
# | __ -|| .'||  _|
# |_____||__,||_|  

groups_labels = ['●', '●', '●', '●', '●', '●', '●', '●', '●']

@WidgetTweaker
def groupBox(output):
    index = GROUPS_LIST.index(output)
    label = groups_labels[index]

    return label

@WidgetTweaker
def volume(output):
    if output.endswith('%'):
        volume = int(output[:-1])

        icons = {
            range(0, 33): '󰕿   ',
            range(33, 66): '󰖀   ',
            range(66, 101): '󰕾   '
        }

        icon = icons[next(filter(lambda r: volume in r, icons.keys()))]

        return icon + output
    elif output == 'M':
        return '󰕿   Muted'
    else:
        return output

@WidgetTweaker
def currentLayout(output):
    return output.capitalize()


# Top bar

bar_top_margin = 5
bar_bottom_margin = 5
bar_left_margin = 0
bar_right_margin = 0
bar_size = 32
bar_background_color = theme['background']
bar_foreground_color = theme['foreground']
bar_background_opacity = 0
bar_global_opacity = 1.0
bar_font = "Opensans Medium"
bar_nerd_font = "JetbrainsMono Nerd Font"
bar_fontsize = 13.2


# Widgets

widget_gap = 6
widget_left_offset = 4
widget_right_offset = 4
widget_padding = 15

# Widgets Decorations

widget_decoration = "RectDecoration"

widget_decoration_border_width = 1
widget_decoration_border_color = theme['accent']
widget_decoration_border_opacity = 1.0
widget_decoration_border_padding_x = 0
widget_decoration_border_padding_y = 0

widget_decoration_powerline_path = "arrow_left"
widget_decoration_powerline_size = 10
widget_decoration_powerline_padding_x = 0
widget_decoration_powerline_padding_y = 0

widget_decoration_rect_filled = True
widget_decoration_rect_color = theme["alt_background"]
widget_decoration_rect_opacity = 1.0
widget_decoration_rect_border_width = 2.7
widget_decoration_rect_border_color = theme["accent"]
widget_decoration_rect_padding_x = 0
widget_decoration_rect_padding_y = 0
widget_decoration_rect_radius = 10



decorations = {
    "BorderDecoration": {
        "border_width": widget_decoration_border_width,
        "colour": widget_decoration_border_color + format(int(widget_decoration_border_opacity * 255), "02x"),
        "padding_x": widget_decoration_border_padding_x,
        "padding_y": widget_decoration_border_padding_y,
    },
    "PowerLineDecoration": {
        "path": widget_decoration_powerline_path,
        "size": widget_decoration_powerline_size,
        "padding_x": widget_decoration_powerline_padding_x,
        "padding_y": widget_decoration_powerline_padding_y,
    },
    "RectDecoration": {
        "group": True,
        "filled": widget_decoration_rect_filled,
        "colour": widget_decoration_rect_color + format(int(widget_decoration_rect_opacity * 255), "02x"),
        "line_width": widget_decoration_rect_border_width,
        "line_colour": widget_decoration_rect_border_color,
        "padding_x": widget_decoration_rect_padding_x,
        "padding_y": widget_decoration_rect_padding_y,
        "radius": widget_decoration_rect_radius,
    }
}

decoration = [getattr(widget.decorations, widget_decoration)(**decorations[widget_decoration])]

widget_defaults = dict(
    font=bar_font,
    foreground=bar_foreground_color,
    fontsize=bar_fontsize,
    padding=widget_padding,
    decorations=decoration
)

extension_defaults = widget_defaults.copy()

sep = [widget.WindowName(foreground="#00000000", fmt="", decorations=[])]
left_offset = [widget.Spacer(length=widget_left_offset, decorations=[])]
right_offset = [widget.Spacer(length=widget_right_offset, decorations=[])]
space = widget.Spacer(length=widget_gap, decorations=[])


class Wallpaper:
    def formatName(name):
        backslash = r"""\&~"#'{([|`^$*"""

        for c in backslash:
            name = name.replace(c, '\\'+c)
        
        return name

    def getSavedWallpaper():
        with open(expanduser('~/.config/nitrogen/bg-saved.cfg'), 'r') as file:
            path = file.read().splitlines()[1].removeprefix('file=').strip() # Get saved background path
            directory = normpath(path[::-1].split('/', 1)[1][::-1])
            name = path.split('/')[-1]

        # if normpath(directory) == normpath(wallpapers_path) and name in Wallpaper.wallpapers: # Checks if the background folder is wallpapers_path is in wallpapers
        #     return Wallpaper.wallpapers.index(name) # Set the pointer on the saved background

    def restorePointer():
        if exists(expanduser('~/.config/nitrogen/bg-saved.cfg')):
            Wallpaper.current = Wallpaper.getSavedWallpaper()
        else:
            Wallpaper.current = 0

    def init():
        # Wallpaper.wallpapers = listdir(wallpapers_path)
        # Wallpaper.wallpapers.sort(key=lambda w: getctime(f"{wallpapers_path}{w}")) # Sort by creation date
        # wallpapers.sort(key=str.lower) # sort by name

        Wallpaper.mode = "zoom-fill"

        Wallpaper.restorePointer()

    # def set():
    #     system(f'nitrogen --save --set-{Wallpaper.mode} {wallpapers_path}{Wallpaper.formatName(Wallpaper.wallpapers[Wallpaper.current])}')

    @lazy.function
    def next(_qtile):
        Wallpaper.current = (Wallpaper.current + 1) % len(Wallpaper.wallpapers)
        Wallpaper.set()

    @lazy.function
    def previous(_qtile):
        Wallpaper.current = (Wallpaper.current - 1) % len(Wallpaper.wallpapers)
        Wallpaper.set()
    
Wallpaper.init()


left = [
    widget.Clock(
        format="%A %d %B %Y %H:%M",
    ), space,

    widget.TextBox(
        "\uf060",
        mouse_callbacks={
            'Button1': Wallpaper.previous(),
            'Button4': Wallpaper.next(),
            'Button5': Wallpaper.previous()
        },
    ),

    widget.TextBox(
        "Wallpaper",
        padding=0,
        mouse_callbacks={
            'Button4': Wallpaper.next(),
            'Button5': Wallpaper.previous()
        }
    ),

    widget.TextBox(
        "\uf061",
        mouse_callbacks={
            'Button1': Wallpaper.next(),
            'Button4': Wallpaper.next(),
            'Button5': Wallpaper.previous()
        },
    ),
]

middle = [
    widget.GroupBox(
        font=f"{bar_font} Bold",
        disable_drag=True,
        borderwidth=0,
        fontsize=15,
        inactive=theme['disabled'],
        active=bar_foreground_color,
        block_highlight_text_color=theme['accent'],
        padding=7,
        fmt=groupBox
    ),
]

right = [
    widget.StatusNotifier(), space,
    
    widget.Volume(
        step=2,
        fmt=volume,
        mouse_callbacks={'Button1':lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')},
        update_interval=0.01,
        limit_max_volume=True,
        volume_app="pavucontrol",
    ), space,

    widget.CurrentLayout(
        fmt=currentLayout,
        mouse_callbacks={
            'Button2': lambda: None,
            'Button3': lazy.prev_layout()
        },
    ), space,

    widget.TextBox(
        '⏻',
        decorations=[getattr(widget.decorations, widget_decoration)(**decorations[widget_decoration]|{'extrawidth': 3})],
        mouse_callbacks={
            'Button1': lazy.spawn("rofi -show drun -theme ~/.config/bspwm/src/rofi-themes/Launcher.rasi")
        },
    ), space,
]


#  _____                               
# |   __| ___  ___  ___  ___  ___  ___ 
# |__   ||  _||  _|| -_|| -_||   ||_ -|
# |_____||___||_|  |___||___||_|_||___|

screens = [
    Screen(
        top=bar.Bar(
            widgets=left_offset + left + sep + middle + sep + right + right_offset,
            size=bar_size,
            background = bar_background_color + format(int(bar_background_opacity * 255), "02x"),
            margin = [bar_top_margin, bar_right_margin, bar_bottom_margin-4, bar_left_margin],
            opacity = bar_global_opacity
        ),
    ),
]