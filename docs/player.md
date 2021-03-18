Player, a static global class, allows control over in-game players and their [hand zones](https://kb.tabletopsimulator.com/host-guides/player-hands/).

Example Usage: `Player["White"].seated` or `Player["Green"].mute()`


##Member Variables

Variable | Description | Type
-- | -- | :--
admin {: #admin } | If the player is promoted or the host of the game. Read only. | [<span class="tag boo"></span>](types.md)
blindfolded {: #blindfolded } | If the player is blindfolded. | [<span class="tag boo"></span>](types.md)
color {: #color } | The player's [Player Color](player-color.md). Read only. | [<span class="tag str"></span>](types.md)
host {: #host } | If the player is the host. Read only. | [<span class="tag boo"></span>](types.md)
lift_height {: #lift_height } | The lift height for the player. This is how far an object is raised when held in a player's hand. Value is ranged 0 to 1. | [<span class="tag flo"></span>](types.md)
promoted {: #promoted } | If the current player is promoted. | [<span class="tag boo"></span>](types.md)
seated {: #seated } | If a player is currently seated at this color. Read only. | [<span class="tag boo"></span>](types.md)
steam_id {: #steam_id } | The Steam ID of the player. This is unique to each player's Steam account. Read only. | [<span class="tag str"></span>](types.md)
steam_name {: #steam_name } | The Steam name of the player. Read only. | [<span class="tag str"></span>](types.md)
team {: #team } | The team of the player.<br>Options: `"None", "Clubs", "Diamonds", "Hearts", "Spades", "Jokers"`. | [<span class="tag str"></span>](types.md)

---

##Function Summary

###Class Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
attachCameraToObject([<span class="tag tab"></span>](types.md) parameters) | Makes a Player's camera follow an Object. | [<span class="ret boo"></span>](types.md) | [:i:](#attachcameratoobject)
broadcast([<span class="tag str"></span>](types.md) message, [<span class="tag col"></span>](types.md) message_color) | Print message on Player's screen and their game chat log. | [<span class="ret boo"></span>](types.md) | [:i:](#broadcast)
changeColor([<span class="tag str"></span>](types.md) player_color) | Changes player to this [Player Color](player-color.md). | [<span class="ret boo"></span>](types.md) | [:i:](#changecolor)
clearSelectedObjects() {: #clearselectedobjects data-toc-label="clearSelectedObjects()" data-toc-child-of="class-function-details" } | Clears a player's current selection. | [<span class="ret boo"></span>](types.md)
getHandCount() {: #gethandcount data-toc-label="getHandCount()" data-toc-child-of="class-function-details" } | Number of [hand zones](https://kb.tabletopsimulator.com/host-guides/player-hands/) owned by this color. | [<span class="ret int"></span>](types.md)
getHandObjects([<span class="tag int"></span>](types.md) hand_index) | Objects that are in this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/). | [<span class="ret tab"></span>](types.md) | [:i:](#gethandobjects)
getHandTransform([<span class="tag int"></span>](types.md) hand_index) | Returns a Table of data on this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/). | [<span class="ret tab"></span>](types.md) | [:i:](#gethandtransform)
getHoldingObjects() {: #getholdingobjects data-toc-label="getHoldingObjects()" data-toc-child-of="class-function-details" } | Objects a Player is holding in their hand. | [<span class="ret tab"></span>](types.md)
getHoverObject() {: #gethoverobject data-toc-label="getHoverObject()" data-toc-child-of="class-function-details" } | Object that the Player's pointer is hovering over. | [<span class="ret obj"></span>](types.md)
getPointerPosition() {: #getpointerposition data-toc-label="getPointerPosition()" data-toc-child-of="class-function-details" } | Player's pointer coordinates. | [<span class="ret vec"></span>](types.md#vector)
getPointerRotation() {: #getpointerrotation data-toc-label="getPointerRotation()" data-toc-child-of="class-function-details" } | Player's pointer rotation on Y axis. | [<span class="ret flo"></span>](types.md)
getSelectedObjects() {: #getselectedobjects data-toc-label="getSelectedObjects()" data-toc-child-of="class-function-details" } | Objects that the Player has selected with an area selection. | [<span class="ret tab"></span>](types.md)
kick() {: #kick data-toc-label="kick()" data-toc-child-of="class-function-details" } | Kicks Player out of the room. | [<span class="ret boo"></span>](types.md)
lookAt([<span class="tag tab"></span>](types.md) parameters) | Moves a Player's camera, forcing 3'rd person camera mode. | [<span class="ret boo"></span>](types.md) | [:i:](#lookat)
mute() {: #mute data-toc-label="mute()" data-toc-child-of="class-function-details" } | Mutes or unmutes Player, preventing/allowing voice chat. | [<span class="ret boo"></span>](types.md)
pingTable([<span class="tag vec"></span>](types.md#vector) position) {: #pingtable data-toc-label="pingTable(...)" data-toc-child-of="class-function-details" } | Emulates the player using the ping tool at the given position (tapping Tab). | [<span class="ret boo"></span>](types.md)
print([<span class="tag str"></span>](types.md) message, [<span class="tag col"></span>](types.md#color) message_color) | Prints a message into the Player's game chat. | [<span class="ret boo"></span>](types.md) | [:i:](#print)
promote() {: #promote data-toc-label="promote()" data-toc-child-of="class-function-details" } | Promotes/demotes a Player. Promoted players have access to most host privileges. | [<span class="ret boo"></span>](types.md) |
setCameraMode([<span class="tag str"></span>](types.md) camera_mode) | Sets the player's camera mode. Camera modes available: "ThirdPerson", "FirstPerson", "TopDown". | [<span class="ret boo"></span>](types.md) | [:i:](#setcameramode)
setHandTransform([<span class="tag tab"></span>](types.md) parameters, [<span class="tag int"></span>](types.md) hand_index) | Sets transform elements of a hand zone. | [<span class="ret boo"></span>](types.md) | [:i:](#sethandtransform)



###Direct Class Functions
These functions return direct references to Players, not a Player Color. See details section for usage.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getAvailableColors() {: #getavailablecolors data-toc-label="getAvailableColors()" data-toc-child-of="direct-class-function-details" } | Returns a table of strings of every valid seat color at the current table. Returned colors are in the default order. | [<span class="ret tab"></span>](types.md)
getColors() {: #getcolors data-toc-label="getColors()" data-toc-child-of="direct-class-function-details" } | Returns a table of strings of every possible seat color. Returned colors are in the default order. | [<span class="ret tab"></span>](types.md)
getPlayers() | Returns Table of all Players in the instance. | [<span class="ret tab"></span>](types.md) | [:i:](#getplayers)
getSpectators() | Returns Table of all Players in spectator (Grey). | [<span class="ret tab"></span>](types.md) | [:i:](#getspectators)


---

##Function Details

###Class Function Details {: data-toc-sort }

####attachCameraToObject(...)

[<span class="ret boo"></span>](types.md) Makes a Player's camera follow an Object.

!!!info "attachCameraToObject(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table with parameters which guide the function.
        * [<span class="tag obj"></span>](types.md) **parameters.object**: The Object to attach the camera to.
        * [<span class="tag vec"></span>](types.md#vector) **parameters.offset**: A Vector to offset the camera by.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}

``` Lua
self.attachCameraToObject({object=self})
```

---


####broadcast(...)

[<span class="ret boo"></span>](types.md) Print message on Player's screen and their game chat log.

!!!info "broadcast(message, message_color)"
    * [<span class="tag str"></span>](types.md) **message**: The message to be displayed.
    * [<span class="tag col"></span>](types.md#color) **message_color**: Tint of the message text.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


####changeColor(...)

[<span class="ret boo"></span>](types.md) Changes player to this [Player Color](player-color.md) (seat).

!!!info "changeColor(player_color)"
    * [<span class="tag str"></span>](types.md) **player_color**: The [Player Color](player-color.md) seat to move the Player to.

``` Lua
Player["White"].changeColor("Red")
```

---


####getHandObjects(...)

[<span class="ret tab"></span>](types.md) Returns a Table of Objects that are in this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "getHandObjects(hand_index)"
    * [<span class="tag int"></span>](types.md) **hand_index**: An index, representing which hand zone to return Objects for.
        * {>>Optional, defaults to 1.<<}

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


####getHandTransform(...)

[<span class="ret tab"></span>](types.md) Returns a Table of data on this [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "getHandTransform(hand_index)"
    * [<span class="tag int"></span>](types.md) **hand_index**: An index, representing which hand zone to return data on.
        * {>>Optional, defaults to 1.<<}

!!!info "Return Data Table"
    * [<span class="tag tab"></span>](types.md) **data**: The Table the data is returned in.
        * [<span class="tag vec"></span>](types.md#vector) **data.position**: Position of the hand zone.
        * [<span class="tag vec"></span>](types.md#vector) **data.rotation**: Rotation of the hand zone.
        * [<span class="tag vec"></span>](types.md#vector) **data.scale**: Scale of the hand zone.
        * [<span class="tag vec"></span>](types.md#vector) **data.forward**: Forward direction of the hand zone.
        * [<span class="tag vec"></span>](types.md#vector) **data.right**: Right direction of the hand zone.
        * [<span class="tag vec"></span>](types.md#vector) **data.up**: Up direction of the hand zone.

!!!tip "Indexing"
    Hand indexes start at 1 and are numbered in the order of their creation. Each Player color has its own indexes.

---


####lookAt(...)

[<span class="ret boo"></span>](types.md) Moves a Player's camera, forcing 3'rd person camera mode.

!!!info "lookAt(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of controlling parameters to point the player camera.
        * [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position to center the camera on.
        * [<span class="tag flo"></span>](types.md) **parameters.pitch**: Pitch angle of the camera. 0 to 90.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](types.md) **parameters.yaw**: Yaw angle of the camera. 0 to 360.
            * {>>Optional, defaults to 0.<<}
        * [<span class="tag flo"></span>](types.md) **parameters.distance**: Distance the camera is from the position Vector.
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

[<span class="ret boo"></span>](types.md) Prints a message into the Player's game chat.

!!!info "print(message, message_color)"
    * [<span class="tag str"></span>](types.md) **message**: The text to be displayed.
    * [<span class="tag col"></span>](types.md#color) **message_color**: Color for the message text to be tinted.
        * {>>Optional, defaults to {r=1, g=1, b=1}.<<}

---


####setCameraMode(...)

[<span class="ret boo"></span>](types.md) Sets the player's camera mode. Camera modes available: "ThirdPerson", "FirstPerson", "TopDown".

!!!info "changeColor(camera_mode)"
    * [<span class="tag str"></span>](types.md) **camera_mode**: The Camera Mode to set the Player's Camera to.

``` Lua
Player["White"].setCameraMode("FirstPerson")
```

---

####setHandTransform(...)

[<span class="ret boo"></span>](types.md) Sets transform elements of a [hand zone](https://kb.tabletopsimulator.com/host-guides/player-hands/).

!!!info "setHandTransform(parameters, hand_index)"
    * [<span class="tag tab"></span>](types.md) **parameters**: The Table of data to transform the hand zone with.
        * [<span class="tag vec"></span>](types.md#vector) **parameters.position**: Position of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](types.md#vector) **parameters.rotation**: Rotation of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](types.md#vector) **parameters.scale**: Scale of the hand zone.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
    * [<span class="tag int"></span>](types.md) **hand_index**: Index, representing which hand zone to modify.
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

###Direct Class Function Details {: data-toc-sort }

####getPlayers()

[<span class="ret tab"></span>](types.md) Returns Table of all Players in the instance.

``` Lua
-- Blindfolding all players
playerList = Player.getPlayers()
for _, playerReference in ipairs(playerList) do
    playerReference.blindfolded = true
end
```

---


####getSpectators()

[<span class="ret tab"></span>](types.md) Returns Table of all Players in spectator (Grey).

``` Lua
-- Printing steam name of all players to host chat
playerList = Player.getSpectators()
for _, playerReference in ipairs(playerList) do
    print(playerReference.steam_name)
end
```
