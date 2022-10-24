The Material of a Renderer [component](component.md) is the primary method of controlling that object's appearance.

## Member Variables

Name | Type | Description | Return
-- | -- | -- | --
game_object {: #game_object } | [GameObject](gameobject.md) | The GameObject the Material is attached to.
shader {: #shader } | [<span class="tag str"></span>](../types.md) | The name of the Shader used by the Material.

## Functions {: data-toc-sort }

Name | Return | Description
-- | -- | --
get([<span class="tag str"></span>](../types.md) name) {: #get data-toc-label="get(...)" data-toc-child-of="functions" } | [<span class="ret var"></span>](../types.md) | Obtains the value of a given Variable on a Material.
getVars() {: #getvars data-toc-label="getVars()" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns a table mapping Var names ([<span class="tag str"></span>](../types.md)) to their type, which is also represented as a [<span class="tag str"></span>](../types.md).
set([<span class="tag str"></span>](../types.md) name, [<span class="tag var"></span>](../types.md) value) {: #set data-toc-label="set(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Sets the Var of the specified `name` to the provided `value`.
