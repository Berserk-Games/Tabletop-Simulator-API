The Object class represents any entity within tabletop simulator. Once you have a reference to an object in you're script you can call functions on it directly. Example: `obj.getPosition(...)`. You can get a reference to an object multiple ways;

* Using the `self` property if your script is on an Object and referring to that Object.
* Using [`getObjectFromGUID(...)`](base.md#getobjectfromguid) with the object's GUID (found by right clicking it with the pointer).
* Getting it as a return from another function, like with [`spawnObject(...)`](base.md#spawnobject).

##Member Variables

###Common Variables
These are variables that are common to all objects. Some variables are read-only, which means you can query the
property, but are unable to assign a new value to it.

!!!example
	Locking/freezing an object by assigning `true` to [locked](#locked).
	```lua
	object.locked = true
	```

!!!example
	Printing whether or not object is [locked](#locked).
	```lua
	if object.locked then
		print("Object is locked")
	else
		print("Object is not locked")
	end
	```

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="alt_view_angle"></a>alt_view_angle | When non-zero, the Alt view will use the specified Euler angle to look at the object. | [<span class="tag vec"></span>](types.md)
<a class="anchor" id="angular_drag"></a>angular_drag | Angular drag. [Unity rigidbody property](https://docs.unity3d.com/2019.1/Documentation/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="auto_raise"></a>auto_raise | If an object should be lifted above other objects to avoid collision when held by a player. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="bounciness"></a>bounciness | Bounciness, value of 0-1. [Unity physics material](https://docs.unity3d.com/2019.1/Documentation/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="drag"></a>drag | Drag. [Unity rigidbody property](https://docs.unity3d.com/2019.1/Documentation/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="drag_selectable"></a>drag_selectable | <p>When `false`, the object will not be selected by regular (click and drag) selection boxes that are drawn around the object.</p><p>Players may proceed to override this behavior by holding the "Shift" modifier whilst drag selecting.</p> | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="dynamic_friction"></a>dynamic_friction | Dynamic friction, value of 0-1. [Unity physics material](https://docs.unity3d.com/2019.1/Documentation/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="grid_projection"></a>grid_projection | If grid lines can appear on the Object if visible grids are turned on. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="guid"></a>guid | The 6 character unique Object identifier within Tabletop Simulator. It is assigned correctly once the `spawning` member variable becomes false. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="held_by_color"></a>held_by_color | The Color of the Player that is holding the object. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="held_flip_index"></a>held_flip_index | 0-23 value. Changes when a Player hits flip or alt + rotate. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="held_position_offset"></a>held_position_offset | Position offset from pointer. | [<span class="tag vec"></span>](types.md#vector)
<a class="anchor" id="held_reduce_force"></a>held_reduce_force | When the Object collides with something while moving this is automatically enabled and reduces the movement force. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="held_rotation_offset"></a>held_rotation_offset | Rotation offset from pointer. | [<span class="tag vec"></span>](types.md#vector)
<a class="anchor" id="held_spin_index"></a>held_spin_index | 0-23 value. Changes when a Player rotates the Object. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="hide_when_face_down"></a>hide_when_face_down | Hide the Object when face-down as if it were in a hand zone. The face is the "top" of the Object, the direction of its positive Y coordinate. Cards/decks default to `true`. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="ignore_fog_of_war"></a>ignore_fog_of_war | Makes the object not be hidden by [Fog of War](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone). | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="interactable"></a>interactable | If an object can be interacted with by Players. Other object will still be able to interact with it. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="is_face_down"></a>is_face_down | If an Object is roughly face-down (like with cards). The face is the "top" of the Object, the direction of its positive Y coordinate. Read only.  | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="loading_custom"></a>loading_custom | If the Object's custom elements (images/models/etc) are loading. Read only. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="locked"></a>locked | If the object is frozen in place (preventing physics interactions). | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="mass"></a>mass | Mass. [Unity rigidbody property](https://docs.unity3d.com/2019.1/Documentation/Manual/class-Rigidbody.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="max_typed_number"></a>max_typed_number | <p>Determines the maximum number of digits which a user may type whilst hovering over an object.</p><p>As soon as a player types the maximum number of digits, the corresponding behavior (e.g. [onObjectNumberTyped](event.md#onobjectnumbertyped)/[onNumberTyped](event.md#onnumbertyped)) is triggered immediately, improving responsiveness.</p> | [<span class="tag int"></span>](types.md)
<a class="anchor" id="measure_movement"></a>measure_movement | Measure Tool will automatically be used when moving the Object. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="memo"></a>memo | A string you can store info in for an object. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="name"></a>name | Internal resource name for this Object. Read only, and only useful for [spawnObjectData()](base.md#spawnobjectdata). Generally, you want [getName()](#getname). | [<span class="tag str"></span>](types.md)
<a class="anchor" id="pick_up_position"></a>pick_up_position | The position the Object was picked up at. Read only. | [<span class="tag vec"></span>](types.md#vector)
<a class="anchor" id="pick_up_rotation"></a>pick_up_rotation | The rotation the Object was picked up at. Read only. | [<span class="tag vec"></span>](types.md#vector)
<a class="anchor" id="remainder"></a>remainder | <p>If this object is a container that cannot exist with less than two contained objects (e.g. a deck), [taking out](#takeObject) the second last contained object will result in the container being destroyed. In its place the last remaining object in the container will be spawned.</p><p>This variable provides a reference to the remaining object when it is being spawned. Otherwise, it's `nil`. Read only.</p> | [<span class="tag obj"></span>](types.md)
<a class="anchor" id="resting"></a>resting | If an Object is at rest. [Unity rigidbody property](https://docs.unity3d.com/2019.1/Documentation/Manual/RigidbodiesOverview.html). | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="script_code"></a>script_code | The Lua Script on the Object. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="script_state"></a>script_state | The saved data on the object. See [onSave()](event.md#onsave). | [<span class="tag str"></span>](types.md)
<a class="anchor" id="spawning"></a>spawning | If the Object is finished spawning. Read only. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="static_friction"></a>static_friction | Static friction, value of 0-1. [Unity physics material](https://docs.unity3d.com/2019.1/Documentation/Manual/class-PhysicMaterial.html). | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="sticky"></a>sticky | If other Objects on top of this one are also picked up when this Object is. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="tag"></a>tag | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [type](#type)_.</p>This object's type. Read only. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="tooltip"></a>tooltip | If the tooltip opens when a pointer hovers over the object. Tooltips display name and description. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="type"></a>type | This object's type. Read only. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="use_gravity"></a>use_gravity | If gravity affects this object. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="use_grid"></a>use_grid | If snapping to grid is enabled or not. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="use_hands"></a>use_hands | If this object can be held in a hand zone. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="use_rotation_value_flip"></a>use_rotation_value_flip | Switches the axis an Object rotates around when flipped. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="use_snap_points"></a>use_snap_points | If snap points are used or ignored. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="value"></a>value | The value of the object for summing up selected objects. Only works if the apropriate bits are set in `obj.value_flags` | [<span class="tag int"></span>](types.md)
<a class="anchor" id="value_flags"></a>value_flags | A bit field, objects with overlapping `value_flag` bits are counted together when selected. | [<span class="tag int"></span>](types.md)

!!! bug
    The `value_flags` and `value` member variables do not persist when the object is reloaded (such as loading a save and entering/exiting containers).

###Behavior Variables

Some objects provide additional behavior. This functionality is accessible as Object member variables, but will be `nil`
unless the Object includes the behavior.

!!!example
	The "Counter" Object has a `Counter` member variable. We'll use it to increment and retrieve the counter's value.
	```lua
	object.Counter.increment()
	print("The counter value is now " .. object.Counter.getValue())
	```

Variable | Type | Available On
-- | -- | --
<a class="anchor" id="assetbundle"></a>AssetBundle | [AssetBundle](behavior/assetbundle.md) | Custom "AssetBundle" objects.
<a class="anchor" id="book"></a>Book | [Book](behavior/book.md) | "Custom PDF" objects.
<a class="anchor" id="browser"></a>Browser | [Browser](behavior/browser.md) | "Tablet" objects.
<a class="anchor" id="clock"></a>Clock | [Clock](behavior/clock.md) | "Digital Clock" objects.
<a class="anchor" id="counter"></a>Counter | [Counter](behavior/counter.md) | "Counter" objects.
<a class="anchor" id="rpgfigurine"></a>RPGFigurine | [RPGFigurine](behavior/rpgfigurine.md) | "RPG Kit" animated figurine objects i.e. [type](#type) "rpgFigurine".
<a class="anchor" id="texttool"></a>TextTool | [TextTool](behavior/texttool.md) | 3D Text objects e.g. text created with the in-game Text tool.

---

##Function Summary

###Transform Functions
These functions handle the physical attributes of an Object: Position, Rotation, Scale, Bounds, Velocity. In other words, moving objects around as well as getting information on how they are moving.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addForce([<span class="tag vec"></span>](types.md#vector) vector, [<span class="tag int"></span>](types.md) force_type) | Adds force to an object in a directional Vector. | [<span class="ret boo"></span>](types.md) | [:i:](#addforce)
addTorque([<span class="tag vec"></span>](types.md#vector) vector, [<span class="tag int"></span>](types.md) force_type) | Adds torque to an object in a rotational Vector. | [<span class="ret boo"></span>](types.md) | [:i:](#addtorque)
<a class="anchor" id="getangularvelocity"></a>getAngularVelocity() | Returns a Vector of the current angular velocity. | [<span class="ret vec"></span>](types.md#vector)
getBounds() | Returns a Vector describing the size of an object in Global terms. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#getbounds)
getBoundsNormalized() | Returns a Vector describing the size of an object in Global terms, as if it was rotated to {0,0,0}. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#getboundsnormalized)
<a class="anchor" id="getposition"></a>getPosition() | Returns a Vector of the current [World Position](types.md#position). | [<span class="ret vec"></span>](types.md#vector)
<a class="anchor" id="getpositionsmooth"></a>getPositionSmooth() | Returns a Vector of the current smooth move target if the object is moving, otherwise returns nil. | [<span class="ret vec"></span>](types.md#vector)
<a class="anchor" id="getrotation"></a>getRotation() | Returns a Vector of the current rotation. | [<span class="ret vec"></span>](types.md#vector)
<a class="anchor" id="getrotationsmoth"></a>getRotationSmooth() | Returns a Vector of the current smooth rotation target if the object is moving, otherwise returns nil. | [<span class="ret vec"></span>](types.md#vector)
getScale() | Returns a Vector of the current scale. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#getscale)
getTransformForward() | Returns a Vector of the forward direction of this object. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#gettransformforward)
getTransformRight() | Returns a Vector of the right direction of this object. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#gettransformright)
getTransformUp() | Returns a Vector of the up direction of this object. | [<span class="ret vec"></span>](types.md#vector) | [:i:](#gettransformup)
<a class="anchor" id="getvelocity"></a>getVelocity() | Returns a Vector of the current velocity. | [<span class="ret vec"></span>](types.md#vector) |
<a class="anchor" id="issmoothmoving"></a>isSmoothMoving() | Indicates if an object is traveling as part of a Smooth move. Smooth moving is performed by setPositionSmooth and setRotationSmooth. | [<span class="ret boo"></span>](types.md) |
positionToLocal([<span class="tag vec"></span>](types.md#vector) vector) | Returns a Vector after converting a world Vector (World Position) to a local Vector ([Local Position](types.md#position)). | [<span class="ret vec"></span>](types.md#vector) | [:i:](#positiontolocal)
positionToWorld([<span class="tag vec"></span>](types.md#vector) vector) | Returns a Vector after converting a local Vector (Local Position) to a world Vector ([World Position](types.md#position)). | [<span class="ret vec"></span>](types.md#vector) | [:i:](#positiontoworld)
rotate([<span class="tag vec"></span>](types.md#vector) vector) | Rotates Object smoothly in the direction of the given Vector. | [<span class="ret boo"></span>](types.md) | [:i:](#rotate)
scale([<span class="tag vec"></span>](types.md#vector) vector or [<span class="tag flo"></span>](types.md)) | Scales Object by a multiple. | [<span class="ret boo"></span>](types.md) | [:i:](#scale)
<a class="anchor" id="setangularvelocity"></a>setAngularVelocity([<span class="tag vec"></span>](types.md#vector) vector) | Sets a Vector as the current angular velocity. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="setposition"></a>setPosition([<span class="tag vec"></span>](types.md#vector) vector) | Instantly moves an Object to the given Vector. The Vector is interpreted as [World Position](types.md#position). | [<span class="ret boo"></span>](types.md) |
setPositionSmooth([<span class="tag vec"></span>](types.md#vector) vector, [<span class="tag boo"></span>](types.md) collide, [<span class="tag boo"></span>](types.md) fast) | Moves the Object smoothly to the given Vector. The Vector is interpreted as [World Position](types.md#position). | [<span class="ret boo"></span>](types.md) | [:i:](#setpositionsmooth)
<a class="anchor" id="setrotation"></a>setRotation([<span class="tag vec"></span>](types.md#vector) vector) | Instantly rotates an Object to the given Vector. | [<span class="ret boo"></span>](types.md) |
setRotationSmooth([<span class="tag vec"></span>](types.md#vector) vector, [<span class="tag boo"></span>](types.md) collide, [<span class="tag boo"></span>](types.md) fast) | Rotates the Object smoothly to the given Vector. | [<span class="ret boo"></span>](types.md) | [:i:](#setrotationsmooth)
<a class="anchor" id="setscale"></a>setScale([<span class="tag vec"></span>](types.md#vector) vector) | Sets a Vector as the current scale. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="setvelocity"></a>setVelocity([<span class="tag vec"></span>](types.md#vector) vector) | Sets a Vector as the current velocity. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="translate"></a>translate([<span class="tag vec"></span>](types.md#vector) vector) | Smoothly moves Object by the given Vector offset. | [<span class="ret boo"></span>](types.md) |


###Tag Functions
These functions deal with the [Tags](https://kb.tabletopsimulator.com/game-tools/object-tags/) associated with the object. An individual tag is a [<span class="tag str"></span>](types.md) and is case-insensitive.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="addtag"></a>addTag([<span class="tag str"></span>](types.md) tag) | Adds the specified tag to the object. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="gettags"></a>getTags() | Returns a table of tags ([<span class="tag str"></span>](types.md)) that have been added to the object. | [<span class="ret tab"></span>](types.md)
<a class="anchor" id="hasanytag"></a>hasAnyTag() | Returns whether the object has any tags. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="hasmatchingtag"></a>hasMatchingTag([<span class="tag obj"></span>](types.md) other) | Returns whether the object and the specified `other` object share at least one tag in common. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="hastag"></a>hasTag([<span class="tag str"></span>](types.md) tag) | Returns whether the object has the specified tag. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="removetag"></a>removeTag([<span class="tag str"></span>](types.md) tag) | Removes the specified tag from the object. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="settags"></a>setTags([<span class="tag tab"></span>](types.md) tags) | Replaces all tags on the object with those contained in the specified table (containing [<span class="tag str"></span>](types.md)). | [<span class="ret boo"></span>](types.md) |

If you want to create your own system in which object tags govern the interactions, the canonical logic is that if the system has no tags it interacts with everything, but if it has any tags then it only interacts with objects which share one of them.  i.e. (assuming the system is represented by an in-game object):
```lua
allow_interaction = not system.hasAnyTag() or system.hasMatchingTag(object)
```


###UI Functions
A new UI system was added to Tabletop Simulator which allows for more flexibility in the creation of UI elements on Objects. The old system (Classic UI) and new system (Custom UI) both work, and each has its own strengths.

####Classic UI
These functions allow for the creation/editing/removal of functional buttons and text inputs which themselves trigger code within your scripts. These buttons/inputs are attached to the object they are created on.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="clearbuttons"></a>clearButtons() | Removes all scripted buttons. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="clearinputs"></a>clearInputs() | Removes all scripted inputs. | [<span class="ret boo"></span>](types.md) |
createButton([<span class="tag tab"></span>](types.md) parameters) | Creates a scripted button attached to the Object. | [<span class="ret boo"></span>](types.md) | [:i:](#createbutton)
createInput([<span class="tag tab"></span>](types.md) parameters) | Creates a scripted input attached to the Object. | [<span class="ret boo"></span>](types.md) | [:i:](#createinput)
editButton([<span class="tag tab"></span>](types.md) parameters) | Modify an existing button. | [<span class="ret boo"></span>](types.md) | [:i:](#editbutton)
editInput([<span class="tag tab"></span>](types.md) parameters) | Modify an existing input. | [<span class="ret boo"></span>](types.md) | [:i:](#editinput)
getButtons() | Returns a Table of all buttons on this Object. | [<span class="ret tab"></span>](types.md) | [:i:](#getbuttons)
getInputs() | Returns a Table of all inputs on this Object. | [<span class="ret tab"></span>](types.md) | [:i:](#getinputs)
removeButton([<span class="tag int"></span>](types.md) index) | Removes a specific button. | [<span class="ret boo"></span>](types.md) | [:i:](#removebutton)
removeInput([<span class="tag int"></span>](types.md) index) | Removes a specific button. | [<span class="ret boo"></span>](types.md) | [:i:](#removeinput)

####Custom UI
Custom UI gives you a wide variety of element types, not just buttons and inputs, to place onto an Object. It is an extension of the UI class, and details on its use can be found [on the UI page](ui.md).


###Get Functions
These functions obtain information from an object.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="getattachments"></a>getAttachments() | Returns a table in the same format as [getObjects()](#getobjects) for containers. | [<span class="ret tab"></span>](types.md) |
<a class="anchor" id="getcolortint"></a>getColorTint() | Color tint. | [<span class="ret col"></span>](types.md#color) |
getCustomObject() | Returns a Table with the Custom Object information of a Custom Object. | [<span class="ret tab"></span>](types.md) | [:i:](#getcustomobject)
<a class="anchor" id="getdata"></a>getData() | Returns a table representation of the object, as in [getJSON()](#getjson), but before being serialized. Works with [spawnObjectData()](base.md#spawnobjectdata). | [<span class="ret tab"></span>](types.md) |
<a class="anchor" id="getdescription"></a>getDescription() | Description, also shows as part of Object's tooltip. | [<span class="ret str"></span>](types.md)
getFogOfWarReveal() | Settings impacting [Fog of War](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone) being revealed. | [<span class="ret tab"></span>](types.md) | [:i:](#getfogofwarreveal)
<a class="anchor" id="getgmnotes"></a>getGMNotes() | Game Master Notes only visible for [Player Color](player-color.md) Black. | [<span class="ret str"></span>](types.md) |
<a class="anchor" id="getguid"></a>getGUID() | String of the Object's unique identifier. | [<span class="ret str"></span>](types.md) |
<a class="anchor" id="getjson"></a>getJSON() | Returns a serialization of the JSON string which represents this item. Works with [spawnObjectJSON()](base.md#spawnobjectjson). | [<span class="ret str"></span>](types.md) |
getJoints() | Returns information on any joints attached to this object. | [<span class="ret tab"></span>](types.md) | [:i:](#getjoints)
<a class="anchor" id="getlock"></a>getLock() | If the Object is locked. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="getname"></a>getName() | Name, also shows as part of Object's tooltip. | [<span class="ret str"></span>](types.md) |
getObjects() | Returns data describing the objects contained within in the zone/bag/deck. | [<span class="ret var"></span>](types.md) | [:i:](#getobjects)
<a class="anchor" id="getquantity"></a>getQuantity() | Returns the number of objects contained within (if the Object is a bag, deck or stack), otherwise -1. | [<span class="ret int"></span>](types.md) |
getRotationValue() | Returns the current rotationValue. Rotation values are used to give value to different rotations (like dice). | [<span class="ret var"></span>](types.md) | [:i:](#getrotationvalue)
getRotationValues() | Returns a Table of rotation values. Rotation values are used to give value to different rotations (like dice). | [<span class="ret tab"></span>](types.md) | [:i:](#getrotationvalues)
<a class="anchor" id="getselectingplayers"></a>getSelectingPlayers() | Returns a table of the player colors currently selecting the object. | [<span class="ret tab"></span>](types.md)
<a class="anchor" id="getstateid"></a>getStateId() | Current [state](https://kb.tabletopsimulator.com/host-guides/creating-states/) ID (index) an object is in. Returns -1 if there are no other states. State ids (indexes) start at 1. | [<span class="ret int"></span>](types.md) |
getStates() | Returns a Table of information on the [states](https://kb.tabletopsimulator.com/host-guides/creating-states/) of an Object. | [<span class="ret tab"></span>](types.md) | [:i:](#getstates)
getValue() | Returns the Object's value. This represents something different depending on the Object's [type](#type). | [<span class="ret var"></span>](types.md) | [:i:](#getvalue)
<a class="anchor" id="isdestroyed"></a>isDestroyed() | Returns true if an Object is (or will be) destroyed. | [<span class="ret boo"></span>](types.md) |





###Set Functions
These functions apply action to an object. They take some property in order to work.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="setcolortint"></a>setColorTint([<span class="tag col"></span>](types.md#color) Color) | Sets the Color tint. | [<span class="ret boo"></span>](types.md) |
setCustomObject([<span class="tag tab"></span>](types.md) parameters) | Sets a custom Object's properties. | [<span class="ret boo"></span>](types.md) | [:i:](#setcustomobject)
<a class="anchor" id="setdescription"></a>setDescription([<span class="tag str"></span>](types.md) description) | Sets a description for an Object. Shows in tooltip after delay. | [<span class="ret boo"></span>](types.md)
setFogOfWarReveal([<span class="tag tab"></span>](types.md) fog_settings) | Establish the settings and enable/disable an Object's revealing of [Fog of War](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone). | [<span class="ret boo"></span>](types.md) | [:i:](#setfogofwarreveal)
<a class="anchor" id="setgmnotes"></a>setGMNotes([<span class="tag str"></span>](types.md) notes) | Sets Game Master Notes only visible for [Player Color](player-color.md) Black. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="setlock"></a>setLock([<span class="tag boo"></span>](types.md) lock) | Sets if an object is locked in place. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="setname"></a>setName([<span class="tag str"></span>](types.md) name) | Sets a name for an Object. Shows in tooltip. | [<span class="ret boo"></span>](types.md)
setRotationValue([<span class="tag var"></span>](types.md) rotation_value) | Sets the Object's rotation value i.e. physically rotates the object. | | [:i:](#setrotationvalue)
setRotationValues([<span class="tag tab"></span>](types.md) rotation_values) | Sets rotation values of an object. Rotation values are used to give value to different rotations (like dice). | [<span class="ret boo"></span>](types.md) | [:i:](#setrotationvalues)
<a class="anchor" id="setstate"></a>setState([<span class="tag int"></span>](types.md) state_id) | Sets [state](https://kb.tabletopsimulator.com/host-guides/creating-states/) of an Object. State ids (indexes) start at 1. | [<span class="ret obj"></span>](types.md) |
setValue([<span class="tag var"></span>](types.md) value) | Sets the Object's value. This represents something different depending on the Object's [type](#type). | [<span class="ret boo"></span>](types.md) | [:i:](#setvalue)





###Action Function
These functions perform general actions on objects.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="addattachment"></a>addAttachment([<span class="tag obj"></span>](types.md) Object) | The Object supplied as param is destroyed and becomes a dummy Object child. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="fnc_addcontextmenuitem"></a>addContextMenuItem([<span class="tag str"></span>](types.md) label, [<span class="tag fun"></span>](types.md) toRunFunc, [<span class="tag boo"></span>](types.md) keep_open) | Adds a menu item to the objects right-click context menu. | [<span class="ret boo"></span>](types.md) | [:i:](#addcontextmenuitem)
clearContextMenu() | Clears all menu items added by function [addContextMenuItem](#fnc_addcontextmenuitem). | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="removeattachment"></a>removeAttachment([<span class="tag int"></span>](types.md) index) | Removes a child with the given index. Use [getAttachments()](#getattachments) to find out the index property. | [<span class="ret obj"></span>](types.md)
<a class="anchor" id="removeattachments"></a>removeAttachments() | Detaches the children of this Object. Returns a table of object references | [<span class="ret tab"></span>](types.md)
<a class="anchor" id="destroyattachment"></a>destroyAttachment([<span class="tag int"></span>](types.md) index) | Destroys an attachment with the given index. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="destroyattachments"></a>destroyAttachments() | Destroys all attachments. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="addtoplayerselection"></a>addToPlayerSelection([<span class="tag str"></span>](types.md) player_color) | Adds object to player's selection. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="removefromlayerselection"></a>removeFromPlayerSelection([<span class="tag str"></span>](types.md) player_color) | Removes object from player's selection. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="flip"></a>flip() | Flips Object over. | [<span class="ret boo"></span>](types.md) |
clone([<span class="tag tab"></span>](types.md) parameters) | Copy/Paste this Object, returning a reference to the new Object. | [<span class="ret obj"></span>](types.md) | [:i:](#clone)
cut([<span class="tag int"></span>](types.md) count) | Cuts (splits) a deck at the given card count. | [<span class="ret tab"></span>](types.md) | [:i:](#cut)
deal([<span class="tag int"></span>](types.md) number, [<span class="tag str"></span>](types.md) player_color, [<span class="tag int"></span>](types.md) index) | Deals Objects. Will deal from decks/bags/stacks/individual items. | [<span class="ret boo"></span>](types.md) | [:i:](#deal)
dealToColorWithOffset([<span class="tag vec"></span>](types.md#vector) offset, [<span class="tag boo"></span>](types.md) flip, [<span class="tag str"></span>](types.md) player_color) | Deals from a deck to a position relative to the hand zone. | [<span class="ret obj"></span>](types.md) | [:i:](#dealtocolorwithoffset)
<a class="anchor" id="destruct"></a>destruct() | Destroys Object. Allows for `self.destruct()`. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="drop"></a>drop() | Forces an Object, if held by a player, to be dropped. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="highlighton"></a>highlightOn([<span class="tag col"></span>](types.md#color) color, [<span class="tag flo"></span>](types.md) duration) | Creates a highlight around an Object. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="highlightoff"></a>highlightOff([<span class="tag col"></span>](types.md#color) color) | Removes a highlight from around an Object. | [<span class="ret boo"></span>](types.md) |
jointTo([<span class="tag obj"></span>](types.md) object, [<span class="tag tab"></span>](types.md) parameters) | Joints objects together, in the same way the Joint tool does. | [<span class="ret boo"></span>](types.md) | [:i:](#jointto)
putObject([<span class="tag obj"></span>](types.md) put_object) | Places an object into a container (chip stacks/bags/decks). | [<span class="ret obj"></span>](types.md) | [:i:](#putobject)
<a class="anchor" id="randomize"></a>randomize([<span class="tag str"></span>](types.md) color) | Shuffles deck/bag, rolls dice/coin, lifts other objects into the air. Same as pressing `R` by default. If the optional parameter `color` is used, this function will trigger `onObjectRandomized()`, passing that player color. | [<span class="ret boo"></span>](types.md) |
registerCollisions([<span class="tag boo"></span>](types.md) stay) | Registers this object for Global collision events. | [<span class="ret boo"></span>](types.md) | [:i:](#registercollisions)
reload() | Returns Object reference of itself after it respawns itself. | [<span class="ret obj"></span>](types.md) | [:i:](#reload)
<a class="anchor" id="reset"></a>reset() | Resets this Object. Resetting a Deck brings all the Cards back into it. Resetting a Bag clears its contents (works for both Loot and Infinite Bags). | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="roll"></a>roll() | Rolls dice/coins. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="shuffle"></a>shuffle() | Shuffles/shakes up contents of a deck or bag. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="shufflestates"></a>shuffleStates() | Returns an Object reference to a new [state](https://kb.tabletopsimulator.com/host-guides/creating-states/) after randomly selecting and changing to one. | [<span class="ret obj"></span>](types.md) |
split([<span class="tag int"></span>](types.md) piles) | Splits a deck, as evenly as possible, into a number of piles. | [<span class="ret tab"></span>](types.md) | [:i:](#split)
spread([<span class="tag flo"></span>](types.md) distance) | Uses the spread action on a deck. | [<span class="ret tab"></span>](types.md) | [:i:](#spread)
takeObject([<span class="tag tab"></span>](types.md) parameters) | Takes an object out of a container (bag/deck/chip stack), returning a reference to the object that was taken out. | [<span class="ret obj"></span>](types.md) | [:i:](#takeobject)
unregisterCollisions() | Unregisters this object for Global collision events. | [<span class="ret boo"></span>](types.md) | [:i:](#unregistercollisions)













###Hide Functions
These functions can hide Objects, similar to how hand zones or hidden zones do.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
setHiddenFrom([<span class="tag tab"></span>](types.md) players) | Hides the Object from the specified players, as if it were in a hand zone. | [<span class="ret boo"></span>](types.md) | [:i:](#sethiddenfrom)
setInvisibleTo([<span class="tag tab"></span>](types.md) players) | Hides the Object from the specified players, as if it were in a hidden zone. | [<span class="ret boo"></span>](types.md) | [:i:](#setinvisibleto)
attachHider([<span class="tag str"></span>](types.md) id, [<span class="tag boo"></span>](types.md) hidden, [<span class="tag tab"></span>](types.md) players) | A more advanced version of `setHiddenFrom(...)`. | [<span class="ret boo"></span>](types.md) | [:i:](#attachhider)
attachInvisibleHider([<span class="tag str"></span>](types.md) id, [<span class="tag boo"></span>](types.md) hidden, [<span class="tag tab"></span>](types.md) players) | A more advanced version of `setInvisibleTo(...)`. | [<span class="ret boo"></span>](types.md) | [:i:](#attachinvisiblehider)



###Global Function
The functions can be used on Objects, but can also be used on the game world using `Global`.

!!!important "Examples of Using Global and Object"
	* `self.getSnapPoints()` gets snap points attached to that Object.
	* `Global.getSnapPoints()` gets snap points not attached to any specific Object but instead are attached to the game world.




Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addDecal([<span class="tag tab"></span>](types.md) parameters) | Add a Decal onto an object or the game world. | [<span class="ret boo"></span>](types.md) | [:i:](#adddecal)
call([<span class="tag str"></span>](types.md) func_name, [<span class="tag tab"></span>](types.md) func_params) | Used to call a Lua function on another entity. | [<span class="ret var"></span>](types.md) | [:i:](#call)
getDecals() | Returns information on all decals attached to this object or the world. | [<span class="ret tab"></span>](types.md) | [:i:](#getdecals)
<a class="anchor" id="getluascript"></a>getLuaScript() | Get a Lua script as a string from the entity. | [<span class="ret str"></span>](types.md) |
getSnapPoints() | Returns a table of sub-tables, each sub-table representing one snap point. | [<span class="ret tab"></span>](types.md) | [:i:](#getsnappoints)
<a class="anchor" id="gettable"></a>getTable([<span class="tag str"></span>](types.md) table_name) | Data value of a variable in another Object's script. Can only return a table. | [<span class="ret tab"></span>](types.md) |
<a class="anchor" id="getvar"></a>getVar([<span class="tag str"></span>](types.md) var_name) | Data value of a variable in another entity's script. Cannot return a table. | [<span class="ret var"></span>](types.md) |
<a class="anchor" id="getvectorlines"></a>getVectorLines() | Returns Table of data representing the current Vector Lines on this entity. See [setVectorLines](#setvectorlines) for table format.| [<span class="ret tab"></span>](types.md) |
setDecals([<span class="tag tab"></span>](types.md) parameters) | Sets which decals are on an object. This removes other decals already present, and can remove all decals as well. | [<span class="ret boo"></span>](types.md) | [:i:](#setdecals)
<a class="anchor" id="setluascript"></a>setLuaScript([<span class="tag str"></span>](types.md) script) | Input a string as an entity's Lua script. Generally only used after spawning a new Object. | [<span class="ret boo"></span>](types.md) |
setSnapPoints([<span class="tag tab"></span>](types.md) parameters) | Spawns snap points from a list of parameters. | [<span class="ret boo"></span>](types.md) | [:i:](#setsnappoints)
<a class="anchor" id="settable"></a>setTable([<span class="tag str"></span>](types.md) func_name, [<span class="tag tab"></span>](types.md) data) | Creates/updates a variable in another entity's script. Only used for tables. | [<span class="ret boo"></span>](types.md) |
<a class="anchor" id="setvar"></a>setVar([<span class="tag str"></span>](types.md) func_name, [<span class="tag var"></span>](types.md) data) | Creates/updates a variable in another entity's script. Cannot set a table. | [<span class="ret boo"></span>](types.md) |
setVectorLines([<span class="tag tab"></span>](types.md) parameters) | Spawns Vector Lines from a list of parameters on this entity. | [<span class="ret boo"></span>](types.md) | [:i:](#setvectorlines)


---





##Function Details

###Transform Function Details

####addForce(...)

[<span class="ret boo"></span>](types.md) Adds force to an object in a directional Vector.

!!!info "addForce(vector, force_type)"
	* [<span class="tag vec"></span>](types.md) **vector**: A Vector of the direction and magnitude of force.
    * [<span class="tag int"></span>](types.md) **force_type**: An Int representing the force type to apply. Options below.
		* {>>Optional, defaults to 3.<<}
        * **1**: Continuous force, uses mass. *(Force)*
        * **2**: Continuous acceleration, ignores mass. *(Acceleration)*
		* **3**: Instant force impulse, uses mass. *(Impulse)*
		* **4**: Instant velocity change, ignores mass. *(Velocity Change)*

---


####addTorque(...)

[<span class="ret boo"></span>](types.md) Adds torque to an object in a rotational Vector.

!!!info "addTorque(vector, force_type)"
	* [<span class="tag vec"></span>](types.md) **vector**: A Vector of the direction and magnitude of rotational force.
	* [<span class="tag int"></span>](types.md) **force_type**: An Int representing the force type to apply. Options below.
		* {>>Optional, defaults to 3.<<}
        * **1**: Continuous force, uses mass. *(Force)*
        * **2**: Continuous acceleration, ignores mass. *(Acceleration)*
		* **3**: Instant force impulse, uses mass. *(Impulse)*
		* **4**: Instant velocity change, ignores mass. *(Velocity Change)*

---



####getBounds()

[<span class="ret vec"></span>](types.md) Returns a Table of Vector information describing the size of an object in Global terms. [Bounds](https://docs.unity3d.com/2019.1/Documentation/ScriptReference/Bounds.html) are part of Unity, and represent an imaginary square box that can be drawn around an object. Unlike scale, it can help indicate the size of an object in in-game units, not just relative model size.

!!!info "Return Table"
	* [<span class="tag tab"></span>](types.md) **center**: The Vector of the center of the bounding box.
	* [<span class="tag tab"></span>](types.md) **size**: The Vector of the size of the bounding box.
	* [<span class="tag tab"></span>](types.md) **offset**: The Vector of the offset of the center of the bounding box from the middle of the Object model.

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

[<span class="ret vec"></span>](types.md) Returns a Table of Vector information describing the size of an object in Global terms, as if it was rotated to {0,0,0}. [Bounds](https://docs.unity3d.com/2019.1/Documentation/ScriptReference/Bounds.html) are part of Unity, and represent an imaginary square box that can be drawn around an object. Unlike scale, it can help indicate the size of an object in in-game units, not just relative model size.

!!!info "Return Table"
	* [<span class="tag tab"></span>](types.md) **center**: The Vector of the center of the bounding box.
	* [<span class="tag tab"></span>](types.md) **size**: The Vector of the size of the bounding box.
	* [<span class="tag tab"></span>](types.md) **offset**: The Vector of the offset of the center of the bounding box from the middle of the Object model.

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

[<span class="ret vec"></span>](types.md) Returns a Vector of the current scale. Scale is not an absolute measurement, it is a multiple of the Object's default model size. So {x=2, y=2, z=2} would be a model twice its default size, not 2 units large.

---


####getTransformForward()

[<span class="ret vec"></span>](types.md) Returns a Vector of the forward direction of this Object. The direction is relative to how the object is facing.

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

[<span class="ret vec"></span>](types.md) Returns a Vector of the forward direction of this object. The direction is relative to how the object is facing.

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

[<span class="ret vec"></span>](types.md) Returns a Vector of the up direction of this Object. The direction is relative to how the object is facing.

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

[<span class="ret vec"></span>](types.md) Returns a Vector after converting a world vector to a local Vector. A world Vector is a positional Vector using the world's coordinate system. A Local Vector is a positional Vector that is relative to the position of the given object.

!!!tip "Object Scale"
	This function takes the Object's scale into account, as the Object is the key relative point.

!!!info "positionToLocal(vector)"
	* [<span class="tag vec"></span>](types.md) **vector**: The world position to convert into a local position.

---


####positionToWorld(...)

[<span class="ret vec"></span>](types.md) Returns a Vector after converting a local Vector to a world Vector. A world Vector is a positional Vector using the world's coordinate system. A Local Vector is a positional Vector that is relative to the position of the given object.

!!!tip "Object Scale"
	This function takes the Object's scale into account, as the Object is the key relative point.

!!!info "positionToLocal(vector)"
	* [<span class="tag vec"></span>](types.md) **vector**: The local position to convert into a world position.

---


####rotate(...)

[<span class="ret boo"></span>](types.md) Rotates Object smoothly in the direction of the given Vector. This does not set the Object to face a specific rotation, it rotates the Object around by the number of degrees given for x/y/z.

!!!info "rotate(vector)"
	* [<span class="tag vec"></span>](types.md) **vector**: The amount of x/y/z to rotate by.

``` Lua
--Rotates object 90 degrees around its Y axis
self.rotate({x=0, y=90, z=0})
```

---


####scale(...)

[<span class="ret boo"></span>](types.md) Scales Object by a multiple. This does not set the Object to a specific scale, it scales the Object by the given multiple.

!!!info "scale(scale)"
	* [<span class="tag vec"></span>](types.md#vector) **scale**: Multiplier for scale.
		* {>>{x=1, y=1, z=1} would not change the scale.<<}
!!!info "scale(scale)"
	* [<span class="tag flo"></span>](types.md) **scale**: Multiplier for scale which is applied to the X/Y/Z.
		* {>>1 would not change the scale.<<}

``` Lua
-- Both examples work to scale an object to be twice its current scale
self.scale({x=2, y=2, z=2})
self.scale(2)
```

---


####setPositionSmooth(...)

[<span class="ret boo"></span>](types.md) Moves the Object smoothly to the given Vector.

!!!info "setPositionSmooth(vector, collide, fast)"
	* [<span class="tag vec"></span>](types.md) **vector**: A positional Vector.
	* [<span class="tag boo"></span>](types.md) **collide**: If the Object will collide with other Objects while moving.
	* [<span class="tag boo"></span>](types.md) **fast**: If the Object is moved quickly.

---


####setRotationSmooth(...)

[<span class="ret boo"></span>](types.md) Rotates the Object smoothly to the given Vector.

!!!info "setRotationSmooth(vector, collide, fast)"
	* [<span class="tag vec"></span>](types.md) **vector**: A rotational Vector.
	* [<span class="tag boo"></span>](types.md) **collide**: If the Object will collide with other Objects while rotating.
	* [<span class="tag boo"></span>](types.md) **fast**: If the Object is rotated quickly.

---


















###UI Function Details

####createButton(...)

[<span class="ret boo"></span>](types.md) Creates a scripted button attached to the Object. Scripted buttons are buttons that can be clicked while in-game that trigger a function in a script.

???tip "Button Tips"
	* Buttons can not be clicked from their back side.
	* Buttons can not be clicked if there is another object between the pointer and the button. This does not include the Object the button is attached to.
	* Buttons are placed relative to the Object they are attached to.
	* The maximum font size is capped at 1000.
	* The minimum width/height is 60. Any lower number (besides 0) will appear to be 60. This prevents visual glitches involving the corner rounding.
	* A button width/height of 0 will cause the button not to be drawn, but its label will be. This can be a way to attach text to an Object.
	* You cannot assign an index to a button. It is given one automatically.

!!!info "createButton(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the information used to spawn the button.
		* [<span class="tag str"></span>](types.md) **parameters.click_function**: A String of the function's name that will be run when button is clicked.
		* [<span class="tag str"></span>](types.md) **parameters.function_owner**: The Object which contains the click_function function.
			* {>>Optional, Defaults to Global.<<}
		* [<span class="tag str"></span>](types.md) **parameters.label**: Text that appears on the button.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Where the button appears, relative to the Object's center.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: How the button is rotated, relative to the Object's rotation.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the button, relative to the Object's scale.
			* {>>Optional, defaults to {x=1, y=1, z=1}.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.width**: How wide the button will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.height**: How tall the button will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.font_size**: Size the label font will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.color**: A Color for the clickable button.
			* {>>Optional, defaults to {r=1, g=1, b=1}.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.font_color**: A Color for the label text.
			* {>>Optional, defaults to {r=0, g=0, b=0}.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.hover_color**: A Color for the background during mouse-over.
			* {>>Optional.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.press_color**: A Color for the background when clicked.
			* {>>Optional.<<}
		* [<span class="tag str"></span>](types.md) **parameters.tooltip**: Popup of text, similar to how an Object's name is displayed on mouseover.
			* {>>Optional, defaults to an empty string.<<}

!!!info "click_function(obj, player_clicker_color, alt_click)"
	*The click function which is activated by clicking this button has its own parameters it is passed automatically.*

	* [<span class="tag obj"></span>](types.md) **obj**: The Object the button is attached to.
	* [<span class="tag str"></span>](types.md) **player_clicker_color**: [Player Color](player-color.md) of the player that pressed the button.
	* [<span class="tag boo"></span>](types.md) **alt_click**: True if a button other than left-click was used to click the button.

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

function click_func(obj, color, alt_click)
	print(obj)
	print(color)
	print(alt_click)
end
```

!!!bug
	Button scale currently distorts button height and width if the button is rotated at anything besides `{0,0,0}`.

---


####createInput(...)

[<span class="ret boo"></span>](types.md) Creates a scripted input attached to the Object. Scripted inputs are boxes you can click inside of in-game to input/edit text. Every letter typed triggers the function. The bool that is returned as part of the input_function allows you to determine when a player has finished editing the input.

???tip "Input Tips"
	* Inputs can not be clicked from their back side.
	* Inputs can not be clicked if there is another object between the pointer and the inputs. This does not include the Object the input is attached to.
	* Inputs are placed relative to the Object they are attached to.
	* The maximum font size is capped at 1000.
	* The minimum width/height is 60. Any lower number (besides 0) will appear to be 60. This prevents visual glitches involving the corner rounding.
	* Font that does not fit in the input window's width/height does NOT display. To know how much height you need for each line, the formula is `(font_size * # of lines) + 23`. In other words, multiply how many lines of text you want to display by your font_size and add 23. That is your height value.
	* You cannot assign an index to an input. It is given one automatically.

!!!info "createInput(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the information used to spawn the input.
		* [<span class="tag str"></span>](types.md) **parameters.input_function**: A String of the function's name that will be run when a key is used or when it is deselected.
		* [<span class="tag obj"></span>](types.md) **parameters.function_owner**: The Object which contains the input_function function.
			* {>>Optional, Defaults to Global.<<}
		* [<span class="tag str"></span>](types.md) **parameters.label**: Text that appears as greyed out text when there is no value in the input.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Where the input appears, relative to the Object's center.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: How the input is rotated, relative to the Object's rotation.
			* {>>Optional, defaults to {x=0, y=0, z=0}.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the input, relative to the Object's scale.
			* {>>Optional, defaults to {x=1, y=1, z=1}.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.width**: How wide the input will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.height**: How tall the input will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag flo"></span>](types.md) **parameters.font_size**: Size the label/value font will be, relative to the Object.
			* {>>Optional, defaults to 100.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.color**: A Color for the input's background.
			* {>>Optional, defaults to {r=1, g=1, b=1}.<<}
		* [<span class="tag col"></span>](types.md#color) **parameters.font_color**: A Color for the value text.
			* {>>Optional, defaults to {r=0, g=0, b=0}.<<}
		* [<span class="tag str"></span>](types.md) **parameters.tooltip**: A popup of text, similar to how an Object's name is displayed on mouseover.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag int"></span>](types.md) **parameters.alignment**: How text is aligned in the input box.
			* {>>Optional, defaults to 1.<<}
			* **1**: Automatic
			* **2**: Left
			* **3**: Center
			* **4**: Right
			* **5**: Justified
		* [<span class="tag str"></span>](types.md) **parameters.value**: Text entered into the input.
			* {>>Optional, defaults to an empty string.<<}
		* [<span class="tag int"></span>](types.md) **parameters.validation**: What characters can be input into the input value field.
			* {>>Optional, defaults to 1.<<}
			* **1**: None
			* **2**: Integer
			* **3**: Float
			* **4**: Alphanumeric
			* **5**: Username
			* **6**: Name
		* [<span class="tag int"></span>](types.md) **parameters.tab**: How the pressing of "tab" is handled when inputting.
			* {>>Optional, defaults to 1.<<}
			* **1**: None
			* **2**: Select Next Input
			* **3**: Indent

!!!info "input_function(obj, player_clicker_color, input_value, selected)"
	*The click function which is activated by editing the text in this input has its own parameters it is passed automatically.*

	* [<span class="tag obj"></span>](types.md) **obj**: The Object the input is attached to.
	* [<span class="tag str"></span>](types.md) **player_clicker_color**: [Player Color](player-color.md) of the player that has selected/edited the input.
	* [<span class="tag str"></span>](types.md) **input_value**: Text currently in the input.
	* [<span class="tag boo"></span>](types.md) **selected**: If the value box is still being edited or not.

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

[<span class="ret boo"></span>](types.md) Modify an existing button. The only parameter that is required is the index. The rest are optional, and not using them will cause the edited button's element to remain. Indexes start at 0. The first button on any given Object has an index of 0, the next button on it has an index of 1, etc. Each Object has its own indexes.

!!!info "editButton(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the information used to spawn the button.
		* [<span class="tag int"></span>](types.md) **parameters.index**: Index of the button you want to edit.
		* [<span class="tag str"></span>](types.md) **parameters.click_function**: Function's name that will be run when button is clicked.
		* [<span class="tag obj"></span>](types.md) **parameters.function_owner**: The Object which contains the click_function function.
		* [<span class="tag str"></span>](types.md) **parameters.label**: Text that appears on the button.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Where the button appears, relative to the Object's center.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: How the button is rotated, relative to the Object's rotation.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the button, relative to the Object's scale.
		* [<span class="tag flo"></span>](types.md) **parameters.width**: How wide the button will be, relative to the Object.
		* [<span class="tag flo"></span>](types.md) **parameters.height**: How tall the button will be, relative to the Object.
		* [<span class="tag flo"></span>](types.md) **parameters.font_size**: Size the label font will be, relative to the Object.
		* [<span class="tag col"></span>](types.md#color) **parameters.color**: A Color for the clickable button.
		* [<span class="tag col"></span>](types.md#color) **parameters.font_color**: A Color for the label text.
		* [<span class="tag col"></span>](types.md#color) **parameters.hover_color**: A Color for the background during mouse-over.
		* [<span class="tag col"></span>](types.md#color) **parameters.press_color**: A Color for the background when clicked.
		* [<span class="tag str"></span>](types.md) **parameters.tooltip**: Text of a popup of text, similar to how an Object's name is displayed on mouseover.

``` Lua
self.editButton({index=0, label="New Label"})
```

---


####editInput(...)

[<span class="ret boo"></span>](types.md) Modify an existing input. The only parameter that is required is the index. The rest are optional, and not using them will cause the edited input's element to remain. Indexes start at 0. The first input on any given Object has an index of 0, the next input on it has an index of 1, etc. Each Object has its own indexes.

!!!info "editInput(parameters)"
	*All fields besides `index` are optional. If not used, the element will default to the element's current setting.*

	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the information used to spawn the input.
		* [<span class="tag int"></span>](types.md) **parameters.index**: Index of the input you want to edit.
		* [<span class="tag str"></span>](types.md) **parameters.input_function**: The function's name that will be run when the input is selected.
		* [<span class="tag obj"></span>](types.md) **parameters.function_owner**: The Object which contains the input_function function.
		* [<span class="tag str"></span>](types.md) **parameters.label**: Text that appears as greyed out text when there is no value in the input.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Where the input appears, relative to the Object's center.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: How the input is rotated, relative to the Object's rotation.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the input, relative to the Object's scale.
		* [<span class="tag flo"></span>](types.md) **parameters.width**: How wide the input will be, relative to the Object.
		* [<span class="tag flo"></span>](types.md) **parameters.height**: How tall the input will be, relative to the Object.
		* [<span class="tag flo"></span>](types.md) **parameters.font_size**: Size the label/value font will be, relative to the Object.
		* [<span class="tag col"></span>](types.md#color) **parameters.color**: A Color for the input's background.
		* [<span class="tag col"></span>](types.md#color) **parameters.font_color**: A Color for the value text.
		* [<span class="tag str"></span>](types.md) **parameters.tooltip**: A popup of text, similar to how an Object's name is displayed on mouseover.
		* [<span class="tag int"></span>](types.md) **parameters.alignment**: How text is aligned in the input box.
			* **1**: Automatic
			* **2**: Left
			* **3**: Center
			* **4**: Right
			* **5**: Justified
		* [<span class="tag str"></span>](types.md) **parameters.value**: A String of the text entered into the input.
		* [<span class="tag int"></span>](types.md) **parameters.validation**: An Int which determines what characters can be input into the value.
			* **1**: None
			* **2**: Integer
			* **3**: Float
			* **4**: Alphanumeric
			* **5**: Username
			* **6**: Name
		* [<span class="tag int"></span>](types.md) **parameters.tab**: An Int which determines how pressing tab is handled when inputting.
			* **1**: None
			* **2**: Select Next Input
			* **3**: Indent

``` Lua
self.editInput({index=0, value="New Value"})
```

---


####getButtons()

[<span class="ret tab"></span>](types.md) Returns a Table of all buttons on this Object. The Table contains parameters tables with the same keys as seen in the [createButton](#createbutton) section, except each Table of parameters also contains an __index__ entry. This is used to identify each button, used by [editButton](#editbutton) and [removeButton](#removebutton).

Indexes start at 0.

---


####getInputs()

[<span class="ret tab"></span>](types.md) Returns a Table of all inputs on this Object. The Table contains parameters tables with the same keys as seen in the [createInput](#createinput) section, except each Table of parameters also contains an __index__ entry. This is used to identify each input, used by [editInput](#editinput) and [removeInput](#removeinput).

Indexes start at 0.

---


####removeButton(...)

[<span class="ret boo"></span>](types.md) Removes a specific button. Indexes start at 0. The first button on any given Object has an index of 0, the next button on it has an index of 1, etc. Each Object has its own indexes.

Removing an index instantly causes all other higher indexes to shift down 1.

!!!info "removeButton(index)"
	* [<span class="tag int"></span>](types.md) **index**: Button index to remove.

---


####removeInput(...)

[<span class="ret boo"></span>](types.md) Removes a specific input. Indexes start at 0. The first input on any given Object has an index of 0, the next input on it has an index of 1, etc. Each Object has its own indexes.

Removing an index instantly causes all other higher indexes to shift down 1.

!!!info "removeInput(index)"
	* [<span class="tag int"></span>](types.md) **index**: Input index to remove.

---



















###Get Function Details







####getCustomObject()

[<span class="ret tab"></span>](types.md) Returns a Table with the Custom Object information of a Custom Object. See the [Custom Game Objects](custom-game-objects.md) page for the kind of information returned.

``` Lua
-- Example returned Table for a custom token
{
	image = "SOME URL HERE",
	thickness = 0.2,
	merge_distance = 15,
	stackable = false,
}
```

!!!tip "Jigsaw Puzzles"
	If you use getCustomObject() on a puzzle piece, it will also return `desired_position`, which is its position if the puzzle is "solved". You can use this to determine where to put the piece.

---


####getFogOfWarReveal()

[<span class="ret tab"></span>](types.md) Settings impacting [Fog of War](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone) being revealed. In the example returned table, these are the default values of any object.

!!!note "Color Selection"
	"Black" and "All" are synonymous for Fog of War. Either means that all players can see the revealed area when `reveal = true`.


``` Lua
-- Example returned Table for a custom token
{
	reveal = false,
	color = 'All',
	range = 5
}
```

---


####getJoints()
[<span class="ret tab"></span>](types.md) Returns information on any joints attached to this object. This information included the GUID of the other objects attached via the joints.

This function returns a table of sub-tables, each sub-table representing one joint.

Example of a return table of an object with 2 joints:
``` Lua
{
	{
		type              = "Spring",
		joint_object_guid = "555555",
		collision         = false,
		break_force       = 1000,
		break_torgue      = 1000,
		axis              = {0,0,0},
		anchor            = {0,0,0},
		connector_anchor  = {0,0,0},
		motor_force       = 0,
		motor_velocity    = 0,
		motor_free_spin   = false,
		spring            = 50,
		damper            = 0.1
		max_distance      = 10
		min_distance      = 0
	},
	{
		type              = "Spring",
		joint_object_guid = "888888",
		collision         = false,
		break_force       = 1000,
		break_torgue      = 1000,
		axis              = {0,0,0},
		anchor            = {0,0,0},
		connector_anchor  = {0,0,0},
		motor_force       = 0,
		motor_velocity    = 0,
		motor_free_spin   = false,
		spring            = 50,
		damper            = 0.1
		max_distance      = 10
		min_distance      = 0
	},
}
```

Example of printing the first sub-table's information:
``` Lua
local jointsInfo = self.getJoints()
for k, v in pairs(jointsInfo[1]) do
	print(k, ":  ", v)
end
```

---



####getObjects()

[<span class="ret var"></span>](types.md) Returns data describing the objects contained within in the zone/bag/deck.

The format of the data returned depends on the kind of object.

#####Containers (Bags/Decks) {: #getobjects-containers }

Containers return a (numerically indexed) table consisting of sub-tables that each have the following properties:

Name | Type | Description
-- | -- | --
description | [<span class="tag str"></span>](types.md) | [Description](#getdescription) of the contained object.
gm_notes | [<span class="tag str"></span>](types.md) | [GM Notes](#getgmnotes) on the contained object.
guid | [<span class="tag str"></span>](types.md) | [GUID](#guid) of the contained object.
index | [<span class="tag int"></span>](types.md) | Index of the contained object, represents the item's order in the container.
lua_script | [<span class="tag str"></span>](types.md) | [Lua script](#script_code) on the contained object.
lua_script_state | [<span class="tag str"></span>](types.md) | [Lua script saved state](#script_state) of the contained object.
memo | [<span class="tag str"></span>](types.md) | [Memo](#memo) on the contained object.
name | [<span class="tag str"></span>](types.md) | <p>Name of the contained object.</p><p>Will correspond with [getName()](#getname), unless it's blank, in which case it'll be the [internal resource name](#name).</p>
nickname | [<span class="tag str"></span>](types.md) | <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use `name`_.</p>[Name](#getname) of the item.
tags | [<span class="tag tab"></span>](types.md) | A table of [<span class="tag str"></span>](types.md) representing the [tags](#gettags) on the contained object.

!!!example
	Find a contained object with the name "Super Card" (within the Bag/Deck `object`), and use its index to
	[take the object out](#takeobject) of the container.
	```lua
	-- Iterate through each contained object
	for _, containedObject in ipairs(object.getObjects()) do
		if containedObject.name == "Super Card" then
			object.takeObject({
				index = containedObject.index
			})
			break -- Stop iterating
		end
	end
	```

#####Zones {: #getobjects-zones }

Zones return a (numerically indexed) table of game Objects occupying the zone.

!!!important
	If the zone has <a href="#gettags">tags</a>, then only objects with compatible tags will be considered "occupying"
	the zone.

!!!example
	[Highlight](#highlighton) red all cards occupying a zone (`object`).
	```lua
	-- Iterate through object occupying the zone
	for _, occupyingObject in ipairs(object.getObjects()) do
		if occupyingObject.type == "Card" then
			occupyingObject.highlightOn('Red')
		end
	end
	```

---

####getRotationValue()

[<span class="ret var"></span>](types.md) Returns the current rotationValue. Rotation values are used to give value to different rotations (like dice) and are set using scripting or the Gizmo tool. The value returned is for the rotation that is closest to being pointed "up".

The returned value will either be a number or a string, depending on the value that was given to that rotation.

``` Lua
local value = self.getRotationValue()
print(value)
```


---


####getRotationValues()

[<span class="ret tab"></span>](types.md) Returns a Table of rotation values. Rotation values are used to give value to different rotations (like dice) based on which side is pointed "up". It works by checking all of the rotation values assigned to an object and determining which one of them is closest to pointing up, and then displaying the value associated with that rotation.

You can manually assign rotation values to objects using the Rotation Value Gizmo tool (in the left side Gizmo menu) or using [setRotationValues(...)](#setrotationvalues).

!!!info "Return Table"
	The returned Table contains sub-Tables, each sub-Table containing these 2 key/value pairs.

	* [<span class="tag var"></span>](types.md) **value**: What value is associated with a given rotation. Often a String or Int.
		* {>>Starting a value with a # will cause it not to show in the Object's tooltip.<<}
	* [<span class="tag vec"></span>](types.md#vector) **rotation**: Rotation of the Object that best represents the given value pointing up.

``` Lua
-- Example returned Table for a coin
{
	{value="Heads", rotation={x=0, y=0, z=0}},
	{value="Tails", rotation={x=180, y=0, z=0}},
}
```

---




####getStates()

[<span class="ret tab"></span>](types.md) Returns a Table of information on the [states](https://kb.tabletopsimulator.com/host-guides/creating-states/) of an Object. Stated Objects have ids (indexes) starting with 1.

!!!tip "The returned table will **NOT** include data on the current state."

!!!info "Return Table"
	Returns a table of sub-tables. Each sub-table represents one other state.

	* [<span class="tag str"></span>](types.md) **name**: Name of the item.
	* [<span class="tag str"></span>](types.md) **description**: Description of the item.
	* [<span class="tag str"></span>](types.md) **guid**: GUID of the item.
	* [<span class="tag int"></span>](types.md) **id**: Index of the item, represents the item's order in the states.
	* [<span class="tag str"></span>](types.md) **lua_script**: Any Lua scripting saved on the item.
	* [<span class="tag str"></span>](types.md) **lua_script_state**: Any JSON save data on this item.
	* {>>nickname: A duplicate of the "name" field.<<}
		* {>>This is for backwards compatibility purposes only.<<}

``` Lua
-- Example returned Table
{
	{
		name             = "First State",
		description      = "",
		guid             = "AAA111",
		id               = 1,
		lua_script       = "",
		lua_script_state = "",
	},
	{
		name             = "Second State",
		description      = "",
		guid             = "BBB222",
		id               = 2,
		lua_script       = "",
		lua_script_state = "",
	},
}
```

---


####getValue()

[<span class="ret var"></span>](types.md)  Returns the Object's value. This represents something different depending on the Object's [type](#type).

!!!important
	If the Object has [rotation values](#getrotationvalues), then this method will return the rotation value i.e. behave
	the same as [getRotationValue()](#getrotationvalue).

See [setValue(...)](#setvalue) for more information.


###Set Function Details


####setCustomObject(...)

[<span class="ret boo"></span>](types.md) Sets a custom Object's properties. It can be used after [spawnObject](base.md#spawnobject) or on an already existing custom Object. If used on an already existing custom Object, you must use [reload](#reload) on the object after setCustomObject for the changes to be displayed.

!!!info "setCustomObject(parameters)"
	The Table of parameters varies, depending on which type of custom Object it is. See the [Custom Game Objects](custom-game-objects.md) page for the parameters needed.

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



####setFogOfWarReveal(...)

[<span class="ret boo"></span>](types.md) Establish the settings and enable/disable an Object's revealing of [Fog of War](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone).

!!!info "setFogOfWarReveal(fog_settings)"
	* [<span class="tag tab"></span>](types.md) **fog_settings**: A Table containing information on if/how this Object should reveal Fog of War.
		* [<span class="tag boo"></span>](types.md) **reveal**: Can the Object currently
			* {>>If this is not used, the current setting for this Object is kept.<<}
		* [<span class="tag str"></span>](types.md#vector) **color**: The rotation Vector of the Object that best represents the given value pointing up.
			* {>>If this is not used, the current setting for this Object is kept.<<}
			* {>>"Black" means "visible to all players."<<}
			* {>>"All" means "visible to all players."<<}
		* [<span class="tag flo"></span>](types.md#vector) **range**: How far from the Object the reveal effect reaches (radius, inches).
			* {>>If this is not used, the current setting for this Object is kept.<<}

``` Lua
-- Example of enabling reveal for all players at 3 units of radius.
params = {
	reveal = true,
	color  = "Black",
	range  = 3,
}
self.setFogOfWarReveal(params)
```

---

####setRotationValue(...)

Sets the Object's rotation value i.e. physically rotates the object.

!!!info "setRotationValue(rotation_value)"
	* [<span class="tag var"></span>](types.md) **rotation_value**: A [rotation value](#getrotationvalues). Should be a [<span class="tag int"></span>](types.md), [<span class="tag str"></span>](types.md) or [<span class="tag flo"></span>](types.md).

The Object will be elevated (smooth moved upward), smoothly rotated to the rotation corresponding with the specified `rotation_value` and then released to fall back into place.

!!!example
	Rotate a die to show the value 6.
	```lua
	die.setRotationValue(6)
	```

---

####setRotationValues(...)

[<span class="ret boo"></span>](types.md) Sets rotation values of an object. Rotation values are used to give value to different rotations (like dice). It works by checking all of the rotation values assigned to an object and determining which one of them is closest to pointing up, and then displaying the value associated with that rotation.

!!!info "setRotationValues(rotation_values)"
	* [<span class="tag tab"></span>](types.md) **rotation_values**: A Table containing Tables with the following values. 1 sub-Table per "face".
		* [<span class="tag var"></span>](types.md) **value**: Value associated with the rotation. Should be a [<span class="tag int"></span>](types.md), [<span class="tag str"></span>](types.md) or [<span class="tag flo"></span>](types.md).
			* {>>If `value` is a string starting with "#", then it will not be displayed in the Object's tooltip.<<}
		* [<span class="tag vec"></span>](types.md#vector) **rotation**: The rotation of the Object that corresponds with the provided `value`.

!!!example
	Set the two different sides (rotations) of a coin to have the values "Heads" and "Tails".
	```lua
	self.setRotationValues({
		{
			value="Heads",
			rotation={x=0, y=0, z=0}
		},
		{
			value="Tails",
			rotation={x=180, y=0, z=0}
		},
	})
	```

---

####setValue(...)

[<span class="ret boo"></span>](types.md) Sets the Object's value. This represents something different depending on the Object's [type](#type).

!!!important
	If the Object has [rotation values](#getrotationvalues), then this method will set the rotation value i.e. behave
	the same as [setRotationValue(...)](#setrotationvalue).

[Object Type](#type) | Value Type | Description
-- | -- | --
`3D Text` | [<span class="tag str"></span>](types.md) | Replaces the 3D Text's content.
`Clock` | [<span class="tag int"></span>](types.md) | Sets the remaining "Stopwatch" time (in seconds) on the Clock.
`Counter` (Digital Counter) | [<span class="tag int"></span>](types.md) | Sets the counter's value.
`Fog` (Hidden Zone) | [<span class="tag str"></span>](types.md) | Changes the hidden zone owner to the specified [Player Color](player-color.md).
`Hand` (Hand Zone) | [<span class="tag str"></span>](types.md) | Changes the hand owner to the specified [Player Color](player-color.md).
`Tablet` | [<span class="tag str"></span>](types.md) | Loads the specified URL in the tablet's browser.

---

###Action Function Details

####addContextMenuItem(...)

[<span class="ret boo"></span>](types.md) Adds a menu item to the objects right-click context menu.

!!!info "addContextMenuItem(label, toRunFunc, keep_open)"
	* [<span class="tag str"></span>](types.md) **label**: Label for the menu item.
	* [<span class="tag fun"></span>](types.md) **toRunFunc**: Execute if menu item is selected.
        * [<span class="tag str"></span>](types.md) **player_color** [Player Color](player-color.md) who selected the menu item.
	* [<span class="tag boo"></span>](types.md) **keep_open**: Keep context menu open after menu
     item was selected.
        * {>>Optional, Default: keep_open = false. Close context menu after selection.<<}

``` Lua
function onLoad()
    self.addContextMenuItem("doStuff", itemAction)
end

function itemAction(player_color)
    print(player_color)
end
```

---

####clone(...)

[<span class="ret obj"></span>](types.md) Copy/Paste this Object.

!!!info "clone(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table with information used when pasting.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Where the Object is placed.
			* {>>Optional, defaults to {x=0, y=3, z=0}.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.snap_to_grid**: If the Object snaps to grid.
			* {>>Optional, defaults to false.<<}

---



####cut(...)

[<span class="ret tab"></span>](types.md) Cuts (splits) a deck down to a given card. In other words, it counts down from the top of the deck and makes a new deck of that size and puts the remaining cards in the other pile.

After the cut, the resulting decks much each have at least 2 cards. This means the parameter used must be between **2** and **totalNumberOfCards - 2**.

!!!important
	New decks take a frame to be created. This means trying to act on them immediately will not work. Use a coroutine or timer to add a delay.

!!!info "cut(count)"
	* [<span class="tag int"></span>](types.md) **count**: How many cards down to cut the deck.
		* {>>Optional, if no value is provided the deck is cut in half.<<}

!!!info "Returned table"
	* [<span class="tag tab"></span>](types.md) The table that is returned
		* [<span class="tag obj"></span>](types.md) **1**: The lower deck, containing the remaining cards in the deck.
		* [<span class="tag obj"></span>](types.md) **2**: The upper deck, containing *count* number of cards.

```Lua
newDecks = deck.cut(5)
--A delay would be required here for these next two lines to work.
--The decks haven't been fully created yet.
newDecks[1].deal(1)
newDecks[2].deal(1)
```







####deal(...)

[<span class="ret boo"></span>](types.md) Deals Objects to hand zones. Will deal from decks/bags/stacks as well as individual items. If dealing an individual item to a hand zone, it is a good idea to make sure that its [Member Variable](#member-variables) for `use_hands` is `true`.

!!!info "deal(number, player_color, index)"
	* [<span class="tag int"></span>](types.md) **number**: How many to deal.
	* [<span class="tag str"></span>](types.md) **player_color**: The [Player Color](player-color.md) to deal to.
		* {>>Optional, defaults to an empty string. If not supplied, it will attempt to deal to all seated players.<<}
	* [<span class="tag int"></span>](types.md) **index**: Index of hand zone to deal to.
		* {>>Optional, defaults to the first created hand zone.<<}

---


####dealToColorWithOffset(...)

[<span class="ret obj"></span>](types.md) Deals from a deck to a position relative to the hand zone.

!!!info "dealToColorWithOffset(offset, flip, player_color)"
	* [<span class="tag vec"></span>](types.md#vector) **offset**: The x/y/z offset to deal to around the given hand zone.
	* [<span class="tag boo"></span>](types.md) **flip**: If the card is flipped over when dealt.
	* [<span class="tag str"></span>](types.md) **player_color**: Hand zone [Player Color](player-color.md) to offset dealing to.

``` Lua
-- Example of dealing 2 cards in front of the White player, face up.
self.dealToColorWithOffset({-2,0,5}, true, "White")
self.dealToColorWithOffset({ 2,0,5}, true, "White")
```

---


####jointTo(...)

[<span class="ret boo"></span>](types.md) Joints objects together, in the same way the Joint tool does.

**Using obj.jointTo(), with no object or parameter used as arguments, will remove all joints from that Object.**

!!!info "jointTo(object, parameters)"
	* [<span class="tag obj"></span>](types.md) **object**: The Object that the selected object will be jointed to.
	* [<span class="tag tab"></span>](types.md) **parameters**: A table of parameters. Which parameters depends on the joint type. See below for more.
	* {>>All parameters have defaults, the same as the Joint Tool.<<}

Example of Fixed:
```Lua
self.jointTo(obj, {
	["type"]        = "Fixed",
	["collision"]   = true,
	["break_force"]  = 1000.0,
	["break_torgue"] = 1000.0,
})
```

Example of Spring:
```Lua
self.jointTo(obj, {
	["type"]        = "Spring",
	["collision"]   = false,
	["break_force"]  = 1000.0,
	["break_torgue"] = 1000.0,
	["spring"]      = 50,
	["damper"]      = 0.1,
	["max_distance"] = 10,
	["min_distance"] = 1
})
```

Example of Hinge:
```Lua
self.jointTo(obj, {
	["type"]        = "Hinge",
	["collision"]   = true,
	["axis"]        = {1,1,1},
	["anchor"]      = {1,1,1},
	["break_force"]  = 1000.0,
	["break_torgue"] = 1000.0,
	["motor_force"]  = 100.0,
	["motor_velocity"] = 10.0,
	["motor_free_spin"] = true
})
```

---


####putObject(...)

[<span class="ret obj"></span>](types.md) Places an object into a container (chip stacks/bags/decks). If neither Object is a container, but they are able to be combined (like with 2 cards), then they form a deck/stack.

!!! info "putObject(put_object)"
	  * [<span class="tag obj"></span>](types.md) **put_object**: An Object to place into the container.

!!! info "Returned Object"
    The container is returned as the Object reference. Either this is the container/deck/stack the other Object was placed into, or the deck/stack that was formed by the putObject action.

!!! info "Putting Cards into Decks"
    When you call this `putObject()` to put a card into a deck, the card goes into the end of the deck which is closest to it in Y elevation. So, if both the card and the deck are resting on the table, the card will be put at the bottom of the deck. if the card is hovering above the deck, it will be put at the top."

``` Lua
-- Example of a script on a bag that places Object into itself
local obj = getObjectFromGUID("AAA111")
self.putObject(obj)
```

---


####registerCollisions(...)

[<span class="ret boo"></span>](types.md) Registers this object for Global collision events, such as [onObjectCollisionEnter](event.md#onobjectcollisionenter). Always returns `true`.

!!!info "registerCollision(stay)"
	* [<span class="tag boo"></span>](types.md) **stay**: Whether we should register for [onObjectCollisionStay](event.md#onobjectcollisionstay). Stay events may negatively impact performance, only set this to `true` if absolutely necessary.
        * {>>Optional, defaults to `false`.<<}

---


####reload()

[<span class="ret obj"></span>](types.md) Returns Object reference of itself after it respawns itself. This function causes the Object to be deleted and respawned instantly to refresh it, so its old Object reference will no longer be valid.

Most often this is used after using [setCustomObject(...)](#setcustomobject) to modify a custom object.

---




####split(...)

[<span class="ret tab"></span>](types.md) Splits a deck, as evenly as possible, into a number of piles.

!!!important
	New decks take a frame to be created. This means trying to act on them immediately will not work. Use a coroutine or timer to add a delay.

!!!info "split(piles)"
	* [<span class="tag int"></span>](types.md) **piles**: How many piles to split the deck into.
		* {>>Optional, if no value is provided, it is split into two piles.<<}
		* {>>Minimum Value: 2<<}
		* {>>Maximum Value: Number-Of-Cards-In-Deck / 2<<}

!!!info "Returned table"
	The number of Objects in the table is equal to the number of decks created by the split. They are ordered so any larger decks come first.

	* [<span class="tag tab"></span>](types.md) The table that is returned
		* [<span class="tag obj"></span>](types.md) **1**: The first deck created
		* [<span class="tag obj"></span>](types.md) **2**: The second deck created
		* [<span class="tag obj"></span>](types.md) **3**: The third deck created (etc)

``` Lua
newDecks = deck.split(4)
--A delay would be required here for these next four lines to work.
--The decks haven't been fully created yet.
newDecks[1].deal(1)
newDecks[2].deal(1)
newDecks[3].deal(1)
newDecks[4].deal(1)

```




---
####spread(...)

[<span class="ret tab"></span>](types.md) Spreads the cards of a deck out on the table.

!!!important
	Cards take a frame to be created. This means trying to act on them immediately will not work. Use a coroutine or timer to add a delay.

!!!info "spread(distance)"
	* [<span class="tag flo"></span>](types.md) **distance**: How far apart should the cards be.
		* {>>Optional, if no value is provided, they will be 0.6 inches apart.<<}
		* {>> Negative values will spread to the left instead of the right.<<}

!!!info "Returned table"
	The number of Objects in the table is equal to the number of cards in the deck. They are returned in the order they were in the deck.

	* [<span class="tag tab"></span>](types.md) The table that is returned
		* [<span class="tag obj"></span>](types.md) **1**: The first card in the deck
		* [<span class="tag obj"></span>](types.md) **2**: The second card in the deck
		* [<span class="tag obj"></span>](types.md) **3**: The third card in the deck (etc)


---

####takeObject(...)

[<span class="ret obj"></span>](types.md) Takes an object out of a container (bag/deck/chip stack), returning a reference to the object that was taken.

Objects that are taken out of a container will take one or more frames to spawn.
Certain interactions (e.g. physics) will not be able to take place until the object has finished spawning.

!!!info "takeObject(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to determine how takeObject will act.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: A Vector of the position to place Object.
			* {>>Optional, defaults to container's position + 2 on the x axis.<<}
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: A Vector of the rotation of the Object.
			* {>>Optional, defaults to the container's rotation.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.flip**: If the Object is flipped over.
			* {>>Optional, defaults to false. Only used with decks, not bags/stacks.<<}
			* {>>If rotation is used, flip's Bool will be ignored.<<}
		* [<span class="tag str"></span>](types.md) **parameters.guid**: GUID of the Object to take.
			* {>>Optional, no default. Only use index or guid, never both.<<}
		* [<span class="tag int"></span>](types.md) **parameters.index**: Index of the Object to take.
			* {>>Optional, no default. Only use index or guid, never both.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.top**: If an object is taken from the top (vs bottom).
			* {>>Optional, defaults to true.<<}
		* [<span class="tag boo"></span>](types.md) **parameters.smooth**: If the taken Object moves smoothly or instantly.
			* {>>Optional, defaults to true.<<}
		* [<span class="tag fun"></span>](types.md#function) **parameters.callback_function**: Callback which will be called when the taken object has finished spawnning.
			* {>>Optional, no default.<<}
			* {>>This function takes a single parameter: the object that was taken.<<}

!!!caution
	Certain containers only exist whilst they have more than one object contained within them (e.g. decks). Once you
	remove the second last object from a container, the container will be destroyed and the remaining contained object
	will spawn in its place. After calling `takeObject(...)` you can check for a [remainder](#remainder).

!!!example
	Take an object out of a container. As we take it out we'll instruct the object to smooth move (default positioning
	behavior) to coordinates (0, 5, 0). Additionally, we're going to add a blue highlight on the object we've taken	out.
	``` Lua
	local takenObject = container.takeObject({
		position = {x = 0, y = 5, z = 0},
	})
	takenObject.highlightOn('Blue')
	```

!!!example "Advanced example"
	<p>Take an object out of a container, and then apply an upward force (impulse) shooting it into the air.</p>
	<p>We can only [apply an impulse](#addforce) to an object once its (underlying rigid body) has finished spawning
	Additionally, freshly spawned objects are frozen in place for a single frame. So we need to wait for the taken
	object to finish spawning (i.e. `callback_function`) _then_ [wait one more frame](wait.md#frames) before applying
	the impulse.</p>
	``` Lua
	container.takeObject({
		callback_function = function(spawnedObject)
			Wait.frames(function()
				-- We've just waited a frame, which has given the object time to unfreeze.
				-- However, it's also given the object time to enter another container, if
				-- it spawned on one. Thus, we must confirm the object is not destroyed.
				if not spawnedObject.isDestroyed() then
					spawnedObject.addForce({0, 30, 0})
				end
			end)
		end,
		smooth = false, -- Smooth moving objects cannot have forces applied to them.
	})
	```

---


####unregisterCollisions(...)

[<span class="ret boo"></span>](types.md) Unregisters this object for Global collision events. Returns `true` if the object was previously registered, `false` otherwise.

!!!info "unregisterCollision()"

---





###Hide Function Details

####setHiddenFrom(...)

[<span class="ret boo"></span>](types.md) Hides the Object from the specified players, as if it were in a hand zone.

Using an empty table will cause the Object to remove the hiding effect.

!!!info "setHiddenFrom(players)"
	* [<span class="tag tab"></span>](types.md) **players**: A table containing colors to hide the Object from.
		* [<span class="tag str"></span>](types.md) **(color_name)**: Strings of the color name of each player.

``` Lua
function onLoad()
    self.setHiddenFrom({"Blue", "White"})
end
```

!!!tip
	Just like Objects in a hand zone, the player/s the object is hidden from can still interact/move the hidden Object. It still exists to them, but is shown as a question mark or as a hidden card.

---



####setInvisibleTo(...)

[<span class="ret boo"></span>](types.md) Hides the Object from the specified players, as if it were in a hidden zone.

Using an empty table will cause the Object to remove the hiding effect.

!!!info "setInvisibleTo(players)"
	* [<span class="tag tab"></span>](types.md) **players**: A table containing colors to hide the Object from.
		* [<span class="tag str"></span>](types.md) **(color_name)**: Strings of the color name of each player.

``` Lua
function onLoad()
    self.setInvisibleTo({"Blue", "White"})
end
```

!!!tip
	Just like Objects in a hidden zone, the player/s the object is hidden from can still interact/move the hidden Object. It still exists to them, just invisibly so.

---


####attachHider(...)

[<span class="ret boo"></span>](types.md) A more advanced version of `setHiddenFrom(...)`, this function is also used to hide objects as if they were in a hand zone. It allows you to identify multiple sources of "hiding" by an ID and toggle the effect on/off easily.

This function is slightly more complicated to use for basic hiding, but allows for much easier hiding in complex situations.

!!!info "attachHider(id, hidden, players)"
	* [<span class="tag str"></span>](types.md) **id**: The unique name for this hiding effect.
		* {>>Tip: You can use descriptive tag names like "fog" or "blindness"<<}
	* [<span class="tag boo"></span>](types.md) **hidden**: If the hiding effect is enabled or not.
	* [<span class="tag tab"></span>](types.md) **players**: A table containing colors to hide the Object from.
		* {>>Optional, an empty table (or no table) hides for everyone.<<}
		* [<span class="tag str"></span>](types.md) **(color_name)**: Strings of the color name of each player.

``` Lua
function onLoad()
    --Enable hide
    self.attachHider("hide", true, {"Blue", "White"})
    --Disable hide
    --self.attachHider("hide", false, {"Blue", "White"})
end
```

!!!tip
	Just like Objects in a hand zone, the player/s the object is hidden from can still interact/move the hidden Object. It still exists to them, but is shown as a question mark or as a hidden card.

---


####attachInvisibleHider(...)

[<span class="ret boo"></span>](types.md) A more advanced version of `setInvisibleTo(...)`, this function is also used to hide objects as if they were in a hidden zone. It allows you to identify multiple sources of "hiding" by an ID and toggle the effect on/off easily.

This function is slightly more complicated to use for basic hiding, but allows for much easier hiding in complex situations.

!!!info "attachInvisibleHider(id, hidden, players)"
	* [<span class="tag str"></span>](types.md) **id**: The unique name for this hiding effect.
		* {>>Tip: You can use descriptive tag names like "fog" or "blindness"<<}
	* [<span class="tag boo"></span>](types.md) **hidden**: If the hiding effect is enabled or not.
	* [<span class="tag tab"></span>](types.md) **players**: A table containing colors to hide the Object from.
		* {>>Optional, an empty table (or no table) hides for everyone.<<}
		* [<span class="tag str"></span>](types.md) **(color_name)**: Strings of the color name of each player.

``` Lua
function onLoad()
    --Enable hide
    self.attachInvisibleHider("hide", true, {"Blue", "White"})
    --Disable hide
    --self.attachInvisibleHider("hide", false, {"Blue", "White"})
end
```

!!!tip
	Just like Objects in a hidden zone, the player/s the object is hidden from can still interact/move the hidden Object. It still exists to them, just invisibly so.

---















---


###Global Function Details

####addDecal(...)

[<span class="ret boo"></span>](types.md) Add a Decal onto an object or the game world.

!!!tip "Relative Vectors"
	When using this function, the vector parameters (position, rotation) are relative to what the decal is being placed on. For example, if you put a decal at `{0,0,0}` on Global, it will attach to the center of the game room. If you do the same to an object, it will place the decal on the origin point of the object.

!!!info "addDecal(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to determine how the function will act.
		* [<span class="tag str"></span>](types.md) **parameters.name**: The name of the decal being placed.
		* [<span class="tag str"></span>](types.md) **parameters.url**: The file path or URL for the image to be displayed.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to place Object.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the Object.
		* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: How the image is scaled.
			* {>>1 is normal scale, 0.5 would be half sized, 2 would be twice as large, etc.<<}

``` Lua
function onLoad()
	local params = {
		name     = "API Icon",
		url      = "https://api.tabletopsimulator.com/img/TSIcon.png",
		position = {0, 5, 0},
		rotation = {90, 0, 0},
		scale    = {1, 1, 1},
	}
	Global.addDecal(params)
end
```


---


####call(...)

[<span class="ret var"></span>](types.md) Used to call a Lua function on another entity.

*Var is only returned if the function called has a `return`. Otherwise return is `nil`. See example.*

> This function can also be used directly on the game world using Global.

!!!info "call(func_name, func_params)"
	* [<span class="tag str"></span>](types.md) **func_name**: Function name you want to activate.
	* [<span class="tag tab"></span>](types.md) **func_params**: A Table containing any data you want to pass to that function.
		* {>>Optional, will not be sent by default.<<}

``` Lua
-- Call, used from an entity's script
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

####getDecals()

[<span class="ret tab"></span>](types.md) Returns a table of sub-tables, each sub-table representing one decal.

!!!info "Sub-table elements"

	* [<span class="tag str"></span>](types.md) **parameters.name**: The name of the decal being placed.
	* [<span class="tag str"></span>](types.md) **parameters.url**: The file path or URL for the image to be displayed.
	* [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to place Object.
	* [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the Object.
	* [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: How the image is scaled.
		* {>>1 is normal scale, 0.5 would be half sized, 2 would be twice as large, etc.<<}

Example returned table:
``` Lua
-- If this object had 2 of the same decal on it
decalTable = self.getDecals()

--[[ This is what the table would look like
{
	{
		name     = "API Icon",
		url      = "https://api.tabletopsimulator.com/img/TSIcon.png",
		position = {0, 5, 0},
		rotation = {90, 0, 0},
		scale    = {5, 5, 5}
	},
	{
		name     = "API Icon",
		url      = "https://api.tabletopsimulator.com/img/TSIcon.png",
		position = {0, 5, 0},
		rotation = {90, 0, 0},
		scale    = {5, 5, 5}
	},
}
]]--

-- Accessing the name of of the second entry would look like this
print(decalTable[2].name)
```

---


####getSnapPoints()

[<span class="ret tab"></span>](types.md) Returns a table of sub-tables, each sub-table representing one snap point.

> This function can also be used directly on the game world (game table) using Global.

!!!info "Format of the returned table"
	* [<span class="tag tab"></span>](types.md) A table containing numerically indexed sub-tables.
		* [<span class="tag tab"></span>](types.md) Sub-table(s), each representing a snap point:
			* [<span class="tag vec"></span>](types.md#vector) **position**: [Local Position](types.md#position) of the snap point. The position is relative to the entity's center.
			* [<span class="tag vec"></span>](types.md#vector) **rotation**: Local Rotation of the snap point. The rotation is relative to the entity's rotation.
			* [<span class="tag boo"></span>](types.md) **rotation_snap**: If the snap point is a "rotation" snap point.


Example:
```Lua
function onLoad()
	snapPointList = Global.getSnapPoints()
	log(snapPointsList)
end
```

Returned table:
```Lua
{
	{
		position = {2,2,2},
	    rotation = {0,90,0},
	    rotation_snap = false
	},
	{
		position = {5,2,5},
	    rotation = {0,0,0},
	    rotation_snap = true
	},
}
```

---

####setDecals(...)

[<span class="ret boo"></span>](types.md) Sets which decals are on an object. This removes other decals already present, and can remove all decals as well.

!!!tip "Removing decals"
	Using this function with an empty table will remove all decals from Global or the object it is used on.
	`Global.setDecals({})`

!!!info "setDecals(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: The main table, which will contain all of the sub-tables.
		* [<span class="tag tab"></span>](types.md) **subtable**: The sub-table containing each individual decal's information. The sub-tables are unnamed.
			* [<span class="tag str"></span>](types.md) **parameters.subtable.name**: The name of the decal being placed.
			* [<span class="tag str"></span>](types.md) **parameters.subtable.url**: The file path or URL for the image to be displayed.
			* [<span class="tag vec"></span>](types.md#vector) **parameters.subtable.position**: A Vector of the position to place Object.
			* [<span class="tag vec"></span>](types.md#vector) **parameters.subtable.rotation**: A Vector of the rotation of the Object.
			* [<span class="tag vec"></span>](types.md) **parameters.subtable.scale**: How the image is scaled.
				* {>>1 is normal scale, 0.5 would be half sized, 2 would be twice as large, etc.<<}

``` Lua
function onLoad()
    local parameters = {
        {
			name     = "API Icon",
			url      = "https://api.tabletopsimulator.com/img/TSIcon.png",
			position = {-2, 5, 0},
			rotation = {90, 0, 0},
			scale    = 5,
		},
        {
			name     = "API Icon",
			url      = "https://api.tabletopsimulator.com/img/TSIcon.png",
			position = {2, 5, 0},
			rotation = {90, 0, 0},
			scale    = 5,
		},
	}

	Global.setDecals(parameters)
end
```


---


####setSnapPoints(...)

[<span class="ret boo"></span>](types.md) Spawns snap points from a list of parameters.

> This function can also be used on the game world (game table) itself using Global.

!!!info "setSnapPoints(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A table containing numerically indexed sub-tables.
		* [<span class="tag tab"></span>](types.md) **sub-table**:
			* [<span class="tag vec"></span>](types.md#vector) **position**: [Local Position](types.md#position) of the snap point. This is relative to the entity's position.
				* {>>Optional, defaults to {0,0,0}.<<}
			* [<span class="tag vec"></span>](types.md#vector) **rotation**: Local Rotation of the snap point. This is relative to the entity's rotation.
				* {>>Optional, defaults to {0,0,0}.<<}
			* [<span class="tag boo"></span>](types.md) **rotation_snap**: If the snap point is a "rotation" snap point.
				* {>>Optional, defaults to false.<<}


```Lua
self.setSnapPoints({
	{
		position = {2,2,2},
	    rotation = {0,90,0},
	    rotation_snap = false
	},
	{
		position = {5,2,5},
	    rotation = {0,0,0},
	    rotation_snap = true
	},
})
```

---



####setVectorLines(...)

[<span class="ret boo"></span>](types.md) Spawns Vector Lines from a list of parameters.

> This function can also be used on the game world itself using Global.

!!!info "setVectorLines(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: The table containing each "line's" data. Each contiguous line has its own sub-table.
		* [<span class="tag tab"></span>](types.md) **points**: Table containing [Vector positions](types.md#vector) for each "point" on the line.
		* [<span class="tag col"></span>](types.md#color) **color**: Color the line will be.
			* {>>Optional, defaults to {1,1,1}.<<}
		* [<span class="tag flo"></span>](types.md) **thickness**: How thick the line is (in Unity units).
			* {>>Optional, defaults to default line size (0.1).<<}
		* [<span class="tag vec"></span>](types.md#vector) **rotation**: Rotation Vector for the line to be angled.
			* {>>Optional, defaults to {0,0,0}.<<}

``` Lua
function onLoad()
	--Make an X above the middle of the table
    Global.setVectorLines({
		{
			points    = { {5,1,5}, {-5,1,-5} },
			color     = {1,1,1},
			thickness = 0.5,
			rotation  = {0,0,0},
		},
		{
			points    = { {-5,1,5}, {5,1,-5} },
			color     = {0,0,0},
			thickness = 0.5,
			rotation  = {0,0,0},
		},
	})
end
```


---
