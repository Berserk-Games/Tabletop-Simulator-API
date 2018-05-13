UI, a static global class, is the method to interact with custom UI elements. It allows you to read/write attributes of elements defined in the XML of the UI. It also allows you to receive information from various inputs (like buttons) on-screen.

Example of calling a function: `UI.getAttributes(id)`.

!!!warning
    **What this class does NOT do is create new UI elements.** Those are created in the custom UI using XML. The UI scripting class is only used to modify or communicate with existing UI elements.
    
    See the [UI API](ui/introUI.md) for info on how.


##Inputs

[Input Elements](ui/inputelements) are able to trigger a function. By default, they trigger a function in Global. [View here](ui/inputelements#targeting-triggers) for information on how to trigger a function on an Object's script.

When creating the input element in XML, you will select the name of the function it activates. Regardless of its name, it always will pass parameters

!!!info "functionName(player, value, id)"
    * [<span class="tag pla"></span>](intro#types) **player**: A direct Player reference to the person that triggered the input.
    * [<span class="tag var"></span>](intro#types) **value**: The value sent by the input. A numeric value or a string, generally.
        * {>>This is not used by buttons!<<}
    * [<span class="tag str"></span>](intro#types) **id**: 
        * {>>This is only passed if the element was given an Id attribute in the XML.<<}

```lua
function onButtonClick(player, value, id)
    print(player.steam_name)
    print(id)
end
```

---

##Element Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
getAttribute([<span class="tag str"></span>](intro#types)&nbsp;id, [<span class="tag str"></span>](intro#types)&nbsp;attribute) | Obtains the value of a specified attribute of a UI element. | [<span class="ret var"></span>](intro#types) | [<span class="i"></span>](#getattribute)
getAttributes([<span class="tag str"></span>](intro#types)&nbsp;id) | Returns the attributes and their values of a UI element. | [<span class="ret tab"></span>](intro#types) | [<span class="i"></span>](#getattributes)
hide([<span class="tag str"></span>](intro#types)&nbsp;id) | Hides the given UI element. Unlike the "active" attribute, hide triggers animations. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#hide)
setAttribute([<span class="tag str"></span>](intro#types)&nbsp;id, [<span class="tag str"></span>](intro#types)&nbsp;attribute, [<span class="tag var"></span>](intro#types)&nbsp;value) | Sets the value of a specified attribute of a UI element. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setattribute)
show([<span class="tag str"></span>](intro#types)&nbsp;id) | Displays the given UI element. Unlike the "active" attribute, show triggers animations. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#show)
setAttributes([<span class="tag str"></span>](intro#types)&nbsp;id, [<span class="tag tab"></span>](intro#types)&nbsp;data) | Updates the value of the supplied attributes of a UI element. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setattributes)


 
---

##Element Function Details

###getAttribute(...)

[<span class="ret var"></span>](intro#types)&nbsp;Obtains the value of a specified attribute of a UI element. What it returns will typically be a string or a number.

!!!info "getAttribute(id, attribute)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](intro#types) **attribute**: The name of the attribute you wish to get the value of.
    
``` Lua
UI.getAttribute("testElement", "fontSize")
```

---


###getAttributes(...)

[<span class="ret tab"></span>](intro#types)&nbsp;Returns the attributes and their values of a UI element. It only returns the attributes (and values) for elements that have had those attributes set by the user.

!!!info "getAttributes(id)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.

!!!info "Return table"
    * [<span class="tag tab"></span>](intro#types) **parameters**: A Table with the attributes as keys and their XML value as the key's value.
        * [<span class="tag str"></span>](intro#types) **texture**: The name of the image element
        * [<span class="tag str"></span>](intro#types) **color**: The hex used for the color element's value.
    
    **IMPORTANT**: This return table is an example of one you may get back from using it on a RawImage element type. The attribute keys you get back and their values will depend on the element you use the function on as well as the attributes you, the user, have assigned to it.

---


###hide(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Hides the given UI element. Unlike the "active" attribute, hide triggers animations.

!!!info "hide(id)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.

    
``` Lua
UI.hide("testElement")
```

---


###setAttribute(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Sets the value of a specified attribute of a UI element.

!!!info "setAttribute(id, attribute, value)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](intro#types) **attribute**: The name of the attribute you want to set the value of.
    * [<span class="tag var"></span>](intro#types) **value**: The value to set for the attribute.

    
``` Lua
UI.setAttribute("testElement", "fontSize", 200)
```

---


###show(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Shows the given UI element. Unlike the "active" attribute, show triggers animations.

!!!info "show(id)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.

    
``` Lua
UI.show("testElement")
```






###setAttributes(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Updates the value of the supplied attributes of a UI element. You do not need to set every attribute with the data table, an element will continue using any previous values you do not overwrite.

!!!info "setAttributes(id, data)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag tab"></span>](intro#types) **data**: A Table with key/value pairs representing attributes and their values.

!!!info "Example data table"
    * [<span class="tag tab"></span>](intro#types) **data**: A Table with parameters which guide the function.
        * [<span class="tag flo"></span>](intro#types) **data.fontSize**: Attribute's desired value value
        * [<span class="tag str"></span>](intro#vector) **data.color**: Attribute's desired value
                    
    **IMPORTANT**: This table is an example of one you may use when setting a text UI element. The attribute keys you use and their values will depend on the element you use the function on.
    
```lua
attributeTable = {
    fontSize = 300,
    color = "#000000"
}
UI.setAttributes("exampleText", attributeTable)
```

---
