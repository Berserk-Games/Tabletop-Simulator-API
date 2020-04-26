All input elements allow for the XML UI to interact with the Lua scripts in the game instance.

!!!tip
    Be sure to check out the [**UI section of the Lua Scripting API**](../ui.md) for how to receive the input from these element types. With Lua scripting, you can even modify the UI elements!

##Targeting Triggers
When using an attribute that triggers scripting, like onValueChanged or onClick, the UI will target a default location. Global UI targets Global script, Object UI targets the Object's script. This behavior can be overwritten. For example:

```xml
<Button onClick="uiClickFunc">Click Me</Button>
```
If this was in the Global UI, this would trigger a function in the Global Lua script `function uiClickFunc()`. But if you want to target a function on an Object's script? Place the GUID for the object before the function name, like so:
```xml
<Button onClick="aaa111/uiClickFunc">Click Me</Button>
```
Now when the button is clicked, it will still try to activate `function uiClickFunc()` but it will try to do so on the Object Lua script of the Object with the GUID of "aaa111".
```xml
<Button onClick="Global/uiClickFunc">Click Me</Button>
```
And if this was in an Object's UI, it would direct the function activation to Global instead of that Object.

Remember you can also use the [Id attribute](attributes.md#general-attributes) to identify which UI element triggered the function.

---


##Element Summary

Element Name | Description | &nbsp;
-- | -- | --
`#!xml <InputField></InputField>` | A text input for single or multiple lines. Is able to send the text (during edit and when finished). | [<span class="i"></span>](#inputfield)
`#!xml <Button></Button>` | A button. Is able to send a trigger event. | [<span class="i"></span>](#button)
`#!xml <Toggle></Toggle>` | A simple on/off toggle. Is able to send on/off status. | [<span class="i"></span>](#toggle)
`#!xml <ToggleButton></ToggleButton>` | A toggle, but styled as a button. | [<span class="i"></span>](#togglebutton)
`#!xml <ToggleGroup></ToggleGroup>` | Allows a group of toggles to act as a radio button, where only 1 of them can be "checked" at once.| [<span class="i"></span>](#togglegroup)
`#!xml <Slider></Slider>` | A value slider. Is able to send Value.  | [<span class="i"></span>](#slider)
`#!xml <Dropdown></Dropdown>` | A dropdown menu. Is able to send the contents of the selection made in it. | [<span class="i"></span>](#dropdown)

---


##Element Details
###InputField

A text input for single or multiple lines. Is able to send the text (during edit and when finished).

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | Each time the text is changed, a Lua function with this name will be triggered. | string | *(none)*
onEndEdit | When the input box is deselected, a Lua function with this name will be triggered. | string | *(none)*
text | The string in the text box, if any. Is the value sent to onValueChanged's or onEndEdit's function. | string | *(none)*
placeholder | A string that is semi-visible when there is no text in the input. | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
colors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
lineType |  | <ul><li>SingleLine</li><li>MultiLineSubmit</li><li>MultiLineNewLine</li></ul> | `SingleLine`
characterValidation |  | <ul><li>None</li><li>Integer</li><li>Decimal</li><li>Alphanumeric</li><li>Name</li><li>EmailAddress</li></ul> | `None`
caretBlinkRate |  | float | `0.85`
caretWidth |  | float | `1`
caretColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#323232`
selectionColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `rgba(0.65,0.8,1,0.75)`
readOnly |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | false
textColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#323232`
characterLimit |  | int | `0` (no limit)

Example:
```xml
<InputField>Default Text</InputField>
```

---


###Button

A button. Is able to send a trigger event.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onClick | When clicked, a Lua function with this name will be triggered. | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
colors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
textShadow |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textOutline |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textAlignment |  | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `UpperLeft`
icon |  | string | *(none)*
iconWidth |  | float |
iconColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) |
iconAlignment |  | <ul><li>Left</li><li>Right</li></ul> | `Left`
padding |  | float float float float | `0 0 0 0`
transition |  | <ul><li>None</li><li>ColorTint</li><li>SpriteSwap</li><li>Animation</li></ul> | `ColorTint`
highlightedSprite |  | string |
pressedSprite |  | string |
disabledSprite |  | string |

Example:
```xml
<!-- Standard Button -->
<Button>Button Text</Button>
<!-- Button with Icon -->
<Button icon="SomeName" />
<!-- Button with Icon and Text -->
<Button icon="SomeName">Button With Icon</Button>
```

!!!tip
    onClick passes nil for the value by default. However, you can assign a string that will be passed in onClick.

    ```xml
    <Button onClick="clickFunction(stringName)" />
    ```

    The above example passes a string with the name of `"stringName"` to the Lua function for the value property.

---


###Toggle

A simple on/off toggle. Is able to send on/off status.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When toggled, a Lua function with this name will be triggered. | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
textColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
colors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
isOn | If the toggle is "on" or not. Is the value sent to onValueChanged's function. | [<span class="tag boo"></span>](attributes.md#attribute-types) | false

Example:
```xml
<Toggle>Toggle Text</Toggle>
<!-- Toggle which is selected by default -->
<Toggle isOn="true">Toggle Text</Toggle>
```

---


###ToggleButton

A toggle, but styled as a button.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When toggled, a Lua function with this name will be triggered. | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
textColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
colors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
isOn | If the toggle is "on" or not. Is the value sent to onValueChanged's function. | [<span class="tag boo"></span>](attributes.md#attribute-types) | false
textShadow |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textOutline |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textAlignment |  | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `UpperLeft`
icon |  | string | *(none)*
iconWidth |  | float |
iconColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) |
iconAlignment |  | <ul><li>Left</li><li>Right</li></ul> | `Left`
padding |  | float float float float | `0 0 0 0`

```xml
<ToggleButton>Toggle Button Text</Toggle>
```

---


###ToggleGroup

Allows a group of toggles to act as a radio button, where only 1 of them can be "checked" at once. Works with Toggle or ToggleButton

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
allowSwitchOff | If this is set to true, then the user may clear their selection from within the ToggleGroup by clicking on the selected Toggle. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
toggleBackgroundImage | Sets the default background image to use for nested Toggle elements. | string |
toggleBackgroundColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
toggleSelectedImage | Sets the default image to use for selected (checked) nested Toggle elements. | string |
toggleSelectedColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`

```xml
<ToggleGroup>
    <VerticalLayout>
        <Toggle>Toggle A</Toggle>
        <Toggle>Toggle B</Toggle>
        <Toggle>Toggle C</Toggle>
    </VerticalLayout>
</ToggleGroup>

<ToggleGroup>
    <HorizontalLayout>
        <ToggleButton>ToggleButton A</ToggleButton>
        <ToggleButton>ToggleButton B</ToggleButton>
        <ToggleButton>ToggleButton C</ToggleButton>
    </HorizontalLayout>
</ToggleGroup>
```

---


###Slider

A value slider. Is able to send Value.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When the slider is moved, a Lua function with this name will be triggered. (rapidly) | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
colors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
minValue |  | float | `0`
maxValue |  | float | `1`
value | The value currently selected. Is the value sent to onValueChanged's function. | float | `0`
wholeNumbers |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | false
direction |  | <ul><li>LeftToRight</li><li>RightToLeft</li><li>TopToBottom</li><li>BottomToTop</li></ul> | `LeftToRight`
backgroundColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
fillColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
fillImage |  | string |
handleColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
handleImage |  | string |

Example:
```xml
<Slider minValue="0" maxValue="1" value="0.5" />
```


---


###Dropdown

A dropdown menu. Is able to send the contents of the selection made in it.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When an option is selected, a Lua function with this name will be triggered. | string | *(none)*
text | The string in the text box, if any. Is the value sent to onValueChanged's or onEndEdit's function. | string | *(none)*
interactable |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
textColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
itemBackgroundColors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | #FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)
itemTextColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
checkColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
checkImage |  | string |
arrowColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
arrowImage |  | string |
dropdownBackgroundColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
dropdownBackgroundImage |  | string |
scrollbarColors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) |
scrollbarImage |  | string |
itemHeight |  | float |

Example:
```
 <Dropdown id="Selection" onValueChanged="optionSelected">
    <Option selected="true">Option 1</Option>
    <Option>Option 2</Option>
    <Option>Option 3</Option>
    <Option>Option 4</Option>
</Dropdown>
```
```
 function optionSelected(player, option, id)
    print(player.steam_name .. " selected: " .. option)
 end
```

---
