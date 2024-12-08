from libqtile.config import Key
from libqtile.lazy import lazy
from constants import MOD, TERMINAL, SHIFT, CONTROL, ALT
from .groups import GROUPS_LIST

__all__ = ["KEY_MAP"]


mod = MOD
terminal = TERMINAL
shift = SHIFT
control = CONTROL
alt = ALT

switch_between_windows = [
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
]

grow_windows = [
    Key([mod, control], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, control], "space", lazy.layout.normalize(), desc="Reset all window sizes"),
]

toggle_layouts = [
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
]

qtile_controls = [
    Key([mod, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

window_controls = [
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
]

volume_controls = [
    Key([mod], "F12", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([mod], "F11", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([mod], "F10", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
]

launch_apps = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([alt], "F12", lazy.spawn("rofi -show drun -theme ~/.config/bspwm/src/rofi-themes/Launcher.rasi"), desc="Launch rofi"),
]

groups = [
    Key([mod], str(i + 1), lazy.group[group.name].toscreen(), desc=f"Switch to group {group.name}") 
    for i, group in enumerate(GROUPS_LIST)
] + [
    Key([mod, shift], str(i + 1), lazy.window.togroup(group.name, switch_group=True), desc=f"Move focused window to group {group.name}") 
    for i, group in enumerate(GROUPS_LIST)
]

KEY_MAP: list = (
    switch_between_windows + 
    grow_windows + 
    toggle_layouts + 
    qtile_controls + 
    window_controls + 
    volume_controls + 
    launch_apps +
    groups
)
