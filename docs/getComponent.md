getComponentVar([<span class="tag str"></span>](types)&nbsp;componentName, [<span class="tag str"></span>](types)&nbsp;varName) | Get the current value of a component of an object. | [<span class="ret var"></span>](types) | [<span class="i"></span>](#getcomponentvar)

setComponentVar([<span class="tag str"></span>](types)&nbsp;componentName, [<span class="tag str"></span>](types)&nbsp;varName, [<span class="tag var"></span>](types)&nbsp;value) | Set the current value of a component of an object. | [<span class="ret boo"></span>](types) | [<span class="i"></span>](#setcomponentvar)

####getComponentVar(...)
[<span class="ret var"></span>](types)&nbsp;Get the current value of a component of an object. A component is a Unity term for certain aspects added to a game object, like "Light" or "BoxCollider". This works on standard game objects, but can be used to greater effect on AssetBundles.

!!!info "getComponentVar(componentName, varName)"
	* [<span class="tag str"></span>](types) **componentName**: The name of the component on the Object.
	* [<span class="tag str"></span>](types) **varName**: The name of the variable which modifies the component.

---



####setComponentVar(...)
[<span class="ret boo"></span>](types)&nbsp;Set the current value of a component of an object. A component is a Unity term for certain aspects added to a game object, like "Light" or "BoxCollider". This works on standard game objects, but can be used to greater effect on AssetBundles.

!!!info "setComponentVar(componentName, varName, value)"
	* [<span class="tag str"></span>](types) **componentName**: The name of the component on the Object.
	* [<span class="tag str"></span>](types) **varName**: The name of the variable which modifies the component.
	* [<span class="tag var"></span>](types) **value**: The value to give the variable.





---
