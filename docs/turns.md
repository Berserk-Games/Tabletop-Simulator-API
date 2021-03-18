Turns, a static global class, is the in-game turns system. It allows you to modify the player turns in the same way that the in-game Turns menu does.

Example usage: `Turns.reverse_order = true`.

##Member Variables

Variable | Description | Type
-- | -- | :--
enable {: #enable } | Enable/disable the turns system.  | [<span class="tag boo"></span>](types.md)
type {: #type } | If the turn order is automatic or custom. 1=auto, 2=custom. | [<span class="tag int"></span>](types.md)
order {: #order } | A table of strings, representing the player turn order. | [<span class="tag tab"></span>](types.md)
reverse_order {: #reverse_order } | Enable/disable reversing turn rotation direction. | [<span class="tag boo"></span>](types.md)
skip_empty_hands {: #skip_empty_hands } | Enable/disable skipping empty hands. | [<span class="tag boo"></span>](types.md)
disable_interactations {: #disable_interactations } | Enable/disable the blocking of players ability to interact with Objects when it is not their turn. | [<span class="tag boo"></span>](types.md)
pass_turns {: #pass_turns } | Enable/disable a player's ability to pass their turn to another. | [<span class="tag boo"></span>](types.md)
turn_color {: #turn_color } | The color of the Player who's turn it is. | [<span class="tag str"></span>](types.md)


##Function Summary {: data-toc-sort }

###Functions

Function Name | Description | Return
-- | -- | --:
getNextTurnColor() {: #getnextturncolor data-toc-label="getNextTurnColor()" data-toc-child-of="functions" } | Returns the Player Color string of the next player in the turn order. | [<span class="ret str"></span>](types.md)
getPreviousTurnColor() {: #getpreviousturncolor data-toc-label="getPreviousTurnColor()" data-toc-child-of="functions" } | Returns the Player Color string of the previous player in the turn order. | [<span class="ret str"></span>](types.md)



---
