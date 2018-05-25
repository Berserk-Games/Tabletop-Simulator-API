UI, a static global class AND an Object class. It is the method to interact with custom UI elements. It allows you to read/write attributes of elements defined in the XML of the UI. It also allows you to receive information from various inputs (like buttons) on-screen and on objects.

!!!attention
    The primary function of this class is to modify the UI, not to create it. The [UI API](ui/introUI.md) is used to create UI on Objects or on the screen (Global).
    

##Global and Object
UI can either be placed on the screen by using the **Global UI** or placed on an Object using **Object UI**. Depending on which you are using, these commands are used differently.

    Example of calling a function targeted at the Global UI:
        UI.getAttributes(id)
    Example of calling a function targeted at an Object UI:
        object.UI.getAttributes(id)


##Inputs

[Input Elements](ui/inputelements) are able to trigger a function. By default, Global UI will trigger a function in Global and Object UI will trigger a function in the Object's script.  To change the target script for an input, [view more details here](ui/inputelements#targeting-triggers).

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
<a class="anchor" id="getxml"></a>getXml() | Returns the current xml string. This will not have any dynamic changes done from scripts. | [<span class="ret boo"></span>](intro#types) | 
hide([<span class="tag str"></span>](intro#types)&nbsp;id) | Hides the given UI element. Unlike the "active" attribute, hide triggers animations. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#hide)
setAttribute([<span class="tag str"></span>](intro#types)&nbsp;id, [<span class="tag str"></span>](intro#types)&nbsp;attribute, [<span class="tag var"></span>](intro#types)&nbsp;value) | Sets the value of a specified attribute of a UI element. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setattribute)
setXml([<span class="tag str"></span>](intro#types)&nbsp;xml) | Replaces the targeted XML script with the string provided. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setxml)
show([<span class="tag str"></span>](intro#types)&nbsp;id) | Displays the given UI element. Unlike the "active" attribute, show triggers animations. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#show)
setAttributes([<span class="tag str"></span>](intro#types)&nbsp;id, [<span class="tag tab"></span>](intro#types)&nbsp;data) | Updates the value of the supplied attributes of a UI element. | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setattributes)


 
---

##Element Function Details

###getAttribute(...)

[<span class="ret var"></span>](intro#types)&nbsp;Obtains the value of a specified attribute of a UI element. What it returns will typically be a string or a number.

!!!important
    This will return the value from the XML UI, not the dynamic UI. For example, if you had a toggle and clicked it on-screen, using getAttribute on `isOn` would still return `false`. This is because elements are not synced between clients by default.
    
    If you wanted them synced you could, using the toggle's onValueChanged function, do a `UI.setAttribute(...)` to make that element's `isOn` equal `true`.

!!!info "getAttribute(id, attribute)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](intro#types) **attribute**: The name of the attribute you wish to get the value of.
    
``` Lua
self.UI.getAttribute("testElement", "fontSize")
```

---


###getAttributes(...)

[<span class="ret tab"></span>](intro#types)&nbsp;Returns the attributes and their values of a UI element. It only returns the attributes (and values) for elements that have had those attributes set by the user.

!!!important
    This will return the value from the XML UI, not the dynamic UI. For example, if you had a toggle and clicked it on-screen, using getAttribute on `isOn` would still return `false`. This is because elements are not synced between clients by default.
    
    If you wanted them synced you could, using the toggle's onValueChanged function, do a `UI.setAttribute(...)` to make that element's `isOn` equal `true`.

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
self.UI.hide("testElement")
```

---


###setAttribute(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Sets the value of a specified attribute of a UI element.

!!!important
    This will override the dynamic value from the XML UI for all players, forcing them to see the same value.

!!!info "setAttribute(id, attribute, value)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](intro#types) **attribute**: The name of the attribute you want to set the value of.
    * [<span class="tag var"></span>](intro#types) **value**: The value to set for the attribute.

    
``` Lua
self.UI.setAttribute("testElement", "fontSize", 200)
```

---


###setXml(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Replaces the targeted XML script with the string provided.

!!!warning
    This will OVERWRITE currently existing XML that is already on the target Global/object.

!!!info "setXml(xml)"
    * [<span class="tag str"></span>](intro#types) **xml**: A single string with the contents of the XML to use

    
``` Lua
self.UI.setXml("<Text>Test</Text>")
```

---


###show(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Shows the given UI element. Unlike the "active" attribute, show triggers animations.

!!!info "show(id)"
    * [<span class="tag str"></span>](intro#types) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.

    
``` Lua
self.UI.show("testElement")
```






###setAttributes(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Updates the value of the supplied attributes of a UI element. You do not need to set every attribute with the data table, an element will continue using any previous values you do not overwrite.

!!!important
    This will override the dynamic value from the XML UI for all players, forcing them to see the same value.

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
self.UI.setAttributes("exampleText", attributeTable)
```

---
