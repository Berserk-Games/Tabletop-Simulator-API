UI, a static global class AND an Object class. It is the method to interact with custom UI elements. It allows you to read/write attributes of elements defined in the XML of the UI. It also allows you to receive information from various inputs (like buttons) on-screen and on objects.

!!!attention
    This class allows for the **manipulation** of UI **at runtime**. It does **NOT** modify or fetch **the original XML** in the editor, but rather what is displayed as it continues to run during a game. Just like with Lua, you can only get/set dynamic values during runtime. You can use [onSave](events.md#onsave) and [onLoad](events.md#onload) to record any data you want to persist through save/load/undo.

    For more information on how to build UI elements within XML, view the [UI API](ui/introUI.md).


##Global and Object

UI can either be placed on the screen by using the **Global UI** or placed on an Object using **Object UI**. Depending on which you are using, these commands are used differently.

    Example of calling a function targeted at the Global UI:
        UI.getAttributes(id)
    Example of calling a function targeted at an Object UI:
        object.UI.getAttributes(id)


##Inputs

[Input Elements](ui/inputelements.md) are able to trigger a function. By default, Global UI will trigger a function in Global and Object UI will trigger a function in the Object's script.  To change the target script for an input, [view more details here](ui/inputelements.md#targeting-triggers).

When creating the input element in XML, you will select the name of the function it activates. Regardless of its name, it always will pass parameters

!!!info "functionName(player, value, id)"
    * [<span class="tag pla"></span>](types.md) **player**: A direct Player reference to the person that triggered the input.
    * [<span class="tag var"></span>](types.md) **value**: The value sent by the input. A numeric value or a string, generally.
        * {>>This is not used by buttons!<<}
    * [<span class="tag str"></span>](types.md) **id**:
        * {>>This is only passed if the element was given an Id attribute in the XML.<<}

```lua
function onButtonClick(player, value, id)
    print(player.steam_name)
    print(id)
end
```

---

##Member Variable Summary

Variable | Description | Type
-- | -- | :--
loading {: #loading } | Indicates whether (the server) has finished loading all UI custom assets. | [<span class="tag boo"></span>](types.md)

---

##Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
getAttribute([<span class="tag str"></span>](types.md) id, [<span class="tag str"></span>](types.md) attribute) | Obtains the value of a specified attribute of a UI element. | [<span class="ret var"></span>](types.md) | [:i:](#getattribute)
getAttributes([<span class="tag str"></span>](types.md) id) | Returns the attributes and their values of a UI element. | [<span class="ret tab"></span>](types.md) | [:i:](#getattributes)
getCustomAssets() | Returns information on all custom assets uploaded to the UI ASSETS pane. | [<span class="ret tab"></span>](types.md) | [:i:](#getcustomassets)
getValue([<span class="tag str"></span>](types.md) id) | Obtains the value between elements tags, like: `<Text>ValueToGet</Text>` | [<span class="ret str"></span>](types.md) | [:i:](#getvalue)
getXml() {: #getxml data-toc-label="getXml()" data-toc-child-of="function-details" } | Returns the contents of the current UI formatted as XML. | [<span class="ret str"></span>](types.md) |
getXmlTable() | Returns the contents of the current UI formatted as a table. | [<span class="ret tab"></span>](types.md) | [:i:](#getxmltable)
hide([<span class="tag str"></span>](types.md) id) | Hides the given UI element. Unlike the "active" attribute, hide triggers animations. | [<span class="ret boo"></span>](types.md) | [:i:](#hide)
setAttribute([<span class="tag str"></span>](types.md) id, [<span class="tag str"></span>](types.md) attribute, [<span class="tag var"></span>](types.md) value) | Sets the value of a specified attribute of a UI element. | [<span class="ret boo"></span>](types.md) | [:i:](#setattribute)
setAttributes([<span class="tag str"></span>](types.md) id, [<span class="tag tab"></span>](types.md) data) | Updates the value of the supplied attributes of a UI element. | [<span class="ret boo"></span>](types.md) | [:i:](#setattributes)
setClass([<span class="tag str"></span>](types.md) id, [<span class="tag str"></span>](types.md) names) | Replaces all classes on a UI element. | [<span class="ret boo"></span>](types.md) | [:i:](#setclass)
setCustomAssets([<span class="tag tab"></span>](types.md) assets) | Sets/replaces the custom assets which your UI may make use of. | [<span class="ret boo"></span>](types.md) | [:i:](#setcustomassets)
setValue([<span class="tag str"></span>](types.md) id, [<span class="tag str"></span>](types.md) value) | Updates the value between elements tags, like: `<Text>ValueChanged</Text>` | [<span class="ret boo"></span>](types.md) | [:i:](#setvalue)
setXml([<span class="tag str"></span>](types.md) xml, [<span class="tag tab"></span>](types.md) assets) | Sets/replaces the UI with the contents of the provided XML. | [<span class="ret boo"></span>](types.md) | [:i:](#setxml)
setXmlTable([<span class="tag tab"></span>](types.md) data, [<span class="tag tab"></span>](types.md) assets) | Sets/replaces the UI with the contents of the provided UI table. | [<span class="ret boo"></span>](types.md) | [:i:](#setxmltable)
show([<span class="tag str"></span>](types.md) id) | Displays the given UI element. Unlike the "active" attribute, show triggers animations. | [<span class="ret boo"></span>](types.md) | [:i:](#show)




---

##Function Details {: data-toc-sort }

###getAttribute(...)

[<span class="ret var"></span>](types.md) Obtains the value of a specified attribute of a UI element. What it returns will typically be a string or a number.

!!!info "getAttribute(id, attribute)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](types.md) **attribute**: The name of the attribute you wish to get the value of.

``` Lua
self.UI.getAttribute("testElement", "fontSize")
```

---


###getAttributes(...)

[<span class="ret tab"></span>](types.md) Returns the attributes and their values of a UI element. It only returns the attributes (and values) for elements that have had those attributes set by the user.

!!!info "getAttributes(id)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.

!!!info "Return table"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table with the attributes as keys and their XML value as the key's value.
        * [<span class="tag str"></span>](types.md) **texture**: The name of the image element
        * [<span class="tag str"></span>](types.md) **color**: The hex used for the color element's value.

    **IMPORTANT**: This return table is an example of one you may get back from using it on a RawImage element type. The attribute keys you get back and their values will depend on the element you use the function on as well as the attributes you, the user, have assigned to it.

---


###getCustomAssets()

[<span class="ret tab"></span>](types.md) Returns information on all custom assets uploaded to the UI ASSETS pane.

!!!info "Return table"
    * [<span class="tag tab"></span>](types.md) **table**: An unnamed table that contains sub-tables. Each sub-table represents one asset.
        * [<span class="tag str"></span>](types.md) **name**: The name of the image element
        * [<span class="tag str"></span>](types.md) **url**: The URL/file location of the asset's source.

``` Lua
function onLoad()
    local assets = UI.getCustomAssets()
    log(assets)
end
```




---


###getValue(...)
[<span class="ret str"></span>](types.md) Obtains the value between elements tags, like: `<Text>ValueObtained</Text>`

!!!info "getValue(id)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.


``` Lua
string = UI.getValue("testElement")
print(string)
```



---





###getXmlTable()

[<span class="ret tab"></span>](types.md) Returns the contents of the current UI formatted as a table.

Example Returned Table:
```lua
{
    {
        tag="HorizontalLayout",
        attributes={
            height=200,
            width=1000,
            color="rgba(0,0,0,0.7)",
        },
        children={
            {
                tag="Text",
                attributes={
                    fontSize=100,
                    color="red",
                },
                value="Example",
            },
            {
                tag="Text",
                attributes={
                    text="Message",
                    fontSize=100,
                    color="blue",
                },
            },
        }
    }
}
```

What the XML would look like which returns that table:
```xml
<HorizontalLayout height="200" width="1000" color="rgba(0,0,0,0.7)">
    <Text fontSize="100" color="red">Example</Text>
    <Text text="Message" fontSize="100" color="blue" />
</HorizontalLayout>
```

---


###hide(...)

[<span class="ret boo"></span>](types.md) Hides the given UI element. Unlike the "active" attribute, hide triggers animations.

!!!info "hide(id)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.


``` Lua
self.UI.hide("testElement")
```

---


###setAttribute(...)

[<span class="ret boo"></span>](types.md) Sets the value of a specified attribute of a UI element.

!!!important
    This will override the run-time value from the XML UI for all players, forcing them to see the same value.

!!!info "setAttribute(id, attribute, value)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](types.md) **attribute**: The name of the attribute you want to set the value of.
    * [<span class="tag var"></span>](types.md) **value**: The value to set for the attribute.


``` Lua
self.UI.setAttribute("testElement", "fontSize", 200)
```

---


###setAttributes(...)

[<span class="ret boo"></span>](types.md) Updates the value of the supplied attributes of a UI element. You do not need to set every attribute with the data table, an element will continue using any previous values you do not overwrite.

!!!important
    This will override the run-time value from the XML UI for all players, forcing them to see the same value.

!!!info "setAttributes(id, data)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag tab"></span>](types.md) **data**: A Table with key/value pairs representing attributes and their values.

!!!info "Example data table"
    * [<span class="tag tab"></span>](types.md) **data**: A Table with parameters which guide the function.
        * [<span class="tag flo"></span>](types.md) **data.fontSize**: Attribute's desired value value
        * [<span class="tag str"></span>](types.md#vector) **data.color**: Attribute's desired value

    **IMPORTANT**: This table is an example of one you may use when setting a text UI element. The attribute keys you use and their values will depend on the element you use the function on.

```lua
attributeTable = {
    fontSize = 300,
    color = "#000000"
}
self.UI.setAttributes("exampleText", attributeTable)
```

---


###setClass(...)

[<span class="ret boo"></span>](types.md) Replaces all classes on a UI element.

!!!info "setClass(id, names)"
    * [<span class="tag str"></span>](types.md) **id**: The ID of the UI element that should have its classes replaced.
    * [<span class="tag str"></span>](types.md) **names**: Space separated class names.

!!!example
    Replace all classes on the element with ID `someElementId` with two classes "important" and "large".
    ``` Lua
    UI.setClass("someElementId", "important large")
    ```

---


###setCustomAssets(...)

[<span class="ret boo"></span>](types.md) Sets/replaces the custom assets which your UI may make use of. Providing an empty table will remove all existing UI Assets.

!!!warning
    This function will overwrite/replace any currently existing assets in Custom UI Assets, not add to them.

!!!info "setCustomAssets(assets)"
    * [<span class="tag tab"></span>](types.md) **assets**: A table/array containing sub-tables which each represent a [custom asset](#setcustomassets-custom-assets).

##### Custom Assets {: #setcustomassets-custom-assets data-toc-omit }

Custom assets are represented as a table with the following properties:

Name | Type | Default | Description
-- | -- | -- | --
name | [<span class="tag str"></span>](types.md) | _Mandatory_ | The name you'll use to refer to this asset in your XML UI.
url | [<span class="tag str"></span>](types.md) | _Mandatory_ | The URL this asset will be loaded from.

Currently, only images are supported as custom assets.

!!!example
    Add two images which can be used within your XML UI.
    ```lua
    UI.setCustomAssets({
        {
            name = "Image1",
            url = "http://placehold.it/120x120&text=image1"
        },
        {
            name = "Image2",
            url = "http://placehold.it/120x120&text=image2"
        },
    })
    ```

---


###setValue(...)
[<span class="ret boo"></span>](types.md) Updates the value between elements tags, like: `<Text>ValueChanged</Text>`

!!!info "setValue(id, value)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.
    * [<span class="tag str"></span>](types.md) **value**: The value to put between the element tags.

``` Lua
UI.setValue("testElement", "New Text To Display")
```



---




###setXml(...)

[<span class="ret boo"></span>](types.md) Sets/replaces the UI with the contents of the provided XML.

!!!info "setXml(xml, assets)"
    * [<span class="tag str"></span>](types.md) **xml**: A string containing XML representing the desired UI.
    * [<span class="tag tab"></span>](types.md) **assets**: A table/array containing sub-tables which each represent a [custom asset](#setcustomassets-custom-assets).
        * {>>Optional. When omitted existing custom assets will not be modified. <<}

!!!warning
    UI changes do not take effect immediately. Any attempt to query the contents of the XML will return stale results
    until [loading](#loading) returns to `false`.


!!!example
    Display a single text label with the contents "Test".
    ```lua
    UI.setXml("<Text>Test</Text>")
    ```

---


###setXmlTable(...)

[<span class="ret boo"></span>](types.md) Sets/replaces the UI with the contents of the provided UI table.

!!!info "setXmlTable(data, assets)"
    * [<span class="tag tab"></span>](types.md) **data**: A table containing sub-tables. One sub-table for each element being created.
        * [<span class="tag str"></span>](types.md) **tag**: The element type.
        * [<span class="tag tab"></span>](types.md) **attributes**: A table containing attribute names for keys. Available attribute types depend on tag's element type.
            * {>>Optional, defaults to not being used.<<}
            * {>>Example key/value pairs: text="Test", color="black"<<}
        * [<span class="tag str"></span>](types.md) **value**: Text that appears `<Text>Here</Text>`, between the `<>` and `</>`.
            * {>>Optional, defaults to an empty string.<<}
        * [<span class="tag tab"></span>](types.md) **children**: A table containing more sub-tables, formatted as above. This does mean the sub-tables can contain their own children as well, containing sub-sub tables, etc.
            * {>>Optional, defaults to not being used.<<}
    * [<span class="tag tab"></span>](types.md) **assets**: A table/array containing sub-tables which each represent a [custom asset](#setcustomassets-custom-assets).
        * {>>Optional. When omitted existing custom assets will not be modified. <<}

!!!warning
    UI changes do not take effect immediately. Any attempt to query the contents of the XML will return stale results
    until [loading](#loading) returns to `false`.

!!!example
    Display two text labels within a horizontal layout.
    ```lua
    UI.setXmlTable({
        {
            tag="HorizontalLayout",
            attributes={
                height=200,
                width=1000,
                color="rgba(0,0,0,0.7)",
            },
            children={
                {
                    tag="Text",
                    attributes={
                        fontSize=100,
                        color="red",
                    },
                    value="Example",
                },
                {
                    tag="Text",
                    attributes={
                        text="Message",
                        fontSize=100,
                        color="blue",
                    },
                },
            }
        }
    })
    ```

---


###show(...)

[<span class="ret boo"></span>](types.md) Shows the given UI element. Unlike the "active" attribute, show triggers animations.

!!!info "show(id)"
    * [<span class="tag str"></span>](types.md) **id**: The Id that was assigned, as an attribute, to the desired XML UI element.


``` Lua
self.UI.show("testElement")
```

---
