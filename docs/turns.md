Turns, a static global class, is the in-game turns system. It allows you to modify the player turns in the same way that the in-game Turns menu does.

Example usage: `Turns.reverse_order = true`.

##Member Variables

Like [Object member variables](object.md#member-variables), Turns has its own member variables.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="enable"></a>enable | Enable/disable the turns system.  | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="type"></a>type | If the turn order is automatic or custom. 1=auto, 2=custom. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="order"></a>order | A table of strings, representing the player turn order. | [<span class="tag tab"></span>](types.md)
<a class="anchor" id="reverse_order"></a>reverse_order | Enable/disable reversing turn rotation direction. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="skip_empty_hands"></a>skip_empty_hands | Enable/disable skipping empty hands. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="disable_interactations"></a>disable_interactations | Enable/disable the blocking of players ability to interact with Objects when it is not their turn. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="pass_turns"></a>pass_turns | Enable/disable a player's ability to pass their turn to another. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="turn_color"></a>turn_color | The color of the Player who's turn it is. | [<span class="tag str"></span>](types.md)


##Function Summary

###Functions

Function Name | Description | Return
-- | -- | --:
<a class="anchor" id="getnextturncolor"></a>getNextTurnColor() | Returns the Player Color string of the next player in the turn order. | [<span class="ret str"></span>](types.md)
<a class="anchor" id="getpreviousturncolor"></a>getPreviousTurnColor() | Returns the Player Color string of the previous player in the turn order. | [<span class="ret str"></span>](types.md)



---
