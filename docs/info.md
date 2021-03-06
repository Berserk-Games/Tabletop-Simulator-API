The static global Info class allows you to manipulate the Info properties in the same way as the in-game interface.

> Example Usage:`#!lua Info.name = "My Game"`.

##Member Variables

Like [Object member variables](object.md#member-variables), Info has its own member variables. They allow for direct access to the Info's properties.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="name"></a>name | Current name of the game you are playing. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="type"></a>type | The type of the game you are playing. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="complexity"></a>complexity | The complexity of the game you are playing. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="playing_time"></a>playing_time | The amount of time the current game takes. | [<span class="tag tab"></span>](types.md)
<a class="anchor" id="number_of_players"></a>number_of_players | The number of players the current game allows. | [<span class="tag tab"></span>](types.md)
<a class="anchor" id="tags"></a>tags | The tags are used to filter your games. | [<span class="tag tab"></span>](types.md)

