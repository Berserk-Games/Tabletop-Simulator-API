# VR Beta

VR in Tabletop Simulator is under active development, and as such is changing all the time.  This thread will be updated each patch with any changes relevant to playing in VR.  Both Vive and Rift are supported, though control layout may change where necessary (due to thumbstick for instance).


## Reverting to original controls

If you would rather just go back to how the VR controls used to work then you can do that in the VR settings UI or via this command in system console:

* `+vr_controls_original`

Note that this will is likely to be deprecated at some point.


## v11.1 VR changes

* Updated to SteamVR action+binding system.
* VR controllers can now act as a joypad for control binding; turn on `Joypad Emulation` in the VR settings, and make sure the `Controller` option at the bottom of the Controls window is ticked.
* Using above, most normal control bindings should work where approriate in VR (e.g. `Copy`, `Paste`, `Flip`, etc.)
* Can now attach the VR UI screen to a controller: rotate your wrist as if you were looking at your watch.
* Added Drawings, Text, Gizmo, Snap, and Decal tools.
* Fixed Zone tools, Line tool (displays measurement, arrow ping).
* Fixed objects (such as chess pieces) warping into upright rotation on grab (now smooth-moves)
* `Trigger Click Effect` now known as `Orient Object`
* `Orient Object` action should now work on all card-like objects (dominos, mahjong tiles, etc).  Also works on jigsaw pieces: will rotate them to next 90-degree angle.
* Fixed snap points.
* Made resize room visual effect less opaque.
* Fixed non-hands objects being picked up by VR virtual hand.
* Fixed tooltips & icons on Oculus Rift.
* Pad bindings now use compass notation (i.e. `vr_left_pad_north` = left controller, up on pad)


## VR settings

The VR settings UI allows you to tailor your VR experience to your own preferences.  All the settings it contains also have a console command; you may script them or bind them in the console (see VR Commands below).

New items added to the VR settings dialog in v11.1:

* `Physical UI Screen`, `Attached UI Screen`, `UI Scale` - Control how the VR UI Screen is displayed.
* `Display VR Players` - Can select whether other VR players are visible (off, hands-only, hands+headset)
* `Wall mode` - will rotate room so the table is vertical.
* `Align Zoomed Object` - Zoom object now matches rotation of the object it is displaying.
* `Grabbing Hides Gem` - Hides controller gem when holding on object.
* `Hover Tooltips` - Display UI hover tooltips above controller.
* `Interface Click Threshold` - When the interface click action is bound to an analog input it will use this value.
* `Laser Activation Threshold` - When laser activation is bound to an analog input it will use this value.
* `Laser Beam Thickness`, `Laser Dot Size` - Control how big the laser pointer is.
* `Left Tool Hotkeys` & `Right Tool Hotkeys` - Bind the default tool select hotkeys to the pad.
* `Tooltips Action Enabled` - Can be turned off here to disable tooltips (instead of having to unbind the action).
* `Floor of mist` - change the floor.


## Current VR Controls*

*Subject to change!

### Vive

* Touching the pad will activate the laser, and clicking the center will Click on whatever you are aiming at.
* Grab/Tool is bound to Trigger.
* Movement is bound to Grip.
* Menu is bound to the Application button.

### Rift

* Squeeze the trigger to activate the laser, and pull it to Click on what you're aiming at.
* Grab/Tool is bound to Grip
* Movement is bound to A/X
* Menu is bound to B/Y

### Other VR Hardware

