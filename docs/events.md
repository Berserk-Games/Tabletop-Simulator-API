Games frequently need to execute code in response to some action, interaction, or change taking place in the game,
collectively referred to as _events_.

## Event Handlers

Event handlers are **functions you define**, that Tabletop Simulator calls.

There are many event handlers that you can define. Each one gives you an opportunity to handle occurrences of a
particular event.

When Tabletop Simulator calls your function, it will provide event-specific details as arguments to your event handler
function.

In order for Tabletop Simulator to discover an event handler, it must be defined as a global variable with a specific
name. The name that you use depends on which event you wish to handle. Event-specific details are covered below.

!!!note
	Whilst event handler _names_ corresponds with just one type of event. Each event may have multiple corresponding
	event handlers (i.e. event handler names) that Tabletop Simulator will look for and execute.

There are three types of event handlers:

* [Universal Event Handlers](#universal-event-handlers)
* [Global Event Handlers](#global-event-handlers)
* [Object Event Handlers](#object-event-handlers)

### Universal Event Handlers

Universal Event Handlers may be defined in the [Global script](intro.md#global-script) _and/or_
[Object scripts](intro.md#object-scripts).

### Global Event Handlers

Global Event Handlers may _only_ be defined in the [Global script](intro.md#global-script).

If you define a function using the name of a Global Event Handler in an
[Object script](intro.md#object-scripts). It simply won't be called.

### Object Event Handlers

Object Event Handlers may _only_ be defined in [Object scripts](intro.md#object-scripts).

If you define a function using the name of an Object Event Handler in your
[Global script](intro.md#global-script). It simply won't be called.

## Event Handler Execution

_Typically_, if there are multiple event handlers for the one event i.e. in an Object script and Global Script _and/or_
multiple Object scripts, then _all_ of these event handlers will be executed.

!!!info
	Some event handlers permit you to return a value in order to trigger an optional side effect. For example, returning
	`false` from a "try" event handler will prevent whatever action is being _tried_. If you return a value that
	triggers an optional side effect, then subsequent event handlers (for the same event occurrence) will _not_ be
	executed.

## Event Summary

### Universal Event Handlers {: #universal-event-handlers-summary }

As described above, you may declare these functions in the [Global script](intro.md#global-script) or in
[Object scripts](intro.md#object-scripts).

Function Name | Description | &nbsp;
-- | -- | --
onBlindfold([<span class="tag pla"></span>](types.md) player, [<span class="tag boo"></span>](types.md) blindfolded) | Called when a player puts on or takes off their blindfold. | [:i:](#onblindfold)
onChat([<span class="tag str"></span>](types.md) message, [<span class="tag pla"></span>](types.md) sender) | Called when a user sends an in-game chat message. | [:i:](#onchat)
onExternalMessage([<span class="tag tab"></span>](types.md) data) | Called when a [custom message](externaleditorapi.md#custom-message) is received from an external process via the External Editor API. | [:i:](#onexternalmessage)
onFixedUpdate() | Called **every physics tick** (90 times a second). This is a frame independent onUpdate(). | [:i:](#onfixedupdate)
onLoad([<span class="tag str"></span>](types.md) script_state) | Called when a save has completely finished loading. | [:i:](#onload)
onObjectCollisionEnter([<span class="tag obj"></span>](types.md) registered_object, [<span class="tag tab"></span>](types.md) collision_info) | Called when an Object starts colliding with a [collision registered](object.md#registercollisions) Object. | [:i:](#onobjectcollisionenter)
onObjectCollisionExit([<span class="tag obj"></span>](types.md) registered_object, [<span class="tag tab"></span>](types.md) collision_info) | Called when an Object stops colliding with a [collision registered](object.md#registercollisions) Object. | [:i:](#onobjectcollisionexit)
onObjectCollisionStay([<span class="tag obj"></span>](types.md) registered_object, [<span class="tag tab"></span>](types.md) collision_info) | Called **every frame** that an Object is colliding with a [collision registered](object.md#registercollisions) Object. | [:i:](#onobjectcollisionstay)
onObjectDestroy([<span class="tag obj"></span>](types.md) object) | Called whenever an object is about to be destroyed. | [:i:](#onobjectdestroy)
onObjectDrop([<span class="tag str"></span>](types.md) player_color, [<span class="tag obj"></span>](types.md) object) | Called when an object is dropped by a player. | [:i:](#onobjectdrop)
onObjectEnterContainer([<span class="tag obj"></span>](types.md) container, [<span class="tag obj"></span>](types.md) object) | Called when an object enters a container. Includes decks | [:i:](#onobjectentercontainer)
onObjectEnterScriptingZone([<span class="tag obj"></span>](types.md) zone, [<span class="tag obj"></span>](types.md) object) {: #onobjectenterscriptingzone data-toc-label="onObjectEnterScriptingZone(...)" data-toc-child-of="universal-event-handler-details" } | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [onObjectEnterZone(...)](#onobjectenterzone)_.</p> Called when an object enters a _scripting_ zone. |
onObjectEnterZone([<span class="tag obj"></span>](types.md) zone, [<span class="tag obj"></span>](types.md) object) | Called when an object enters a zone. | [:i:](#onobjectenterzone)
onObjectFlick([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color, [<span class="tag vec"></span>](types.md) impulse) | Called when a player flicks an object. | [:i:](#onobjectflick)
onObjectHover([<span class="tag str"></span>](types.md) player_color, [<span class="tag obj"></span>](types.md) object) | Called when the object being hovered over by a player's pointer (cursor) changes. | [:i:](#onobjecthover)
onObjectLeaveContainer([<span class="tag obj"></span>](types.md) container, [<span class="tag obj"></span>](types.md) object) | Called when an object leaves a container. | [:i:](#onobjectleavecontainer)
onObjectLeaveScriptingZone([<span class="tag obj"></span>](types.md) zone, [<span class="tag obj"></span>](types.md) object) {: #onobjectleavescriptingzone data-toc-label="onObjectLeaveScriptingZone(...)" data-toc-child-of="universal-event-handler-details" } | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [onObjectLeaveZone(...)](#onobjectleavezone)_.</p> Called when an object leaves a _scripting_ zone. |
onObjectLeaveZone([<span class="tag obj"></span>](types.md) zone, [<span class="tag obj"></span>](types.md) object) | Called when an object leaves a zone. | [:i:](#onobjectleavezone)
onObjectLoopingEffect([<span class="tag obj"></span>](types.md) object, [<span class="tag int"></span>](types.md) index) | Called whenever the looping effect of an [AssetBundle](behavior/assetbundle.md) is activated. | [:i:](#onobjectloopingeffect)
onObjectNumberTyped([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color, [<span class="tag int"></span>](types.md) number) | Called when a player types a number whilst hovering over an object. | [:i:](#onobjectnumbertyped)
onObjectPageChange([<span class="tag obj"></span>](types.md) object) | Called when a Custom PDF object changes page. | [:i:](#onobjectpagechange)
onObjectPeek([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color) | Called when a player peeks at an Object. | [:i:](#onobjectpeek)
onObjectPickUp([<span class="tag str"></span>](types.md) player_color, [<span class="tag obj"></span>](types.md) object) | Called whenever a Player picks up an Object. | [:i:](#onobjectpickup)
onObjectRandomize([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color) | Called when an Object is randomized. Like when shuffling a deck or shaking dice. | [:i:](#onobjectrandomize)
onObjectRotate([<span class="tag obj"></span>](types.md) object, [<span class="tag flo"></span>](types.md) spin, [<span class="tag flo"></span>](types.md) flip, [<span class="tag str"></span>](types.md) player_color,  [<span class="tag flo"></span>](types.md) old_spin, [<span class="tag flo"></span>](types.md) old_flip) | Called when a player rotates an object. | [:i:](#onobjectrotate)
onObjectSearchEnd([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color) | Called when a search is finished on a container. | [:i:](#onobjectsearchend)
onObjectSearchStart([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color) | Called when a search is started on a container. | [:i:](#onobjectsearchstart)
onObjectSpawn([<span class="tag obj"></span>](types.md) object) | Called when an object is spawned/created. | [:i:](#onobjectspawn)
onObjectStateChange([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) old_state_guid) | Called after an object changes state. | [:i:](#onobjectstatechange)
onObjectTriggerEffect([<span class="tag obj"></span>](types.md) object, [<span class="tag int"></span>](types.md) index) | Called whenever the trigger effect of an [AssetBundle](behavior/assetbundle.md) is activated. | [:i:](#onobjecttriggereffect)
onPlayerAction([<span class="tag pla"></span>](types.md) player, [Action](#onplayeraction-actions) action, [<span class="tag tab"></span>](types.md) targets) | Called when a player attempts to perform an action. | [:i:](#onplayeraction)
onPlayerChangeColor([<span class="tag str"></span>](types.md) player_color) | Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect. | [:i:](#onplayerchangecolor)
onPlayerChangeTeam([<span class="tag str"></span>](types.md) player_color, [<span class="tag str"></span>](types.md) team) | Called when a player changes team. | [:i:](#onplayerchangeteam)
onPlayerConnect([<span class="tag pla"></span>](types.md) player) | Called when a [Player](player/instance.md) connects to a game. | [:i:](#onplayerconnect)
onPlayerDisconnect([<span class="tag pla"></span>](types.md) player) | Called when a [Player](player/instance.md) disconnects from a game. | [:i:](#onplayerdisconnect)
onPlayerPing([<span class="tag pla"></span>](types.md) player, [<span class="tag vec"></span>](types.md) position) | Called when a player [pings](https://kb.tabletopsimulator.com/game-tools/line-tool/#ping) a location. | [:i:](#onplayerping)
onPlayerTurn([<span class="tag pla"></span>](types.md) player, [<span class="tag pla"></span>](types.md) previous_player) | Called at the start of a player's turn. | [:i:](#onplayerturn)
onSave() | Called whenever a script needs to save its state. | [:i:](#onsave)
onScriptingButtonDown([<span class="tag int"></span>](types.md) index, [<span class="tag str"></span>](types.md) player_color) | Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10. | [:i:](#onscriptingbuttondown)
onScriptingButtonUp([<span class="tag int"></span>](types.md) index, [<span class="tag str"></span>](types.md) player_color) | Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10. | [:i:](#onscriptingbuttonup)
onUpdate() | Called **every frame**. | [:i:](#onupdate)

### Global Event Handlers {: #global-event-handler-summary }

As described above, you may declare these functions in the [Global script](intro.md#global-script).

Function Name | Description | &nbsp;
-- | -- | --
filterObjectEnterContainer([<span class="tag obj"></span>](types.md) container, [<span class="tag obj"></span>](types.md) object) {: #filterobjectentercontainer data-toc-label="filterObjectEnterContainer(...)" data-toc-child-of="global-event-handler-details" } | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [tryObjectEnterContainer(...)](#tryobjectentercontainer)_.</p> Called when an object attempts to enter a container. |
onZoneGroupSort([<span class="tag obj"></span>](types.md) zone, [<span class="tag tab"></span>](types.md) group, [<span class="tag boo"></span>](types.md) reversed) | Called when sorting is required for a group of objects being laid out by a layout zone. | [:i:](#onzonegroupsort)
tryObjectEnterContainer([<span class="tag obj"></span>](types.md) container, [<span class="tag obj"></span>](types.md) object) | Called when an object attempts to enter a container. | [:i:](#tryobjectentercontainer)
tryObjectRandomize([<span class="tag obj"></span>](types.md) object, [<span class="tag str"></span>](types.md) player_color) | Called when a player attempts to randomize an Object. | [:i:](#tryobjectrandomize)
tryObjectRotate([<span class="tag obj"></span>](types.md) object, [<span class="tag flo"></span>](types.md) spin, [<span class="tag flo"></span>](types.md) flip, [<span class="tag str"></span>](types.md) player_color,  [<span class="tag flo"></span>](types.md) old_spin, [<span class="tag flo"></span>](types.md) old_flip) | Called when a player attempts to rotate an object. | [:i:](#tryobjectrotate)

### Object Event Handlers {: #object-event-handlers-summary }

As described [above](#object-event-handlers), you may declare these functions in
[Object scripts](intro.md#object-scripts).

These events pertain to the script-owner Object (accessible as `self` within the script).

!!!important
	These **cannot** declare these event handlers in the [Global script](intro.md#global-script).

Function Name | Description | &nbsp;
-- | -- | --
filterObjectEnter([<span class="tag obj"></span>](types.md) object) | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [tryObjectEnter(...)](#tryobjectenter)_.</p> Called when an object attempts to enter the script-owner Object (container). | [:i:](#tryobjectenter)
onCollisionEnter([<span class="tag tab"></span>](types.md) collision_info) | Called when an Object starts colliding with the script-owner Object. | [:i:](#oncollisionenter)
onCollisionExit([<span class="tag tab"></span>](types.md) collision_info) | Called when an Object stops colliding with the script-owner Object. | [:i:](#oncollisionexit)
onCollisionStay([<span class="tag tab"></span>](types.md) collision_info) | Called **every frame** that an Object is colliding with the script-owner Object. | [:i:](#oncollisionstay)
onDestroy() | Called when the script-owner Object is about to be destroyed. | [:i:](#ondestroy)
onDrop([<span class="tag str"></span>](types.md) player_color) | Called when a player drops the script-owner Object. | [:i:](#ondrop)
onFlick([<span class="tag str"></span>](types.md) player_color, [<span class="tag vec"></span>](types.md) impulse) | Called when a player flicks the script-owner Object | [:i:](#onflick)
onGroupSort([<span class="tag tab"></span>](types.md) group, [<span class="tag boo"></span>](types.md) reversed) | Called when sorting is required for a group of objects being laid out by the script-owner layout zone. | [:i:](#ongroupsort)
onHover([<span class="tag str"></span>](types.md) player_color) | Called when a player moves their pointer (cursor) over the script-owner Object. | [:i:](#onhover)
onNumberTyped([<span class="tag str"></span>](types.md) player_color, [<span class="tag int"></span>](types.md) number) | Called when a player types a number whilst hovering over the script-owner Object. | [:i:](#onnumbertyped)
onPageChange() | Called when the script-owner Custom PDF's page is changed. | [:i:](#onpagechange)
onPeek([<span class="tag str"></span>](types.md) player_color) | Called when a player peeks at the script-owner Object. | [:i:](#onpeek)
onPickUp([<span class="tag str"></span>](types.md) player_color) | Called when a player picks up the script-owner Object. | [:i:](#onpickup)
onRandomize([<span class="tag str"></span>](types.md) player_color) | Called when the script-owner Object is randomized. Like when shuffling a deck or shaking dice. | [:i:](#onrandomize)
onRotate([<span class="tag flo"></span>](types.md) spin, [<span class="tag flo"></span>](types.md) flip, [<span class="tag str"></span>](types.md) player_color,  [<span class="tag flo"></span>](types.md) old_spin, [<span class="tag flo"></span>](types.md) old_flip) | Called when a player rotates the script-owner Object. | [:i:](#onrotate)
onSearchEnd([<span class="tag str"></span>](types.md) player_color) | Called when a player finishes searches the script-owner Object. | [:i:](#onsearchend)
onSearchStart([<span class="tag str"></span>](types.md) player_color) | Called when a player starts searching the script-owner Object. | [:i:](#onsearchstart)
onStateChange([<span class="tag str"></span>](types.md) old_state_guid) | Called when the script-owner Object spawned as a result of an Object state change. | [:i:](#onstatechange)
tryObjectEnter([<span class="tag obj"></span>](types.md) object) | Called when another object attempts to enter the script-owner Object (container).| [:i:](#tryobjectenter)
tryRandomize([<span class="tag str"></span>](types.md) player_color) | Called when a player attempts to randomize the script-owner Object. | [:i:](#tryrandomize)
tryRotate([<span class="tag flo"></span>](types.md) spin, [<span class="tag flo"></span>](types.md) flip, [<span class="tag str"></span>](types.md) player_color,  [<span class="tag flo"></span>](types.md) old_spin, [<span class="tag flo"></span>](types.md) old_flip) | Called when a player attempts to rotate the script-owner Object. | [:i:](#tryrotate)

---

## Universal Event Handler Details {: data-toc-sort }

###onBlindfold(...)

Called when a player puts on or takes off their blindfold.

!!!info "onBlindfold(player, blindfolded)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) who put on or took off their blindfold.
	* [<span class="tag boo"></span>](types.md) **blindfolded**: Whether the player is now blindfolded.

!!!example
	Print a message indicating which player put on or took off their blindfold.
	``` Lua
	function onBlindfold(player, blindfolded)
		if blindfolded then
			print(player.color .. " put their blindfold on.")
		else
			print(player.color .. " took their blindfold off.")
		end
	end
	```

---

###onChat(...)

Called when a user sends an in-game chat message.

Return `false` to prevent the message appearing in the chat window.

!!!info "onChat(message, sender)"
	* [<span class="tag str"></span>](types.md) **message**: Chat message which triggered the function.
	* [<span class="tag pla"></span>](types.md) **sender**: Player which sent the chat message.

!!!example
	Prevent the blue player from sending messages to other player's. Instead print the message to the host. Permit chat from all other players.
	```lua
	function onChat(message, sender)
		if sender.color == "Blue" then
			print("Blue said: " .. message)
			return false
		end

		return true
	end
	```

---


###onExternalMessage(...)

Called when a [custom message](externaleditorapi.md#custom-message) is received from an external process via the External Editor API.

!!!info "onExternalMessage(data)"
	* [<span class="tag tab"></span>](types.md) **data**: The data sent by the external process.

!!!example
	Log the contents of received custom external messages.
	```lua
	function onExternalMessage(data)
		log(data, "External Message")
	end
	```

---


###onFixedUpdate()

Called **every physics tick** (90 times a second). This is a frame independent onUpdate().

!!!danger
	Due to the frequency at which this function is called, any implementation must be very simple/fast, in order to avoid
	slowing down your game.

!!!example
	Print a message every 180 physics ticks.
	``` Lua
	local tick_count = 0
	function onFixedUpdate()
		tick_count = tick_count + 1
		if tick_count >= 180 then
			print("180 physics ticks passed.")
			tick_count = 0
		end
	end
	```

###onLoad(...)

**Global Script**

Called when a saved game (and all Objects it contains) have finished loading. This includes manually loaded games/saves,
as well as when a user rewinds.

**Object Script**

This will be called when a saved game finishes loading _or_ when the script-owner Object has finished loading for some
other reason e.g. if the script-owner Object was pulled out of a container mid-game.

!!!info "onLoad(script_state)"
	* [<span class="tag str"></span>](types.md) **script_state**: The previously saved script state i.e. value returned
	from [onSave(...)](#onsave), or an empty string if there is no saved script state available.


!!!example
	Decodes a JSON representation of a game state, consisting of nested tables, strings, numbers and object GUIDs. Then
	obtains an Object from the saved GUID.
	```lua
    local some_object -- We'll store an object reference to use later.

	function onLoad(script_state)
		-- JSON decode our saved state
		local state = JSON.decode(script_state)

		-- In this example, we're assuming the existence of some specific saved state data.
		local questions = state.questions -- access a nested table

		for _, qa in ipairs(state.questions) do
			print("Question: " .. qa.question)
			print("Answer: " .. qa.answer)
		end

		some_object = getObjectFromGUID(state.guids.some_object)

		-- Let's highlight some_object a random color.
		-- Because why not.

		local colors = {'Blue', 'Yellow', 'Green'}
		some_object.highlightOn(colors[math.random(1, 3)])

		return JSON.encode(state)
	end
	```
	Refer to [onSave(...)](#onsave) to see an example of how this same save state structure could be created. Subscribe
	to the [onSave/onLoad example mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2430471959) for a more
	functionally complete example.

---

###onObjectCollisionEnter(...)

Called when an Object starts colliding with a [collision registered](object.md#registercollisions) Object.

!!!info "onObjectCollisionEnter(registered_object, collision_info)"
	* [<span class="tag obj"></span>](types.md) **registered_object**: The object registered to receive collision events.
	* [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object coming into contact with `registered_object`.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the direction and magnitude of the collision.

``` Lua
-- Example Usage
function onObjectCollisionEnter(registered_object, info)
	print(tostring(info.collision_object) .. " collided with " .. tostring(registered_object))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---


###onObjectCollisionExit(...)

Called when an Object stops colliding with a [collision registered](object.md#registercollisions) Object.

!!!info "onObjectCollisionExit(registered_object, collision_info)"
	* [<span class="tag obj"></span>](types.md) **registered_object**: The object registered to receive collision events.
	* [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object leaving contact with `registered_object`.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the velocity of the object that has moved out of contact.

``` Lua
-- Example Usage
function onObjectCollisionExit(registered_object, info)
	print(tostring(info.collision_object) .. " stopped colliding with " .. tostring(registered_object))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---


###onObjectCollisionStay(...)

Called **every frame** that an Object is colliding with a [collision registered](object.md#registercollisions) Object.

!!!warning
	Due to the frequency at which this function may be called, any implementation must be very simple/fast, in order to
	avoid slowing down your game.

!!!info "onObjectCollisionStay(registered_object, collision_info)"
	* [<span class="tag obj"></span>](types.md) **registered_object**: The object registered to receive collision events.
    * [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object coming into contact with `registered_object`.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the direction and magnitude of the collision.

``` Lua
-- Example Usage
function onObjectCollisionStay(registered_object, info)
	print(tostring(info.collision_object) .. " still colliding with " .. tostring(registered_object))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---

###onObjectDestroy(...)

Called whenever an object is about to be destroyed.

The Object reference (`object`) is valid in this callback, but won't be valid next frame (as the Object will be
destroyed by then).

This event fires immediately before the Object’s [onDestroy()](#ondestroy).

!!!info "onObjectDestroy(object)"
	* [<span class="tag obj"></span>](types.md) **object**: The object that is about to be destroyed.

!!!example
	Print the name of the Object which is about to be destroyed.
	``` Lua
	function onObjectDestroy(object)
		print(object.getName())
	end
	```

---


###onObjectDrop(...)

Called when an object is dropped by a player.

!!!info "onObjectDrop(player_color, object)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player who dropped the Object.
	* [<span class="tag obj"></span>](types.md) **object**: The Object in game which was dropped.

``` Lua
function onObjectDrop(colorName, object)
	print(colorName .. " dropped " .. object.getName())
end
```

---

###onObjectEnterContainer(...)

Called when an object enters a container.

!!!info "onObjectEnterContainer(container, object)"
	* [<span class="tag obj"></span>](types.md) **container**: Container that was entered.
	* [<span class="tag obj"></span>](types.md) **object**: Object that entered the container.

!!!example
	Each time an object enters a container, print the GUID of the object and the GUID of the container it entered.
	```lua
	function onObjectEnterContainer(container, object)
		print("Object " .. object.guid .. " entered container " .. container.guid)
	end
	```

---

###onObjectEnterZone(...)

Called when an object enters a zone.

!!!important
	Objects with [tags](object.md#tag-functions) will only enter zones with compatible tags.

!!!info "onObjectEnterZone(zone, object)"
	* [<span class="tag obj"></span>](types.md) **zone**: Zone that was entered.
	* [<span class="tag obj"></span>](types.md) **object**: Object that entered the zone.

!!!example
	Each time an object enters a zone, print the GUID of the object and the GUID of the scripting zone it entered.
	```lua
	function onObjectEnterZone(zone, object)
		print("Object " .. object.guid .. " entered zone " .. zone.guid)
	end
	```

---

###onObjectFlick(...)

Called whenever a player [flicks](https://kb.tabletopsimulator.com/game-tools/flick-tool/) flicks an object.

!!!info "onObjectFlick(object, player_color, impulse)"
* [<span class="tag obj"></span>](types.md) **object**: The object that was flicked.
* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who flicked an object.
* [<span class="tag vec"></span>](types.md) **impulse**: The impulse applied to the object.

!!!example
	Print the player color, type of the flicked object, and magnitude of the flick:
	``` Lua
	function onObjectFlick(object, player_color, impulse)
		print(player_color .. " flicked a " .. object.type ..  " with impulse " .. impulse:magnitude())
	end
	```

---

###onObjectHover(...)

Called when the object being hovered over by a player's pointer (cursor) changes.

!!!info "onObjectHover(player_color, object)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who moved their pointer over an object.
	* [<span class="tag obj"></span>](types.md) **object**: Object the player's pointer is hovering over, or `nil` when a player moves their pointer such that it is no longer hovering over an object.

!!!example
	Each time a player hovers over an object, print the player color and the GUID of the object being hovered over. If a player moves their cursor such that
	they're no longer hovering over an object, print "Nothing" instead of the object GUID.
	```lua
	function onObjectHover(player_color, object)
		local target = object and object.guid or "Nothing"
		print(player_color .. " hovered over " .. target)
	end
	```

---

###onObjectLeaveContainer(...)

Called when an object leaves a container.

!!!info "onObjectLeaveContainer(container, object)"
	* [<span class="tag obj"></span>](types.md) **container**: Container the object left.
	* [<span class="tag obj"></span>](types.md) **object**: Object that left the container.

!!!example
	Each time an object leaves a container, print the GUID of the object and the GUID of the container it left.
	```lua
	function onObjectLeaveContainer(container, object)
		print("Object " .. object.guid .. " left container " .. container.guid)
	end
	```

---

###onObjectLeaveZone(...)

Called when an object leaves a zone.

!!!info "onObjectLeaveZone(zone, object)"
	* [<span class="tag obj"></span>](types.md) **zone**: Zone that was left.
	* [<span class="tag obj"></span>](types.md) **object**: The object that left.

!!!example
	Each time an object leaves a zone, print the GUID of the object and the GUID of the zone it left.
	```lua
	function onObjectLeaveZone(zone, object)
		print("Object " .. object.guid .. " left zone " .. zone.guid)
	end
	```

---

###onObjectLoopingEffect(...)

Called whenever the looping effect of an [AssetBundle](behavior/assetbundle.md) is activated.

!!!info "onObjectLoopingEffect(object, index)"
	* [<span class="tag obj"></span>](types.md) **object**: AssetBundle which had its loop activated.
	* [<span class="tag int"></span>](types.md) **index**: Index number for the loop activated.

``` Lua
function onObjectLoopingEffect(object, index)
	print("Loop " .. index .. " activated.")
end
```

---

###onObjectNumberTyped(...)

Called when a player types a number whilst hovering over an object.

If you wish to prevent the default behavior (e.g. drawing a card) then you may return `true` to indicate you've handled the event yourself.

!!!info "onObjectNumberTyped(object, player_color, number)"
	* [<span class="tag obj"></span>](types.md) **object**: The object the player was hovering over whilst typing a number.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that typed the number.
	* [<span class="tag int"></span>](types.md) **number**: The number typed.

!!!example
	Print the player color, the number they entered and the type of object being hovered over:
	``` Lua
	function onObjectNumberTyped(object, player_color, number)
		print(player_color .. " typed " .. number .. " whilst hovering over a " .. object.type)
	end
	```

!!!example
	Prevent players drawing more than 2 cards at a time:
	``` Lua
	function onObjectNumberTyped(object, player_color, number)
		if object.type == 'Deck' and number > 2 then
			print("Sorry. You can only draw a maximum of 2 cards.")
			return true
		end
	end
	```

---

###onObjectPageChange(...)

Called when an object's Custom PDF page is changed.

!!!info "onObjectPageChange(object)"
	* [<span class="tag obj"></span>](types.md) **object**: The object that's page changed.

!!!example
	Print the name of the object and what page it changed to:
	``` Lua
	function onObjectPageChange(object)
		print(object.getName() .. " changed page to " .. object.Book.getPage())
	end
	```

---



###onObjectPeek(...)

Called when a player [peeks](https://kb.tabletopsimulator.com/player-guides/advanced-controls/#peek) at an Object.

!!!info "onObjectPeek(object, player)"
	* [<span class="tag obj"></span>](types.md) **object**: The Object that was peeked at.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that peeked.

!!!example
	Print the color of the player that peeked at an object.
	``` Lua
	function onObjectPeek(object, player_color)
		print(player_color .. " peeked at an Object.")
	end
	```

---


###onObjectPickUp(...)

Called whenever a Player picks up an Object.

!!!info "onObjectPickUp(player_color, object)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player who picked up the object.
	* [<span class="tag obj"></span>](types.md) **object**: Object which was picked up.

``` Lua
function onObjectPickUp(colorName, object)
	print(colorName .. " picked up " .. object.getName())
end
```

---


###onObjectRandomize(...)

Called when an Object is randomized. Like when shuffling a deck or shaking dice.

!!!info "onObjectRandomize(object, player_color)"
	* [<span class="tag obj"></span>](types.md) **object**: The Object which triggered this function.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.



``` Lua
function onObjectRandomize(object, color)
	print(object.getName() .. " was randomized by " .. color)
end
```

---

###onObjectRotate(...)

Called when a player rotates an object.

!!!warning
	Only called in response to explicit player rotation actions. Will _not_ be called when physics/collisions cause an
	object to rotate.

!!!info "onObjectRotate(object, spin, flip, player_color, old_spin, old_flip)"
	* [<span class="tag obj"></span>](types.md) **object**: The object the player is trying to rotate.
	* [<span class="tag flo"></span>](types.md) **spin**: The object's target spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **flip**: The object's target flip rotation in degrees within the interval \[0, 360).
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that performed the rotation.
	* [<span class="tag flo"></span>](types.md) **old_spin**: The object's previous spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **old_flip**: The object's previous flip rotation in degrees within the interval \[0, 360).

!!!example
	When an object is rotated, print which player was responsible and what rotation was performed.
	```lua
	function onObjectRotate(object, spin, flip, player_color, old_spin, old_flip)
		if spin ~= old_spin then
			print(player_color .. " spun " .. tostring(object) .. " from " .. old_spin .. " degrees to " .. spin .. " degrees")
		end

		if flip ~= old_flip then
			print(player_color .. " flipped " .. tostring(object) .. " from " .. old_flip .. " degrees to " .. flip .. " degrees")
		end
	end
	```

---


###onObjectSearchEnd(...)

Called when a search is finished on a container.

!!!info "onObjectSearchEnd(object, player_color)"
    * [<span class="tag obj"></span>](types.md) **object**: The Object which was searched.
    * [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.

---


###onObjectSearchStart(...)

Called when a search is started on a container.

!!!info "onObjectSearchStart(object, player_color)"
    * [<span class="tag obj"></span>](types.md) **object**: The Object which was searched.
    * [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.

---


###onObjectSpawn(...)

Called when an object is spawned/created.

!!!info "onObjectSpawn(object)"
	* [<span class="tag obj"></span>](types.md) **object**: Object which was spawned.

``` Lua
function onObjectSpawn(object)
	print(object)
end
```

---

###onObjectStateChange(...)

Called after an object changes state.

!!!info "onObjectStateChange(object, old_state_guid)"
	* [<span class="tag obj"></span>](types.md) **object**: The new Object that spawned as a result of the state change.
	* [<span class="tag str"></span>](types.md) **old_state_guid**: The GUID of previous state/Object.

!!!example
	Print the current and previous Object state GUIDs.
	``` Lua
	function onObjectStateChange(object, old_state_guid)
		print("New state GUID: " .. object.guid)
		print("Previous state GUID: " .. old_state_guid)
	end
	```

---


###onObjectTriggerEffect(...)

Called whenever the trigger effect of an [AssetBundle](behavior/assetbundle.md) is activated.

!!!info "onObjectTriggerEffect(object, index)"
	* [<span class="tag obj"></span>](types.md) **object**: AssetBundle object which had its trigger activated.
	* [<span class="tag int"></span>](types.md) **index**: Index number for the trigger activated.

``` Lua
function onObjectTriggerEffect(object, index)
	print("Loop " .. index .. " activated.")
end
```

---

###onPlayerAction(...)

[<span class="ret boo"></span>](types.md) Called when a player attempts to perform an action.

Return `false` to prevent the action's default behavior.

!!!info "onPlayerAction(player, action, targets)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) that is attempting the action.
	* [Action](#onplayeraction-actions) **action**: Action that is being attempted.
	* [<span class="tag tab"></span>](types.md) **targets**: List of objects which are the target of the action being attempted.

#### Actions {: #onplayeraction-actions }

The `action` parameter will be provided as an [<span class="tag int"></span>](types.md) equal to a `Player.Action.*`
property e.g. `Player.Action.FlipOver`.

Please refer to the examples [below](#onplayeraction-flip-example), for a demonstration of how you can check which
action is being attempted.

[Player.Action](player/manager.md#actions) | Player is attempting to...
--- | ---
Copy | Copy (or commence cloning) the targets.
Cut | Cut (copy and delete) the targets.
Delete | Delete the targets.
FlipIncrementalLeft | Incrementally rotate the targets counter-clockwise around their flip axes, typically the scene's Z-axis.
FlipIncrementalRight | Incrementally rotate the targets clockwise around their flip axes, typically the scene's Z-axis.
FlipOver | Rotate the targets 180 degrees around their flip axes, typically the scene's Z-axis i.e. toggle the targets between face up and face down.
Group | Group the targets.
Paste | Paste (spawn) the targets.
PickUp | Pick up the targets.
Randomize | Randomize the targets.
RotateIncrementalLeft | Rotate the targets incrementally, typically counter-clockwise around the scene's Y-axis. Instead of being rotated exclusively around the Y-axis, dice will be rotated to the previous rotation value.
RotateIncrementalRight | Rotate the targets incrementally, typically clockwise around the scene's Y-axis. Instead of being rotated exclusively around the Y-axis, dice will be rotated to the next rotation value.
RotateOver | Rotate the targets 180 degrees around the scene's Y-axis.
Select | Add the targets to the player's selection.
Under | Move the targets underneath objects below them on table.

!!!example
	<p id="onplayeraction-flip-example">Prevent more than 2 objects being flipped over at a time.</p>
	```lua
	function onPlayerAction(player, action, targets)
		if action == Player.Action.FlipOver
			or action == Player.Action.FlipIncrementalLeft
			or action == Player.Action.FlipIncrementalRight
		then
			return #targets <= 2
		end

		return true
	end
	```

!!!example
	Only allow the black player (Game Master) to delete cards and decks.
	```lua
		function onPlayerAction(player, action, targets)
			if action == Player.Action.Delete and player.color ~= "Black" then
				for _, target in ipairs(targets) do
					if target.type ~= "Card" and target.type ~= "Deck" then
						target.destroy()
					end
				end

				return false
			end

			return true
		end
	```

---

###onPlayerChangeColor(...)

Called when a player changes color or selects it for the first time. It also returns `"Grey"` if they disconnect.

!!!info "onPlayerChangeColor(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.

``` Lua
function onPlayerChangeColor(color)
	print(color)
end
```

---

###onPlayerChangeTeam(...)

Called when a player changes team.

!!!info "onPlayerChangeTeam(player_color, team)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.
    * [<span class="tag str"></span>](types.md) **team**: Team to which the player has changed.  Options below.
        * "" (empty string, if changed to None)
        * Diamonds
        * Hearts
        * Jokers
        * Clubs
        * Spades

``` Lua
function onPlayerChangeTeam(player_color, team)
	print(player_color)
    print(team)
end
```

---

###onPlayerConnect(...)

Called when a [Player](player/instance.md) connects to a game.

!!!info "onPlayerConnect(player)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) that connected.

---


###onPlayerDisconnect(...)

Called when a [Player](player/instance.md) disconnects from a game.

!!!info "onPlayerDisconnect(player)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) that disconnected.

---


###onPlayerPing(...)

Called when a player [pings](https://kb.tabletopsimulator.com/game-tools/line-tool/#ping) a location.

!!!info "onPlayerPing(player, position)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) who performed the ping.
	* [<span class="tag vec"></span>](types.md) **position**: The location that was pinged.

!!!example
	When a player pings a location, print a message with the player's color and the coordinates pinged.
	```lua
	function onPlayerPing(player, position)
		print(player.color .. " pinged " .. position:string())
	end
	```

---


###onPlayerTurn(...)

Called at the start of a player's turn. [Turns](turns.md) must be enabled.

!!!info "onPlayerTurn(player, previous_player)"
	* [<span class="tag pla"></span>](types.md) **player**: [Player](player/instance.md) whose turn is starting.
	* [<span class="tag pla"></span>](types.md) **previous_player**: [Player](player/instance.md) whose turn just finished, or `nil` if this is the first turn.

!!!example
	When a new turn starts, print whose turn ended and whose turn it now is:
	```lua
	function onPlayerTurn(player, previous_player)
		if previous_player == nil then
			print(player.color .. " is going first. It's now their turn.")
		else
			print(previous_player.color .. "'s turn is over. It's now " .. player.color .. "'s turn.")
		end
	end
	```

---


###onSave()

Return a [<span class="tag str"></span>](types.md).

This event handler provides you with an opportunity to persist your script's state, such that when a save game is loaded
(or the user rewinds) the data you've persisted will be made available to [onLoad(...)](#onload).

A script's saved state is just a singular [<span class="tag str"></span>](types.md). The convention for storing complex
state is to create a Lua table, [JSON.encode(...)](json.md#encode) it, and return the JSON encoded string from this
function.

**Global Script**

This event is called whenever the user manually saves game, when an auto-save is created _and_ when a rewind checkpoint
is created, by default, that's every 10 seconds. Due to the frequency at which this event handler is called, it's
important that your function be fast.

**Object Script**

In addition to saves and rewind checkpoints, this event handler will also be called on an Object that requires its state
be saved mid-game e.g. when the script-owner Object enters a container.

!!!tip
	[JSON.encode(...)](json.md#encode) has limitations with regards to what data it can encode. It _cannot_ encode
	references to Objects. If you wish to encode a reference to an object, encode the Object's [GUID](object.md#guid)
    and in [onLoad(...)](#onload) obtain a new Object reference via
	[getObjectFromGUID(...)](base.md#getobjectfromguid).

!!!warning
	Pressing "Save & Play" (in either the in-game Scripting Editor or Atom) does _not_ trigger the save event.

    In this context "Save" is referring to saving your script only. Save & Play will in fact reload your game,
	_discarding any non-scripting changes_ made since the game was last (manually) loaded/saved.

!!!example
	Returns a JSON encoding of a game state consisting of nested tables, strings, numbers and object references
	(encoded as GUIDs). In this example, `some_object` is an [Object](object.md).
	```lua
	function onSave()
		local state = {
			questions = { -- nested table
				{
					question = "What day comes after Saturday?", -- string
					answer = "Sunday",
				},
				{
					question = "Unknown",
					answer = 42, -- number
				}
			},
			guids = {
				some_object = some_object.guid -- GUID (a string)
			}
		}
		return JSON.encode(state)
	end
	```
	Refer to [onLoad(...)](#onload) to see an example of this same save state structure being loaded. Subscribe to the
	[onSave/onLoad example mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2430471959) for a more
	functionally complete example.

---


###onScriptingButtonDown(...)

Called when a scripting button (numpad by default) is pressed. The index range that is returned is 1-10.

!!!info "onScriptingButtonDown(index, player_color)"
	* [<span class="tag int"></span>](types.md) **index**: Index number, representing which key was pressed.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.

``` Lua
function onScriptingButtonDown(index, color)
	print(index)
end
```

---

###onScriptingButtonUp(...)

Called when a scripting button (numpad by default) is released. The index range that is returned is 1-10.

!!!info "onScriptingButtonUp(index, player_color)"
	* [<span class="tag int"></span>](types.md) **index**: Index number, representing which key was released.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.

``` Lua
function onScriptingButtonUp(index, color)
	print(index)
end
```

---


###onUpdate()

Called **every frame**.

!!!danger
	Due to the frequency at which this function is called, any implementation must be very simple/fast, in order to avoid
	slowing down your game.

!!!example
	Print a message every 180 frames.
	``` Lua
	local frame_count = 0
	function onFixedUpdate()
	frame_count = frame_count + 1
		if frame_count >= 180 then
			print("180 frames passed.")
			frame_count = 0
		end
	end
	```

---


## Global Event Handler Details {: data-toc-sort }

###onZoneGroupSort(...)

[<span class="ret tab"></span>](types.md) Called when sorting is required for a group of objects being laid out by a
layout zone.

Return a table of objects (those provided in `group`) to override the layout zone's ordering algorithm. Return `nil` to
use the layout zone's default order.

!!!info "onZoneGroupSort(zone, group, reversed)"
	* [<span class="tag obj"></span>](types.md) **zone**: Layout zone which is laying out the group of objects.
	* [<span class="tag tab"></span>](types.md) **group**: List of objects that are being grouped together in the layout zone.
	* [<span class="tag boo"></span>](types.md) **reversed**: Whether the layout zone has been configured to sort in reverse.

!!!example
	Sort objects by [value](object.md#value). Please note that, by default, objects do not have a value. You'd have to
	assign your objects values first.
	```lua
	function onZoneGroupSort(zone, group, reversed)
		table.sort(group, function(a, b)
			return a.value < b.value
		end)
		return group
	end
	```

###tryObjectEnterContainer(...)

[<span class="ret boo"></span>](types.md) Called when an object attempts to enter a container.

Return `false` to prevent the object entering.

!!!info "tryObjectEnterContainer(container, object)"
	* [<span class="tag obj"></span>](types.md) **container**: The container the Object is trying to enter.
	* [<span class="tag obj"></span>](types.md) **object**: The Object entering the container.

!!!example
	```lua
	function tryObjectEnterContainer(container, object)
		print(object.getName()) -- Print entering object's name
		return true -- Allows object to enter.
	end
	```

---

###tryObjectRandomize(...)

[<span class="ret boo"></span>](types.md) Called when a player attempts to randomize an Object.

Return `false` to prevent the Object being randomized.

!!!info "tryObjectRandomize(object, player_color)"
	* [<span class="tag obj"></span>](types.md) **object**: The Object the player is trying to randomize.
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that is attempting the randomization.

!!!example
	Only allow the blue player to randomize objects.
	```lua
	function tryObjectRandomize(object, player_color)
		return player_color == "Blue"
	end
	```

---

###tryObjectRotate(...)

[<span class="ret boo"></span>](types.md) Called when a player attempts to rotate an object.

Return `false` to prevent the object being rotated.

!!!info "tryObjectRotate(object, spin, flip, player_color, old_spin, old_flip)"
	* [<span class="tag obj"></span>](types.md) **object**: The object the player is trying to rotate.
	* [<span class="tag flo"></span>](types.md) **spin**: The object's target spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **flip**: The object's target flip rotation in degrees within the interval \[0, 360).
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that is attempting the rotation.
	* [<span class="tag flo"></span>](types.md) **old_spin**: The object's current spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **old_flip**: The object's current flip rotation in degrees within the interval \[0, 360).

!!!example
	Only allow the blue player to rotate objects.
	```lua
	function tryObjectRotate(object, spin, flip, player_color, old_spin, old_flip)
		return player_color == "Blue"
	end
	```

---


## Object Event Handler Details

###onCollisionEnter(...)

Called when an Object starts colliding with the script-owner Object.

!!!info "onCollisionEnter(collision_info)"
	* [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object coming into contact with the script-owner Object.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the direction and magnitude of the collision.
``` Lua
-- Example Usage
function onCollisionEnter(info)
	print(tostring(info.collision_object) .. " collided with " .. tostring(self))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---


###onCollisionExit(...)

Called when an Object stops colliding with the script-owner Object.

!!!info "onCollisionExit(collision_info)"
	* [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object leaving contact with the script-owner Object.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the velocity of the object that has moved out of contact.

``` Lua
-- Example Usage
function onCollisionExit(info)
	print(tostring(info.collision_object) .. " stopped colliding with " .. tostring(self))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---


###onCollisionStay(...)

Called **every frame** that an Object is colliding with the script-owner Object.

!!!warning
	Due to the frequency at which this function may be called, any implementation must be very simple/fast, in order to
	avoid slowing down your game.

!!!info "onCollisionStay(collision_info)"
	* [<span class="tag tab"></span>](types.md) **collision_info**: A table containing data about the collision.
		* [<span class="tag obj"></span>](types.md) **collision_info.*collision_object***: Object coming into contact with the script-owner Object.
		* [<span class="tag tab"></span>](types.md) **collision_info.*contact_points***: Table/array full of contact points, where each 3D point is represented by a (number indexed) table, _not_ a [Vector](vector.md).
		* [<span class="tag tab"></span>](types.md) **collision_info.*relative_velocity***: Table (number indexed) representation of a 3D vector (but _not_ a [Vector](vector.md)) indicating the direction and magnitude of the collision.

``` Lua
-- Example Usage
function onCollisionStay(info)
	print(tostring(info.collision_object) .. " still colliding with " .. tostring(self))
end
```
``` Lua
-- Example collision_info table
{
	collision_object = objectReference,
	contact_points = {
		{5, 0, -2}
	},
	relative_velocity = {0, 20, 0}
}
```

---


###onDestroy()

Called when the script-owner Object is about to be destroyed.

The `self` (the script-owner Object) is valid in this callback, but won't be valid next frame (as the Object will be
destroyed by then).

This event fires immediately after [onObjectDestroy()](#onobjectdestroy).

!!!example
	Print a message when the script-owner Object is destroyed.
	``` Lua
	function onDestroy()
		print("This object was destroyed!")
	end
	```

---

###onDrop(...)

Called when the script-owner Object is dropped.

!!!info "onDrop(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player.

``` Lua
function onDrop(color)
	print(color)
end
```

---

###onFlick(...)

Called when a player [flicks](https://kb.tabletopsimulator.com/game-tools/flick-tool/) the script-owner Object.

!!!info "onFlick(player_color, impulse)"
* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who flicked the script-owner Object.
* [<span class="tag vec"></span>](types.md) **impulse**: The impulse applied to the script-owner Object.

!!!example
	Print the player color and magnitude of the flick:
	``` Lua
	function onFlick(player_color, impulse)
		print(player_color .. " flicked with impulse " .. impulse:magnitude())
	end
	```

---

###onGroupSort(...)

[<span class="ret tab"></span>](types.md) Called when sorting is required for a group of objects being laid out by the
script-owner layout zone.

Return a table of objects (those provided in `group`) to override the layout zone's ordering algorithm. Return `nil` to
use the layout zone's default order.

!!!info "onGroupSort(group, reversed)"
	* [<span class="tag tab"></span>](types.md) **group**: List of objects that are being grouped together in the layout zone.
	* [<span class="tag boo"></span>](types.md) **reversed**: Whether the layout zone has been configured to sort in reverse.

!!!example
	Sort objects by [value](object.md#value). Please note that, by default, objects do not have a value. You'd have to
	assign your objects values first.
	```lua
	function onGroupSort(group, reversed)
		table.sort(group, function(a, b)
			return a.value < b.value
		end)
		return group
	end
	```

---

###onHover(...)

Called when a player moves their pointer (cursor) over the script-owner Object.

!!!info "onHover(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who moved the pointer over the script-owner Object.

``` Lua
function onHover(player_color)
    print(player_color)
end
```

---

###onNumberTyped(...)

Called when a player types a number whilst hovering over the script-owner Object.

If you wish to prevent the default behavior (e.g. drawing a card, if the script-owner Object is a deck) then you may
return `true` to indicate you've handled the event yourself.

!!!info "onNumberTyped(player_color, number)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that typed the number.
	* [<span class="tag int"></span>](types.md) **number**: The number typed.

!!!example
	Print the player color and the number they typed:
	``` Lua
	function onNumberTyped(player_color, number)
		print(player_color .. " typed " .. number)
	end
	```

!!!example
	Prevent players drawing more than 2 cards at a time (from the script-owner Object):
	``` Lua
	function onNumberTyped(player_color, number)
		if self.type == 'Deck' and number > 2 then
			print("Sorry. You can only draw a maximum of 2 cards.")
			return true
		end
	end
	```

---

###onPageChange()

Called when the script-owner Custom PDF's page is changed.

!!!example
	Print the script-owner Object's name and what page it changed to:
	``` Lua
	function onPageChange()
		print(self.getName() .. " changed page to " .. self.Book.getPage())
	end
	```

---


###onPeek(...)

Called when a player [peeks](https://kb.tabletopsimulator.com/player-guides/advanced-controls/#peek) at the script-owner Object.

!!!info "onPeek(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that peeked.

!!!example
	Print the color of the player that peeked at the script-owner Object.
	``` Lua
	function onPeek(player_color)
		print(player_color .. " peeked.")
	end
	```


---


###onPickUp(...)

Called when a player picks up the script-owner Object.

!!!info "onPickUp(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player.

``` Lua
function onPickUp(color)
	print(color)
end
```

---

###onRandomize(...)

Called when the script-owner Object is randomized. Like when shuffling a deck or shaking dice.

!!!info "onRandomize(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player who triggered the function.


``` Lua
function onRandomize(color)
	print(self.getName() .. " was randomized by " .. color)
end
```

---

###onRotate(...)

Called when a player rotates script-owner Object.

!!!warning
	Only called in response to explicit player rotation actions. Will _not_ be called when physics/collisions cause the
	script-owner Object to rotate.

!!!info "onRotate(spin, flip, player_color, old_spin, old_flip)"
	* [<span class="tag flo"></span>](types.md) **spin**: The script-owner Object's target spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **flip**: The script-owner Object's target flip rotation in degrees within the interval \[0, 360).
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that performed the rotation.
	* [<span class="tag flo"></span>](types.md) **old_spin**: The script-owner Object's previous spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **old_flip**: The script-owner Object's previous flip rotation in degrees within the interval \[0, 360).

!!!example
	When the script-owner Object is rotated, print which player was responsible and what rotation was performed.
	```lua
	function onRotate(spin, flip, player_color, old_spin, old_flip)
		if spin ~= old_spin then
			print(player_color .. " spun " .. tostring(self) .. " from " .. old_spin .. " degrees to " .. spin .. " degrees")
		end

		if flip ~= old_flip then
			print(player_color .. " flipped " .. tostring(self) .. " from " .. old_flip .. " degrees to " .. flip .. " degrees")
		end
	end
	```

---

###onSearchEnd(...)

Called when a player first searches the script-owner Object.

!!!info "onSearchEnd([<span class="tag str"></span>](types.md) player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player.

---

###onSearchStart(...)

Called when a player finishes searching the script-owner Object.

!!!info "onSearchStart([<span class="tag str"></span>](types.md) player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the Player.

---

###onStateChange(...)

Called when the script-owner Object spawned as a result of an Object state change.

!!!info "onStateChange(old_state_guid)"
	* [<span class="tag str"></span>](types.md) **old_state_guid**: The GUID of previous state/Object.

!!!example
	Print the current and previous Object state GUIDs.
	``` Lua
	function onStateChange(old_state_guid)
		print("New state GUID: " .. self.guid)
		print("Previous state GUID: " .. old_state_guid)
	end
	```

---

###tryObjectEnter(...)

Called when another object attempts to enter the script-owner Object (container).

Return `false` to prevent the object entering.

!!!info "tryObjectEnter(object)"
	* [<span class="tag obj"></span>](types.md) **object**: The object that has tried to enter the script-owner Object.

!!!example
	Print the name of the object entering the script-owner container.
	```lua
	function tryObjectEnter(object)
		print(object.getName())
		return true -- Allows the object to enter.
	end
	```

---

###tryRandomize(...)

Called when a player attempts to randomize the script-owner Object.

Return `false` to prevent the randomization taking place.

!!!info "tryRandomize(player_color)"
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that is attempting the randomization.

!!!example
	Only allow the blue player to randomize the script-owner Object.
	```lua
	function tryRandomize(player_color)
		return player_color == "Blue"
	end
	```

---

###tryRotate(...)

Called when a player attempts to rotate the script-owner Object.

Return `false` to prevent the rotation taking place.

!!!info "tryRotate(spin, flip, player_color, old_spin, old_flip)"
	* [<span class="tag flo"></span>](types.md) **spin**: The script-owner Object's target spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **flip**: The script-owner Object's target flip rotation in degrees within the interval \[0, 360).
	* [<span class="tag str"></span>](types.md) **player_color**: [Player Color](player/colors.md) of the player that is attempting the rotation.
	* [<span class="tag flo"></span>](types.md) **old_spin**: The script-owner Object's current spin (around Y-axis) rotation in degrees within the interval \[0, 360).
	* [<span class="tag flo"></span>](types.md) **old_flip**: The script-owner Object's current flip rotation in degrees within the interval \[0, 360).

!!!example
	Only allow the blue player to rotate the script-owner Object.
	```lua
	function tryRotate(spin, flip, player_color, old_spin, old_flip)
		return player_color == "Blue"
	end
	```

---
