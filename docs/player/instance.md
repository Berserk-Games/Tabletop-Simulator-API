# Player Instance

Player instances can be retrieved from the [Player Manager](manager.md) and are also frequently passed to callbacks.

## Member Variables

Variable | Type | Description
-- | -- | --
admin {: #admin } | [<span class="tag boo"></span>](../types.md) | If the player is promoted or the host of the game. Read only.
blindfolded {: #blindfolded } | [<span class="tag boo"></span>](../types.md) | If the player is blindfolded.
color {: #color } | [<span class="tag str"></span>](../types.md) | The player's [Player Color](colors.md). Read only.
host {: #host } | [<span class="tag boo"></span>](../types.md) | If the player is the host. Read only.
lift_height {: #lift_height } | [<span class="tag flo"></span>](../types.md) | The lift height for the player. This is how far an object is raised when held in a player's hand. Value is ranged 0 to 1.
promoted {: #promoted } | [<span class="tag boo"></span>](../types.md) | If the current player is promoted.
seated {: #seated } | [<span class="tag boo"></span>](../types.md) | If a player is currently seated at this color. Read only.
steam_id {: #steam_id } | [<span class="tag str"></span>](../types.md) | The Steam ID of the player. This is unique to each player's Steam account. Read only.
steam_name {: #steam_name } | [<span class="tag str"></span>](../types.md) | The Steam name of the player. Read only.
team {: #team } | [<span class="tag str"></span>](../types.md) | The team of the player.<br>Options: `"None", "Clubs", "Diamonds", "Hearts", "Spades", "Jokers"`.

---

## Function Summary

Function Name | Return | Description | &nbsp;
-- | -- | -- | --
attachCameraToObject([<span class="tag tab"></span>](../types.md) parameters) | [<span class="ret boo"></span>](../types.md) | Makes a Player's camera follow an Object. | [:i:](#attachcameratoobject)
broadcast([<span class="tag str"></span>](../types.md) message, [<span class="tag col"></span>](../types.md) message_color) | [<span class="ret boo"></span>](../types.md) | Print message on Player's screen and their game chat log. | [:i:](#broadcast)
changeColor([<span class="tag str"></span>](../types.md) player_color) | [<span class="ret boo"></span>](../types.md) | Changes player to this [Player Color](colors.md). | [:i:](#changecolor)
clearSelectedObjects() {: #clearselectedobjects data-toc-label="clearSelectedObjects()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Clears a player's current selection. |
getHandCount() {: #gethandcount data-toc-label="getHandCount()" data-toc-child-of="function-details" } | [<span class="ret int"></span>](../types.md) | Number of [hand zones](https://kb.tabletopsimulator.com/host-guides/player-hands/) owned by this color. |
getHandObjects([<span class="tag int"></span>](../types.md) hand_index) | [<span class="ret tab"></span>](../types.md) | Objects that are in this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/). | [:i:](#gethandobjects)
getHandTransform([<span class="tag int"></span>](../types.md) hand_index)| [<span class="ret tab"></span>](../types.md) | Returns a Table of data on this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/). | [:i:](#gethandtransform)
getHoldingObjects() {: #getholdingobjects data-toc-label="getHoldingObjects()" data-toc-child-of="function-details" } | [<span class="ret tab"></span>](../types.md) | Objects a Player is holding in their hand. |
getHoverObject() {: #gethoverobject data-toc-label="getHoverObject()" data-toc-child-of="function-details" } | [<span class="ret obj"></span>](../types.md) | Object that the Player's pointer is hovering over. |
getPointerPosition() {: #getpointerposition data-toc-label="getPointerPosition()" data-toc-child-of="function-details" } | [<span class="ret vec"></span>](../types.md#vector) | Player's pointer coordinates. |
getPointerRotation() {: #getpointerrotation data-toc-label="getPointerRotation()" data-toc-child-of="function-details" } | [<span class="ret flo"></span>](../types.md) | Player's pointer rotation on Y axis. |
getSelectedObjects() {: #getselectedobjects data-toc-label="getSelectedObjects()" data-toc-child-of="function-details" } | [<span class="ret tab"></span>](../types.md) | Objects that the Player has selected with an area selection. |
kick() {: #kick data-toc-label="kick()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Kicks Player out of the room. |
lookAt([<span class="tag tab"></span>](../types.md) parameters) | [<span class="ret boo"></span>](../types.md) | Moves a Player's camera, forcing 3'rd person camera mode. | [:i:](#lookat)
mute() {: #mute data-toc-label="mute()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Mutes or unmutes Player, preventing/allowing voice chat. |
pingTable([<span class="tag vec"></span>](../types.md#vector) position) {: #pingtable data-toc-label="pingTable(...)" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Emulates the player using the ping tool at the given position (tapping Tab). |
print([<span class="tag str"></span>](../types.md) message, [<span class="tag col"></span>](../types.md#color) message_color) | [<span class="ret boo"></span>](../types.md) | Prints a message into the Player's game chat. | [:i:](#print)
promote() {: #promote data-toc-label="promote()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Promotes/demotes a Player. Promoted players have access to most host privileges. |
setCameraMode([<span class="tag str"></span>](../types.md) camera_mode) | [<span class="ret boo"></span>](../types.md) | Sets the player's camera mode. Camera modes available: "ThirdPerson", "FirstPerson", "TopDown". | [:i:](#setcameramode)
setHandTransform([<span class="tag tab"></span>](../types.md) parameters, [<span class="tag int"></span>](../types.md) hand_index) | [<span class="ret boo"></span>](../types.md) | Sets transform elements of a hand zone. | [:i:](#sethandtransform)

---

## Function Details {: data-toc-sort }

### attachCameraToObject(...)

[<span class="ret boo"></span>](../types.md) Makes a Player's camera follow an Object.

!!!info "attachCameraToObject(parameters)"
    * [<span class="tag tab"></span>](../types.md) **parameters**: A Table with parameters which guide the function.
        * [<span class="tag obj"></span>](../types.md) **parameters.object**: The Object to attach the camera to.
        * [<span class="tag vec"></span>](../types.md#vector) **parameters.offset**: A Vector to offset the camera by.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}

``` Lua
self.attachCameraToObject({object=self})
```

---


### broadcast(...)

[<span class="ret boo"></span>](../types.md) Print message on Player's screen and their game chat log.

!!!info "broadcast(message, message_color)"
    * [<span class="tag str"></span>](../types.md) **message**: The message to be displayed.
    * [<span class="tag col"></span>](../types.md#color) **message_color**: Tint of the message text.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


### changeColor(...)

[<span class="ret boo"></span>](../types.md) Changes player to this [Player Color](colors.md) (seat).

!!!info "changeColor(player_color)"
    * [<span class="tag str"></span>](../types.md) **player_color**: The [Player Color](colors.md) seat to move the Player to.

``` Lua
Player["White"].changeColor("Red")
```

---


### getHandObjects(...)

[<span class="ret tab"></span>](../types.md) Returns a Table of Objects that are in this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "getHandObjects(hand_index)"
    * [<span class="tag int"></span>](../types.md) **hand_index**: An index, representing which hand zone to return Objects for.
        * {>>Optional, defaults to 1.<<}

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


### getHandTransform(...)

[<span class="ret tab"></span>](../types.md) Returns a Table of data on this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "getHandTransform(hand_index)"
    * [<span class="tag int"></span>](../types.md) **hand_index**: An index, representing which hand zone to return data on.
        * {>>Optional, defaults to 1.<<}

!!!info "Return Data Table"
    * [<span class="tag tab"></span>](../types.md) **data**: The Table the data is returned in.
        * [<span class="tag vec"></span>](../types.md#vector) **data.position**: Position of the hand zone.
        * [<span class="tag vec"></span>](../types.md#vector) **data.rotation**: Rotation of the hand zone.
        * [<span class="tag vec"></span>](../types.md#vector) **data.scale**: Scale of the hand zone.
        * [<span class="tag vec"></span>](../types.md#vector) **data.forward**: Forward direction of the hand zone.
        * [<span class="tag vec"></span>](../types.md#vector) **data.right**: Right direction of the hand zone.
        * [<span class="tag vec"></span>](../types.md#vector) **data.up**: Up direction of the hand zone.

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


### lookAt(...)

[<span class="ret boo"></span>](../types.md) Moves a Player's camera, forcing 3'rd person camera mode.

!!!info "lookAt(parameters)"
    * [<span class="tag tab"></span>](../types.md) **parameters**: A Table of controlling parameters to point the player camera.
        * [<span class="tag vec"></span>](../types.md#vector) **parameters.position**: Position to center the camera on.
        * [<span class="tag flo"></span>](../types.md) **parameters.pitch**: Pitch angle of the camera. 0 to 90.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](../types.md) **parameters.yaw**: Yaw angle of the camera. 0 to 360.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](../types.md) **parameters.distance**: Distance the camera is from the position Vector.
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


### print(...)

[<span class="ret boo"></span>](../types.md) Prints a message into the Player's game chat.

!!!info "print(message, message_color)"
    * [<span class="tag str"></span>](../types.md) **message**: The text to be displayed.
    * [<span class="tag col"></span>](../types.md#color) **message_color**: Color for the message text to be tinted.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


### setCameraMode(...)

[<span class="ret boo"></span>](../types.md) Sets the player's camera mode. Camera modes available: "ThirdPerson", "FirstPerson", "TopDown".

!!!info "changeColor(camera_mode)"
    * [<span class="tag str"></span>](../types.md) **camera_mode**: The Camera Mode to set the Player's Camera to.

``` Lua
Player["White"].setCameraMode("FirstPerson")
```

---

### setHandTransform(...)

[<span class="ret boo"></span>](../types.md) Sets transform elements of a [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "setHandTransform(parameters, hand_index)"
    * [<span class="tag tab"></span>](../types.md) **parameters**: The Table of data to transform the hand zone with.
        * [<span class="tag vec"></span>](../types.md#vector) **parameters.position**: Position of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](../types.md#vector) **parameters.rotation**: Rotation of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](../types.md#vector) **parameters.scale**: Scale of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
    * [<span class="tag int"></span>](../types.md) **hand_index**: Index, representing which hand zone to modify.
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
