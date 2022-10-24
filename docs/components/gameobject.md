!!!danger
	Component APIs are an advanced feature. An **understanding of how Unity works is required** to utilize them.

## Member Variables

Name | Type | Description
-- | -- | --
name {: #name } | [<span class="tag str"></span>](../types.md) | The name of the GameObject.

## Functions {: data-toc-sort }

Name | Return | Description
-- | -- | --
getChild([<span class="tag str"></span>](../types.md) name) {: #getchild data-toc-label="getChild(...)" data-toc-child-of="functions" } | [GameObject](gameobject.md) | Returns a child GameObject matching the specified `name`.
getChildren() {: #getchildren data-toc-label="getChildren()" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns the list of children GameObjects.
getComponent([<span class="tag str"></span>](../types.md) name) {: #getcomponent data-toc-label="getComponent(...)" data-toc-child-of="functions" } | [Component](component.md) | Returns a Component matching the specified `name` from the GameObject's list of Components.
getComponentInChildren([<span class="tag str"></span>](../types.md) name) {: #getcomponentinchildren data-toc-label="getComponentInChildren(...)" data-toc-child-of="functions" } | [Component](component.md) | Returns a Component matching the specified `name`. Found by searching the Components of the GameObject and its [children](#getchildren) recursively (depth first).
getComponents([<span class="tag str"></span>](../types.md) name) {: #getcomponents data-toc-label="getComponents(...)" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns the GameObject's list of Components. `name` is optional, when specified only Components with specified `name` will be included.
getComponentsInChildren([<span class="tag str"></span>](../types.md) name) {: #getcomponentsinchildren data-toc-label="getComponentsInChildren(...)" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns a list of Components found by searching the GameObject and its [children](#getchildren) recursively (depth first). `name` is optional, when specified only Components with specified `name` will be included.
getMaterials() {: #getmaterials data-toc-label="getMaterials()" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns the GameObject's list of Materials.
getMaterialsInChildren() {: #getmaterialsinchildren data-toc-label="getMaterialsInChildren()" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns a list of Materials found by searching the GameObject and its [children](#getchildren) recursively (depth first).
