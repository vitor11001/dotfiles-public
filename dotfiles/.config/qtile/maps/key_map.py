from libqtile.config import Key
from libqtile.lazy import lazy
from global_vars import MOD, TERMINAL

mod = MOD
terminal = TERMINAL


KEY_MAP = [
    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "space", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Qtile controls
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key([mod, "shift"], "q",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),

    # Window controls, fullscreen, floating, kill
    Key(
        [mod], "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod], "t", 
        lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"
    ),
    Key(
        [mod], "c", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    # Volume controls
    Key([mod], "F12", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([mod], "F11", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([mod], "F10", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Launch Apps
    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
    Key(
        [mod], "d", 
        lazy.spawn("rofi -show drun"), 
        desc="Launch Rofi"
    ),
    
]
