Player, a static global class, allows control over in-game players and their [hand zones](http://berserk-games.com/knowledgebase/hands/).

Example Usage: `Player["White"].seated` or `Player["Green"].mute()`


##Member Variables

Like [Object member variables](/object#member-variables), Player has its own member variables.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="admin"></a>admin | If the player is promoted or the host of the game. Read only. | [<span class="tag boo"></span>](/types)
<a class="anchor" id="blindfolded"></a>blindfolded | If the player is blindfolded. | [<span class="tag boo"></span>](/types)
<a class="anchor" id="color"></a>color | The player's [Player Color](/player-color). Read only. | [<span class="tag str"></span>](/types)
<a class="anchor" id="host"></a>host | If the player is the host. Read only. | [<span class="tag boo"></span>](/types)
<a class="anchor" id="lift_height"></a>lift_height | The lift height for the player. This is how far an object is raised when held in a player's hand. Value is ranged 0 to 1. | [<span class="tag flo"></span>](/types)
<a class="anchor" id="promoted"></a>promoted | If the current player is promoted. | [<span class="tag boo"></span>](/types)
<a class="anchor" id="seated"></a>seated | If a player is currently seated at this color. Read only. | [<span class="tag boo"></span>](/types)
<a class="anchor" id="steam_id"></a>steam_id | The Steam ID of the player. This is unique to each player's Steam account. Read only. | [<span class="tag str"></span>](/types)
<a class="anchor" id="steam_name"></a>steam_name | The Steam name of the player. Read only. | [<span class="tag str"></span>](/types)
<a class="anchor" id="team"></a>team | The team of the player.<br>Options: `"None", "Clubs", "Diamonds", "Hearts", "Spades", "Jokers"`. | [<span class="tag str"></span>](/types)

---

##Function Summary

###Class Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
attachCameraToObject([<span class="tag tab"></span>](/types)&nbsp;parameters) | Makes a Player's camera follow an Object. | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#attachcameratoobject)
broadcast([<span class="tag str"></span>](/types)&nbsp;message, [<span class="tag str"></span>](/types)&nbsp;Color) | Print message on Player's screen and their game chat log. | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#broadcast)
changeColor([<span class="tag str"></span>](/types)&nbsp;player_color) | Changes player to this [Player Color](/player-color). | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#changecolor)
<a class="anchor" id="gethandcount"></a>getHandCount() | Number of [hand zones](http://berserk-games.com/knowledgebase/hands/) owned by this color. | [<span class="ret int"></span>](/types)
getHandObjects([<span class="tag int"></span>](/types)&nbsp;hand_index) | Objects that are in this [hand zone](http://berserk-games.com/knowledgebase/hands/). | [<span class="ret tab"></span>](/types) | [<span class="i"></span>](#gethandobjects)
getHandTransform([<span class="tag int"></span>](/types)&nbsp;hand_index) | Returns a Table of data on this [hand zone](http://berserk-games.com/knowledgebase/hands/). | [<span class="ret tab"></span>](/types) | [<span class="i"></span>](#gethandtransform)
<a class="anchor" id="getholdingobjects"></a>getHoldingObjects() | Objects a Player is holding in their hand. | [<span class="ret tab"></span>](/types)
<a class="anchor" id="gethoverobject"></a>getHoverObject() | Object that the Player's pointer is hovering over. | [<span class="ret obj"></span>](/types)
<a class="anchor" id="getpointerposition"></a>getPointerPosition() | Player's pointer coordinates. | [<span class="ret vec"></span>](/types#vector)
<a class="anchor" id="getpointerrotation"></a>getPointerRotation() | Player's pointer rotation. | [<span class="ret vec"></span>](/types#vector)
<a class="anchor" id="getselectedobjects"></a>getSelectedObjects() | Objects that the Player has selected with an area selection. | [<span class="ret tab"></span>](/types)
<a class="anchor" id="kick"></a>kick() | Kicks Player out of the room. | [<span class="ret boo"></span>](/types)
lookAt([<span class="tag tab"></span>](/types)&nbsp;parameters) | Moves a Player's camera, forcing 3'rd person camera mode. | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#lookat)
<a class="anchor" id="mute"></a>mute() | Mutes or unmutes Player, preventing/allowing voice chat. | [<span class="ret boo"></span>](/types)
<a class="anchor" id="pingtable"></a>pingTable([<span class="tag vec"></span>](/types#vector)&nbsp;position) | Emulates the player using the ping tool at the given position (tapping Tab). | [<span class="ret boo"></span>](/types)
print([<span class="tag str"></span>](/types)&nbsp;message, [<span class="tag col"></span>](/types#color)&nbsp;message_color) | Prints a message into the Player's game chat. | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#print)
<a class="anchor" id="promote"></a>promote() | Promotes/demotes a Player. Promoted players have access to most host privileges. | [<span class="ret boo"></span>](/types) |
setHandTransform([<span class="tag tab"></span>](/types)&nbsp;parameters, [<span class="tag int"></span>](/types)&nbsp;hand_index) | Sets transform elements of a hand zone. | [<span class="ret boo"></span>](/types) | [<span class="i"></span>](#sethandtransform)



###Direct Class Functions
These functions return direct references to Players, not a Player Color. See details section for usage.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
<a class="anchor" id="getavailablecolors"></a>getAvailableColors() | Returns a table of strings of every valid seat color at the current table. Returned colors are in the default order. | [<span class="ret tab"></span>](/types)
<a class="anchor" id="getcolors"></a>getColors() | Returns a table of strings of every possible seat color. Returned colors are in the default order. | [<span class="ret tab"></span>](/types)
getPlayers() | Returns Table of all Players in the instance. | [<span class="ret tab"></span>](/types) | [<span class="i"></span>](#getplayers)
getSpectators() | Returns Table of all Players in spectator (Grey). | [<span class="ret tab"></span>](/types) | [<span class="i"></span>](#getspectators)


---

##Function Details

###Class Function Details

####attachCameraToObject(...)

[<span class="ret boo"></span>](/types)&nbsp;Makes a Player's camera follow an Object.

!!!info "attachCameraToObject(parameters)"
    * [<span class="tag tab"></span>](/types) **parameters**: A Table with parameters which guide the function.
        * [<span class="tag obj"></span>](/types) **parameters.object**: The Object to attach the camera to.
        * [<span class="tag vec"></span>](/types#vector) **parameters.offset**: A Vector to offset the camera by.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}

``` Lua
self.attachCameraToObject({object=self})
```

---


####broadcast(...)

[<span class="ret boo"></span>](/types)&nbsp;Print message on Player's screen and their game chat log.

!!!info "broadcast(message, message_color)"
    * [<span class="tag str"></span>](/types) **message**: The message to be displayed.
    * [<span class="tag col"></span>](/types#color) **message_color**: Tint of the message text.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


####changeColor(...)

[<span class="ret boo"></span>](/types)&nbsp;Changes player to this [Player Color](/player-color) (seat).

!!!info "changeColor(player_color)"
    * [<span class="tag str"></span>](/types) **player_color**: The [Player Color](/player-color) seat to move the Player to.

``` Lua
Player["White"].changeColor("Red")
```

---


####getHandObjects(...)

[<span class="ret tab"></span>](/types)&nbsp;Returns a Table of Objects that are in this [hand zone](http://berserk-games.com/knowledgebase/hands/).

!!!info "getHandObjects(hand_index)"
    * [<span class="tag int"></span>](/types) **hand_index**: An index, representing which hand zone to return Objects for.
        * {>>Optional, defaults to 1.<<}

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


####getHandTransform(...)

[<span class="ret tab"></span>](/types)&nbsp;Returns a Table of data on this [hand zone](http://berserk-games.com/knowledgebase/hands/).

!!!info "getHandTransform(hand_index)"
    * [<span class="tag int"></span>](/types) **hand_index**: An index, representing which hand zone to return data on.
        * {>>Optional, defaults to 1.<<}

!!!info "Return Data Table"
    * [<span class="tag tab"></span>](/types) **data**: The Table the data is returned in.
        * [<span class="tag vec"></span>](/types#vector) **data.position**: Position of the hand zone.
        * [<span class="tag vec"></span>](/types#vector) **data.rotation**: Rotation of the hand zone.
        * [<span class="tag vec"></span>](/types#vector) **data.scale**: Scale of the hand zone.
        * [<span class="tag vec"></span>](/types#vector) **data.forward**: Forward direction of the hand zone.
        * [<span class="tag vec"></span>](/types#vector) **data.right**: Right direction of the hand zone.
        * [<span class="tag vec"></span>](/types#vector) **data.up**: Up direction of the hand zone.

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


####lookAt(...)

[<span class="ret boo"></span>](/types)&nbsp;Moves a Player's camera, forcing 3'rd person camera mode.

!!!info "lookAt(parameters)"
    * [<span class="tag tab"></span>](/types) **parameters**: A Table of controlling parameters to point the player camera.
        * [<span class="tag vec"></span>](/types#vector) **parameters.position**: Position to center the camera on.
        * [<span class="tag flo"></span>](/types) **parameters.pitch**: Pitch angle of the camera. 0 to 90.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](/types) **parameters.yaw**: Yaw angle of the camera. -180 to 180.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](/types) **parameters.distance**: Distance the camera is from the position Vector.
            * {>>Optional, defaults to 40.<<}

``` Lua
-- Assuming someone is in the White seat
Player["White"].lookAt({
    position = {x=0,y=0,z=0},
    pitch    = 25,
    yaw      = 180,
    distance = 20,
})
```

---


####print(...)

[<span class="ret boo"></span>](/types)&nbsp;Prints a message into the Player's game chat.

!!!info "print(message, message_color)"
    * [<span class="tag str"></span>](/types) **message**: The text to be displayed.
    * [<span class="tag col"></span>](/types#color) **message_color**: Color for the message text to be tinted.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


####setHandTransform(...)

[<span class="ret boo"></span>](/types)&nbsp;Sets transform elements of a [hand zone](http://berserk-games.com/knowledgebase/hands/).

!!!info "setHandTransform(parameters, hand_index)"
    * [<span class="tag tab"></span>](/types) **parameters**: The Table of data to transform the hand zone with.
        * [<span class="tag vec"></span>](/types#vector) **parameters.position**: Position of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](/types#vector) **parameters.rotation**: Rotation of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](/types#vector) **parameters.scale**: Scale of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
    * [<span class="tag int"></span>](/types) **hand_index**: Index, representing which hand zone to modify.
        * {>>Optional, defaults to 1.<<}

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

``` Lua
-- Example of moving/rotating/scaling hand zone
params = {
    position = {x=0, y=5, z=0},
    rotation = {x=0, y=45, z=0},
    scale    = {x=2, y=2, z=2},
}
Player["White"].setHandTransform(params, 2)
```

---


###Direct Class Function Details

####getPlayers()

[<span class="ret tab"></span>](/types)&nbsp;Returns Table of all Players in the instance.

``` Lua
-- Blindfolding all players
playerList = Player.getPlayers()
for _, playerReference in ipairs(playerList) do
    playerReference.blindfolded = true
end
```

---


####getSpectators()

[<span class="ret tab"></span>](/types)&nbsp;Returns Table of all Players in spectator (Grey).

``` Lua
-- Printing steam name of all players to host chat
playerList = Player.getSpectators()
for _, playerReference in ipairs(playerList) do
    print(playerReference.steam_name)
end
```
