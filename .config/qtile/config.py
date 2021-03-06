# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import os

mod = "mod4"
terminal = "kitty"

home = os.path.expanduser('~')

MYCOLORS = [
    '#073642',
    '#dc322f',
    '#00ff2a',
    '#b58900',
    '#268bd2',
    '#d33682',
    '#2aa198',
    '#eee8d5'
]

BLACK = MYCOLORS[0]
RED = MYCOLORS[1]
GREEN = MYCOLORS[2]
YELLOW = MYCOLORS[3]
BLUE = MYCOLORS[4]
MAGENTA = MYCOLORS[5]
CYAN = MYCOLORS[6]
WHITE = MYCOLORS[7]

default_browser = "google-chrome-stable"
default_editor = "codium"
default_explorer = "pcmanfm"

volumecontrol = home + "/.local/bin/volumecontrol"
brightnesscontrol = home + "/.local/bin/brightnesscontrol"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # dmenu launcher
    Key([mod], "d", lazy.spawn("dmenu_run -p 'Run: '"), desc='Run Launcher'),
    # restart qtile
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    # browser
    Key([mod], "b", lazy.spawn(default_browser), desc='Start Web Browser'),
    Key([mod], "t", lazy.spawn(default_editor), desc='Start Text Editor'),
    Key([mod], "e", lazy.spawn(default_explorer), desc='Start File Explorer'),
    Key([mod], "m", lazy.spawn("meld"), desc="Start Meld"),
    Key([mod], "g", lazy.spawn("gitkraken"), desc="Start Gitkraken"),

    # fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='Toggle fullscreen'),

    # dmenu scripts
    Key([mod, "shift"], "e", lazy.spawn("dm-logout"), desc="Logout Screen"),
    Key([mod, "shift"], "w", lazy.spawn("dm-wifi"), desc="Wifi Menu"),
    Key([mod, "shift"], "s", lazy.spawn("dm-websearch"), desc="Web Search"),
    Key([mod, "shift"], "v", lazy.spawn("dm-kill"), desc="Kill App"),
    Key([mod, "shift"], "c", lazy.spawn("dm-maim"), desc="Take screenshot"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Audio
    Key([], "XF86AudioMute", lazy.spawn(volumecontrol + " mute"), desc="Mute Audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(volumecontrol + " down"), desc="Volume down"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volumecontrol + " up"), desc="Volume up"),
    Key([mod, "shift"], "m", lazy.spawn(volumecontrol + " mutemic"), desc="Mute mic"),

    Key([], "XF86MonBrightnessDown", lazy.spawn(brightnesscontrol + " down"), desc="Brightness down"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(brightnesscontrol + " up"), desc="Brightness up"),
]

group_names = [("DEV", {'layout': 'columns'}),
               ("SYS", {'layout': 'columns'}),
               ("WWW", {'layout': 'columns'}),
               ("DOC", {'layout': 'columns'}),
               ("VMS", {'layout': 'floating'}),
               ("CHAT", {'layout': 'columns'}),
               ("MED", {'layout': 'columns'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(i), lazy.group[name].toscreen(),
            desc="Switch to group {}".format(name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    layout.Bsp(),
    layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    layout.RatioTile(),
    layout.Tile(),
    layout.TreeTab(),
    layout.VerticalTile(),
    layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.GenPollText(
                    update_interval=1,
                    **widget_defaults,
                    func=lambda: subprocess.check_output(os.path.expanduser("~/.local/bin/statusbar/volumecontrol")).decode(),
                    mouse_callbacks = {
                        'Button1': lambda: qtile.cmd_spawn(os.path.expanduser("~/.local/bin/statusbar/volumecontrol down"), shell=True),
                        'Button2': lambda: qtile.cmd_spawn(os.path.expanduser("~/.local/bin/statusbar/volumecontrol mute"), shell=True),
                        'Button3': lambda: qtile.cmd_spawn(os.path.expanduser("~/.local/bin/statusbar/volumecontrol up"), shell=True)
                    }
                ),
                widget.DF(
                    partition = '/home',
                    visible_on_warn = False,
                    measure = 'G',
                ),
                widget.CheckUpdates(
                    **widget_defaults,
                    update_interval = 120,
                    distro = 'Arch_paru',
                    display_format = 'Updates: {updates}',
                    color_have_updates = GREEN,
                    execute = 'kitty -e paru',
                    no_update_string = "No updates available",
                ),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            30,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
