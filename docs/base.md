These are a loose collection of functions which can be used to perform a variety of actions within Tabletop Simulator. Some of them are used in almost every script.

##Function Summary

###Global Functions
General functions which work within any function.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
clearPixelPaint() | Remove pixel paint from the instance. | [<span class="ret boo"></span>](typeandclass) | 
clearVectorPaint() | Remove vector paint from the instance. | [<span class="ret boo"></span>](typeandclass) | 
copy([<span class="tag tab"></span>](typeandclass) object_list) | Copy a list of Objects to the clipboard. Works with [paste(...)](#paste). | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#copy)
destroyObject([<span class="tag obj"></span>](typeandclass) obj) | Destory an Object. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#destroyobject)
flipTable() | Flip the table. | [<span class="ret boo"></span>](typeandclass) | 
getAllObjects() | Returns Table of all spawned [Objects](object) in the game. | [<span class="ret tab"></span>](typeandclass) | 
getNotes() | Returns the contents of the on-screen notes section. | [<span class="ret str"></span>](typeandclass) | 
getObjectFromGUID([<span class="tag str"></span>](typeandclass) guid) | Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist. | [<span class="ret obj"></span>](typeandclass) | [<span class="i"></span>](#getobjectfromguid)
getSeatedPlayers() | Returns Table of the [Player Colors](player-color) strings of seated players. | [<span class="ret tab"></span>](typeandclass) | 
paste([<span class="tag tab"></span>](typeandclass) parameters) | Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy). | [<span class="ret tab"></span>](typeandclass) | [<span class="i"></span>](#paste)
setNotes([<span class="tag str"></span>](typeandclass) notes) | Replace the text in the notes window with the string. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#setnotes)
spawnObject([<span class="tag tab"></span>](typeandclass) parameters) | Spawns an Object. View the [Spawnable Object](spawnableobjects) page for Objects that can be spawned. | [<span class="ret obj"></span>](typeandclass) | [<span class="i"></span>](#spawnobject)
startLuaCoroutine([<span class="tag obj"></span>](typeandclass) function_owner, [<span class="tag str"></span>](typeandclass) function_name) | Start a coroutine. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#startluacoroutine)
stringColorToRGB([<span class="tag str"></span>](typeandclass) player_color) | Converts a [Player Color](player-color) string into a Color Table for tinting. | [<span class="ret col"></span>](typeandclass#color) | [<span class="i"></span>](#stringcolortorgb)

###Message Functions
Functions which handle sending and displaying data.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
broadcastToAll([<span class="tag str"></span>](typeandclass) message, [<span class="tag col"></span>](typeandclass#color) message_tint) | Print an on-screen message to all Players, as well as their in-game chat. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#broadcasttoall)
broadcastToColor([<span class="tag str"></span>](typeandclass) message, [<span class="tag str"></span>](typeandclass) player_color, [<span class="tag col"></span>](typeandclass#color) message_tint) | Print an on-screen message to a specified Player, as well as their in-game chat. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#broadcasttocolor)
log([<span class="tag var"></span>](typeandclass) element, [<span class="tag str"></span>](typeandclass) tag, [<span class="tag str"></span>](typeandclass) label) | Print information to the log tab. (Shortcut: ~) | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#log)
logStyle([<span class="tag str"></span>](typeandclass) tag, [<span class="tag col"></span>](typeandclass#color) tint, [<span class="tag str"></span>](typeandclass) prefix, [<span class="tag str"></span>](typeandclass) postfix) | Set style options for the specified tag type for the log. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#logstyle)
print([<span class="tag str"></span>](typeandclass) message) | Prints a string into chat that only the host is able to see. Used for debugging scripts. | [<span class="ret nil"></span>](typeandclass) | [<span class="i"></span>](#print)
printToAll([<span class="tag str"></span>](typeandclass) message, [<span class="tag col"></span>](typeandclass#color) message_tint) | Print a message into the chat of all connected players. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#printtoall)
printToColor([<span class="tag str"></span>](typeandclass) message, [<span class="tag str"></span>](typeandclass) player_color, [<span class="tag col"></span>](typeandclass#color) message_tint) | Print a message to a specific [Player Color](player-color). | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#printtocolor)
sendExternalMessage([<span class="tag tab"></span>](typeandclass) data) | Send a table to your external script editor, most likely Atom. This is for custom editor functionality. | [<span class="ret boo"></span>](typeandclass) | 


###Notebook Functions
Functions that interact with the in-game notebook tabs.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addNotebookTab([<span class="tag tab"></span>](typeandclass) parameters) | Adds a notebook tab, returning its index. | [<span class="ret int"></span>](typeandclass) | [<span class="i"></span>](#addnotebooktab)
editNotebookTab([<span class="tag tab"></span>](typeandclass) parameters) | Edit an existing Tab in the notebook. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#editnotebooktab)
getNotebookTabs() | Returns Table containing data on all tabs in the notebook. | [<span class="ret tab"></span>](typeandclass) | [<span class="i"></span>](#getnotebooktabs)
removeNotebookTab([<span class="tag int"></span>](typeandclass) index) | Remove a notebook tab. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#removenotebooktab)



---

##Function Details

###Global Function details

####copy(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Copying a list of Objects the clipboard. Works with [paste(...)](#paste).

!!!info "copy(object_list)"
	* [<span class="tag tab"></span>](typeandclass) **object_list**: A Table of in-game objects to be copied.
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

[<span class="ret boo"></span>](typeandclass)&nbsp; Destroy an Object.

!!!info "destroyObject(obj)"
	* [<span class="tag obj"></span>](typeandclass) **obj**: The Object you wish to delete from the instance.

---


####getObjectFromGUID(...)

[<span class="ret obj"></span>](typeandclass)&nbsp; Returns Object by its GUID. Will return `nil` if this GUID doesn't currently exist.

!!!info "getObjectFromGUID(guid)"
	* [<span class="tag str"></span>](typeandclass) **guid**: GUID of the Object to get a reference of.
		* {>>GUID can be obtained by right clicking an object and going to Scripting.<<}
		* {>>In a script, it can be obtained from any Object by using .getGUID().<<}


---


####paste(...)

[<span class="ret obj"></span>](typeandclass)&nbsp; Pastes Objects in-game that were copied to the in-game clipboard. Works with [copy(...)](#copy).

!!!info "paste(parameters)"
	* [<span class="tag tab"></span>](typeandclass) **parameters**: A Table containing instructions of where to spawn the Objects.
		* [<span class="tag vec"></span>](typeandclass#vector) **parameters.position**: Position of the first object to paste.
			* {>>Optional, defaults to {0, 3, 0}.<<}
		* [<span class="tag boo"></span>](typeandclass) **parameters.snap_to_grid**: If snap-to-grid is active on the spawned item/s.
			* {>>Optional, defaults to false (off).<<}

---


####setNotes(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Replace the text in the notes window with the string. The notes is an area which displays text in the lower-left corner of the screen.

!!!info "setNotes(notes)"
	* [<span class="tag str"></span>](typeandclass) **notes**: What to place into the notes area.

``` Lua
setNotes("This appears in the notes section")
```

---


####spawnObject(...)

[<span class="ret obj"></span>](typeandclass)&nbsp; Spawn an Object. View the [Spawnable Object](spawnableobject) page for Objects that can be spawned.

If you are spawning a **custom Object**, you should call [setCustomObject](object#setcustomobject) immediately after spawnObject to set its custom properties.

!!!tip
	Spawned Objects take a moment to be physically spawned into the game. The purpose of the callback functionality is to allow you to run additional actions after the Object has been initiated fully into the instance.

!!!info "spawnObject(parameters)"
	* [<span class="tag tab"></span>](typeandclass) **parameters**: A Table of parameters used to determine how spawnObject will act.
		* [<span class="tag str"></span>](typeandclass) **parameters.type**: [Spawnable Object](spawnableobject) type.
		* [<span class="tag vec"></span>](typeandclass#vector) **parameters.position**: Position to place Object.
			* {>>Optional, defaults to {x=0, y=3, z=0}.<<}
		* [<span class="tag vec"></span>](typeandclass#vector) **parameters.rotation**: Rotation of the Object.
			* {>>Optional, defaults to {x=0, y=0, z=0}<<}
		* [<span class="tag vec"></span>](typeandclass#vector) **parameters.scale**: Scale of the Object.
			* {>>Optional, defaults to {x=1, y=1, z=1}<<}
		* [<span class="tag boo"></span>](typeandclass) **parameters.sound**: If the spawned Object noise is played.
			* {>>Optional, defaults to true.<<}
		* [<span class="tag boo"></span>](typeandclass) **parameters.snap_to_grid**: If snap-to-grid is active on the Object.
			* {>>Optional, defaults to false.<<}
		* [<span class="tag str"></span>](typeandclass) **parameters.callback**: Name of the function you want activated once the Object is initiated.
			* {>>Optional, no callback is triggered without it.<<}
			* {>>A callback function has 2 parameters, the Object spawned and, if used, the Table of params.<<}
		* [<span class="tag obj"></span>](typeandclass) **parameters.callback_owner**: Which Object has the callback function on it. Global is a valid target as well.
			* {>>Optional, defaults to Global. Serves no purpose if callback is not also used.<<}
		* [<span class="tag tab"></span>](typeandclass) **parameters.params**: A Table of data to send to the callback to use as parameters. See example.
			* {>>Optional, default is to not be used.<<}

``` Lua
function onLoad()
	futureName = "Spawned By Script!"
	spawnParams = {
		type = "rpg_BEAR",
		position       = {x=0, y=3, z=-5},
		rotation       = {x=0, y=90, z=0},
		scale          = {x=2, y=2, z=2},
		sound          = false,
		snap_to_grid   = true,
		callback       = "spawn_callback",
		callback_owner = Global,
		params         = {name = futureName}
	}
	spawnObject(spawnParams)
end

function spawn_callback(object_spawned, params)
	object_spawned.setName(params.name)
	object_spawned.setColorTint({r=0,g=1,b=0})
end
```

---


####startLuaCoroutine(...)

[<span class="ret obj"></span>](typeandclass)&nbsp; Start a coroutine. A coroutine is similar to a function, but has the unique ability to have its run paused until the next frame of the game using `coroutine.yield(0)`.

!!!Attention
	You MUST return a 1 at the end of any coroutine or it will throw an error.

!!!info "startLuaCoroutine(function_owner, function_name)"
	* [<span class="tag obj"></span>](typeandclass) **function_owner**: The Object that the function being called is on. Global is a valid target.
	* [<span class="tag str"></span>](typeandclass) **function_name**: Name of the function being called as a coroutine.

``` Lua
function onLoad()
	startLuaCoroutine(Global, "print_coroutine")
end

--Prints a message, waits 250 frames, prints another message
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

[<span class="ret tab"></span>](typeandclass)&nbsp; Converts a [Player Color](player-color) string into a Color Table for tinting.

!!!info "stringColorToRGB(player_color)"
	* [<span class="tag str"></span>](typeandclass) **player_color** A String of a [Player Color](player-color).

``` Lua
printToAll("Blue message", stringColorToRGB("Blue"))
```

---


###Message Function Details

####broadcastToAll(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Print an on-screen message to all Players.

!!!info "broadcastToAll(message, message_tint)"
	* [<span class="tag str"></span>](typeandclass) **message**: Message to display on-screen.
	* [<span class="tag col"></span>](typeandclass#color) **message_tint**: A Table containing the RGB color tint for the text.

``` Lua
msg = "Hello all."
rgb = {r=1, g=0, b=0}
broadcastToAll(msg, rgb)
```

---


####broadcastToColor(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Print an on-screen message to a specified Player and their in-game chat.

!!!info "broadcastToColor(message, [player_color](player), message_tint)"
	* [<span class="tag str"></span>](typeandclass) **message**: Message to display on-screen.
	* [<span class="tag str"></span>](typeandclass) **player_color**: [Player Color](player-color) to receive the message.
	* [<span class="tag col"></span>](typeandclass#color) **message_tint**: RGB color tint for the text.

``` Lua
msg = "Hello White."
color = "White"
rgb = {r=1, g=0, b=0}
broadcastToColor(msg, color, rgb)
```

---


####log(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Print information to the log. The log is a separate chat window which is visible to all players in the instance.

If a table is used for "element", the log will automatically display the key/value contents of it.

!!!info "log(element, tag, label)"
	* [<span class="tag var"></span>](typeandclass) **element**: The information you want placed into the log.
	* [<span class="tag str"></span>](typeandclass) **tag**: Name that is usable to categorize log entries. (See: [logStyle](logstyle))
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](typeandclass) **label**: Text to be placed before the Var element is printed to the log.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}

``` Lua
log(getAllObjects(), "table", "All Objects:")
```

---


####logStyle(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Set style options for the specified tag type for the log. This can also be set in the system console with the "log_style_tag" command.

!!!info "logStyle(tag, tint, prefix, postfix)"
	* [<span class="tag str"></span>](typeandclass) **tag**: A String of the log's tag.
	* [<span class="tag col"></span>](typeandclass#color) **tint**: RGB value to tint the log entry's text.
		* {>>String color will also work. Example: "Red"<<}
	* [<span class="tag str"></span>](typeandclass) **prefix**: Text to place before this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}
	* [<span class="tag str"></span>](typeandclass) **postfix**: Text to place after this type of log entry.
		* {>>Optional, defaults to an empty String. Empty Strings are not displayed.<<}

``` Lua
function onLoad()
	logStyle("players", {0.5,0.5,0.5}, "", "End List")
	log(getSeatedPlayers(), "players")
end
```

---


####print(...)

[<span class="ret nil"></span>](typeandclass)&nbsp; Print a string into chat that only the host is able to see. Used for debugging scripts.

!!!info "print(message)"
	* [<span class="tag tab"></span>](typeandclass) **message**: Text to print into the chat log.


---


####printToAll(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Print a message into the in-game chat of all connected players.

!!!info "printToAll(message, message_tint)"
	* [<span class="tag tab"></span>](typeandclass) **message**: Message to place into players' in-game chats.
	* [<span class="tag col"></span>](typeandclass#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToAll("Hello World!", {r=1,g=0,b=0})
```

---


####printToColor(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Print a message to the in-game chat of a specific player.

!!!info "printToColor(message, [player_color](player-color), message_tint)"
	* [<span class="tag str"></span>](typeandclass) **message**: Message to place into the player's in-game chat.
	* [<span class="tag str"></span>](typeandclass) **player_color**: [Player Color](player-color) of the player that will receive the message.
	* [<span class="tag col"></span>](typeandclass#color) **message_tint**: RGB values for the text's color tint.

``` Lua
printToColor("Hello Red.", "Red", {r=1,g=0,b=0})
```

---


###Notebook Function Details











####addNotebookTab(...)

[<span class="ret int"></span>](typeandclass)&nbsp; Add a new notebook tab. If it failed to create a new tab, a -1 is returned instead. Indexes for notebook tabs begin at 0.

!!!info "addNotebookTab(parameters)"
	* [<span class="tag tab"></span>](typeandclass) **parameters**: A Table containing spawning parameters.
		* [<span class="tag str"></span>](typeandclass) **parameters.title**: Title for the new tab.
		* [<span class="tag str"></span>](typeandclass) **parameters.body**: Text to place into the body of the new tab.
			* {>>Optional, defaults to an empty string<<}
		* [<span class="tag str"></span>](typeandclass) **parameters.color**: [Player Color](player) for the new tab's color.
			* {>>Optional, defaults to "Grey"<<}

``` Lua
parameters = {
	title = "New Tab",
	body = "Body text example.",
	color = "Grey"
}
addNotebookTab(parameters)
```

---


####editNotebookTab(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Edit an existing Tab in the notebook. Indexes for notebook tabs begin at 0.

!!!info "editNotebookTab(parameters)"
	* [<span class="tag tab"></span>](typeandclass) **parameters**: A Table containing instructions for the notebook edit.
		* [<span class="tag int"></span>](typeandclass) **parameters.index**: Index number for the tab.
		* [<span class="tag str"></span>](typeandclass) **parameters.title**: Title for the tab.
			* {>>Optional, defaults to the current title of the tab begin edited.<<}
		* [<span class="tag str"></span>](typeandclass) **parameters.body**: Text for the body for the tab.
			* {>>Optional, defaults to the current body of the tab begin edited.<<}
		* [<span class="tag str"></span>](typeandclass) **parameters.color**: [Player Color](player-color) for who the tab belongs to.
			* {>>Optional, defaults to the current color of the tab begin edited.<<}

``` Lua
params = {
	index = 5,
	title = "Edited Title",
	body = "This tab was edited via script.",
	color = "Grey"
}
editNotebookTab(params)
```

---


####getNotebookTabs()

[<span class="ret tab"></span>](typeandclass)&nbsp; Returns a Table containing data on all tabs in the notebook. Indexes for notebook tabs begin at 0.

``` Lua
--Example Usage
tabInfo = getNotebookTabs()
```
``` Lua
--Example Returned Table
{
	{index=0, title="", body="", color="Grey"},
	{index=1, title="", body="", color="Grey"},
	{index=2, title="", body="", color="Grey"},
}
```

---


####removeNotebookTab(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Remove a notebook tab. Notebook tab indexes begin at 0.

!!!info "removeNotebookTab(index)"
	* [<span class="tag int"></span>](typeandclass) **index**: Index for the tab to remove.

``` Lua
removeNotebookTab(0)
```

---
