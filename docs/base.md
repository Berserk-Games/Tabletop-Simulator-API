These are a loose collection of functions which can be used to perform a variety of actions within Tabletop Simulator.

These functions can utilize in-game Objects, but none of them can be enacted on in-game Objects. They all deal with the game space.

##Function Summary

###Global Functions
General functions which work within any script.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
copy([<span class="tag tab"></span>](types.md)&nbsp;object_list) | Copy a list of Objects to the clipboard. Works with [paste(...)](#paste). | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#copy)
destroyObject([<span class="tag obj"></span>](types.md)&nbsp;obj) | Destory an Object. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#destroyobject)
<a class="anchor" id="fliptable"></a>flipTable() | Flip the table. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="getallobjects"></a>getAllObjects() | Returns Table of all spawned [Objects](object.md) in the game. | [<span class="ret tab"></span>](types.md) |
getObjectFromGUID([<span class="tag str"></span>](types.md)&nbsp;guid) | Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist. | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#getobjectfromguid)
<a class="anchor" id="getseatedplayers"></a>getSeatedPlayers() | Returns Table of the [Player Colors](player-color.md) strings of seated players. | [<span class="ret tab"></span>](types.md) |
group([<span class="tag tab"></span>](types.md)&nbsp;objects) | Groups objects together, like how the `G` key does for players. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#group)
paste([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy). | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#paste)
<a class="anchor" id="setlookingforplayers"></a>setLookingForPlayers([<span class="tag boo"></span>](types.md)&nbsp;lfp) | Enables/disables looking for group. This is visible in the server browsers, indicating if you are recruiting for a game. | [<span class="ret boo"></span>](types.md) |
spawnObject([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Spawns an Object. See [Built-in](built-in-object.md) and [Custom](custom-game-objects.md) Spawnable Object pages for further details. | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#spawnobject)
spawnObjectJSON([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Spawns an Object using a JSON string. Works with [getJSON()](object.md#getjson). | [<span class="ret obj"></span>](types.md) | [<span class="i"></span>](#spawnobjectjson)
startLuaCoroutine([<span class="tag obj"></span>](types.md)&nbsp;function_owner, [<span class="tag str"></span>](types.md)&nbsp;function_name) | Start a coroutine. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#startluacoroutine)
stringColorToRGB([<span class="tag str"></span>](types.md)&nbsp;player_color) | Converts a [Player Color](player-color.md) string into a Color Table for tinting. | [<span class="ret col"></span>](types.md#color) | [<span class="i"></span>](#stringcolortorgb)


###Message Functions
Functions which handle sending and displaying data.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
broadcastToAll([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print an on-screen message to all Players, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#broadcasttoall)
broadcastToColor([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag str"></span>](types.md)&nbsp;player_color, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print an on-screen message to a specified Player, as well as their in-game chat. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#broadcasttocolor)
log([<span class="tag var"></span>](types.md)&nbsp;element, [<span class="tag str"></span>](types.md)&nbsp;label, [<span class="tag str"></span>](types.md)&nbsp;tag) | Print information to the log tab. (Shortcut: ~) | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#log)
logStyle([<span class="tag str"></span>](types.md)&nbsp;tag, [<span class="tag col"></span>](types.md#color)&nbsp;tint, [<span class="tag str"></span>](types.md)&nbsp;prefix, [<span class="tag str"></span>](types.md)&nbsp;postfix) | Set style options for the specified tag type for the log. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#logstyle)
print([<span class="tag str"></span>](types.md)&nbsp;message) | Prints a string into chat that only the host is able to see. Used for debugging scripts. | [<span class="ret nil"></span>](types.md) | [<span class="i"></span>](#print)
printToAll([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print a message into the chat of all connected players. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#printtoall)
printToColor([<span class="tag str"></span>](types.md)&nbsp;message, [<span class="tag str"></span>](types.md)&nbsp;player_color, [<span class="tag col"></span>](types.md#color)&nbsp;message_tint) | Print a message to a specific [Player Color](player-color.md). | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#printtocolor)
<a class="anchor" id="sendexternalmessage"></a>sendExternalMessage([<span class="tag tab"></span>](types.md)&nbsp;data) | Send a table to your external script editor, most likely Atom. This is for custom editor functionality. | [<span class="ret boo"></span>](types.md) |



---

##Function Details

###Global Function details

####copy(...)

[<span class="ret boo"></span>](types.md)&nbsp;Copying a list of Objects the clipboard. Works with [paste(...)](#paste).

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

``` Lua
function onLoad()
    local objList = {
        getObjectFromGUID("b80a72"),
        getObjectFromGUID("a333b4"),
        getObjectFromGUID("c9f9d3"),
    }
    group(objList)
end
```




---

####paste(...)

[<span class="ret obj"></span>](types.md)&nbsp;Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy).

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

[<span class="ret obj"></span>](types.md)&nbsp;Start a coroutine. A coroutine is similar to a function, but has the unique ability to have its run paused until the next frame of the game using `coroutine.yield(0)`.

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

[<span class="ret tab"></span>](types.md)&nbsp;Converts a [Player Color](player-color.md) string into a Color Table for tinting.

!!!info "stringColorToRGB(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color** A String of a [Player Color](player-color.md).

``` Lua
printToAll("Blue message", stringColorToRGB("Blue"))
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

!!!info "broadcastToColor(message, [player_color](player.md), message_tint)"
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

[<span class="ret boo"></span>](types.md)&nbsp;Print information to the log. The log is a separate chat window in which you can also enter console commands. It is only visible to the host.

If a table is used for "element", the log will automatically display the key/value contents of it.

!!!info "log(element, label, tag)"
	* [<span class="tag var"></span>](types.md) **element**: The information you want placed into the log.
	* [<span class="tag str"></span>](types.md) **label**: Text to be placed before the Var element is printed to the log.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](types.md) **tag**: Name that is usable to categorize log entries. (See: [logStyle](#logstyle))
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}


``` Lua
log(getAllObjects(), "All Objects:", "table")
```

---


####logStyle(...)

[<span class="ret boo"></span>](types.md)&nbsp;Set style options for the specified tag type for the log. This can also be set in the system console with the "log_style_tag" command.

!!!info "logStyle(tag, tint, prefix, postfix)"
	* [<span class="tag str"></span>](types.md) **tag**: A String of the log's tag.
	* [<span class="tag col"></span>](types.md#color) **tint**: RGB value to tint the log entry's text.
		* {>>String color will also work. Example: "Red"<<}
	* [<span class="tag str"></span>](types.md) **prefix**: Text to place before this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](types.md) **postfix**: Text to place after this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}

``` Lua
function onLoad()
	logStyle("players", {0.5,0.5,0.5}, "", "End List")
	log(getSeatedPlayers(), "players")
end
```

---


####print(...)

[<span class="ret nil"></span>](types.md)&nbsp;Print a string into chat that only the host is able to see. Used for debugging scripts.

!!!info "print(message)"
	* [<span class="tag tab"></span>](types.md) **message**: Text to print into the chat log.


---


####printToAll(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print a message into the in-game chat of all connected players.

!!!info "printToAll(message, message_tint)"
	* [<span class="tag tab"></span>](types.md) **message**: Message to place into players' in-game chats.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToAll("Hello World!", {r=1,g=0,b=0})
```

---


####printToColor(...)

[<span class="ret boo"></span>](types.md)&nbsp;Print a message to the in-game chat of a specific player.

!!!info "printToColor(message, [player_color](player-color.md), message_tint)"
	* [<span class="tag str"></span>](types.md) **message**: Message to place into the player's in-game chat.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player-color.md) of the player that will receive the message.
	* [<span class="tag col"></span>](types.md#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToColor("Hello Red.", "Red", {r=1,g=0,b=0})
```

---
