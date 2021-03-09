The static global `Hands` class allows you to control the behavior of Hand Zones.

##Member Variables

###Member Variable Summary

Variable | Description | Type | &nbsp;
-- | -- | -- | --
<a class="anchor" id="enable"></a>enable | Whether hand zones are enabled i.e. hold objects. | [<span class="tag boo"></span>](types.md) |
<a class="anchor" id="disable_unused"></a>disable_unused | Whether hands zones belonging to a color without a seated player should be disabled. | [<span class="tag boo"></span>](types.md) |
<a class="anchor" id="hiding"></a>hiding | Determines which hand contents are hidden from which players. | [<span class="tag int"></span>](types.md) | [:i:](#hiding)

##Member Variable Details

####hiding

[<span class="tag int"></span>](types.md) Determines which hands are hidden from which players.

Value | Description
-- | --
1 | Default. The contents of a player's hands are only visible to the owner.
2 | Reverse. The contents of a player's hands are visible to all other players, but not the owner.
3 | Disable. Contents of all player hands are visible to all players.

!!!example
    Make all hand contents visible to everyone.
    ```lua
    Hands.hiding = 3
    ```

---

##Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getHands() | Returns a table of all Hand Zone Objects in the game. | [<span class="ret tab">](types.md) | &nbsp;

---
