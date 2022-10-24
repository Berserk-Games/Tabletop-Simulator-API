The Container behavior is present on Container objects such as Bags, Stacks and Decks.

---

## Function Summary

Function Name | Return | Description | &nbsp;
-- | -- | -- | --:
search([<span class="tag pla"></span>](../types.md) player, [<span class="tag int"></span>](../types.md) max_card) | Activate search window for player, optionally limited to top N cards | [<span class="ret boo"></span>](../types.md) | [:i:](#search)

---

## Function Details {: data-toc-sort }

### search(...)

[<span class="ret boo"></span>](../types.md) Show the Search window for the container to `player`.  If you specify `max_cards` then the search will be limited to that many cards from the top of the deck.


!!!info "search(player, max_cards)"
    * [<span class="tag pla"></span>](../types.md) **player**: The player to show the Search window to.
    * [<span class="tag int"></span>](../types.md) **max_cards**: Optional maximum number of cards to show.

``` Lua
deck.Container.search(Player.Blue, 3)
```