* For information on other VR hardware see the section on `SteamVR Action+Binding`
* Here is an overview of [Tabletop Simulator's default bindings for Vive and Rift](http://blog.onelivesleft.com/2019/03/tabletop-simulators-steamvr-binding.html)

### Common

* Hold the Movement button on one controller to move as if you are pulling yourself around, or on both controllers to rotate + scale.
* Hit the Menu button to display the system menu on the UI screen, or hold the Menu button for 3 seconds to reset your position.
* Pad Left, Right and Up are used as tool hotkeys: click them to use the tool they show, or hold them to store your current tool. (You may disable tool bindings on either or both controllers, inside the VR settings window).
* Pad Down is Zoom.
* Zoom turns the controller into a zoomed-in version of the last active object.  Clicking Pad Down will keep the controller in zoom mode until you click it again, and if you touch Pad Left or Pad Right while zoomed you can alter the scale of the object.
* Objects may be activated either by touching them with the gem, or by pointing at them with the laser beam.  If an object is active then you can Grab  it or Click on it (for context menu).
* While holding an object the pad will change function depending on what the object is.  In general pad left and pad right will rotate it, and pad up will flip it.
* Clicking the Trigger while holding an object will toggle the Orient Object action: a card/domino will straighten and hide from other players, a jigsaw piece will rotate to next 90-degree step.

### SteamVR Action+Binding : Customize Controls

SteamVR's new action + binding system means that you may customize the control scheme almost without limitation.  It also means that you can get unsupported hardware to work simply by setting up your own control scheme.

You may access the controller binding interface inside VR or on your desktop in a web browser.

* VR: in SteamVR settings go to `Controller Binding`
* Desktop: go to http://localhost:8998/dashboard/controllerbinding.html (you must be running SteamVR in ther background)

Click on `TableTop Simulator`, then on the binding you want to edit, or `create binding` to make a new one.

There are some actions deemed "Mandatory" that you will need to assign (Grab and Main Menu), and a lot more that are "Suggested". This would be a simple minimal setup:

* `Grab` on grip (use as button : held)
* `Main Menu` on a button (click)
* `Enable Movement` on a button (held)
* `Activate Laser Pointer` on trigger pull
* `Interface Click` on trigger pull
* `Orient Object` on trigger click
* `Peek` on trigger press
* `Display Tooltips` on the same binding as Enable Movement

Touchpad for context actions:
* `North/South/East/West/Center Touch` on relevant Touchpad Touch
* `North/South/East/West/Center Click` on relevant Touchpad Click
* `Pad Click` on touchpad use as button : click

Joystick for context actions:
* `North/South/East/West Touch + Click` on joystick directions
* `Center Click` & `Pad Click` on joystick click (use as button)
* `Center Touch` on joystick touch (use as button)

You might have to add `Pose` and `Haptic` bindings: in Pose set `Left Hand Raw` / `Right Hand Raw` to `Pose`, and all `Haptics` set to `Haptics`.

* Walkthrough of [Tabletop Simulator's default bindings for Vive and Rift](http://blog.onelivesleft.com/2019/03/tabletop-simulators-steamvr-binding.html)

Of course, you are free to bind everything to suit yourself, and if you make a good layout you can upload to the workshop for others to use too.

For example, say you wanted to only use the right controller to pick up and manipulate objects, thus freeing up the left controller's pad for any other actions you wished.  Go into the `Controller Binding` in SteamVR settings, hit the `Edit these bindings` button (and untick `Mirror Mode` if it is on), and on the left controller hit the bin icon next to the pad sections which are bound to `NORTH_TOUCH`, `NORTH_CLICK`, etc.  The left controller will now no longer send those actions to TTS - make sure you leave its `Button #` bindings intact.  In TTS, turn on `Joypad Emulation` in the VR Settings UI, and then on the standard `Controls` window you can tick the `Controller` checkbox at the bottom, and then use each direction on the left pad for any useful action in that window you wish.  Note that some actions have a VR specific version which is not compatible with the standard actions (don't use the standard `Grab` action for instance; use the `Grab` action in the SteamVR `Controller Binding` UI instead).


## Editting autoexec

You can do this in TTS by typing `edit autoexec` in the system console, or out-with the game (with notepad for example) by editing this file in your user folder: `Documents\My Games\Tabletop Simulator\autoexec.cfg`
As of v11 you no longer need to do this to make most commands store their setting; they will do that automatically.  However, you may wish to edit autoexec in order to set up more personalized bindings (see below).


## VR commands

You no longer need to use console commands to customize your VR experience as you can access all the most relevant ones for VR in the VR Settings UI.  However, the commands are still there and if you want to use them you are free to do so.  Any command which is an ON/OFF command can be set by typing it with a prefix: `+` will turn on that setting, `-` will turn it off, `!` will toggle it.  For example, `+vr_wall_mode` will enable wall mode, while `!vr_wall_mode` will turn it off if it is on, and on if it is off.
The command version of the settings is probably most useful for allowing you to `bind` the setting to a button on the VR controller.   To make this persist you must put it in your autoexec.  For example, if you unticked the `Left Tool Hotkeys` option in the VR settings, you would free up the left controller pad for your own bindings (while not holding something).  You could then edit your autoexec to something like:
```
bind vr_left_pad_west sendkey Keypad1
bind vr_left_pad_north !vr_ui_floating
bind vr_left_pad_east add vr_mode_ui_attachment 1 3
```
This sets the left pad to:
* left on the pad (west) emulates a keypress: 1 on the numeric keypad, i.e. `Scripting 1`
* up on the pad (north) toggles whether the UI screen will be on the wall or floating in world space.
* right on the pad (east) will cycle the UI screen attachment when it is not on the wall: floating above the table, attached to left controller, attached to right controller.

To investigate the VR commands in the console, type `help vr`; this will give you a summary of them all.  Type `help <command>` to get specific info on <command>.


### New in v11.1:

* `sendkey`
* `vr_display_network_players_off`
* `vr_display_network_players_hands`
* `vr_display_network_players_all`
* `vr_grabbing_hides_gem`
* `vr_hover_tooltips`
* `vr_interface_click_threshold`
* `vr_joypad_emulation`
* `vr_laser_activation_threshold`
* `vr_laser_beam_thickness`
* `vr_laser_dot_size`
* `vr_left_controller_bind_tool_hotkeys`
* `vr_mode_display_network_players`
* `vr_mode_ui_attachment`
* `vr_right_controller_bind_tool_hotkeys`
* `vr_tooltips_action_enabled`
* `vr_ui_attach_left`
* `vr_ui_attach_right`
* `vr_ui_detached`
* `vr_ui_floating`
* `vr_ui_scale`
* `vr_ui_suppressed`
* `vr_wall_mode`
* `vr_zoom_object_aligned`

### Renamed

* `vr_thumbstick_repeat_duration` -> `vr_interface_repeat_duration`
* `vr_trigger_click_effect_delay` -> `vr_orient_object_delay`

### Removed

* `vr_cards_held_like_in_hand`
* `vr_tooltips_when_gripping`
* `vr_trigger_activates_laser`
* `vr_trigger_activates_ui`
* `vr_trigger_click_effect`
