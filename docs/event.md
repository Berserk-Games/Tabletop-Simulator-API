Events are functions which are activated by Tabletop Simulator when something takes place in-game. It is possible to use all of them within scripts on Objects, and most will also work in Global scripts.

Many contain parameters which can be used to utilize additional information related to the event.

##Function Summary

###Default Events (Global & Object)
These are functions which are triggered by an event taking place in-game. They work when within the script of an Object or the Global script.

Function Name | Description | &nbsp;
-- | -- | --
filterObjectEnterContainer([<span class="tag obj"></span>](/types)&nbsp;container, [<span class="tag obj"></span>](/types)&nbsp;enter_object) | Called when an object attempts to enter any container. The object is prevented from entering unless "true" is returned. | [<span class="i"></span>](#filterobjectentercontainer)
onChat([<span class="tag str"></span>](/types)&nbsp;message, [<span class="tag pla"></span>](/types)&nbsp;sender) | Called when a chat message is sent in game chat. | [<span class="i"></span>](#onchat)
onExternalMessage([<span class="tag tab"></span>](/types)&nbsp;data) | Called when an external script editor (like [Atom](atom)) sends a message back to the game. Used for custom editor functionality. | [<span class="i"></span>](#onexternalmessage)
onFixedUpdate() | Called **every physics tick** (90 times a second). This is a frame independent onUpdate(). | [<span class="i"></span>](#onfixedupdate)
onLoad([<span class="tag str"></span>](/types)&nbsp;save_state) | Called when a game save is finished loading every Object. It is where most setup code will go. | [<span class="i"></span>](#onload)
onObjectDestroy([<span class="tag obj"></span>](/types)&nbsp;dying_object) | Called whenever any object is destroyed. | [<span class="i"></span>](#onobjectdestroy)
onObjectDrop([<span class="tag str"></span>](/types)&nbsp;player_color, [<span class="tag obj"></span>](/types)&nbsp;dropped_object) | Called whenever any object is dropped by a player. | [<span class="i"></span>](#onobjectdrop)
onObjectEnterScriptingZone([<span class="tag obj"></span>](/types)&nbsp;zone, [<span class="tag obj"></span>](/types)&nbsp;enter_object) | Called when any object enters any scripting zone. | [<span class="i"></span>](#onobjectenterscriptingzone)
onObjectEnterContainer([<span class="tag obj"></span>](/types)&nbsp;container, [<span class="tag obj"></span>](/types)&nbsp;enter_object) | Called when any object enters any container. Includes decks | [<span class="i"></span>](#onobjectentercontainer)
onObjectLeaveScriptingZone([<span class="tag obj"></span>](/types)&nbsp;zone, [<span class="tag obj"></span>](/types)&nbsp;enter_object) | Called when any object leaves any scripting zone. | [<span class="i"></span>](#onobjectleavescriptingzone)
onObjectLeaveContainer([<span class="tag obj"></span>](/types)&nbsp;container, [<span class="tag obj"></span>](/types)&nbsp;leave_object) | Called when any object leaves any container. | [<span class="i"></span>](#onobjectleavecontainer)
onObjectLoopingEffect([<span class="tag obj"></span>](/types)&nbsp;loop_object, [<span class="tag int"></span>](/types)&nbsp;index) | Called whenever the looping effect of an [AssetBundle](assetbundle) is activated. | [<span class="i"></span>](#onobjectloopingeffect)
onObjectPeek([<span class="tag obj"></span>](/types)&nbsp;object, [<span class="tag str"></span>](/types)&nbsp;player) | Called when a player using peek to look under an Object. | [<span class="i"></span>](#onobjectpeek)
onObjectPickUp([<span class="tag str"></span>](/types)&nbsp;player_color, [<span class="tag obj"></span>](/types)&nbsp;picked_up_object) | Called whenever a Player picks up an Object. | [<span class="i"></span>](#onobjectpickup)
onObjectRandomize([<span class="tag obj"></span>](/types)&nbsp;randomize_object, [<span class="tag str"></span>](/types)&nbsp;player_color) | Called when an Object is randomized. Like when shuffling a deck or shaking dice. | [<span class="i"></span>](#onobjectrandomize)
onObjectSearchEnd([<span class="tag obj"></span>](/types)&nbsp;obj, [<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a search is finished on any container. | [<span class="i"></span>](#onobjectsearchend)
onObjectSearchStart([<span class="tag obj"></span>](/types)&nbsp;obj, [<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a search is started on any container. | [<span class="i"></span>](#onobjectsearchstart)
onObjectSpawn([<span class="tag obj"></span>](/types)&nbsp;spawn_object) | Called when any Object is spawned/created. | [<span class="i"></span>](#onobjectspawn)
onObjectTriggerEffect([<span class="tag obj"></span>](/types)&nbsp;trigger_object, [<span class="tag int"></span>](/types)&nbsp;index) | Called whenever the trigger effect of an [AssetBundle](assetbundle) is activated. | [<span class="i"></span>](#onobjecttriggereffect)
onPlayerChangeColor([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect. | [<span class="i"></span>](#onplayerchangecolor)
onPlayerConnect([<span class="tag pla"></span>](/types)&nbsp;person) | Called when a [Player](player) connects to a game. | [<span class="i"></span>](#onplayerconnect)
onPlayerDisconnect([<span class="tag pla"></span>](/types)&nbsp;person) | Called when a [Player](player) disconnects from a game. | [<span class="i"></span>](#onplayerdisconnect)
onPlayerTurn([<span class="tag str"></span>](/types)&nbsp;player_color) | Called at the start of a player's turn when using the in-game turn system. | [<span class="i"></span>](#onplayerturn)
onSave() | Called whenever your game is saved. | [<span class="i"></span>](#onsave)
onScriptingButtonDown([<span class="tag int"></span>](/types)&nbsp;index, [<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10. | [<span class="i"></span>](#onscriptingbuttondown)
onScriptingButtonUp([<span class="tag int"></span>](/types)&nbsp;index, [<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10. | [<span class="i"></span>](#onscriptingbuttonup)
onUpdate() | Called **every frame**. | [<span class="i"></span>](#onupdate)










###Default Events (Object Only)
These are functions which are triggered by an event taking place in-game. They only work within scripts that are on Objects, never in Global.

Function Name | Description | &nbsp;
-- | -- | --
filterObjectEnter([<span class="tag obj"></span>](/types)&nbsp;obj) | Called when an object attempts to enter this object. The object is prevented from entering unless "true" is returned. | [<span class="i"></span>](#filterobjectenter)
onCollisionEnter([<span class="tag tab"></span>](/types)&nbsp;collision_info) | Called when an Object starts colliding with the Object the function is on. | [<span class="i"></span>](#oncollisionenter)
onCollisionExit([<span class="tag tab"></span>](/types)&nbsp;collision_info) | Called when an Object stops colliding with the Object the function is on. | [<span class="i"></span>](#oncollisionexit)
onCollisionStay([<span class="tag tab"></span>](/types)&nbsp;collision_info) | Called **every frame** that an Object is colliding with the Object this function is on. | [<span class="i"></span>](#oncollisionstay)
onDestroy() | Called when an Object it is on is destroyed. | [<span class="i"></span>](#ondestroy)
onDrop([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a player releases an Object after picking it up. | [<span class="i"></span>](#ondrop)
onPeek([<span class="tag str"></span>](/types)&nbsp;player) | Called when a player using peek to look under this Object. | [<span class="i"></span>](#onpeek)
onPickUp([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a player picks up an Object. | [<span class="i"></span>](#onpickup)
onRandomize([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when this Object is randomized. Like when shuffling a deck or shaking dice. | [<span class="i"></span>](#onrandomize)
onSearchEnd([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a player finishes searches this Object. | [<span class="i"></span>](#onsearchend)
onSearchStart([<span class="tag str"></span>](/types)&nbsp;player_color) | Called when a player starts searching this Object. | [<span class="i"></span>](#onsearchstart)













---

##Function Details (Global & Object)

###onChat(...)

This function is called when a message is sent through the in-game chat. It does not trigger when global chat messages are sent. Using `#!lua return false` inside of this function prevents the chat message which triggered it to be suppressed.

!!!info "onChat(message, sender)"
	* [<span class="tag str"></span>](/types)&nbsp;**message**: Chat message which triggered the function.
	* [<span class="tag pla"></span>](/types)&nbsp;**sender**: Player which sent the chat message.

``` Lua
function onChat(message, player)
	print(message)
	print(player.color)
end
```

---


###onExternalMessage(...)

This function is called when an external script editor (like [Atom](atom)) sends a message back to the game. Used for custom editor functionality.

!!!info "onExternalMessage(data)"
	* [<span class="tag tab"></span>](/types)&nbsp;**data**: The data returned by the external editor into the game.

``` Lua
function onExternalMessage(data)
	print("External message received")
end
```

---


###onFixedUpdate()

Called **every physics tick** (90 times a second). This is a frame independent onUpdate().

!!!warning
	This is a very expensive function and can easily slow/crash your game if misused. Use with caution.

``` Lua
function onFixedUpdate()
	self.addTorque({0,100,0}, 1)
end
```


###onLoad(...)

This function is called when a game save is finished loading every Object. This is where most setup code will go. The fast-forward and rewind feature will also cause this function to activate. If this function is in an Object's script and that Object is spawned, like by removing it from a container, it too will trigger onLoad().

!!!info "onLoad(save_state)"
	* [<span class="tag str"></span>](/types)&nbsp;**save_state**: The encoded string containing any save_state (saved) data.
		* {>>If there is no data saved, this returns an empty String.<<}

``` Lua
function onLoad()
	print("Loading complete")
end
```

???example "Example of onLoad and onSave being used to save/load data"
    ``` Lua
	-- Runs whenever game is saved/autosaved
	function onSave()
		local data_to_save = {someData=50}
		saved_data = JSON.encode(data_to_save)
		--saved_data = "" --Remove -- at start & save to clear save data
		return saved_data
	end

	-- Runs when game is loaded
	function onLoad(saved_data)
		-- Loads the tracking for if the game has started yet
		if saved_data ~= "" then
			local loaded_data = JSON.decode(saved_data)
			someData = loaded_data.someData
		else
			someData = 50
		end
	end
    ```
---


###onObjectDestroy(...)

Called whenever any object is destroyed. The dying Object has 1 frame left to live. This event fires immediately before the dying Object’s `onDestroy()` but their lifetime is the same final frame.

!!!info "onObjectDestroy(dying_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**dying_object**: The object that was destroyed.

``` Lua
function onObjectDestroy(destroyedObj)
	print(destroyedObj.getName())
end
```

---


###onObjectDrop(...)

Called whenever any object is dropped by a player.

!!!info "onObjectDrop(player_color, dropped_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**dropped_object**: The Object in game which was dropped.
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player who dropped the Object.

``` Lua
function onObjectDrop(colorName, obj)
	print(colorName .. " dropped " .. obj.getName())
end
```

---


###onObjectEnterScriptingZone(...)

Called when any object enters any scripting zone.

!!!info "onObjectEnterScriptingZone(zone, enter_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**zone**: The Object of the scripting zone.
	* [<span class="tag obj"></span>](/types)&nbsp;**enter_object**: The Object triggering the function.

``` Lua
function onObjectEnterScriptingZone(zone, obj)
	print(obj.getGUID())
end
```

---


###onObjectEnterContainer(...)

Called when any object enters any container. Includes Objects entering decks.

!!!info "onObjectEnterContainer(container, enter_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**container**: Container the Object entered.
	* [<span class="tag obj"></span>](/types)&nbsp;**enter_object**: Object that entered the container.

``` Lua
function onObjectEnterContainer(bag, obj)
	print(bag)
	print(obj)
end
```

---



###onObjectLeaveScriptingZone(...)

Called when any object leaves any scripting zone.

!!!info "onObjectLeaveScriptingZone(zone, enter_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**zone**: The Object of the scripting zone.
	* [<span class="tag obj"></span>](/types)&nbsp;**enter_object**: The Object triggering the function.

``` Lua
function onObjectLeaveScriptingZone(zone, obj)
	print(obj.getGUID())
end
```

---


###onObjectLeaveContainer(...)

Called when any object leaves any container.

!!!info "onObjectLeaveContainer(container, leave_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**container**: Container the object left.
	* [<span class="tag obj"></span>](/types)&nbsp;**leave_object**: Object that left the container.

``` Lua
function onObjectLeaveContainer(bag, obj)
	print(bag)
	print(obj)
end
```

---


###onObjectLoopingEffect(...)

Called whenever the looping effect of an [AssetBundle](assetbundle) is activated.

!!!info "onObjectLoopingEffect(loop_object, index)"
	* [<span class="tag obj"></span>](/types)&nbsp;**loop_object**: AssetBundle which had its loop activated.
	* [<span class="tag int"></span>](/types)&nbsp;**index**: Index number for the loop activated.

``` Lua
function onObjectLoopingEffect(obj, index)
	print("Loop " .. index .. " activated.")
end
```

---



###onObjectPeek(...)

Called when a player using peek to look under an Object.

!!!info "onObjectPeek(object, player)"
	* [<span class="tag obj"></span>](/types)&nbsp;**object**: A reference to the Object which was peeked at.
	* [<span class="tag str"></span>](/types)&nbsp;**player**: Name of the [Player Color](player-color) that peeked.



``` Lua
function onObjectPeek(object, color)
	printToAll(color .. " peeked at an Object.", {1,0,0})
end
```




---


###onObjectPickUp(...)

Called whenever a Player picks up an Object.

!!!info "onObjectPickUp(player_color, picked_up_object)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player who picked up the object.
	* [<span class="tag obj"></span>](/types)&nbsp;**picked_up_object**: The Object in game which was picked up.

``` Lua
function onObjectPickUp(colorName, obj)
	print(colorName .. " picked up " .. obj.getName())
end
```

---


###onObjectRandomize(...)

Called when an Object is randomized. Like when shuffling a deck or shaking dice.

!!!info "onObjectRandomize(randomize_object, player_color)"
	* [<span class="tag obj"></span>](/types)&nbsp;**spawn_object**: The Object which triggered this function.
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.



``` Lua
function onObjectRandomize(obj, color)
	print(obj.getName() .. " was randomized by " .. color)
end
```

---


###onObjectSearchEnd(...)

Called when a search is finished on any container.

!!!info "onObjectSearchEnd(obj, player_color)"
* [<span class="tag obj"></span>](/types)&nbsp;**obj**: The Object which was searched.
* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.

---


###onObjectSearchStart(...)

Called when a search is started on any container.

!!!info "onObjectSearchStart(obj, player_color)"
* [<span class="tag obj"></span>](/types)&nbsp;**obj**: The Object which was searched.
* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.

---


###onObjectSpawn(...)

Called when any Object is spawned/created.

!!!info "onObjectSpawn(spawn_object)"
	* [<span class="tag obj"></span>](/types)&nbsp;**spawn_object**: The Object which triggered this function.

``` Lua
function onObjectSpawn(obj)
	print(obj)
end
```

---


###onObjectTriggerEffect(...)

Called whenever the trigger effect of an [AssetBundle](assetbundle) is activated.

!!!info "onObjectTriggerEffect(loop_object, index)"
	* [<span class="tag obj"></span>](/types)&nbsp;**loop_object**: AssetBundle which had its trigger activated.
	* [<span class="tag int"></span>](/types)&nbsp;**index**: Index number for the trigger activated.

``` Lua
function onObjectTriggerEffect(obj, index)
	print("Loop " .. index .. " activated.")
end
```

---




###onPlayerChangeColor(...)

Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect.

!!!info "onPlayerChangeColor(player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.

``` Lua
function onPlayerChangeColor(color)
	print(color)
end
```

---


###onPlayerConnect(...)

Called when a [Player](player) connects to a game.

!!!info "onPlayerConnect(person)""
	* [<span class="tag pla"></span>](/types)&nbsp;**person**: Player reference to who connected.

---


###onPlayerDisconnect(...)

Called when a [Player](player) disconnects from a game.

!!!info "onPlayerDisconnect(person)""
	* [<span class="tag pla"></span>](/types)&nbsp;**person**: Player reference to who disconnected.

---


###onPlayerTurn(...)
Called at the start of a player's turn when using the in-game turn system.

!!!info "onPlayerTurn(player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who's turn is starting.

``` Lua
function onPlayerTurn(color)
	print(color .. "'s turn starts now.")
end
```

---


###onSave()

This is called whenever the game saves, either manually or by auto-save. This will work in both a Global script, and an Object script. It is used to allow information to persist through saving/loading, for example, to let your script remember its data previously after hitting the Undo or Redo button. By placing script information into a Lua table, then encoding that data into [JSON](event#json), you are able to save information about the script's current state onto the script's parent, in the form of a string. You can also return a string value in this function to stash it.

!!!important
	When using `onSave()`, information is saved into the save file you are using. Using *Save & Apply* does NOT cause it to record data, only overwriting your save will update what information `onSave()` is trying to record.

!!!warning
	You can save almost any data in a table using this function, but Object references **DO NOT** persist. If you need to record an Object using `onSave()`, record its GUID instead.

``` Lua
data_table = {answer=42}

function onSave()
	saved_data = JSON.encode(data_table)
	return saved_data
end
```

Check the [`onLoad()`](#onload) section for how to load that stored JSON information into your script.

---


###onScriptingButtonDown(...)

Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10.

!!!info "onScriptingButtonDown(index, player_color)"
	* [<span class="tag int"></span>](/types)&nbsp;**index**: Index number, representing which key was pressed.
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.

``` Lua
function onScriptingButtonDown(index, color)
	print(index)
end
```

---

###onScriptingButtonUp(...)

Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10.

!!!info "onScriptingButtonUp(index, player_color)"
	* [<span class="tag int"></span>](/types)&nbsp;**index**: Index number, representing which key was released.
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.

``` Lua
function onScriptingButtonUp(index, color)
	print(index)
end
```

---


###onUpdate()

Called **every frame**.

!!!warning
	This is a very expensive function and can easily slow/crash your game if misused. Use with caution.

``` Lua
function onUpdate()
	print("This will probably slow your game down.")
end
```

---

---





##Function Details (Object only)

###onCollisionEnter(...)

This function is called when an Object starts colliding with the Object the function is on. Does not work in Global.

!!!info "onCollisionEnter(collision_info)"
	* [<span class="tag tab"></span>](/types)&nbsp;**collision_info**: A Table containing data on colliding object.
		* [<span class="tag obj"></span>](/types)&nbsp;**collision_info.*collision_object***: Object coming into contact with `self`.
		* [<span class="tag tab"></span>](/types)&nbsp;**collision_info.*contact_points***: Sub-table full of the Vectors where contact took place.
		* [<span class="tag vec"></span>](/types#vector) **collision_info.*relative_velocity***: Direction and magnitude at the time of collision.

``` Lua
-- Example Usage
function onCollisionEnter(info)
	print(info.collision_object)
end
```
``` Lua
-- Example returned table
{
	collision_object = objectReference
	contact_points = {
		{x=5, y=0, z=-2, 5, 0, -2},
	}
	relative_velocity = {x=0, y=20, z=0, 0, 20, 0}
}
```

---


###onCollisionExit(...)

This function is called when an Object stops colliding with the Object the function is on. Does not work in Global.

!!!info "onCollisionExit(collision_info)"
	* [<span class="tag tab"></span>](/types)&nbsp;**collision_info**: A Table containing data on colliding object.
		* [<span class="tag obj"></span>](/types)&nbsp;**collision_info.*collision_object***: Object leaving contact with `self`.
		* [<span class="tag tab"></span>](/types)&nbsp;**collision_info.*contact_points***: Sub-table full of the Vectors where contact last broke off.
		* [<span class="tag vec"></span>](/types#vector) **collision_info.*relative_velocity***: Direction and magnitude of the departing Object.

``` Lua
-- Example Usage
function onCollisionExit(info)
	print(info.collision_object)
end
```
``` Lua
-- Example returned table
{
	collision_object = objectReference
	contact_points = {
		{x=5, y=0, z=-2, 5, 0, -2},
	}
	relative_velocity = {x=0, y=20, z=0, 0, 20, 0}
}
```

---


###onCollisionStay(...)

This function is called **every frame** that an Object is colliding with the Object this function is on. Does not work in Global.

!!!warning
	This is a very expensive function and can easily slow/crash your game if misused. Use with caution.

!!!info "onCollisionExit(collision_info)"
	* [<span class="tag tab"></span>](/types)&nbsp;**collision_info**: A Table containing data on colliding object.
		* [<span class="tag obj"></span>](/types)&nbsp;**collision_info.*collision_object***: Object coming into contact with `self`.
		* [<span class="tag tab"></span>](/types)&nbsp;**collision_info.*contact_points***: Sub-table full of the Vectors where contact is taking place.
		* [<span class="tag vec"></span>](/types#vector) **collision_info.*relative_velocity***: Direction and magnitude of the Object, currently.

``` Lua
-- Example Usage
function onCollisionStay(info)
	print(info.collision_object)
end
```
``` Lua
-- Example returned table
{
	collision_object = objectReference
	contact_points = {
		{x=5, y=0, z=-2, 5, 0, -2},
	}
	relative_velocity = {x=0, y=20, z=0, 0, 20, 0}
}
```

---


###onDestroy()

This function is called when an [Object](object) it is on is destroyed. When `onDestroy()` is called, the Object has one frame left to live but its recommended to avoid using it as a reference here. This event fires immediately after [onObjectDestroy()](#onobjectdestroy) but their lifetime is the same final frame. Does not work in Global.

``` Lua
function onDestroy()
	print("This object was destroyed!")
end
```

---

###onDrop(...)

This function is called when this [Object](object) is dropped. Does not work in Global.

!!!info "onDrop(player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player.

``` Lua
function onDrop(color)
	print(color)
end
```

---


###filterObjectEnter(...)

Called when an object attempts to enter this object. The object is prevented from entering unless "true" is returned.

!!!info "filterObjectEnter(obj)"
	* [<span class="tag obj"></span>](/types)&nbsp;**obj**: The object that has tried to enter the object this script is attached to.

``` Lua
function filterObjectEnter(obj)
	print(obj.getName()) -- Print entering object's name
	return true -- Allows object to enter.
end
```


---

###onPeek(...)

Called when a player using peek to look under an Object.

!!!info "onPeek(player)"
	* [<span class="tag str"></span>](/types)&nbsp;**player**: Name of the [Player Color](player-color) that peeked.


``` Lua
function onPeek(color)
	printToAll(color .. " peeked at an Object.", {1,0,0})
end
```


---


###onPickUp(...)

Called when a player picks up an Object.

!!!info "onPickUp(player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player.

``` Lua
function onPickUp(color)
	print(color)
end
```

---



###onRandomize(...)

Called when an Object is randomized. Like when shuffling a deck or shaking dice.

!!!info "onRandomize(player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the player who triggered the function.


``` Lua
function onRandomize(color)
	print(self.getName() .. " was randomized by " .. color)
end
```

---






###onSearchEnd(...)

Called when a player first searches this Object.

!!!info "onSearchEnd([<span class="tag str"></span>](/types)&nbsp;player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player.

---


###onSearchStart(...)

Called when a player finishes searching this Object.

!!!info "onSearchStart([<span class="tag str"></span>](/types)&nbsp;player_color)"
	* [<span class="tag str"></span>](/types)&nbsp;**player_color**: [Player Color](player-color) of the Player.

---
