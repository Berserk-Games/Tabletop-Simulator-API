The Object class represents any entity within tabletop simulator. Once you have a reference to an object in youre script you can call functions on it directly. Example: `obj.getPosition(...)`. You can get a reference to an object multiple ways;

* Using the `self` property if your script is on an Object and referring to that Object.
* Using [`getObjectFromGUID(...)`](base#getobjectfromguid) with the object's GUID (found by right clicking it with the pointer).
* Getting it as a return from another function, like with [`spawnObject(...)`](base#spawnobject).

##Member Variable Summary

###Member Variables
These are variables that objects share. They allow for direct access to an Object's property information without a helping function. Some are read-only.

Read Example = `isResting = self.resting` Write Example = `self.resting = true`

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="angular_drag"></a>angular_drag | Angular drag. [Unity rigidbody property](https://docs.unity3d.com/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](intro#types) <a class="anchor" id="angular_drag"></a>
<a class="anchor" id="auto_raise"></a>auto_raise | If an object should be lifted above other objects to avoid collision when held by a player. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="bounciness"></a>bounciness | Bounciness, value of 0-1. [Unity physics material](https://docs.unity3d.com/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](intro#types)
<a class="anchor" id="drag"></a>drag | Drag. [Unity rigidbody property](https://docs.unity3d.com/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](intro#types)
<a class="anchor" id="dynamic_friction"></a>dynamic_friction | Dynamic friction, value of 0-1. [Unity physics material](https://docs.unity3d.com/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](intro#types)
<a class="anchor" id="grid_projection"></a>grid_projection | If grid lines can appear on the Object if visible grids are turned on. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="guid"></a>guid | The 6 character unique Object identifier within Tabletop Simulator. | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="held_by_color"></a>held_by_color | The Color of the Player that is holding the object. | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="interactable"></a>interactable | If an object can be interacted with by Players. Other object will still be able to interact with it. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="mass"></a>mass | Mass. [Unity rigidbody property](https://docs.unity3d.com/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](intro#types)
<a class="anchor" id="name"></a>name | The Object's name. Read only, use `setName("")` to write to it. | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="resting"></a>resting | If an Object is at rest. [Unity rigidbody property](https://docs.unity3d.com/412/Documentation/Components/RigidbodySleeping.html). | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="script_code"></a>script_code | The Lua Script on the Object. | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="script_state"></a>script_state | The saved data on the object. See [onSave()](event#onsave). | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="static_friction"></a>static_friction | Static friction, value of 0-1. [Unity physics material](https://docs.unity3d.com/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](intro#types)
<a class="anchor" id="sticky"></a>sticky | If other Objects on top of this one are also picked up when this Object is. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="tag"></a>tag | This object's type. Read only. | [<span class="tag str"></span>](intro#types)
<a class="anchor" id="tooltip"></a>tooltip | If the tooltip opens when a pointer hovers over the object. Tooltips display name and description. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="use_gravity"></a>use_gravity | If gravity affects this object. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="use_grid"></a>use_grid | If snapping to grid is enabled or not. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="use_hands"></a>use_hands | If this object can be held in a hand zone. | [<span class="tag boo"></span>](intro#types)
<a class="anchor" id="use_snap_points"></a>use_snap_points | If snap points are used or ignored. | [<span class="tag boo"></span>](intro#types)

These member variables are classes of their own, and have their own member variables. Each one is for a special type of Object.

Variable Name | Description
-- | --
<a class="anchor" id="assetbundle"></a>AssetBundle | An [AssetBundle](assetbundle), which is a type of custom object made in Unity.
<a class="anchor" id="clock"></a>Clock | A [Clock](clock), which is the in-game digital clock.
<a class="anchor" id="counter"></a>Counter | A [Counter](counter), which is the in-game digital counter.
<a class="anchor" id="rpgfigurine"></a>RPGFigurine | An [RPGFigurine](rpgfigurine), which is an in-game animated figurine.
<a class="anchor" id="texttool"></a>TextTool | A [TextTool](texttool), which is an in-game text display system.

---








##Function Summary

###Transform Functions
These functions handle the physical attributes of an Object: Position, Rotation, Scale, Bounds, Velocity. In other words, moving objects around as well as getting information on how they are moving.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addForce([<span class="tag vec"></span>](intro#vector)&nbsp;vector, [<span class="tag int"></span>](intro#types)&nbsp;force_type) | Adds force to an object in a directional Vector. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#addforce)
addTorque([<span class="tag vec"></span>](intro#vector)&nbsp;vector, [<span class="tag int"></span>](intro#types)&nbsp;force_type) | Adds torque to an object in a rotational Vector. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#addtorque)
<a class="anchor" id="getangularvelocity"></a>getAngularVelocity() | Returns a Vector of the current angular velocity. | [<span class="ret vec"></span>](intro#vector)
getBounds() | Returns a Vector describing the size of an object in Global terms. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#getbounds)
getBoundsNormalized() | Returns a Vector describing the size of an object in Global terms, as if it was rotated to {0,0,0}. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#getboundsnormalized)
<a class="anchor" id="getposition"></a>getPosition() | Returns a Vector of the current world position. | [<span class="ret vec"></span>](intro#vector)
<a class="anchor" id="getrotation"></a>getRotation() | Returns a Vector of the current rotation. | [<span class="ret vec"></span>](intro#vector)
getScale() | Returns a Vector of the current scale. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#getscale)
getTransformForward() | Returns a Vector of the forward direction of this object. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#gettransformforward)
getTransformRight() | Returns a Vector of the right direction of this object. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#gettransformright)
getTransformUp() | Returns a Vector of the up direction of this object. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#gettransformup)
<a class="anchor" id="getvelocity"></a>getVelocity() | Returns a Vector of the current velocity. | [<span class="ret vec"></span>](intro#vector) |
<a class="anchor" id="issmoothmoving"></a>isSmoothMoving() | Indicates if an object is traveling as part of a Smooth move. Smooth moving is performed by setPositionSmooth and setRotationSmooth. | [<span class="ret boo"></span>](intro#types) |
positionToLocal([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Returns a Vector after converting a world Vector to a local Vector. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#positiontolocal)
positionToWorld([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Returns a Vector after converting a local Vector to a world Vector. | [<span class="ret vec"></span>](intro#vector) | [<span class="i"></span>](#positiontoworld)
rotate([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Rotates Object smoothly in the direction of the given Vector. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#rotate)
scale([<span class="tag vec"></span>](intro#vector)&nbsp;vector or [<span class="tag flo"></span>](intro#types)) | Scales Object by a multiple. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#scale)
<a class="anchor" id="setangularvelocity"></a>setAngularVelocity([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Sets a Vector as the current angular velocity. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="setposition"></a>setPosition([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Instantly moves an Object to the given Vector. | [<span class="ret boo"></span>](intro#types) |
setPositionSmooth([<span class="tag vec"></span>](intro#vector)&nbsp;vector, [<span class="tag boo"></span>](intro#types)&nbsp;collide, [<span class="tag boo"></span>](intro#types)&nbsp;fast) | Moves the Object smoothly to the given Vector. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setpositionsmooth)
<a class="anchor" id="setrotation"></a>setRotation([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Instantly rotates an Object to the given Vector. | [<span class="ret boo"></span>](intro#types) |
setRotationSmooth([<span class="tag vec"></span>](intro#vector)&nbsp;vector, [<span class="tag boo"></span>](intro#types)&nbsp;collide, [<span class="tag boo"></span>](intro#types)&nbsp;fast) | Rotates the Object smoothly to the given Vector. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setrotationsmooth)
<a class="anchor" id="setscale"></a>setScale([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Sets a Vector as the current scale. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="setvelocity"></a>setVelocity([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Sets a Vector as the current velocity. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="translate"></a>translate([<span class="tag vec"></span>](intro#vector)&nbsp;vector) | Smoothly moves Object by the given Vector offset. | [<span class="ret boo"></span>](intro#types) |



###UI Functions
These functions allow for the creation/editing/removal of functional buttons and text inputs which themselves trigger code within your scripts.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="clearbuttons"></a>clearButtons() | Removes all scripted buttons. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="clearinputs"></a>clearInputs() | Removes all scripted inputs. | [<span class="ret boo"></span>](intro#types) |
createButton([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Creates a scripted button attached to the Object. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#createbutton)
createInput([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Creates a scripted input attached to the Object. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#createinput)
editButton([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Modify an existing button. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#editbutton)
editInput([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Modify an existing input. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#editinput)
getButtons() | Returns a Table of all buttons on this Object. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getbuttons)
getInputs() | Returns a Table of all inputs on this Object. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getinputs)
removeButton([<span class="tag int"></span>](intro#types)&nbsp;index) | Removes a specific button. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#removebutton)
removeInput([<span class="tag int"></span>](intro#types)&nbsp;index) | Removes a specific button. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#removeinput)



###Get Functions
These functions obtain information from an object.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="getcolortint"></a>getColorTint() | Color tint. | [<span class="ret col"></span>](intro#color) |
getCustomObject() | Returns a Table with the Custom Object information of a Custom Object. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getcustomobject)
<a class="anchor" id="getdescription"></a>getDescription() | Description, also shows as part of Object's tooltip. | [<span class="ret str"></span>](intro#types)
<a class="anchor" id="getguid"></a>getGUID() | String of the Object's unique identifier. | [<span class="ret str"></span>](intro#types) |
<a class="anchor" id="getlock"></a>getLock() | If the Object is locked. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="getluascript"></a>getLuaScript() | Get a Lua script as a string. | [<span class="ret str"></span>](intro#types) |
<a class="anchor" id="getname"></a>getName() | Name, also shows as part of Object's tooltip. | [<span class="ret str"></span>](intro#types) |
getObjects() | Returns a Table of Objects in the script zone/bag/deck. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getobjects)
<a class="anchor" id="getquantity"></a>getQuantity() | How many objects are in the stack. Returns -1 if the Object is not a stack. | [<span class="ret int"></span>](intro#types) |
getRotationValues() | Returns a Table of rotation values. Rotation values are used to give value to different rotations (like dice). | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getrotationvalues)
<a class="anchor" id="getstateid"></a>getStateId() | Current [state](http://berserk-games.com/knowledgebase/creating-states/) ID (index) an object is in. Returns -1 if there are no other states. State ids (indexes) start at 1. | [<span class="ret int"></span>](intro#types) |
getStates() | Returns a Table of information on the [states](http://berserk-games.com/knowledgebase/creating-states/) of an Object. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getstates)
<a class="anchor" id="gettable"></a>getTable([<span class="tag str"></span>](intro#types)&nbsp;func_name) | Data value of a variable in another Object's script. Can only return a table. | [<span class="ret tab"></span>](intro#types) |
getValue() | Object value. What the value represents depends on what type of Object this function is used on. | [<span class="ret int"></span>](intro#types) | [<span class="i"></span>](#getvalue)
<a class="anchor" id="getvar"></a>getVar([<span class="tag str"></span>](intro#types)&nbsp;func_name) | Data value of a variable in another Object's script. Cannot return a table. | [<span class="ret var"></span>](intro#types) |



###Set Functions
These functions apply action to an object. They take some property in order to work.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="setcolortint"></a>setColorTint([<span class="tag col"></span>](intro#color)&nbsp;Color) | Sets the Color tint. | [<span class="ret boo"></span>](intro#types) |
setCustomObject([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Sets a custom Object's properties. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setcustomobject)
<a class="anchor" id="setdescription"></a>setDescription([<span class="tag str"></span>](intro#types)&nbsp;description) | Sets a description for an Object. Shows in tooltip after delay. | [<span class="ret boo"></span>](intro#types)
<a class="anchor" id="setlock"></a>setLock([<span class="tag boo"></span>](intro#types)&nbsp;lock) | Sets if an object is locked in place. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="setluascript"></a>setLuaScript([<span class="tag str"></span>](intro#types)&nbsp;script) | Input a string as an Object's Lua script. Generally only used after spawning a new Object. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="setname"></a>setName([<span class="tag str"></span>](intro#types)&nbsp;name) | Sets a name for an Object. Shows in tooltip. | [<span class="ret boo"></span>](intro#types)
setRotationValues([<span class="tag tab"></span>](intro#types)&nbsp;rotation_values) | Sets rotation values of an object. Rotation values are used to give value to different rotations (like dice). | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setrotationvalues)
<a class="anchor" id="setstate"></a>setState([<span class="tag int"></span>](intro#types)&nbsp;state_id) | Sets [state](http://berserk-games.com/knowledgebase/creating-states/) of an Object. State ids (indexes) start at 1. | [<span class="ret obj"></span>](intro#types) |
<a class="anchor" id="settable"></a>setTable([<span class="tag str"></span>](intro#types)&nbsp;func_name, [<span class="tag tab"></span>](intro#types)&nbsp;data) | Creates/updates a variable in another Object's script. Only used for tables. | [<span class="ret boo"></span>](intro#types) |
setValue([<span class="tag var"></span>](intro#types)&nbsp;value) | Sets an Int as the value. What the value represents depends on what type of Object it is. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setvalue)
<a class="anchor" id="setvar"></a>setVar([<span class="tag str"></span>](intro#types)&nbsp;func_name, [<span class="tag var"></span>](intro#types)&nbsp;data) | Creates/updates a variable in another Object's script. Cannot set a table. | [<span class="ret boo"></span>](intro#types) |



###Action Function
These functions perform general actions on objects and do not require any input parameters.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
call([<span class="tag str"></span>](intro#types)&nbsp;func_name, [<span class="tag tab"></span>](intro#types)&nbsp;func_params) | Used to call a Lua function on this Object. | [<span class="ret var"></span>](intro#types) | [<span class="i"></span>](#call)
<a class="anchor" id="flip"></a>flip() | Flip Object over. | [<span class="ret boo"></span>](intro#types) |
clone([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Copy/Paste this Object, returning a reference to the new Object. | [<span class="ret obj"></span>](intro#types) | [<span class="i"></span>](#clone)
<a class="anchor" id="cut"></a>cut() | Cuts (splits in half) a deck or stack Object. | [<span class="ret boo"></span>](intro#types) |
deal([<span class="tag int"></span>](intro#types)&nbsp;number, [<span class="tag str"></span>](intro#types)&nbsp;player_color, [<span class="tag int"></span>](intro#types)&nbsp;index) | Deals Objects. Will deal from decks/bags/stacks/individual items. | [<span class="ret obj"></span>](intro#types) | [<span class="i"></span>](#deal)
dealToColorWithOffset([<span class="tag vec"></span>](intro#vector)&nbsp;offset, [<span class="tag boo"></span>](intro#types)&nbsp;flip, [<span class="tag str"></span>](intro#types)&nbsp;player_color) | Deals from a deck to a position relative to the hand zone. | [<span class="ret obj"></span>](intro#types) | [<span class="i"></span>](#dealtocolorwithoffset)
<a class="anchor" id="destruct"></a>destruct() | Destroys Object. Allows for `self.destruct()`. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="highlighton"></a>highlightOn([<span class="tag col"></span>](intro#color)&nbsp;color, [<span class="tag flo"></span>](intro#types)&nbsp;duration) | Creates a highlight around an Object. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="highlightoff"></a>highlightOff([<span class="tag col"></span>](intro#color)&nbsp;color) | Removes a highlight from around an Object. | [<span class="ret boo"></span>](intro#types) |
putObject([<span class="tag obj"></span>](intro#types)&nbsp;put_object) | Places an object into a container (chip stacks/bags/decks). | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#putobject)
<a class="anchor" id="randomize"></a>randomize() | Shuffles deck/bag, rolls dice/coin, lifts other objects into the air. Same as pressing `R` by default. | [<span class="ret boo"></span>](intro#types) |
reload() | Returns Object reference of itself after it respawns itself. | [<span class="ret obj"></span>](intro#types) | [<span class="i"></span>](#reload)
<a class="anchor" id="reset"></a>reset() | Resets this Object. Resetting a Deck brings all the Cards back into it. Resetting a Bag clears its contents (works for both Loot and Infinite Bags). | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="roll"></a>roll() | Rolls dice/coins. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="shuffle"></a>shuffle() | Shuffles/shakes up contents of a deck or bag. | [<span class="ret boo"></span>](intro#types) |
<a class="anchor" id="shufflestates"></a>shuffleStates() | Returns an Object reference to a new [state](http://berserk-games.com/knowledgebase/creating-states/) after randomly selecting and changing to one. | [<span class="ret obj"></span>](intro#types) |
takeObject([<span class="tag tab"></span>](intro#types)&nbsp;parameters) | Returns an Object reference of Object taken from a container (bag/deck/chip stack) and placed into the world. | [<span class="ret obj"></span>](intro#types) | [<span class="i"></span>](#takeobject)

---








##Function Details

###Transform Function Details

####addForce(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Adds force to an object in a directional Vector.

!!!info "addForce(vector, force_type)"
	* [<span class="tag tab"></span>](intro#types) **Vector**: A Vector of the direction and magnitude of force.
    * [<span class="tag int"></span>](intro#types) **force_type**: An Int representing the force type to apply. Options below.
		* {>>Optional, defaults to 3.<<}
        * **1**: Continuous force, uses mass. *(Force)*
        * **2**: Continuous acceleration, ignores mass. *(Acceleration)*
		* **3**: Instant force impulse, uses mass. *(Impulse)*
		* **4**: Instant velocity change, ignores mass. *(Velocity Change)*

---


####addTorque(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Adds torque to an object in a rotational Vector.

!!!info "addTorque(vector, force_type)"
	* [<span class="tag tab"></span>](intro#types) **Vector**: A Vector of the direction and magnitude of rotational force.
	* [<span class="tag int"></span>](intro#types) **Force Type**: An Int representing the force type to apply. Options below.
		* {>>Optional, defaults to 3.<<}
        * **1**: Continuous force, uses mass. *(Force)*
        * **2**: Continuous acceleration, ignores mass. *(Acceleration)*
		* **3**: Instant force impulse, uses mass. *(Impulse)*
		* **4**: Instant velocity change, ignores mass. *(Velocity Change)*

---



####getBounds()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of Vector information describing the size of an object in Global terms. [Bounds](https://docs.unity3d.com/ScriptReference/Bounds.html) are part of Unity, and represent an imaginary square box that can be drawn around an object. Unlike scale, it can help indicate the size of an object in in-game units, not just relative model size.

!!!info "Return Table"
	* [<span class="tag tab"></span>](intro#types) **center**: The Vector of the center of the bounding box.
	* [<span class="tag tab"></span>](intro#types) **size**: The Vector of the size of the bounding box.
	* [<span class="tag tab"></span>](intro#types) **offset**: The Vector of the offset of the center of the bounding box from the middle of the Object model.

``` Lua
-- Example returned Table
{
	center = {x=0, y=3, z=0, 0, 3, 0},
	size = {x=5, y=5, z=5}, 5, 5, 5},
	offset = {x=0, y=-1, z=0, 0, -1, 0}
}
```

---


####getBoundsNormalized()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of Vector information describing the size of an object in Global terms, as if it was rotated to {0,0,0}. [Bounds](https://docs.unity3d.com/ScriptReference/Bounds.html) are part of Unity, and represent an imaginary square box that can be drawn around an object. Unlike scale, it can help indicate the size of an object in in-game units, not just relative model size.

!!!info "Return Table"
	* [<span class="tag tab"></span>](intro#types) **center**: The Vector of the center of the bounding box.
	* [<span class="tag tab"></span>](intro#types) **size**: The Vector of the size of the bounding box.
	* [<span class="tag tab"></span>](intro#types) **offset**: The Vector of the offset of the center of the bounding box from the middle of the Object model.

``` Lua
-- Example returned Table
{
	center = {x=0, y=3, z=0, 0, 3, 0},
	size = {x=5, y=5, z=5}, 5, 5, 5},
	offset = {x=0, y=-1, z=0, 0, -1, 0}
}
```

---


####getScale()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector of the current scale. Scale is not an absolute measurement, it is a multiple of the Object's default model size. So {x=2, y=2, z=2} would be a model twice its default size, not 2 units large.

---


####getTransformForward()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector of the forward direction of this Object. The direction is relative to how the object is facing.

``` Lua
-- Example of moving forward 5 units
function onLoad()
    distance = 5
    pos_target = self.getTransformForward()
    pos_current = self.getPosition()
    pos = {
        x = pos_current.x + pos_target.x * distance,
        y = pos_current.y + pos_target.y * distance,
        z = pos_current.z + pos_target.z * distance,
    }
    self.setPositionSmooth(pos)
end
```

---


####getTransformRight()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector of the forward direction of this object. The direction is relative to how the object is facing.

``` Lua
-- Example of moving right 5 units
function onLoad()
    distance = 5
    pos_target = self.getTransformRight()
    pos_current = self.getPosition()
    pos = {
        x = pos_current.x + pos_target.x * distance,
        y = pos_current.y + pos_target.y * distance,
        z = pos_current.z + pos_target.z * distance,
    }
    self.setPositionSmooth(pos)
end
```

---


####getTransformUp()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector of the up direction of this Object. The direction is relative to how the object is facing.

``` Lua
-- Example of moving up 5 units
function onLoad()
    distance = 5
    pos_target = self.getTransformUp()
    pos_current = self.getPosition()
    pos = {
        x = pos_current.x + pos_target.x * distance,
        y = pos_current.y + pos_target.y * distance,
        z = pos_current.z + pos_target.z * distance,
    }
    self.setPositionSmooth(pos)
end
```

---


####positionToLocal(...)

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector after converting a world vector to a local Vector. A world Vector is a positional Vector using the world's coordinate system. A Local Vector is a positional Vector that is relative to the position of the given object.

!!!tip "Object Scale"
	This function takes the Object's scale into account, as the Object is the key relative point.
	
!!!info "positionToLocal(vector)"
	* [<span class="tag vec"></span>](intro#types) **vector**: The world position to convert into a local position.

---


####positionToWorld(...)

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Vector after converting a local Vector to a world Vector. A world Vector is a positional Vector using the world's coordinate system. A Local Vector is a positional Vector that is relative to the position of the given object.

!!!tip "Object Scale"
	This function takes the Object's scale into account, as the Object is the key relative point.
	
!!!info "positionToLocal(vector)"
	* [<span class="tag vec"></span>](intro#types) **vector**: The local position to convert into a world position.

---


####rotate(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Rotates Object smoothly in the direction of the given Vector. This does not set the Object to face a specific rotation, it rotates the Object around by the number of degrees given for x/y/z.

!!!info "rotate(vector)"
	* [<span class="tag vec"></span>](intro#types) **vector**: The amount of x/y/z to rotate by.

``` Lua
--Rotates object 90 degrees around its Y axis
self.rotate({x=0, y=90, z=0})
```

---


####scale(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Scales Object by a multiple. This does not set the Object to a specific scale, it scales the Object by the given multiple.

!!!info "scale(scale)"
	* [<span class="tag vec"></span>](intro#vector) **scale**: Multiplier for scale.
		* {>>{x=1, y=1, z=1} would not change the scale.<<}
!!!info "scale(scale)"
	* [<span class="tag flo"></span>](intro#types) **scale**: Multiplier for scale which is applied to the X/Y/Z.
		* {>>1 would not change the scale.<<}

``` Lua
-- Both examples work to scale an object to be twice its current scale
self.scale({x=2, y=2, z=2})
self.scale(2)
```

---


####setPositionSmooth(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Moves the Object smoothly to the given Vector.

!!!info "setPositionSmooth(vector, collide, fast)"
	* [<span class="tag tab"></span>](intro#types) **Vector**: A positional Vector.
	* [<span class="tag boo"></span>](intro#types) **collide**: If the Object will collide with other Objects while moving.
	* [<span class="tag boo"></span>](intro#types) **fast**: If the Object is moved quickly.

---


####setRotationSmooth(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Rotates the Object smoothly to the given Vector.

!!!info "setRotationSmooth(vector, collide, fast)"
	* [<span class="tag tab"></span>](intro#types) **Vector**: A rotational Vector.
	* [<span class="tag boo"></span>](intro#types) **collide**: If the Object will collide with other Objects while rotating.
	* [<span class="tag boo"></span>](intro#types) **fast**: If the Object is rotated quickly.

---


###UI Function Details

####createButton(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Creates a scripted button attached to the Object. Scripted buttons are buttons that can be clicked while in-game that trigger a function in a script.

???tip "Button Tips"
	* Buttons can not be clicked from their back side.
	* Buttons can not be clicked if there is another object between the pointer and the button. This does not include the Object the button is attached to.
	* Buttons are placed relative to the Object they are attached to.
	* The maximum font size is capped at 1000.
	* The minimum width/height is 60. Any lower number (besides 0) will appear to be 60. This prevents visual glitches involving the corner rounding.
	* A button width/height of 0 will cause the button not to be drawn, but its label will be. This can be a way to attach text to an Object.
	* You cannot assign an index to a button. It is given one automatically.

!!!info "createButton(parameters)"
	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table containing the information used to spawn the button.
		* [<span class="tag str"></span>](intro#types) **parameters.click_function**: A String of the function's name that will be run when button is clicked.
		* [<span class="tag str"></span>](intro#types) **parameters.function_owner**: The Object which contains the click_function function.
			* {>>Optional, Defaults to Global.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.label**: Text that appears on the button.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: Where the button appears, relative to the Object's center.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.rotation**: How the button is rotated, relative to the Object's rotation.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.scale**: Scale of the button, relative to the Object's scale.
			* {>>Optional, defaults to {x=1, y=1, z=1}.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.width**: How wide the button will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.height**: How tall the button will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.font_size**: Size the label font will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag col"></span>](intro#color) **parameters.color**: A Color for the clickable button.
			* {>>Optional, defaults to {r=1, g=1, b=1}.<<}
		* [<span class="tag col"></span>](intro#color) **parameters.font_color**: A Color for the label text.
			* {>>Optional, defaults to {r=0, g=0, b=0}.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.tooltip**: Popup of text, similar to how an Object's name is displayed on mouseover.
			* {>>Optional, defaults to an empty string.<<}

!!!info "click_function(obj, player_clicker_color)"
	*The click function which is activated by clicking this button has its own parameters it is passed automatically.*

	* [<span class="tag obj"></span>](intro#types) **obj**: The Object the button is attached to.
	* [<span class="tag str"></span>](intro#types) **player_clicker_color**: [Player Color](player-color) of the player that pressed the button.

``` Lua
function onLoad()
	params = {
		click_function = "click_func",
		function_owner = self,
		label          = "Test",
		position       = {0, 1, 0},
		rotation       = {0, 180, 0},
		width          = 800,
		height         = 400,
		font_size      = 340,
		color          = {0.5, 0.5, 0.5},
		font_color     = {1, 1, 1},
		tooltip        = "This text appears on mouseover.",
	}
	self.createButton(params)
end

function click_func(obj, color)
	print(obj)
	print(color)
end
```

!!!bug
	Button scale currently distorts button height and width if the button is rotated at anything besides `{0,0,0}`.

---


####createInput(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Creates a scripted input attached to the Object. Scripted inputs are boxes you can click inside of in-game to input/edit text. Every letter typed triggers the function. The bool that is returned as part of the input_function allows you to determine when a player has finished editing the input.

???tip "Input Tips"
	* Inputs can not be clicked from their back side.
	* Inputs can not be clicked if there is another object between the pointer and the inputs. This does not include the Object the input is attached to.
	* Inputs are placed relative to the Object they are attached to.
	* The maximum font size is capped at 1000.
	* The minimum width/height is 60. Any lower number (besides 0) will appear to be 60. This prevents visual glitches involving the corner rounding.
	* Font that does not fit in the input window's width/height does NOT display. To know how much height you need for each line, the formula is `(font_size * # of lines) + 23`. In other words, multiply how many lines of text you want to display by your font_size and add 23. That is your height value.
	* You cannot assign an index to an input. It is given one automatically.

!!!info "createInput(parameters)"
	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table containing the information used to spawn the input.
		* [<span class="tag str"></span>](intro#types) **parameters.input_function**: A String of the function's name that will be run when a key is used or when it is deselected.
		* [<span class="tag obj"></span>](intro#types) **parameters.function_owner**: The Object which contains the input_function function.
			* {>>Optional, Defaults to Global.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.label**: Text that appears as greyed out text when there is no value in the input.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: Where the input appears, relative to the Object's center.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.rotation**: How the input is rotated, relative to the Object's rotation.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.scale**: Scale of the input, relative to the Object's scale.
			* {>>Optional, defaults to {x=1, y=1, z=1}.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.width**: How wide the input will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.height**: How tall the input will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](intro#types) **parameters.font_size**: Size the label/value font will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag col"></span>](intro#color) **parameters.color**: A Color for the input's background.
			* {>>Optional, defaults to {r=1, g=1, b=1}.<<}
		* [<span class="tag col"></span>](intro#color) **parameters.font_color**: A Color for the value text.
			* {>>Optional, defaults to {r=0, g=0, b=0}.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.tooltip**: A popup of text, similar to how an Object's name is displayed on mouseover.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag int"></span>](intro#types) **parameters.alignment**: How text is aligned in the input box.
			* {>>Optional, defaults to 1.<<}
			* **1**: Automatic
			* **2**: Left
			* **3**: Center
			* **4**: Right
			* **5**: Justified
		* [<span class="tag str"></span>](intro#types) **parameters.value**: Text entered into the input.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag int"></span>](intro#types) **parameters.validation**: What characters can be input into the input value field.
			* {>>Optional, defaults to 1.<<}
			* **1**: None
			* **2**: Integer
			* **3**: Float
			* **4**: Alphanumeric
			* **5**: Username
			* **6**: Name
		* [<span class="tag int"></span>](intro#types) **parameters.tab**: How the pressing of "tab" is handled when inputting.
			* {>>Optional, defaults to 1.<<}
			* **1**: None
			* **2**: Select Next Input
			* **3**: Indent

!!!info "input_function(obj, player_clicker_color, input_value, selected)"
	*The click function which is activated by editing the text in this input has its own parameters it is passed automatically.*

	* [<span class="tag obj"></span>](intro#types) **obj**: The Object the input is attached to.
	* [<span class="tag str"></span>](intro#types) **player_clicker_color**: [Player Color](player-color) of the player that has selected/edited the input.
	* [<span class="tag str"></span>](intro#types) **input_value**: Text currently in the input.
	* [<span class="tag boo"></span>](intro#types) **selected**: If the value box is still being edited or not.

``` Lua
function onLoad()
	self.createInput({
	    input_function = "input_func",
	    function_owner = self,
	    label          = "Gold",
	    alignment      = 4,
	    position       = {x=0, y=1, z=0},
	    width          = 800,
	    height         = 300,
	    font_size      = 323,
	    validation     = 2,
	})
end

function input_func(obj, color, input, stillEditing)
	print(input)
	if not stillEditing then
		print("Finished editing.")
	end
end
```

---


####editButton(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Modify an existing button. The only parameter that is required is the index. The rest are optional, and not using them will cause the edited button's element to remain. Indexes start at 0. The first button on any given Object has an index of 0, the next button on it has an index of 1, etc. Each Object has its own indexes.

!!!info "editButton(parameters)"
	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table containing the information used to spawn the button.
		* [<span class="tag int"></span>](intro#types) **parameters.index**: Index of the button you want to edit.
		* [<span class="tag str"></span>](intro#types) **parameters.click_function**: Function's name that will be run when button is clicked.
		* [<span class="tag obj"></span>](intro#types) **parameters.function_owner**: The Object which contains the click_function function.
		* [<span class="tag str"></span>](intro#types) **parameters.label**: Text that appears on the button.
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: Where the button appears, relative to the Object's center.
		* [<span class="tag vec"></span>](intro#vector) **parameters.rotation**: How the button is rotated, relative to the Object's rotation.
		* [<span class="tag vec"></span>](intro#vector) **parameters.scale**: Scale of the button, relative to the Object's scale.
		* [<span class="tag flo"></span>](intro#types) **parameters.width**: How wide the button will be, relative to the Object.
		* [<span class="tag flo"></span>](intro#types) **parameters.height**: How tall the button will be, relative to the Object.
		* [<span class="tag flo"></span>](intro#types) **parameters.font_size**: Size the label font will be, relative to the Object.
		* [<span class="tag col"></span>](intro#color) **parameters.color**: A Color for the clickable button.
		* [<span class="tag col"></span>](intro#color) **parameters.font_color**: A Color for the label text.
		* [<span class="tag str"></span>](intro#types) **parameters.tooltip**: Text of a popup of text, similar to how an Object's name is displayed on mouseover.

``` Lua
self.editButton({index=0, label="New Label"})
```

---


####editInput(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Modify an existing input. The only parameter that is required is the index. The rest are optional, and not using them will cause the edited input's element to remain. Indexes start at 0. The first input on any given Object has an index of 0, the next input on it has an index of 1, etc. Each Object has its own indexes.

!!!info "editInput(parameters)"
	*All fields besides `index` are optional. If not used, the element will default to the element's current setting.*

	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table containing the information used to spawn the input.
		* [<span class="tag int"></span>](intro#types) **parameters.index**: Index of the input you want to edit.
		* [<span class="tag str"></span>](intro#types) **parameters.input_function**: The function's name that will be run when the input is selected.
		* [<span class="tag obj"></span>](intro#types) **parameters.function_owner**: The Object which contains the input_function function.
		* [<span class="tag str"></span>](intro#types) **parameters.label**: Text that appears as greyed out text when there is no value in the input.
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: Where the input appears, relative to the Object's center.
		* [<span class="tag vec"></span>](intro#vector) **parameters.rotation**: How the input is rotated, relative to the Object's rotation.
		* [<span class="tag vec"></span>](intro#vector) **parameters.scale**: Scale of the input, relative to the Object's scale.
		* [<span class="tag flo"></span>](intro#types) **parameters.width**: How wide the input will be, relative to the Object.
		* [<span class="tag flo"></span>](intro#types) **parameters.height**: How tall the input will be, relative to the Object.
		* [<span class="tag flo"></span>](intro#types) **parameters.font_size**: Size the label/value font will be, relative to the Object.
		* [<span class="tag col"></span>](intro#color) **parameters.color**: A Color for the input's background.
		* [<span class="tag col"></span>](intro#color)&nbsp;**parameters.font_color**: A Color for the value text.
		* [<span class="tag str"></span>](intro#types) **parameters.tooltip**: A popup of text, similar to how an Object's name is displayed on mouseover.
		* [<span class="tag int"></span>](intro#types) **parameters.alignment**: How text is aligned in the input box.
			* **1**: Automatic
			* **2**: Left
			* **3**: Center
			* **4**: Right
			* **5**: Justified
		* [<span class="tag str"></span>](intro#types) **parameters.value**: A String of the text entered into the input.
		* [<span class="tag int"></span>](intro#types) **parameters.validation**: An Int which determines what characters can be input into the value.
			* **1**: None
			* **2**: Integer
			* **3**: Float
			* **4**: Alphanumeric
			* **5**: Username
			* **6**: Name
		* [<span class="tag int"></span>](intro#types) **parameters.tab**: An Int which determines how pressing tab is handled when inputting.
			* **1**: None
			* **2**: Select Next Input
			* **3**: Indent

``` Lua
self.editInput({index=0, value="New Value"})
```

---


####getButtons()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of all buttons on this Object. The Table contains parameters tables with the same keys as seen in the [createButton](#createbutton) section, except each Table of parameters also contains an __index__ entry. This is used to identify each button, used by [editButton](#editbutton) and [removeButton](#removebutton).

Indexes start at 0.

---


####getInputs()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of all inputs on this Object. The Table contains parameters tables with the same keys as seen in the [createInput](#createinput) section, except each Table of parameters also contains an __index__ entry. This is used to identify each input, used by [editInput](#editinput) and [removeInput](#removeinput).

Indexes start at 0.

---


####removeButton(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Removes a specific button. Indexes start at 0. The first button on any given Object has an index of 0, the next button on it has an index of 1, etc. Each Object has its own indexes.

Removing an index instantly causes all other higher indexes to shift down 1.

!!!info "removeButton(index)"
	* [<span class="tag int"></span>](intro#types) **index**: Button index to remove.

---


####removeInput(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Removes a specific input. Indexes start at 0. The first button on any given Object has an index of 0, the next input on it has an index of 1, etc. Each Object has its own indexes.

Removing an index instantly causes all other higher indexes to shift down 1.

!!!info "removeInput(index)"
	* [<span class="tag int"></span>](intro#types) **index**: Input index to remove.

---


###Get Function Details


####getCustomObject()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table with the Custom Object information of a Custom Object. See the [Spawnable Objects](spawnableobjects) page for the kind of information returned.

``` Lua
-- Example returned Table for a custom token
{
	image = "SOME URL HERE",
	thickness = 0.2,
	merge_distance = 15,
	stackable = false,
}
```

---


####getObjects()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of objects in the script zone/bag/deck. What it returns varies depending on the type of Object it is used on.

If an Object is inside of a container, it does not exist in-game. As a result, you only get data on each Object, not an Object reference.

!!!info "Return Table by Object Type"
	!!!info "Scripting Zone"
		Returns a Table of Object references to every object in the scripting zone.

		``` Lua
		{
			object_1,
			object_2,
		}
		```

	!!!info "Bag"
		Returns a Table of sub-Tables, each sub-Table containing data on 1 bagged item. Indexes start at 0.

		* [<span class="tag str"></span>](intro#types) **name**: Name of the Object.
		* [<span class="tag str"></span>](intro#types) **guid**: GUID of the Object.
		* [<span class="tag int"></span>](intro#types) **index**: Index of the Object, represents the Object's place in the bag.

		``` Lua
		{
			{
				name  = "Object Name",
				guid  = "AAA111",
				index = 0,
			},
		}
		```

	!!!info "Deck"
		Returns a Table of sub-Tables, each sub-Table containing data on 1 card. Indexes start at 0.

		* [<span class="tag str"></span>](intro#types) **nickname**: Name of the card.
		* [<span class="tag str"></span>](intro#types) **description**: Description of the card.
		* [<span class="tag str"></span>](intro#types) **guid**: GUID of the card.
		* [<span class="tag int"></span>](intro#types) **index**: Index of the card, represents the card's order in the deck.
		* [<span class="tag str"></span>](intro#types) **lua_script**: Any Lua scripting saved on the card.

		``` Lua
		{
			{
				nickname    = "Object Name",
				description = "Object Descripotion",
				guid        = "AAA111",
				index       = 0,
				lua_script  = "Any Lua Script On This Card",
			},
		}
		```

This function is often used with [takeObject(...)](#takeobject) to remove objects from containers.

---


####getRotationValues()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of rotation values. Rotation values are used to give value to different rotations (like dice) based on which side is pointed "up". It works by checking all of the rotation values assigned to an object and determining which one of them is closest to pointing up, and then displaying the value associated with that rotation.

You can manually assign rotation values to objects using the Rotation Value Gizmo tool (in the left side Gizmo menu) or using [setRotationValues(...)](setrotationvalues).

!!!info "Return Table"
	The returned Table contains sub-Tables, each sub-Table containing these 2 key/value pairs.

	* [<span class="tag var"></span>](intro#types) **value**: What value is associated with a given rotation. Often a String or Int.
	* [<span class="tag vec"></span>](intro#vector)&nbsp;**rotation**: Rotation of the Object that best represents the given value pointing up.

``` Lua
-- Example returned Table for a coin
{
	{value="Heads", rotation={x=0, y=0, z=0}},
	{value="Tails", rotation={x=180, y=0, z=0}},
}
```

---


####getStates()

[<span class="ret tab"></span>](intro#types)&nbsp;Returns a Table of information on the [states](http://berserk-games.com/knowledgebase/creating-states/) of an Object. Stated Objects have ids (indexes) starting with 1.

!!!info "Return Table"
	* [<span class="tag str"></span>](intro#types)&nbsp;**name**: Name of the Object.
	* [<span class="tag str"></span>](intro#types)&nbsp;**guid**: GUID of the Object.
	* [<span class="tag int"></span>](intro#types)&nbsp;**id**: ID (index) of the state.

``` Lua
-- Example returned Table
{
	{
		name = "First State",
		guid = "AAA111",
		id   = 1,
	},
	{
		name = "Second State",
		guid = "BBB222",
		id   = 2,
	},
}
```

---


####getValue()

[<span class="ret int"></span>](intro#types)&nbsp;Gets a value. What the value represents depends on what type of Object this function is used on.

Object | Value
-- | --
[Clock](clock) | Returns Int of stopwatch/timer current time *(in seconds)*.
[Counter](clock) | Returns Int of counter value.
Rotation Value | Returns Var of the face-up value.
Hidden Zone | Returns String of the Player [Color](color) of the zone.
Poker Chip | Returns Int of the face value. {>>Does not work on custom chips.<<}
Tablet | Returns String of the current URL.

---


###Set Function Details

####setCustomObject(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Sets a custom Object's properties. It can be used after [spawnObject](base#spawnobject) or on an already existing custom Object. If used on an already existing custom Object, you must use [reload](#reload) on the object after setCustomObject for the changes to be displayed.

!!!info "setCustomObject(parameters)"
	The Table of parameters varies, depending on which type of custom Object it is. See the [Spawnable Object](spawnableobjects) page for the parameters needed.

``` Lua
-- Example of a custom token
params = {
	image = "SOME URL HERE",
	thickness = 0.2,
	merge_distance = 15,
	stackable = false,
}
obj.setCustomObject(params)
```

---


####setRotationValues(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Sets rotation values of an object. Rotation values are used to give value to different rotations (like dice). It works by checking all of the rotation values assigned to an object and determining which one of them is closest to pointing up, and then displaying the value associated with that rotation.

!!!info "setRotationValues(rotation_values)"
	* [<span class="tag tab"></span>](intro#types)&nbsp;**rotation_values**: A Table containing Tables with the following values. 1 sub-Table per "face".
		* [<span class="tag var"></span>](intro#types)&nbsp;**rotation_values.value**: What value is associated with a given rotation. Often a String or Int.
		* [<span class="tag vec"></span>](intro#vector)&nbsp;**rotation_values.rotation**: The rotation Vector of the Object that best represents the given value pointing up.

``` Lua
-- Example setting of rotation values for a coin
rotation_values = {
	{value="Heads", rotation={x=0, y=0, z=0}},
	{value="Tails", rotation={x=180, y=0, z=0}},
}
self.setRotationValues(rotation_values)
```

---


####setValue(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Sets a value on an Object. What the value represents depends on what type of Object it is.

Object | Value
-- | --
[Clock](clock) | Set Int for stopwatch/timer current time *(in seconds)*.
[Counter](clock) | Set Int for counter value.
Rotation Value | Set Var for the face-up value.
Hidden Zone | Set String for the Player [Color](color) of the zone.
Tablet | Set String for the current URL.

---


###Action Function Details

####call(...)

[<span class="ret var"></span>](intro#types)&nbsp;Used to call a Lua function on this Object. This is used to remotely call functions in other scripts, either in Global or Object scripts. `Global` is the "Object" to use to call a function in the Global script.

*Var is only returned if the function called has a `return`. Otherwise return is `nil`. See example.*

!!!info "call(func_name, func_params)"
	* [<span class="tag str"></span>](intro#types) **func_name**: Function name you want to activate.
	* [<span class="tag tab"></span>](intro#types) **func_params**: A Table containing any data you want to pass to that function.
		* {>>Optional, will not be sent by default.<<}

``` Lua
-- Call, used from an Object script
params = {
	msg   = "Hello world!",
	color = {r=0.2, g=1, b=0.2},
}
-- Success would be set to true by the return value in the function
success = Global.call("testFunc", params)
```
``` Lua
-- Function in Global
function testFunc(params)
	broadcastToAll(params.msg, params.color)
	return true
end
```

---


####clone(...)

[<span class="ret obj"></span>](intro#types)&nbsp;Copy/Paste this Object.

!!!info "clone(parameters)"
	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table with information used when pasting.
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: Where the Object is placed.
			* {>>Optional, defaults to {x=0, y=3, z=0}.<<}
		* [<span class="tag boo"></span>](intro#types) **parameters.snap_to_grid**: If the Object snaps to grid.
			* {>>Optional, defaults to false.<<}

---


####deal(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Deals Objects to hand zones. Will deal from decks/bags/stacks as well as individual items. If dealing an individual item to a hand zone, it is a good idea to make sure that its [Member Variable](#member-variables) for `use_hands` is `true`.

!!!info "deal(number, player_color, index)"
	* [<span class="tag int"></span>](intro#types) **number**: How many to deal.
	* [<span class="tag str"></span>](intro#types) **player_color**: The [Player Color](player-color) to deal to.
		* {>>Optional, defaults to an empty string. If not supplied, it will attempt to deal to all seated players.<<}
	* [<span class="tag int"></span>](intro#types) **index**: Index of which Object to deal from a container.
		* {>>Optional, defaults to 0. If not supplied it will deal in regular order.<<}

---


####dealToColorWithOffset(...)

[<span class="ret obj"></span>](intro#types)&nbsp;Deals from a deck to a position relative to the hand zone.

!!!info "dealToColorWithOffset(offset, flip, player_color)"
	* [<span class="tag vec"></span>](intro#vector) **offset**: The x/y/z offset to deal to around the given hand zone.
	* [<span class="tag boo"></span>](intro#types) **flip**: If the card is flipped over when dealt.
	* [<span class="tag str"></span>](intro#types) **player_color**: Hand zone [Player Color](player-color) to offset dealing to.

``` Lua
-- Example of dealing 2 cards in front of the White player, face up.
self.dealToColorWithOffset({-2,0,5}, true, "White")
self.dealToColorWithOffset({ 2,0,5}, true, "White")
```


####putObject(...)

[<span class="ret obj"></span>](intro#types)&nbsp;Places an object into a container (chip stacks/bags/decks).

!!!info "putObject(put_object)"
	* [<span class="tag obj"></span>](intro#types) **put_object**: An Object to place into the container.

``` Lua
-- Example of a script on a bag that places Object into itself
local obj = getObjectFromGUID("AAA111")
self.putObject(obj)
```

---


####reload()

[<span class="ret obj"></span>](intro#types)&nbsp;Returns Object reference of itself after it respawns itself. This function causes the Object to be deleted and respawned instantly to refresh it, so its old Object reference will no longer be valid.

Most often this is used after using [setCustomObject(...)](#setcustomobject) to modify a custom object.

---


####takeObject(...)

[<span class="ret obj"></span>](intro#types)&nbsp;Takes an object from a container (bag/deck/chip stack) and places it in the world.

!!!tip
	Spawned Objects take a moment to be physically spawned into the game. The purpose of the callback functionality is to allow you to run additional actions after the Object has been initiated fully into the instance. It is also possible to add a delay using a [coroutine](#startluacoroutine).

!!!info "takeObject(parameters)"
	* [<span class="tag tab"></span>](intro#types) **parameters**: A Table of parameters used to determine how takeObject will act.
		* [<span class="tag vec"></span>](intro#vector) **parameters.position**: A Vector of the position to place Object.
			* {>>Optional, defaults to container's position + 2 on the x axis.<<}
		* [<span class="tag vec"></span>](intro#vector) **parameters.rotation**: A Vector of the rotation of the Object.
			* {>>Optional, defaults to the container's rotation.<<}
		* [<span class="tag boo"></span>](intro#types) **parameters.flip**: If the Object is flipped over.
			* {>>Optional, defaults to false. Only used with decks, not bags/stacks.<<}
			* {>>If rotation is used, flip's Bool will be ignored.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.guid**: GUID of the Object to take.
			* {>>Optional,  no default. Only use index or guid, never both.<<}
		* [<span class="tag int"></span>](intro#types) **parameters.index**: Index of the Object to take.
			* {>>Optional,  no default. Only use index or guid, never both.<<}
		* [<span class="tag boo"></span>](intro#types) **parameters.top**: If an object is taken from the top (vs bottom).
			* {>>Optional, defaults to true.<<}
		* [<span class="tag boo"></span>](intro#types) **parameters.smooth**: If the taken Object moves smoothly or instantly.
			* {>>Optional, defaults to true.<<}
		* [<span class="tag str"></span>](intro#types) **parameters.callback**: Function name you want activated once the Object is initiated.
			* {>>Optional, no default.<<}
			* {>>A callback function has 2 parameters, the Object spawned and, if used, the Table of params.<<}
		* [<span class="tag obj"></span>](intro#types) **parameters.callback_owner**: What Object has the callback function in its script. Global is a valid target.
			* {>>Optional, defaults to container Object. Serves no purpose if callback is not also used.<<}
		* [<span class="tag tab"></span>](intro#types) **parameters.params**: Data to send to the callback to use as parameters. See example.
			* {>>Optional, no default. Serves no purpose if callback is not also used.<<}

``` Lua
function onLoad()
    futureName = "Taken from container!"
    takeParams = {
        position = {x=0, y=3, z=5},
        callback = "take_callback",
        callback_owner = self,
        params = {name = futureName},
    }
    self.takeObject(takeParams)
end

function take_callback(object_spawned, params)
    object_spawned.setName(params.name)
end
```


???tip "Tip for using GUID to pull Object"
	When getting the GUIDs of objects in a container, it is possible items can have the same GUID while in a container. This is because only once two items try to exist at the same time is one of them given a new GUID, and Objects in a container do not currently exist. Removing all Objects from the container at once will force all of them to be given unique GUIDs.

???tip "Tip for using index to pull Object"
	When you take an Object from the container, all higher indexes are reduced by 1 instantly. If you pull more than once Object at once by their index, you must account for this index changing.
