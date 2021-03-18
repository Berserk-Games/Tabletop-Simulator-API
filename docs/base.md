These are a loose collection of functions which can be used to perform a variety of actions within Tabletop Simulator.

These functions can utilize in-game Objects, but none of them can be enacted on in-game Objects. They all deal with the game space.

##Function Summary

###Global Functions
General functions which work within any script.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addContextMenuItem([<span class="tag str"></span>](types.md) label, [<span class="tag fun"></span>](types.md) toRunFunc, [<span class="tag boo"></span>](types.md) keep_open, [<span class="tag boo"></span>](types.md) require_table) | Adds a menu item to the Global right-click context menu. Global menu is shown when player right-clicks on empty space or table. | [<span class="ret boo"></span>](types.md) | [:i:](#addcontextmenuitem)
clearContextMenu() | Clears all menu items added by function [addContextMenuItem](#addcontextmenuitem). | [<span class="ret boo"></span>](types.md) |
copy([<span class="tag tab"></span>](types.md) object_list) | Copy a list of Objects to the clipboard. Works with [paste(...)](#paste). | [<span class="ret boo"></span>](types.md) | [:i:](#copy)
destroyObject([<span class="tag obj"></span>](types.md) obj) | Destroy an Object. | [<span class="ret boo"></span>](types.md) | [:i:](#destroyobject)
flipTable() {: #fliptable data-toc-label="flipTable()" data-toc-child-of="global-function-details" } | Flip the table. | [<span class="ret boo"></span>](types.md) |
getAllObjects() {: #getallobjects data-toc-label="getAllObjects()" data-toc-child-of="global-function-details" } | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [getObjects()](#getobjects)_.</p>Returns a Table of all [Objects](object.md) in the game _except hand zones_. | [<span class="ret tab"></span>](types.md) |
getObjectFromGUID([<span class="tag str"></span>](types.md) guid) | Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist. | [<span class="ret obj"></span>](types.md) | [:i:](#getobjectfromguid)
getObjects() {: #getobjects data-toc-label="getObjects()" data-toc-child-of="global-function-details" } | Returns a Table of all [Objects](object.md) in the game. | [<span class="ret tab"></span>](types.md) |
getObjectsWithTag([<span class="tag str"></span>](types.md) tag) | Returns Table of all [Objects](object.md) which have the specified tag attached. | [<span class="ret tab"></span>](types.md) | [:i:](#getobjectswithtag)
getObjectsWithAnyTags([<span class="tag tab"></span>](types.md) tags) | Returns Table of all [Objects](object.md) which have at least one of the specified tags attached. | [<span class="ret tab"></span>](types.md) | [:i:](#getobjectswithanytags)
getObjectsWithAllTags([<span class="tag tab"></span>](types.md) tags) | Returns Table of all [Objects](object.md) which have all of the specified tags attached. | [<span class="ret tab"></span>](types.md) | [:i:](#getobjectswithalltags)
getSeatedPlayers() {: #getseatedplayers data-toc-label="getSeatedPlayers()" data-toc-child-of="global-function-details" } | Returns a Table of the [Player Colors](player/colors.md) strings of seated players. | [<span class="ret tab"></span>](types.md) |
group([<span class="tag tab"></span>](types.md) objects) | Groups objects together, like how the `G` key does for players. | [<span class="ret tab"></span>](types.md) | [:i:](#group)
paste([<span class="tag tab"></span>](types.md) parameters) | Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy). | [<span class="ret tab"></span>](types.md) | [:i:](#paste)
setLookingForPlayers([<span class="tag boo"></span>](types.md) lfp) {: #setlookingforplayers data-toc-label="setLookingForPlayers(...)" data-toc-child-of="global-function-details" } | Enables/disables looking for group. This is visible in the server browsers, indicating if you are recruiting for a game. | [<span class="ret boo"></span>](types.md) |
spawnObject([<span class="tag tab"></span>](types.md) parameters) | Spawns an Object. See [Built-in](built-in-object.md) and [Custom](custom-game-objects.md) Spawnable Object pages for further details. | [<span class="ret obj"></span>](types.md) | [:i:](#spawnobject)
spawnObjectData([<span class="tag tab"></span>](types.md) parameters) | Spawns an Object using a data table. Works with [getData()](object.md#getdata). | [<span class="ret obj"></span>](types.md) | [:i:](#spawnobjectdata)
spawnObjectJSON([<span class="tag tab"></span>](types.md) parameters) | Spawns an Object using a JSON string. Works with [getJSON()](object.md#getjson). | [<span class="ret obj"></span>](types.md) | [:i:](#spawnobjectjson)
startLuaCoroutine([<span class="tag obj"></span>](types.md) function_owner, [<span class="tag str"></span>](types.md) function_name) | Start a coroutine. | [<span class="ret boo"></span>](types.md) | [:i:](#startluacoroutine)
stringColorToRGB([<span class="tag str"></span>](types.md) player_color) | Converts a [Player Color](player/colors.md) string into a Color Table for tinting. | [<span class="ret col"></span>](types.md#color) | [:i:](#stringcolortorgb)

####Hotkey Functions
Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addHotkey([<span class="tag str"></span>](types.md) label, [<span class="tag fun"></span>](types.md) toRunFunc, [<span class="tag boo"></span>](types.md) trigger_on_key_up)  | Adds a bindable hotkey to the game. | [<span class="ret boo"></span>](types.md) | [:i:](#addhotkey)
clearHotkeys() {: #clearhotkeys data-toc-label="clearHotkeys()" data-toc-child-of="hotkey-function-details" } | Clears all hotkeys previously added via [addHotkey(...)](#addhotkey). | [<span class="ret boo"></span>](types.md) |
showHotkeyConfig() {: #showhotkeyconfig data-toc-label="showHotkeyConfig()" data-toc-child-of="hotkey-function-details" } | Shows the hotkey configuration window under Options->Game Keys. | [<span class="ret boo"></span>](types.md) |

###Message Functions
Functions which handle sending and displaying data.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
broadcastToAll([<span class="tag str"></span>](types.md) message, [<span class="tag col"></span>](types.md#color) message_tint) | Print an on-screen message to all Players, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [:i:](#broadcasttoall)
broadcastToColor([<span class="tag str"></span>](types.md) message, [<span class="tag str"></span>](types.md) player_color, [<span class="tag col"></span>](types.md#color) message_tint) | Print an on-screen message to a specified Player, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [:i:](#broadcasttocolor)
log([<span class="tag var"></span>](types.md) value, [<span class="tag str"></span>](types.md) label, [<span class="tag str"></span>](types.md) tags) | Logs a message to the _host's_ System Console. (Shortcut: ~) | [<span class="ret boo"></span>](types.md) | [:i:](#log)
logString([<span class="tag var"></span>](types.md) value, [<span class="tag str"></span>](types.md) label, [<span class="tag str"></span>](types.md) tags, [<span class="tag boo"></span>](types.md) concise, [<span class="tag boo"></span>](types.md) displayTag) | _Returns_ a String formatted similarly to the output of [log(...)](#log). | [<span class="ret str"></span>](types.md) | [:i:](#logstring)
logStyle([<span class="tag str"></span>](types.md) tag, [<span class="tag col"></span>](types.md#color) tint, [<span class="tag str"></span>](types.md) prefix, [<span class="tag str"></span>](types.md) postfix) | Set style options for the specified tag type for the log. | [<span class="ret boo"></span>](types.md) | [:i:](#logstyle)
print([<span class="tag str"></span>](types.md) message) | Prints a string into chat that only the host is able to see. Used for debugging scripts. | [<span class="ret nil"></span>](types.md) | [:i:](#print)
printToAll([<span class="tag str"></span>](types.md) message, [<span class="tag col"></span>](types.md#color) message_tint) | Print a message into the chat of all connected players. | [<span class="ret boo"></span>](types.md) | [:i:](#printtoall)
printToColor([<span class="tag str"></span>](types.md) message, [<span class="tag str"></span>](types.md) player_color, [<span class="tag col"></span>](types.md#color) message_tint) | Print a message to a specific [Player Color](player/colors.md). | [<span class="ret boo"></span>](types.md) | [:i:](#printtocolor)
sendExternalMessage([<span class="tag tab"></span>](types.md) data) {: #sendexternalmessage data-toc-label="sendExternalMessage(...)" data-toc-child-of="message-function-details" } | Send a table to your external script editor, most likely Atom. This is for custom editor functionality. | [<span class="ret boo"></span>](types.md) |



---

##Function Details

###Global Function Details {: data-toc-sort }

####addContextMenuItem(...)

[<span class="ret boo"></span>](types.md) Adds a menu item to the Global right-click context menu. Global menu is shown when player right-clicks on empty space or table.

!!!info "addContextMenuItem(label, toRunFunc, keep_open, require_table)"
	* [<span class="tag str"></span>](types.md) **label**: Label for the menu item.
	* [<span class="tag fun"></span>](types.md) **toRunFunc**: Execute if menu item is selected.
        * [<span class="tag str"></span>](types.md) **player_color** [Player Color](player/colors.md) who selected the menu item.
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

[<span class="ret boo"></span>](types.md) Copy a list of Objects to the clipboard. Works with [paste(...)](#paste).

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

[<span class="ret boo"></span>](types.md) Destroy an Object.

!!!info "destroyObject(obj)"
	* [<span class="tag obj"></span>](types.md) **obj**: The Object you wish to delete from the instance.

---


####getObjectFromGUID(...)

[<span class="ret obj"></span>](types.md) Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist.

!!!info "getObjectFromGUID(guid)"
	* [<span class="tag str"></span>](types.md) **guid**: GUID of the Object to get a reference of.
		* {>>GUID can be obtained by right clicking an object and going to Scripting.<<}
		* {>>In a script, it can be obtained from any Object by using .getGUID().<<}


---

####group(...)

[<span class="ret tab"></span>](types.md) Groups objects together, like how the `G` key does for players. It returns a table of object references to any decks/stacks formed.

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

[<span class="ret tab"></span>](types.md) Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy).

!!!info "paste(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing instructions of where to spawn the Objects.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position of the first object to paste.
			* {>>Optional, defaults to {0, 3, 0}.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.snap_to_grid**: If snap-to-grid is active on the spawned item/s.
			* {>>Optional, defaults to false (off).<<}


---


####spawnObject(...)

[<span class="ret obj"></span>](types.md) Spawns an Object. See [Built-in](built-in-object.md) and [Custom](custom-game-objects.md) Spawnable Objects pages for details of specific spawnable objects.

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

[<span class="ret boo"></span>](types.md) Start a coroutine. A coroutine is similar to a function, but has the unique ability to have its run paused until the next frame of the game using `coroutine.yield(0)`.

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

[<span class="ret col"></span>](types.md) Converts a [Player Color](player/colors.md) string into a Color Table for tinting.

!!!info "stringColorToRGB(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color** A String of a [Player Color](player/colors.md).

``` Lua
printToAll("Blue message", stringColorToRGB("Blue"))
```

---

### Hotkey Function Details {: data-toc-sort }

####addHotkey(...)

[<span class="ret boo"></span>](types.md) Adds a bindable hotkey to the game.

Players can bind key to hotkeys from the `Options` -> `Game Keys` UI after this function is called.

!!!important
	Added hotkeys are unable to persist between loads/rewinds, because the bound callback function may no longer exist.
	Therefore [addHotkey(...)](#addhotkey) needs to be called each time the game is loaded. As long as the same labels
	are used, then player hotkey bindings will persist.

!!!info "addHotkey(label, callback, triggerOnKeyUp)"
	* [<span class="tag str"></span>](types.md) **label**: A label displayed to users.
	* [<span class="tag fun"></span>](types.md) **callback**(playerColor, hoveredObject, pointerPosition, isKeyUp): The function that will be executed whenever the hotkey is pressed, and _also_ when released if `triggerOnKeyUp` is `true`.
        * [<span class="tag str"></span>](types.md) **playerColor**: [Player Color](player/colors.md) of the player that pressed the hotkey.
        * [<span class="tag obj"></span>](types.md) **hoveredObject**: The object that the Player's pointer was hovering over at the moment the key was pressed/released. `nil` if no object was under the Player's pointer at the time.
        * [<span class="tag vec"></span>](types.md) **pointerPosition**: [Word Position](types.md#position) of the Player's pointer at the moment the key was pressed/released.
        * [<span class="tag boo"></span>](types.md) **isKeyUp**: Whether this callback is being triggered in response to a hotkey being released.
	* [<span class="tag boo"></span>](types.md) **triggerOnKeyUp**: Whether the `callback` is _also_ executed when the hotkey is released. The `callback` is always triggered when the hotkey is pressed.
        * {>>Optional, defaults to false.<<}

Hotkey bindings do not prevent the behavior of Settings key bindings i.e. if `R` (shuffle by default) is assigned as a
hotkey, the hotkey callback and the default shuffle behavior will both be executed whenever `R` is pressed.

!!!example
	```lua
	addHotkey("My Hotkey", function(playerColor, object, pointerPosition, isKeyUp)
		local action = isKeyUp and "released" or "pressed"
		print(playerColor .. " " .. action .. " the hotkey")
	end, true)
	```

---

###Message Function Details {: data-toc-sort }

####broadcastToAll(...)

[<span class="ret boo"></span>](types.md) Print an on-screen message to all Players.

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

[<span class="ret boo"></span>](types.md) Print an on-screen message to a specified Player and their in-game chat.

!!!info "broadcastToColor(message, player_color, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to display on-screen.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) to receive the message.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB color tint for the text.

``` Lua
msg = "Hello White."
color = "White"
rgb = {r=1, g=0, b=0}
broadcastToColor(msg, color, rgb)
```

---


####log(...)

[<span class="ret boo"></span>](types.md) Logs a message to the _host's_ System Console (accessible from `~` pane of in-game chat window).

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

[<span class="ret str"></span>](types.md) _Returns_ a String formatted similarly to the output of [log(...)](#log).

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

[<span class="ret boo"></span>](types.md) Configures style options for a [log(...)](#log) tag.

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

[<span class="ret nil"></span>](types.md) Print a string into chat that only the host is able to see. Used for debugging scripts.

!!!info "print(message)"
	* [<span class="tag str"></span>](types.md) **message**: Text to print into the chat log.


---


####printToAll(...)

[<span class="ret boo"></span>](types.md) Print a message into the in-game chat of all connected players.

!!!info "printToAll(message, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to place into players' in-game chats.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToAll("Hello World!", {r=1,g=0,b=0})
```

---


####printToColor(...)

[<span class="ret boo"></span>](types.md) Print a message to the in-game chat of a specific player.

!!!info "printToColor(message, player_color, message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to place into the player's in-game chat.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that will receive the message.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToColor("Hello Red.", "Red", {r=1,g=0,b=0})
```

---
