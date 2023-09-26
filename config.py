from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

powerline = {
    "decorations": [
        PowerLineDecoration(path="forward_slash",)
    ]
}

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

mod = "mod4"
myBrowser = "firefox"
myTerm = "alacritty"

keys = [

Key([mod], "j", lazy.layout.left()),
Key([mod], "l", lazy.layout.right()),
Key([mod], "k", lazy.layout.down()),
Key([mod], "i", lazy.layout.up()),
Key([mod, "shift"], "j", lazy.layout.swap_left()),
Key([mod, "shift"], "l", lazy.layout.swap_right()),
Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
Key([mod, "shift"], "i", lazy.layout.shuffle_up()),
Key([mod], "h", lazy.layout.grow()),
Key([mod], "u", lazy.layout.shrink()),
Key([mod], "o", lazy.layout.normalize()),
Key([mod], "p", lazy.layout.maximize()),
Key([mod, "shift"], "space", lazy.layout.flip()),

    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
   	 Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='browser'
             ),

	Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Term'
             ),

	Key([mod], "f",
             lazy.spawn('thunar'),
             desc='file manager'
             ),

	Key(["Control"], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),

	Key([mod, "shift"], "Return",
             lazy.spawn('rofi -show drun -show-icons -icon-theme "Gruvbox-Plus-Dark"'),
             desc='rofi drun'
             ),

	Key(["Control"], "Tab",
             lazy.spawn('rofi -show window -show-icons -icon-theme "Gruvbox-Plus-Dark"'),
             desc='Current windows'
             ),
#Key([mod], "F6", lazy.spawn("brightnessctl set +5%")),
#Key([mod], "F5", lazy.spawn("brightnessctl set -5%")),

# Brightness
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

# Volume
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

]

groups = [
	Group('1', label=' 󰖟 '),
	Group('2', label='  '),
	Group('3', label=' 󰅭 '),
	Group('4', label=' 󰭻 '),
	Group('5', label=' 󰑈 '),
	Group('6', label=' 󰊗 '),
	Group('7', label='  '),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layout_theme = {"border_width": 3,
                "margin": 20,
                "border_focus": "#00A1D5",
                "border_normal": "#001D31"
                }
#colors
colors = {"green": "#00BE67",
	  "deepblue": "#001D31",
	  "blue": "#0d0970",
	  "sky": "#00A1D5",
	  "pink": "F500BD",
	  "whitepink": "FF86C9",
	  "black": "000000",
	  "white": "FFFFFF",
	  "grey": "121212",
	}


layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Columns(**layout_theme,),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=16,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
		#widget.CurrentLayout(),
                widget.CurrentLayoutIcon(
		background=colors["sky"],
		padding=5,
		),
		 widget.GroupBox(
			padding_x=3,
			highlight_method='line',
			highlight_color=colors["sky"],
			this_current_screen_border=colors["blue"],
			background=colors["sky"], **powerline
		),
                #widget.TextBox(
		#	text="",
		#	padding=0,
		#	fontsize=30,
		#	foreground=colors["sky"],
		#	background=colors["deepblue"],
		#),
		#widget.Sep(),
                widget.Prompt(
			background=colors["deepblue"],
		),
		widget.WindowName(
			background=colors["deepblue"],
		),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
			background=colors["deepblue"],
		),
		widget.Volume(
			fmt="  {}",
			background=colors["deepblue"],
		),
		widget.KeyboardLayout(configured_keyboards=['us','th'],
			background=colors["deepblue"],
			padding=5, **powerline
			),
		widget.Memory(
			fmt="  {}",
			foreground=colors["white"],
			background=colors["blue"],
			measure_mem='M',
			format='{MemUsed: .0f}{mm}',
			padding=2,
		),
		widget.CPU(
			format=' 󰍛 {load_percent}%',
			foreground=colors["white"],
			background=colors["blue"],
		),
		widget.ThermalSensor(
			fmt="  {}",
			foreground=colors["white"],
			background=colors["blue"], **powerline
		),
		widget.Battery(
#			format='{char} {percent:2.0%} {hour:d}:{min:02d}',
			charge_char='󱊦',
			discharge_char='󱊣',
			background=colors["whitepink"],
			foreground=colors["deepblue"],**powerline
			),
		widget.Clock(format=" %a %I:%M %p",
			background=colors["sky"],
			#foreground=colors["deepblue"],
			padding=5,
		),
		widget.QuickExit(default_text='  ',
			background=colors["sky"],
			#foreground=colors["deepblue"],
		),

            ],
            25,
            border_width=[2, 1, 2, 1],  # Draw top and bottom borders
            border_color=colors["sky"]  # Borders color 
      ),

	# set wallpapaer
	#wallpaper = '/home/tonst/Pictures/Wallpaper/peakpx.jpg',

	# set wallpaper mode
	#wallpaper_mode='stretch'

    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
