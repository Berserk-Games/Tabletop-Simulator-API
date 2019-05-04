boundaryAs mentioned in the [Introduction](xml/introUI), attributes are modifiers that can be applied to elements. They can be applied to individual elements or to whole groups of them.

!!!important
    They consists of two parts, a **tag** and a **value**. ***The value is always in quotation marks.***

##Attribute types

For XML, most of the attribute types are self-explanatory, like string or float (See Lua Scripting section for details on those). However XML has some unique types.

* <span class="tag xmlco"></span>
    * **HTML 6 Char Hex**: `#FFFFFF` {>>(white 100% opacity)<<}
    * **8 Char Hex**: `#FFFFFFCC` {>>(white 80% opacity)<<}
    * **RGB Color**: `rgb(1,1,1)` {>>(white 100% opacity)<<}
    * **RGBA Color**: `rgba(1,1,1,0.8)` {>>(white 80% opacity)<<}
    * **Player Color**: `White` {>>(white 100% opacity)<<}
* <span class="tag xmlcb"></span>
    * Color block values are used to specify the colors for elements such as buttons and input fields.
    * Format: **(normalColor|highlightedColor|pressedColor|disabledColor)** where each color is formatted as above, e.g. `#FFFFFF|White|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
* <span class="tag boo"></span>
    * **True**: `1` or `true`
    * **False**: `0` or `false`

---

##Common Attributes

Elements all share some common attributes which are not repeated under their separate entries. They can be broker down into category.

###General Attributes
Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
active | Specifies whether or not this element is active. This can be used to hide/show elements via scripting. Triggering this via script will not trigger animations. | bool | `true`
class | This allows you to group elements together by giving them the same class. It is used with [Defaults](defaults). | string | (none)
id | Used by Lua scripting to identify an element within the XML. | string | (none)
isDropReceiver | Determine if an object triggers onElementDropped. | bool | false
visibility | What colors are able to see the element. See below for additional details. | string | (visible to all)

####Visibility Targets
The visibility attribute allows for only certain people or groups to see an element. Hiding an element will hide its children as well.

#####Visible To All Players
Not using the visibility attribute (or setting it to an empty string) does not limit the visibility of the element.

#####Visiblity Selection
* `Host`:  Only visible to the game host.
* `Admin`: Only visible to the host and any promoted player.
* `Red`: Only visible to the player in that seat color. (Works with all valid [color names](/player-color))
* `Clubs`: Only visible to members of that player group. (Works with all valid [team names](/player#team))

#####Combining Groups
You are able to list multiple color names in a single string by placing a vertical line `|` between valid entries.

Example: `"Red|Blue|Host"` would be visible to the red seat, blue seat and the host of the server.



###Text Attributes
Many, but not all, elements have a text attribute.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
text | This can be used to determine the text that appears. It can also be modified externally by the script. | string | *(none)*
alignment | | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | MiddleCenter
color | | [<span class="tag xmlco"></span>](attributes#attribute-types) | `#323232`
fontStyle | | <ul><li>Normal</li><li>Bold</li><li>Italic</li><li>BoldItalic</li></ul> | `Normal`
fontSize | | float | `14`
resizeTextForBestFit | Resize text to fit? | [<span class="tag boo"></span>](attributes#attribute-types) | `false`
resizeTextMinSize | Minimum font size | float | `10`
resizeTextMaxSize | Maximum font size | float | `40`
horizontalOverflow | | <ul><li>Wrap</li><li>Overflow</li></ul> | `Overflow`
verticalOverflow | | <ul><li>Truncate</li><li>Overflow</li></ul> | `Truncate`


###Image Attributes
Applies to elements with an image component. The string that `image`s all take is the **NAME THE IMAGE WAS GIVEN WHEN YOU PUT IT IN THE IN-GAME ASSET MANAGER**.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
image | Name of image (in the asset manager). | string | (*none*)
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
position |  | float(x) float(y) float(z) |
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


###Tooltip Attributes
Allow any element to have a tooltip (text that appears when the element is hovered over by the mouse).

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
tooltip | Tooltip text. | string | *(none)*
tooltipBorderColor | Color of the tooltips border. | [<span class="tag xmlco"></span>](attributes#attribute-types) | `#FFFFFF`
tooltipBackgroundColor | Color of the tooltips background | [<span class="tag xmlco"></span>](attributes#attribute-types) | `rgba(0,0,0,0.62)`
tooltipTextColor | Color of the text within this tooltip | [<span class="tag xmlco"></span>](attributes#attribute-types) |
tooltipPosition | Position of this tooltip in relation to the element. | <ul><li>Above</li><li>Below</li><li>Left</li><li>Right</li></ul> | `Right`
tooltipBorderImage | This attribute allows you to override the default image used for the tooltips border. | string |
tooltipBackgroundImage | This attribute allows you to override the default image used for the tooltips background. | string |
tooltipOffset | This attribute allows you to modify the distance this tooltip will appear from the element. | float |

###Event Attributes
Allows Lua scripting events to be triggered by any element, through a variety of interactions. See the [Input Elements](inputelements) page for how to interact with Lua scripting.

Attribute&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onClick | Clicking on the element. | string |
onMouseEnter | Pointer entering the boundary of the element. | string |
onMouseExit | Pointer leaving the boundary of the element. | string |
onDrag | Element drag event. | string |
onBeginDrag | Element beginning to be dragged. | string |
onEndDrag | Element being release from its drag. | string |
onMouseDown | Mouse click action. | string |
onMouseUp | Mouse click finishing action. | string |
onSubmit |  | string |
onElementDropped | An element needs isDropReceiver for this to trigger | string

!!!note
    onClick, onMouseEnter, onMouseExit, onMouseDown and onMouseUp all pass the click button. The values are -1 LMB, -2RMB, -3 MMB, 0 touch single, 1 double touche, 2 triple touch.





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
