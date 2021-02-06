These are a loose collection of functions which can be used to perform a variety of actions within Tabletop Simulator.

These functions can utilize in-game Objects, but none of them can be enacted on in-game Objects. They all deal with the game space.

##Function Summary

###Global Functions
General functions which work within any script.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="fnc_addcontextmenuitem"></a>addContextMenuItem([<span class="tag str"></span>](types.md)&nbsp;label, [<span class="tag fun"></span>](types.md)&nbsp;toRunFunc, [<span class="tag boo"></span>](types.md)&nbsp;keep_open, [<span class="tag boo"></span>](types.md)&nbsp;require_table) | Adds a menu item to the Global right-click context menu. Global menu is shown when player right-clicks on empty space or table. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#addcontextmenuitem)
clearContextMenu() | Clears all menu items added by function [addContextMenuItem](#fnc_addcontextmenuitem). | [<span class="ret boo"></span>](types.md) |
copy([<span class="tag tab"></span>](types.md)&nbsp;object_list) | Copy a list of Objects to the clipboard. Works with [paste(...)](#paste). | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#copy)
destroyObject([<span class="tag obj"></span>](types.md)&nbsp;obj) | Destroy an Object. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#destroyobject)
<a class="anchor" id="fliptable"></a>flipTable() | Flip the table. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="getallobjects"></a>getAllObjects() | Returns Table of all spawned [Objects](object.md) in the game. | [<span class="ret tab"></span>](types.md) |
getObjectFromGUID([<span class="tag str"></span>](types.md)&nbsp;guid) | Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist. | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#getobjectfromguid)
<a class="anchor" id="getseatedplayers"></a>getSeatedPlayers() | Returns Table of the [Player Colors](player-color.md) strings of seated players. | [<span class="ret tab"></span>](types.md) |
group([<span class="tag tab"></span>](types.md)&nbsp;objects) | Groups objects together, like how the `G` key does for players. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#group)
paste([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy). | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#paste)
<a class="anchor" id="setlookingforplayers"></a>setLookingForPlayers([<span class="tag boo"></span>](types.md)&nbsp;lfp) | Enables/disables looking for group. This is visible in the server browsers, indicating if you are recruiting for a game. | [<span class="ret boo"></span>](types.md) |
spawnObject([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Spawns an Object. See [Built-in](built-in-object.md) and [Custom](custom-game-objects.md) Spawnable Object pages for further details. | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#spawnobject)
spawnObjectData([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Spawns an Object using a data table. Works with [getData()](object.md#getdata). | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#spawnobjectdata)
spawnObjectJSON([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Spawns an Object using a JSON string. Works with [getJSON()](object.md#getjson). | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#spawnobjectjson)
startLuaCoroutine([<span class="tag obj"></span>](types.md)&nbsp;function_owner, [<span class="tag str"></span>](types.md)&nbsp;function_name) | Start a coroutine. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#startluacoroutine)
stringColorToRGB([<span class="tag str"></span>](types.md)&nbsp;player_color) | Converts a [Player Color](player-color.md) string into a Color Table for tinting. | [<span class="ret col"></span>](types.md#color) | [<span class="i"></span>](#stringcolortorgb)

####Hotkey Functions
Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="fnc_addhotkey"></a>addHotkey([<span class="tag str"></span>](types.md)&nbsp;label, [<span class="tag fun"></span>](types.md)&nbsp;toRunFunc, [<span class="tag boo"></span>](types.md)&nbsp;trigger_on_key_up) | Adds a bindable Hotkey to the game. User may assign a key to it in Options->Game Keys after the game was created. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#addhotkey)
<a class="anchor" id="fnc_clearhotkeys"></a>clearHotkeys() | Clears all Hotkeys added by [addHotkey](#fnc_addhotkey) | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="fnc_showhotkeyconfig"></a>showHotkeyConfig() | Shows the Hotkey configuration window under Options->Game Keys. | [<span class="ret boo"></span>](types.md) |

###Message Functions
Functions which handle sending and displaying data.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
broadcastToAll([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print an on-screen message to all Players, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#broadcasttoall)
broadcastToColor([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag str"></span>](types.md)&nbsp;player_color, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print an on-screen message to a specified Player, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#broadcasttocolor)
log([<span class="tag var"></span>](types.md)&nbsp;value, [<span class="tag str"></span>](types.md)&nbsp;label, [<span class="tag str"></span>](types.md)&nbsp;tags) | Logs a message to the _host's_ System Console. (Shortcut: ~) | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#log)
logString([<span class="tag var"></span>](types.md)&nbsp;value, [<span class="tag str"></span>](types.md)&nbsp;label, [<span class="tag str"></span>](types.md)&nbsp;tags, [<span class="tag boo"></span>](types.md)&nbsp;concise, [<span class="tag boo"></span>](types.md)&nbsp;displayTag) | _Returns_ a String formatted similarly to the output of [log(...)](#log). | [<span class="ret str"></span>](types.md) | [<span class="i"></span>](#logstring)
logStyle([<span class="tag str"></span>](types.md)&nbsp;tag, [<span class="tag col"></span>](types.md#color)&nbsp;tint, [<span class="tag str"></span>](types.md)&nbsp;prefix, [<span class="tag str"></span>](types.md)&nbsp;postfix) | Set style options for the specified tag type for the log. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#logstyle)
print([<span class="tag str"></span>](types.md)&nbsp;message) | Prints a string into chat that only the host is able to see. Used for debugging scripts. | [<span class="ret nil"></span>](types.md) | [<span class="i"></span>](#print)
printToAll([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print a message into the chat of all connected players. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#printtoall)
printToColor([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag str"></span>](types.md)&nbsp;player_color, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print a message to a specific [Player Color](player-color.md). | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#printtocolor)
<a class="anchor" id="sendexternalmessage"></a>sendExternalMessage([<span class="tag tab"></span>](types.md)&nbsp;data) | Send a table to your external script editor, most likely Atom. This is for custom editor functionality. | [<span class="ret boo"></span>](types.md) |



---

##Function Details

###Global Function details

####addContextMenuItem(...)

[<span class="ret boo"></span>](types.md)&nbsp;Adds a menu item to the Global right-click context menu. Global menu is shown when player right-clicks on empty space or table.

!!!info "addContextMenuItem(label, toRunFunc, keep_open, require_table)"
	* [<span class="tag str"></span>](types.md) **label**: Label for the menu item.
	* [<span class="tag fun"></span>](types.md) **toRunFunc**: Execute if menu item is selected.
        * [<span class="tag str"></span>](types.md) **player_color** [Player Color](player-color.md) who selected the menu item.
        * [<span class="tag vec"></span>](types.md) **menu_position** Global position of the right-click context menu.
	* [<span class="tag boo"></span>](types.md) **keep_open**: Keep context menu open after menu
     item was selected.
        * {>>Optional, Default: keep_open = false. Close context menu after selection.<<}
	* [<span class="tag boo"></span>](types.md) **require_table**: Show added menu item when right-clicked on empty space or table.            
		* {>>Optional, Default: require_table = false. Show when right-clicked on empty space or table <<}

``` Lua
function onLoad()
    addContextMenuItem("doStuff", itemAction)
end

function itemAction(player_color, menu_position)
    print(player_color)
end
```

---

####copy(...)

[<span class="ret boo"></span>](types.md)&nbsp;Copy a list of Objects to the clipboard. Works with [paste(...)](#paste).

!!!info "copy(object_list)"
	* [<span class="tag tab"></span>](types.md) **object_list**: A Table of in-game objects to be copied.
		* {>>This is similar to highlighting the objects in-game and copying them.<<}

``` Lua
object_list = {
	getObjectFromGUID("######"),
	getObjectFromGUID("######"),
}
copy(object_list)
```

---

####destroyObject(...)

[<span class="ret boo"></span>](types.md)&nbsp;Destroy an Object.

!!!info "destroyObject(obj)"
	* [<span class="tag obj"></span>](types.md) **obj**: The Object you wish to delete from the instance.

---


####getObjectFromGUID(...)

[<span class="ret obj"></span>](types.md)&nbsp;Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist.

!!!info "getObjectFromGUID(guid)"
	* [<span class="tag str"></span>](types.md) **guid**: GUID of the Object to get a reference of.
		* {>>GUID can be obtained by right clicking an object and going to Scripting.<<}
		* {>>In a script, it can be obtained from any Object by using .getGUID().<<}


---

####group(...)

[<span class="ret tab"></span>](types.md)&nbsp;Groups objects together, like how the `G` key does for players. It returns a table of object references to any decks/stacks formed.

Not all objects CAN be grouped. If the G key won't work on them, neither will this function.


!!!info "group(objects)"
	* [<span class="tag tab"></span>](types.md) **objects**: A list of objects to be grouped together.

!!!info "Format of the returned table"
    * [<span class="tag tab"></span>](types.md) A table containing the grouped objects, numerically indexed.
		* [<span class="tag obj"></span>](types.md) Object(s)
			* {>>Different types of object are grouped independently i.e. cards will form into a deck, each type of checker will form their own stack.<<}

``` Lua
-- Example
function onLoad()
    local objects = {
        -- IMPORTANT: To get the example to work, you need to replace ###### by a real GUID of the object.
        getObjectFromGUID("######"), -- card
        getObjectFromGUID("######"), -- card
        getObjectFromGUID("######"), -- checker
        getObjectFromGUID("######"), -- checker
    }
    local objGroupedList = group(objects)
    log(objGroupedList)
end

```
``` Lua
-- Possible Output for objGroupedList
{
    1: <Deck>
    2: <CheckerStack>
}
```


---

####paste(...)

[<span class="ret tab"></span>](types.md)&nbsp;Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy).

!!!info "paste(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing instructions of where to spawn the Objects.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position of the first object to paste.
			* {>>Optional, defaults to {0, 3, 0}.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.snap_to_grid**: If snap-to-grid is active on the spawned item/s.
			* {>>Optional, defaults to false (off).<<}


---


####spawnObject(...)

[<span class="ret obj"></span>](types.md)&nbsp;Spawns an Object. See [Built-in](built-in-object.md) and [Custom](custom-game-objects.md) Spawnable Objects pages for details of specific spawnable objects.

If you are spawning a **custom Object**, you should call [setCustomObject](object.md#setcustomobject) immediately after spawnObject to set its custom properties.

!!!tip
	Spawned Objects take a moment to be physically spawned into the game. The purpose of the callback functionality is to allow you to run additional actions after the Object has been initiated fully into the instance. You can also add a delay after spawning using a [Wait](wait.md) function.

!!!info "spawnObject(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to determine how spawnObject will act.
		* [<span class="tag str"></span>](types.md) **parameters.type**: [Built-in](built-in-object.md) or [Custom](custom-game-objects.md) Game Object name.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to place Object.
			* {>>Optional, defaults to {x=0, y=3, z=0}.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the Object.
			* {>>Optional, defaults to {x=0, y=0, z=0}<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the Object.
			* {>>Optional, defaults to {x=1, y=1, z=1}<<}
		* [<span class="tag boo"></span>](types.md) **parameters.sound**: If the spawned Object noise is played.
			* {>>Optional, defaults to true.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.snap_to_grid**: If snap-to-grid is active on the Object.
			* {>>Optional, defaults to false.<<}
		* [<span class="tag fun"></span>](types.md#function) **parameters.callback_function**: The function to activate after the Object has finished spawning into the scene.
			* {>>Optional, defaults to not being used.<<}
			* {>>A reference to the object spawned is always passed to callback_function. See the example for how to access it.<<}


``` Lua
function onLoad()
	futureName = "Spawned By Script!"
	spawnParams = {
		type = "rpg_BEAR",
		position          = {x=0, y=3, z=-5},
		rotation          = {x=0, y=90, z=0},
		scale             = {x=2, y=2, z=2},
		sound             = false,
		snap_to_grid      = true,
		callback_function = function(obj) spawn_callback(obj, "Bear", "Green") end
	}
	spawnObject(spawnParams)
end

function spawn_callback(object_spawned, name, color)
	object_spawned.setName(name)
	object_spawned.setColorTint(color)
end
```

---


####spawnObjectData(...)

Spawns an Object using a data table. Works with [getData()](object.md#getdata). It works just like spawnObject, but instead of a `type`, you supply a `data` table. The other parameters will overwrite those in the Data.

!!!info "spawnObjectData(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to determine how spawnObjectData will act.
		* [<span class="tag tab"></span>](types.md) **parameters.data**: [getData()](object.md#getdata) table.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to place Object.
			* {>>Optional, defaults to data table's value.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the Object.
			* {>>Optional, defaults to data table's value.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the Object.
			* {>>Optional, defaults to data table's value.<<}
		* [<span class="tag fun"></span>](types.md#function) **parameters.callback_function**: The function to activate after the Object has finished spawning into the scene.
			* {>>Optional, defaults to not being used.<<}
			* {>>A reference to the object spawned is always passed to callback_function. See the example for how to access it.<<}

``` Lua
local futureName = "Spawned By Script!"
spawnParams = {
    data              = self.getData(),
    position          = {x=0, y=3, z=-5},
    rotation          = {x=0, y=90, z=0},
    scale             = {x=2, y=2, z=2},
    callback_function = function(obj) spawn_callback(obj, futureName, "Red") end
    --alternative format:
    --callback_function = |obj| spawn_callback(obj, futureName, "Red")
}
spawnObjectData(spawnParams)

function spawn_callback(object_spawned, name, color)
	object_spawned.setName(name)
	object_spawned.setColorTint(color)
end
```

!!!tip
    You can modify an object's data prior to spawning, this is currently the only way to "Create States" via API (using the "States" key).

---


####spawnObjectJSON(...)

Spawns an Object using a JSON string. Works with [getJSON()](object.md#getjson). It works just like spawnObject, but instead of a `type`, you supply a `json` string. The other parameters will overwrite those in the JSON.

!!!tip
	Spawned Objects take a moment to be physically spawned into the game. The purpose of the callback functionality is to allow you to run additional actions after the Object has been initiated fully into the instance. You can also add a delay after spawning using a [Wait](wait.md) function.

!!!info "spawnObjectJSON(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to determine how spawnObjectJSON will act.
		* [<span class="tag str"></span>](types.md) **parameters.json**: [getJSON()](object.md#getjson) string.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to place Object.
			* {>>Optional, defaults to JSON's value.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the Object.
			* {>>Optional, defaults to JSON's value.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the Object.
			* {>>Optional, defaults to JSON's value.<<}
		* [<span class="tag fun"></span>](types.md#function) **parameters.callback_function**: The function to activate after the Object has finished spawning into the scene.
			* {>>Optional, defaults to not being used.<<}
			* {>>A reference to the object spawned is always passed to callback_function. See the example for how to access it.<<}

``` Lua
function onLoad()
	futureName = "Spawned By Script!"
	spawnParams = {
		json              = self.getJSON(),
		position          = {x=0, y=3, z=-5},
		rotation          = {x=0, y=90, z=0},
		scale             = {x=2, y=2, z=2},
		sound             = false,
		snap_to_grid      = true,
		callback_function = function(obj) spawn_callback(obj, futureName, "Red") end
		--alternative format:
		--callback_function = |obj| spawn_callback(obj, futureName, "Red")
	}
	spawnObject(spawnParams)
end

function spawn_callback(object_spawned, name, color)
	object_spawned.setName(name)
	object_spawned.setColorTint(color)
end
```

---




####startLuaCoroutine(...)

[<span class="ret boo"></span>](types.md)&nbsp;Start a coroutine. A coroutine is similar to a function, but has the unique ability to have its run paused until the next frame of the game using `coroutine.yield(0)`.

!!!Attention
	You MUST return a 1 at the end of any coroutine or it will throw an error.

!!!info "startLuaCoroutine(function_owner, function_name)"
	* [<span class="tag obj"></span>](types.md) **function_owner**: The Object that the function being called is on. Global is a valid target.
	* [<span class="tag str"></span>](types.md) **function_name**: Name of the function being called as a coroutine.

``` Lua
function onLoad()
	startLuaCoroutine(Global, "print_coroutine")
end

-- Prints a message, waits 250 frames, prints another message
function print_coroutine()
	print("Routine has Started")
	count = 0
	while count < 250 do
		count = count + 1
		coroutine.yield(0)
	end

	print("Routine has Finished")

	return 1
end
```

---

####stringColorToRGB(...)

[<span class="ret col"></span>](types.md)&nbsp;Converts a [Player Color](player-color.md) string into a Color Table for tinting.

!!!info "stringColorToRGB(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color** A String of a [Player Color](player-color.md).

``` Lua
printToAll("Blue message", stringColorToRGB("Blue"))
```

---

####addHotkey(...)

[<span class="ret boo"></span>](types.md)&nbsp;Adds a bindable Hotkey to the game. User may assign a key to it in Options->Game Keys after the game was created.

!!!info "addHotkey(label, toRunFunc, trigger_on_key_up)"
	* [<span class="tag str"></span>](types.md) **label**: A String for the Hotkey.
	* [<span class="tag fun"></span>](types.md) **toRunFunc**(player_color, hovered_object, world_position, key_down_up): The function that is executed at the moment the binded key is pressed.
        * [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player-color.md) who pressed the Hotkey.
        * [<span class="tag obj"></span>](types.md) **hovered_object**: The object over which the Player's pointer hovers at the moment. **nil** if there is no object under the Player's pointer.
        * [<span class="tag vec"></span>](types.md) **world_position**: [Word Position](types.md#position) of the Player's pointer who pressed the Hotkey.
        * [<span class="tag boo"></span>](types.md) **key_down_up**: Indicates the moment at which the function **toRunFunc** is executed.
            * **true**: Key is released.
            * **false**: Key is pressed.
	* [<span class="tag boo"></span>](types.md) **trigger_on_key_up**: Controls the timing at which the function **toRunFunc** is executed.
        * {>>Optional, Default: trigger_on_key_up = false.<<}
        * **true**: Executes the function 2 times. At the moment the key is pressed and released.
        * **false**: Executes the function 1 time. At the moment the key is pressed.

!!!important
    * The key binding does not overwrite the key binding under Setting. e.g. if "R" (default: shuffle) is assigned as Hotkey, the Hotkey function and the default shuffle is executed by pressing the key "R".
    * The added Hotkeys are not persistent, therefore the function addHotkey(...) needs to called each time the game is loaded.
        * The key assigned by the player remains, if the label is unchanged.

``` Lua
function onLoad()
    addHotkey("This is the first Hotkey for the game.", hotkey1)
    addHotkey("This is the second Hotkey for the game.", hotkey2)
end

function hotkey1(player_color, hovered_object, world_position, key_down_up)
    print(player_color)
end

function hotkey2(player_color, hovered_object, world_position, key_down_up)
    print(player_color)
end
```

---

###Message Function Details

####broadcastToAll(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print an on-screen message to all Players.

!!!info "broadcastToAll(message, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to display on-screen.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: A Table containing the RGB color tint for the text.

``` Lua
msg = "Hello all."
rgb = {r=1, g=0, b=0}
broadcastToAll(msg, rgb)
```

---


####broadcastToColor(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print an on-screen message to a specified Player and their in-game chat.

!!!info "broadcastToColor(message, player_color, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to display on-screen.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player-color.md) to receive the message.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB color tint for the text.

``` Lua
msg = "Hello White."
color = "White"
rgb = {r=1, g=0, b=0}
broadcastToColor(msg, color, rgb)
```

---


####log(...)

[<span class="ret boo"></span>](types.md)&nbsp;Logs a message to the _host's_ System Console (accessible from `~` pane of in-game chat window).

!!!info "log(value, label, tags)"
	* [<span class="tag var"></span>](types.md) **value**: The value you want to log.
	* [<span class="tag str"></span>](types.md) **label**: Text to be logged before `value`.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](types.md) **tags**: The log tag/style _or_ a space separated list of log tags/styles. (See: [logStyle(...)](#logstyle))
		* {>>Optional, defaults to logging with the <default> log style.<<}

If `value` is not already a [<span class="tag str"></span>](types.md), then it will be converted to a human-readable representation.

If `value` is a [<span class="tag tab"></span>](types.md), then the table's contents (keys &amp; values) will be displayed. The contents of nested tables will also be displayed up to a user-configurable depth.

!!!tip
	Table contents max depth is configurable via the `log_max_table_depth` System Console command.

As an advanced feature, multiple log tags may be provided by space-separating several tags (in the one String) provided as the `tags` parameter. The message style will be taken from the _first_ tag that the user has not explicitly disabled.

!!!example
	Log a simple message:
	``` Lua
	log("Something happened")
	```

!!!example
	Log a table (of objects):
	``` Lua
	log(getObjects())
	```

!!!example
	Log a message with a label and using the `"error"` log style:
	``` Lua
	log("Something unexpected happened.", "Oh no!", "error")
	```

---


####logString(...)

[<span class="ret str"></span>](types.md)&nbsp;_Returns_ a String formatted similarly to the output of [log(...)](#log). 

!!!info "logString(value, label, tags, concise, displayTag)"
	* [<span class="tag var"></span>](types.md) **value**: The value you want to log.
	* [<span class="tag str"></span>](types.md) **label**: Text to be logged before `value`.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](types.md) **tags**: The log tag/style _or_ a space separated list of log tags/styles.
		* {>>Optional, defaults to logging without any tags.<<}
	* [<span class="tag boo"></span>](types.md) **concise**: Whether the resultant String should be generated in a more compact form (less newline characters).
		* {>>Optional, defaults to `false`.<<}
	* [<span class="tag boo"></span>](types.md) **displayTag**: Whether the specified tag(s) should be included as prefix of the resultant String.
		* {>>Optional, defaults to `false`.<<}

If `value` is not already a [<span class="tag str"></span>](types.md), then it will be converted to a human-readable representation.

If `value` is a [<span class="tag tab"></span>](types.md), then the table's contents (keys &amp; values) will be included in the resultant String. The contents of nested tables will also be displayed up to a user-configurable depth.

!!!tip
	Table contents max depth is configurable via the `log_max_table_depth` System Console command.

In some circumstances log strings have newlines inserted e.g. between the `label` and the textual representation of `value`. Providing `true` as the value for `concise` will use space separators instead of newlines.

!!!example
	_Print_, as opposed to log, the contents of a table (of objects):
	``` Lua
	print(logString(getObjects()))
	```

---


####logStyle(...)

[<span class="ret boo"></span>](types.md)&nbsp;Configures style options for a [log(...)](#log) tag.

!!!tip
	Tag log styles can also be set via the System Console with the `log_style_tag` command.

!!!info "logStyle(tag, tint, prefix, postfix)"
	* [<span class="tag str"></span>](types.md) **tag**: A String of the log's tag.
	* [<span class="tag col"></span>](types.md#color) **tint**: RGB value to tint the log entry's text.
		* {>>String color will also work. Example: "Red"<<}
	* [<span class="tag str"></span>](types.md) **prefix**: Text to place before this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](types.md) **postfix**: Text to place after this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}

!!!example
	Sets the log style (grey text and a suffix) for the log tag `"seats"`. Then proceeds to log a table of available seat colors, using this tag/style.
	``` Lua
	logStyle("seats", {0.5, 0.5, 0.5}, "", "End List")
	log(Player.getAvailableColors(), nil, "seats")
	```

---


####print(...)

[<span class="ret nil"></span>](types.md)&nbsp;Print a string into chat that only the host is able to see. Used for debugging scripts.

!!!info "print(message)"
	* [<span class="tag str"></span>](types.md) **message**: Text to print into the chat log.


---


####printToAll(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print a message into the in-game chat of all connected players.

!!!info "printToAll(message, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to place into players' in-game chats.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToAll("Hello World!", {r=1,g=0,b=0})
```

---


####printToColor(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print a message to the in-game chat of a specific player.

!!!info "printToColor(message, player_color, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to place into the player's in-game chat.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player-color.md) of the player that will receive the message.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToColor("Hello Red.", "Red", {r=1,g=0,b=0})
```

---
