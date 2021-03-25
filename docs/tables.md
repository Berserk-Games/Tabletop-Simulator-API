`Tables` is a global which provides the ability to interact with the Table object.

## Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getCustomURL() {: #getcustomurl data-toc-label="getCustomURL()" data-toc-child-of="function-details" } | Returns the image URL of the current [Custom Table](https://kb.tabletopsimulator.com/host-guides/tables/#custom-table), or `nil` if the current table is not a Custom Table. | [<span class="ret str"></span>](types.md) | &nbsp;
getTable() {: #gettable data-toc-label="getTable()" data-toc-child-of="function-details" } | Returns the current Table's [name](object.md#name) i.e. equivalent to `getTableObject().name`. | [<span class="ret str"></span>](types.md) | &nbsp;
getTableObject() {: #gettableobject data-toc-label="getTableObject()" data-toc-child-of="function-details" } | Returns the current Table object. | [<span class="ret obj"></span>](types.md) | &nbsp;
setCustomURL([<span class="tag str"></span>](types.md) url) {: #setcustomurl data-toc-label="setCustomURL(...)" data-toc-child-of="function-details" } | Sets the image URL for the current [Custom Table](https://kb.tabletopsimulator.com/host-guides/tables/#custom-table). Has no effect if the current Table is not a Custom Table. | [<span class="ret boo"></span>](types.md) | &nbsp;
setTable([<span class="tag str"></span>](types.md) name) | Replaces the current Table with the Table matching the specified `name`. | [<span class="ret boo"></span>](types.md) | [:i:](#settable)

## Table Names

[getTable()](#gettable) will return one of the following table names. [setTable(...)](#settable) will also accept these
names in addition to [human-readable names](#human-readable-names).

* Table_Circular
* Table_Custom
* Table_Custom_Square
* Table_Glass
* Table_Hexagon
* Table_None
* Table_Octagon
* Table_Plastic
* Table_Poker
* Table_RPG
* Table_Square

## Function Details {: data-toc-sort }

### setTable(...)

[<span class="ret boo"></span>](types.md) Replaces the current Table with the Table matching the specified `name`.

!!!info "setTable(name)"
	* [<span class="tag str"></span>](types.md) **name**: Table [name](#table-names) or [human-readable name](#human-readable-names).

#### Human-Readable Names

In addition to the table names [listed above](#table-names), `setTable(...)` will also accept the following
human-readable names:

* Custom Rectangle
* Custom Square
* Hexagon
* None
* Octagon
* Poker
* Rectangle
* Round
* Round Glass
* Round Plastic
* Square

!!!example
    Replace the current Table with the Poker Table.
    ```lua
    Tables.setTable("Poker")
    ```
