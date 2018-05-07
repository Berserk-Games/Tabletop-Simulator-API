As mentioned in the [Introduction](xml/introUI), attributes are modifiers that can be applied to elements. They can be applied to individual elements or to whole groups of them.

!!!important 
    They consists of two parts, a **tag** and a **value**. ***The value is always in quotation marks.***

##Attribute types

For XML, most of the attribute types are self-explanatory, like string or float (See Lua Scripting section for details on those). However XML has some unique types.

* <span class="tag xmlco"></span>
    * **HTML 6 Char Hex**: `#FFFFFF` {>>(white 100% opacity)<<}
    * **8 Char Hex**: `#FFFFFFCC` {>>(white 80% opacity)<<}
    * **RGB Color**: `rgb(1,1,1)` {>>(white 100% opacity)<<}
    * **RGBA Color**: `rgba(1,1,1,0.8)` {>>(white 80% opacity)<<}
* <span class="tag xmlcb"></span>
    * Color block values are used to specify the colors for elements such as buttons and input fields.
    * Format: **(normalColor|highlightedColor|pressedColor|disabledColor)** where each color is formatted as above, e.g. `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
* <span class="tag boo"></span>
    * **True**: `1` or `true`
    * **False**: `0` or `false`

---

##Common Attributes

Elements all share some common attributes which are not repeated under their separate entries. They can be broker down into category.

###General Attributes

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
active | Specifies whether or not this element is active. This can be used to hide/show elements via scripting. | bool | `true`
class | This allows you to group elements together by giving them the same class. It is used with [Defaults](defaults). | string | (none)
id | Used by Lua scripting to identify an element within the XML. | string | (none)
visibility | What colors are able to see the element. | string | (visible to all)

!!!important "Designating Multiple Visibility Targets"
    For visiblity, you can use multiple color names by putting a `|` between each color name. `"Red|Blue|Green"`
    

###Image Attributes
Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
preserveAspect | Should the aspect ratio of this image be preserved? | [<span class="tag boo"></span>](attributes#attribute-types) | *(varies)*
color | Color for this element's image	 | [<span class="tag xmlco"></span>](attributes#attribute-types) | `clear` or `#FFFFFF`
type | Image Type | Simple, Sliced, Filled, Tiled | *(varies)*
raycastTarget | If the element blocks clicks. | [<span class="tag boo"></span>](attributes#attribute-types) | `true`


###Appearance Attributes

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
shadow | Defines the shadow color of this element. | [<span class="tag xmlco"></span>](attributes#attribute-types) | (none)
shadowDistance | Defines the distance of the shadow for this element. | float(x) float(y) | `1 -1`
outline | Defines the outline color of this element. | [<span class="tag xmlco"></span>](attributes#attribute-types) | (none)
outlineSize | Defines the size of this elements outline. | float(x) float(y) | `1 -1`

###Layout Element Attributes

These will only apply to elements within a layout group.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
ignoreLayout | Should this element ignore its parent layout group? | [<span class="tag boo"></span>](attributes#attribute-types) | `false`
minWidth | 	Minimum width for this element. | float | 
minHeight | 	Minimum height for this element. | float | 
preferredWidth | Preferred width for this element. | float | 
preferredHeight | Preferred height for this element. | float | 
flexibleWidth | Should the width of this element be flexible? | <ul><li>1</li><li>0</li></ul> | 
flexibleHeight | Should the height of this element be flexible? | <ul><li>1</li><li>0</li></ul> | 

###Position/Size Attributes (Basic)

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
rectAlignment | Defines this elements position within its parent. Only applies to elements not contained within layout groups. | UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight | `MiddleCenter`
width | Defines the width of this element. | float (fixed width) or a Percentage value | `100%`
height | Defines the height of this element. | float (fixed width) or a Percentage value | `100%`
offsetXY | Defines an offset to the position of this element, e.g. a value of `-32 0` will cause this element to be 32 pixels to the left of where it would otherwise be. | float (x) float (y) | `0 0`

###Position/Size Attributes (Adv)

These provide deeper access to Unity's [RectTransform](https://docs.unity3d.com/ScriptReference/RectTransform.html) properties.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
anchorMin |  | float(x) float(y) | 
anchorMax |  | float(x) float(y) | 
sizeDelta |  | float(x) float(y) | 
pivot |  | float(x) float(y) | 
rotation |  | float(x) float(y) float(z) | 
scale |  | float(x) float(y) | 
offsetMin |  | float(left) float(bottom) | 
offsetMax |  | float(left) float(bottom) | 

###Dragging Attributes

Allow users to move elements by click/dragging.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
allowDragging | Allow this element to be dragged? <br>{>>Does not work on child elements of layout groups)<<} | [<span class="tag boo"></span>](attributes#attribute-types) | `false`
restrictDraggingToParentBounds | Prevent this element from being dragged outside of its parent? | [<span class="tag boo"></span>](attributes#attribute-types) | `true`
returnToOriginalPositionWhenReleased | If this is set to true, then the element will return to its original position when it is released. | [<span class="tag boo"></span>](attributes#attribute-types) | `true`

###Animation Attributes

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
showAnimation |  | <ul><li>None</li><li>Grow</li><li>FadeIn</li><li>SlideIn_Left</li><li>SlideIn_Right</li><li>SlideIn_Top</li><li>SlideIn_Bottom</li></ul> | `None`
hideAnimation |  | <ul><li>None</li><li>Shrink</li><li>FadeOut</li><li>SlideOut_Left</li><li>SlideOut_Right</li><li>SlideOut_Top</li><li>SlideOut_Bottom</li></ul> | `None`
showAnimationDelay | Adds a short delay before playing this element's show animation. | float | `0`
hideAnimationDelay | Adds a short delay before playing this element's hide animation. | float | `0`
animationDuration | Specifies how long show/hide animations should take to play. | float | `0.25`

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


--- 
