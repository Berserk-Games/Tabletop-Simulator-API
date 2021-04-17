# Player Manager

`Player` is a global which allows you to retrieve [Player instances](instance.md) and [Player colors](colors.md).

## Function Summary

Function Name | Return | Description | &nbsp;
-- | -- | -- | --
getAvailableColors() {: #getavailablecolors data-toc-label="getAvailableColors()" data-toc-child-of="function-details" } | [<span class="ret tab"></span>](../types.md) | Returns a table of strings of every valid seat color at the current table. Returned colors are in the default order. |
getColors() {: #getcolors data-toc-label="getColors()" data-toc-child-of="function-details" } | [<span class="ret tab"></span>](../types.md) | Returns a table of strings of every possible seat color. Returned colors are in the default order. |
getPlayers() | [<span class="ret tab"></span>](../types.md) | Returns a table of all [Player instances](instance.md). | [:i:](#getplayers)
getSpectators() | [<span class="ret tab"></span>](../types.md) | Returns a table of all spectator (Grey) [Player instances](instance.md). | [:i:](#getspectators)

---

## Actions

The [onPlayerAction](../events.md#onplayeraction) event allows you to handle player actions. A list of player actions
is available as `Player.Action`.

!!!example
    Log all available player actions:
    ```lua
    log(Player.Action)
    ```

For more details about these actions, please refer to the documentation for
[onPlayerAction](../events.md#onplayeraction).

---

## Function Details {: data-toc-sort }

### getPlayers()

[<span class="ret tab"></span>](../types.md) Returns a table of all [Player instances](instance.md).

!!!example
    Blindfold all players.
    ```lua
    for _, player in ipairs(Player.getPlayers()) do
        player.blindfolded = true
    end
    ```

---

### getSpectators()

[<span class="ret tab"></span>](../types.md) Returns a table of all spectator (Grey) [Player instances](instance.md).

!!!example
    Print the steam name of all spectators.
    ```lua
    for _, spectator in ipairs(Player.getSpectators()) do
        print(spectator.steam_name)
    end
    ```
