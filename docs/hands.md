The static global Hands class allows you to interact with Hand Objects. This allows you to manipulate the properties of Hand Zones in the same way as the in-game interface.

> Example Usage:`#!lua Hands.enable = true`.

##Member Variables

Like [Object member variables](object.md#member-variables), Hands has its own member variables. They allow for direct access to the Hand's properties.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="enable"></a>enable | Should player Hands hold objects. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="disable_unused"></a>disable_unused | Hands not used by a player will not be enabled. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="hiding"></a>hiding | How objects are hidden in Hands. 1 = Default, 2 = Reverse, 3 = Disable| [<span class="tag int"></span>](types.md)


##Function Summary

###Class Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getValue() | Returns the color of a Hand Zone. | [<span class="ret str"></span>](types.md) | &nbsp;
setValue([<span class="tag str"></span>](types.md)&nbsp;color) | Sets the color of a Hand Zone. | [<span class="ret boo"></span>](types.md) | &nbsp;

###Direct Class Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getHands() | Returns a Table of all Hand Zone Objects in the game. | [<span class="ret tab">](types.md) | &nbsp;

---
