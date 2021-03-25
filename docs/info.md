`Info` global allows you to manipulate the information about your game/mod, in the same way as the in-game Options ->
Info menu.

This information helps players find your game/mod within Tabletop Simulator's server list and via Steam Workshop's
search/filter capabilities.

!!!example "Example Usage"
    ```lua
    Info.name = "My Game"
    ```

##Member Variables

Variable | Description | Type
-- | -- | :--
complexity {: #complexity } | The complexity of the current game/mod. | [<span class="tag str"></span>](types.md)
name {: #name } | Name of the current game/mod. | [<span class="tag str"></span>](types.md)
number_of_players {: #number_of_players } | The number of players the current game/mod allows. | [<span class="tag tab"></span>](types.md)
playing_time {: #playing_time } | The amount of time the current game/mod takes. | [<span class="tag tab"></span>](types.md)
tags {: #tags } | The tags associated with the current game/mod. | [<span class="tag tab"></span>](types.md)
type {: #type } | The category of the current mod. | [<span class="tag str"></span>](types.md)
