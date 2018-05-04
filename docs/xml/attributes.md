As mentioned in the [Introduction](xml/introUI), attributes are modifiers that can be applied to elements. They can be applied to individual elements or to whole groups of them.

!!!important 
    They consists of two parts, a **tag** and a **value**. ***The value is always in quotation marks.***

##Attribute types

For XML, most of the attribute types are self-explanatory, like string or float (See Lua Scripting section for details on those). However XML has some unique types.

* **color**
    * **HTML 6 Char Hex**: `#FFFFFF` {>>(white 100% opacity)<<}
    * **8 Char Hex**: `#FFFFFFCC` {>>(white 80% opacity)<<}
    * **RGB Color**: `rgb(1,1,1)` {>>(white 100% opacity)<<}
    * **RGBA Color**: `rgba(1,1,1,0.8)` {>>(white 80% opacity)<<}
* **colorblock**
    * Color block values are used to specify the colors for elements such as buttons and input fields.
    * Format: **(normalColor|highlightedColor|pressedColor|disabledColor)** where each color is formatted as above, e.g. `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
* **bool**
    * **True**: `1` or `true`
    * **False**: `0` or `false`
* **RectOffset**
    * Padding accepts multiple padding values
        * **left/right/top/bottom**: Example: `5 5 10 10`
        * **all sides**: Example: `10`

---

##Common Attributes

All elements share certain Attributes.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
active | Specifies whether or not this element is active. | bool | `true`
class | This allows you to group elements together by giving them the same class. It is used with [Defaults](defaults). | string | (none)
id | Used by Lua scripting to identify an element within the XML. | string | (none)
visibility | What colors are able to see the element. | string | (visible to all)
rectAlignment | Defines this elements position within its parent. Only applies to elements not contained within layout groups. | UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight | MiddleCenter
width | Defines the width of this element. | float (fixed width) or a Percentage value | 100%
height | Defines the height of this element. | float (fixed width) or a Percentage value | 100%
offsetXY | Defines an offset to the position of this element, e.g. a value of `-32 0` will cause this element to be 32 pixels to the left of where it would otherwise be. | float (x) float (y) | 0 0

!!!important
    For visiblity, you can use multiple color names by putting a `|` between each color name. `"Red|Blue|Green"`

---


##Usage

###Single Element Attributes

This is how you would assign attributes to a single element.

####One Attribute

```xml
<Button onClick="test">Hello</Button>
```

####Multiple Attributes

```xml
<Button onClick="test" allowDragging="true">Hello</Button>
```

####Many Attributes

```xml
<Button 
    height="100" 
    width="200"
    color="blue"
    onClick="test"
    allowDragging="true"
    rectAlignment="MiddleRight"
    tooltip="Test Tooltip" 
    tooltipPosition="Above"
    fontSize="32" 
    textColor="#ff0000"
>Hello
</Button>
```

###Defaults

The defaults Tag allows you to set default values for UI elements. Primarily this will be used to set styles and the like, but there is no restriction on what default values you can set.

Defaults can be applied to all instances of a particular tag type, or only those of a particular class (as set by the class attribute). Please note that elements may use more than one class (separated by spaces).

As with its HTML counterpart (CSS), XmlLayout Defaults are applied in a cascading fashion. This means that an element will always use the most recent value for an attribute - for example, if an element implements a class, it will use the attribute values defined by that class except when the element itself also defines those attributes (attributes defined on the element will always take precedence).

Defaults tags can be placed anywhere in the Xml document, but will only apply to elements after it.

**Example:**
```xml
<Defaults>
    <!-- Set the default color and font size for all Text elements -->
    <Text color="#DDDDDD" fontSize="16" />
    
    <!-- Set the default color for all Text elements using the 'darker' class -->
    <Text class="darker" color="#AAAAAA" />    
</Defaults>

<!-- This text's color will be "#DDDDDD" and its font size will be "16" -->
<Text>Text</Text>

<!-- This text's color will be "#AAAAAA" and its font size will be "16" -->
<Text class="darker">Text</Text>

<!-- This button will use the background image "Sprites/Layout/Button" -->
<Button>Button Text</Button>

<!-- Set the default border and text color for all tooltips -->
<Tooltip tooltipBorderColor="rgb(1,1,1)" tooltipTextColor="rgb(1,1,1)" />
```


--- 
