Events are functions which are activated by Tabletop Simulator when something takes place in-game. It is possible to use all of them within scripts on Objects, and most will also work in Global scripts.

##Function Summary

###Default Events (Global & Object)
These are functions which are triggered by an event taking place in-game. They work when within the script of an Object or the Global script.

Function Name | Description | &nbsp; 
-- | -- | --:
onChat(String message, Player) | Called when a chat message is sent in game chat. | [<span class="i"></span>](#onchat)
onConnect(Player) | Called when a [Player](player) connects to a game.
onDisconnect(Player) | Called when a [Player](player) disconnects from a game.
onExternalMessage(Table) | Called when an external script editor (like [Atom](atom)) sends a message back to the game. Used for custom editor functionality. | [<span class="i"></span>](#onexternalmessage)
onFixedUpdate() | Called **every physics tick** (90 times a second). This is a frame independent onUpdate(). | [<span class="i"></span>](#onfixedupdate)
onLoad(String save_state) | Called when a game save is finished loading every Object. It is where most setup code will go. | [<span class="i"></span>](#onload)
onObjectDestroy(Object dying_object) | Called whenever any object is destroyed. | [<span class="i"></span>](#onobjectdestroy)
onObjectDrop(string player_color, Object dropped_object) | Called whenever any object is dropped by a player. | [<span class="i"></span>](#onobjectdrop)
onObjectEnterScriptingZone(Object zone, Object enter_object) | Called when any object enters any scripting zone. | [<span class="i"></span>](#onobjectenterscriptingzone)
onObjectLeaveScriptingZone(Object zone, Object enter_object) | Called when any object leaves any scripting zone. | [<span class="i"></span>](#onobjectleavescriptingzone)
onObjectLeaveContainer(Object container, Object leave_object) | Called when any object leaves any container. | [<span class="i"></span>](#onobjectleavecontainer)
onObjectLoopingEffect(Object loop_object, Int index) | Called whenever the looping effect of an [AssetBundle](assetbundle) is activated. | [<span class="i"></span>](#onobjectloopingeffect)
onObjectPickUp(String player_color, Object picked_up_object) | Called whenever a Player picks up an Object. | [<span class="i"></span>](#onobjectpickup)
onObjectRandomize(Object randomize_object, String player_color) | Called when an Object is randomized. Like when shuffling a deck or shaking dice. | [<span class="i"></span>](#onobjectrandomize)
onObjectSpawn(Object spawn_object) | Called when any Object is spawned/created. | [<span class="i"></span>](#onobjectspawn)
onObjectTriggerEffect(Object trigger_object, Int index) | Called whenever the trigger effect of an [AssetBundle](assetbundle) is activated. | [<span class="i"></span>](#onobjecttriggereffect)
onPlayerChangeColor(String [player_color](player)) | Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect. | [<span class="i"></span>](#onplayerchangecolor)
onPlayerTurnEnd(String [player_color_end](player),String [player_color_next](player)) | Called at the end of a player's turn when using the in-game turn system. | [<span class="i"></span>](#onplayerturnend)
onPlayerTurnStart(String [player_color_start](player),String [player_color_prev](player)) | Called at the start of a player's turn when using the in-game turn system. | [<span class="i"></span>](#onplayerturnstart)
onSave() | Called whenever your game is saved. | [<span class="i"></span>](#onsave)
onScriptingButtonDown(Int index, String [player_color](player)) | Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10. | [<span class="i"></span>](#onscriptingbuttondown)
onScriptingButtonUp(Int index, String [player_color](player)) | Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10. | [<span class="i"></span>](#onscriptingbuttonup)
onUpdate() | Called **every frame**. | [<span class="i"></span>](#onupdate)










###Default Events (Object Only)
These are functions which are triggered by an event taking place in-game. They only work within scripts that are on Objects, never in Global.

Function Name | Description
-- | --
onCollisionEnter(Table collision_info) | Called when an Object starts colliding with the Object the function is on. | [<span class="i"></span>](#oncollisionenter)
onCollisionExit(Table collision_info) | Called when an Object stops colliding with the Object the function is on. | [<span class="i"></span>](#oncollisionexit)
onCollisionStay(Table collision_info) | Called **every frame** that an Object is colliding with the Object this function is on. | [<span class="i"></span>](#oncollisionstay)
onDestroy() | Called when an Object it is on is destroyed. | [<span class="i"></span>](#ondestroy)
onDrop(String [player_color](player)) | Called when a player releases an Object after picking it up. | [<span class="i"></span>](#ondrop)
onPickUp(String [player_color](player)) | Called when a player picks up an Object. | [<span class="i"></span>](#onpickup)






---

##Function Details (Global & Object)

###onChat(...)

This function is called when a message is sent through the in-game chat. It does not trigger when global chat messages are sent. Using `#!lua return false` inside of this function prevents the chat message which triggered it to be supressed.

!!!info "onChat(String message, Player)""
	* **String message**: A String containing the chat message which triggered the function.
	* **Player**: A reference to the Player which sent the chat message.

``` Lua
function onChat(message, player)
	print(message)
	print(player.color)
end
```

---


###onExternalMessage(...)

This function is called when an external script editor (like [Atom](atom)) sends a message back to the game. Used for custom editor functionality.

!!!info "onExternalMessage(Table)"
	* **Table**: The data returned by the external editor into the game.

``` Lua
function onExternalMessage(data)
	print("External message received")
end
```

---


###onFixedUpdate()

Called **every physics tick** (90 times a second). This is a frame independent onUpdate(). | [<span class="i"></span>](#onfixedupdate)

!!!warning
	This is a very expensive function and can easily slow/crash your game if missused. Use with caution.

``` Lua
function onFixedUpdate()
	self.addTorque({0,100,0}, 1)
end
```


###onLoad(...)

This function is called when a game save is finished loading every Object. This is where most setup code will go. The fast-forward and rewind feature will also cause this function to activate. If this function is in an Object's script and that Object is spawned, like by removing it from a container, it too will trigger onLoad().

!!!info "onLoad(String save_state)"
	* **String save_state**: The encoded string containing any save_state (saved) data.
		* {>>If there is no data saved, this returns an empty String.<<}

``` Lua
function onLoad()
	print("Loading complete")
end
```

???example "Example of onLoad and onSave being used to save/load data"
    ``` Lua
	--Runs whenever game is saved/autosaved
	function onSave()
		local data_to_save = {someData=50}
		saved_data = JSON.encode(data_to_save)
		--saved_data = "" --Remove -- at start & save to clear save data
		return saved_data
	end

	--Runs when game is loaded
	function onLoad(saved_data)
		--Loads the tracking for if the game has started yet
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

!!!info "onObjectDestroy(Object dying_object)"
	* **Object dying_object**: The object that was destroyed.

``` Lua
function onObjectDestroy(destroyedObj)
	print(destroyedObj.getName())
end
```

---


###onObjectDrop(...)

Called whenever any object is dropped by a player.

!!!info "onObjectDrop(String player_color, Object dropped_object)"
	* **String player_color**: A String of the color of the player who dropped the object.
	* **Object dropped_object**: The Object in game which was dropped.

``` Lua
function onObjectDrop(colorName, obj)
	print(colorName .. " dropped " .. obj.getName())
end
```

---


###onObjectEnterScriptingZone(...)

Called when any object enters any scripting zone.

!!!info "onObjectEnterScriptingZone(Object zone, Object enter_object)"
	* **Object zone**: The Object of the scripting zone.
	* **Object enter_object**: The Object triggering the function.

``` Lua
function onObjectEnterScriptingZone(zone, obj)
	print(obj.getGUID())
end
```

---


###onObjectLeaveScriptingZone(...)

Called when any object leaves any scripting zone.

!!!info "onObjectLeaveScriptingZone(Object zone, Object enter_object)"
	* **Object zone**: The Object of the scripting zone.
	* **Object enter_object**: The Object triggering the function.

``` Lua
function onObjectLeaveScriptingZone(zone, obj)
	print(obj.getGUID())
end
```

---


###onObjectLeaveContainer(...)

Called when any object leaves any container.

!!!info "onObjectLeaveContainer(Object container, Object leave_object)"
	* **Object container**: The Object reference for the container the object left.
	* **Object leave_object**: The Object reference for the object that left the container.

``` Lua
function onObjectLeaveContainer(bag, obj)
	print(bag)
	print(obj)
end
```

---


###onObjectLoopingEffect(...)

Called whenever the looping effect of an [AssetBundle](assetbundle) is activated.

!!!info "onObjectLoopingEffect(Object loop_object, Int index)"
	* **Object loop_object**: The Object reference to the AssetBundle which had its loop activated.
	* **Int index**: The Int of the index number for the loop activated.

``` Lua
function onObjectLoopingEffect(obj, index)
	print("Loop " .. index .. " activated.")
end
```

---


###onObjectPickUp(...)

Called whenever a Player picks up an Object.

!!!info "onObjectPickUp(String player_color, Object picked_up_object)"
	* **String player_color**: A String of the color of the player who picked up the object.
	* **Object picked_up_object**: The Object in game which was picked up.

``` Lua
function onObjectPickUp(colorName, obj)
	print(colorName .. " picked up " .. obj.getName())
end
```

---


###onObjectRandomize(...)

Called when an Object is randomized. Like when shuffling a deck or shaking dice.

!!!info "onObjectRandomize(Object randomize_object, String player_color)"
	* **Object spawn_object**: The Object which triggered this function.
	* **String player_color**: A String of the color of the player who triggered the function.

``` Lua
function onObjectRandomize(obj, color)
	print(obj.getName() .. " was randomized by " .. color)
end
```

---


###onObjectSpawn(...)

Called when any Object is spawned/created.

!!!info "onObjectSpawn(Object spawn_object)"
	* **Object spawn_object**: The Object which triggered this function.

``` Lua
function onObjectSpawn(obj)
	print(obj)
end
```

---


###onObjectTriggerEffect(...)

Called whenever the trigger effect of an [AssetBundle](assetbundle) is activated.

!!!info "onObjectTriggerEffect(Object loop_object, Int index)"
	* **Object loop_object**: The Object reference to the AssetBundle which had its trigger activated.
	* **Int index**: The Int of the index number for the trigger activated.

``` Lua
function onObjectTriggerEffect(obj, index)
	print("Loop " .. index .. " activated.")
end
```

---


###onPlayerChangeColor(...)

Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect.

!!!info "onPlayerChangeColor(String player_color)"
	* **String player_color**: A String of the color of the player who triggered the function.

``` Lua
function onPlayerChangeColor(color)
	print(color)
end
```

---


###onPlayerTurnEnd(...)

Called at the end of a player's turn when using the in-game turn system.

!!!info "onPlayerTurnEnd(String player_color_end, String player_color_next)"
	* **String player_color_end**: A String of the color of the player who's turn ended.
	* **String player_color_next**: A String of the color of the player who's turn is next.

``` Lua
function onPlayerTurnEnd(color_end, color_next)
	print(color_end .. "'s turn has ended.")
	print(color_next .. "'s turn starts now.")
end
```

---


###onPlayerTurnStart(...)

Called at the end of a player's turn when using the in-game turn system.

!!!info "onPlayerTurnStart(String player_color_start, String player_color_prev)"
	* **String player_color_start**: A String of the color of the player who's turn is starting.
	* **String player_color_prev**: A String of the color of the player who's turn just ended.

``` Lua
function onPlayerTurnStart(color_start, color_prev)
	print(color_start .. "'s turn starts now.")
	print(color_prev .. "'s turn has ended.")
end
```

---


###onSave()

Called whenever your game is saved, either manually or by auto-save. It is used to allow information to persist through saving/loading. It allows you to place information into a table that is written into the save file. It works on Global information and can also be used to save information onto an Object.

!!!important
	When using `onSave()`, information is saved into the save file you are using. Using *Save & Apply* does NOT cause it to record data, only overwriting your save will update what information `onSave()` is trying to record.

!!!warning
	You can save almost any data in a table using this function, but Object references **DO NOT** persist. If you need to record an Object using `onSave()`, record its GUID instead.

``` Lua
data_table = {answer=42}

function onSave()
	saved_data = JSON.encode(data_table)
	self.script_state = saved_data
end
```

Check the [`onLoad()`](#onload) section for how to load the information you record into your save file.

---


###onScriptingButtonDown(...)

Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10.

!!!info "onScriptingButtonDown(Int index, String player_color)"
	* **Int index**: An Int for the index number, representing which key was pressed.
	* **String player_color**: A String of the color of the player who triggered the function.

``` Lua
function onScriptingButtonDown(index, color)
	print(index)
end
```

---

###onScriptingButtonUp(...)

Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10.

!!!info "onScriptingButtonUp(Int index, String player_color)"
	* **Int index**: An Int for the index number, representing which key was released.
	* **String player_color**: A String of the color of the player who triggered the function.

``` Lua
function onScriptingButtonUp(index, color)
	print(index)
end
```

---


###onUpdate()

Called **every frame**.

!!!warning
	This is a very expensive function and can easily slow/crash your game if missused. Use with caution.

``` Lua
function onUpdate()
	print("This will probably slow your game down."
end
```

---

---





##Function Details (Object only)

###onCollisionEnter(...)

This function is called when an Object starts colliding with the Object the function is on. Does not work in Global.

!!!info "onCollisionEnter(Table collision_info)"
	* **table collision_info**: A Table containing data on colliding object.
		* **collision_info.*collision_object*** = [Object](object) collision_object
		* **collision_info.*contact_points*** = Table contact_points
			* {>>This is an array (table) of tables. Each contact point is a vector.<<}
		* **collision_info.*relative_velocity*** = [Vector](vector)

``` Lua
--Example Usage
function onCollisionEnter(info)
	print(info.collision_object)
end
```
``` Lua
--Example returned table
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

!!!info "onCollisionExit(Table collision_info)"
	* **table collision_info**: A Table containing data on colliding object.
		* **collision_info.*collision_object*** = [Object](object) collision_object
		* **collision_info.*contact_points*** = Table contact_points
			* {>>This is an array (table) of tables. Each contact point is a vector.<<}
		* **collision_info.*relative_velocity*** = [Vector](vector)

``` Lua
--Example Usage
function onCollisionExit(info)
	print(info.collision_object)
end
```
``` Lua
--Example returned table
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
	This is a very expensive function and can easily slow/crash your game if missused. Use with caution.

!!!info "onCollisionStay(Table collision_info)"
	* **table collision_info**: A Table containing data on colliding object.
		* **collision_info.*collision_object*** = [Object](object) collision_object
		* **collision_info.*contact_points*** = Table contact_points
			* {>>This is an array (table) of tables. Each contact point is a vector.<<}
		* **collision_info.*relative_velocity*** = [Vector](vector)

``` Lua
--Example Usage
function onCollisionStay(info)
	print(info.collision_object)
end
```
``` Lua
--Example returned table
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

!!!info "onDrop(String player_color)"
	* **String player_color**: A String of a [Player](player)'s color.

``` Lua
function onDrop(color)
	print(color)
end
```

---


###onPickUp(...)

Called when a player picks up an Object.

!!!info "onPickUp(String player_color)"
	* **String player_color**: A String of a [Player](player)'s color.

``` Lua
function onPickUp(color)
	print(color)
end
```

---
