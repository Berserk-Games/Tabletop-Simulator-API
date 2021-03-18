As mentioned in the [Introduction](introUI.md), attributes are modifiers that can be applied to elements. They can be applied to individual elements or to whole groups of them.

!!!important
    They consists of two parts, a **tag** and a **value**. ***The value is always in quotation marks.***

## Attribute types

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

## Common Attributes

Elements all share some common attributes which are not repeated under their separate entries. They can be broker down into category.

### General Attributes

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
active | Specifies whether or not this element and its children are visible and contribute to layout. Modifying this via script will not trigger animations. | bool | `true`
class | A list of classes, separated by spaces. An element will inherit attributes from any of its classes defined in [Defaults](defaults.md). | string | *(none)*
id | A unique string used to identify the element from Lua scripting. | string | *(none)*
visibility | A pipe-separated list of visibility targets. An element is always treated as inactive to players not specified here. | string | *(visible to all)*

!!!note "Visibility Targets"
    Targets for the `visibility` attribute are as follows:

    * The game host: `Host`
    * Any promoted player (including the host): `Admin`
    * Every [player color](../player/colors.md): `White`, `Brown`, `Red`, `Orange`, `Yellow`, `Green`, `Teal`, `Blue`, `Purple`, `Pink`, `Grey`, and `Black`
    * Every [team](../player/instance.md#team): `Clubs`, `Diamonds`, `Hearts`, `Spades`, `Jokers`, and `None`

    Not setting the visibility attribute (or setting it to an empty string) does not limit the visibility of the element.

    Multiple targets can be listed by separating them with a pipe (`|`). In this case if *any* of the targets applies to a player then the element will be active for that player.

    Example: `"Red|Blue|Host"` would be visible to the red seat, blue seat, and the host of the server.

### Text Attributes

Many, but not all, elements have a text attribute.

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
text | Text to be displayed. | string | *(none)*
alignment | Typographic alignment of the text within its bounding box. | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `MiddleCenter`
color | Color of the text. Elements that also take an image `color` use `textColor` for this. | [<span class="tag xmlco"></span>](#attribute-types) | `#323232`
fontStyle | Typographic emphasis on the text. | <ul><li>Normal</li><li>Bold</li><li>Italic</li><li>BoldAndItalic</li></ul> | `Normal`
fontSize | Height of the text in pixels. | float | `14`
resizeTextForBestFit | If set then `fontSize` is ignored and the text will be sized to be as large as possible while still fitting within its bounding box. | [<span class="tag boo"></span>](#attribute-types) | `false`
resizeTextMinSize | When `resizeTextForBestFit` is set, text will not be sized smaller than this. | float | `10`
resizeTextMaxSize | When `resizeTextForBestFit` is set, text will not be sized larger than this. | float | `40`
horizontalOverflow | Defines what happens when text extends beyond the left or right edges of its bounding box. | <ul><li>Wrap</li><li>Overflow</li></ul> | `Overflow`
verticalOverflow | Defines what happens when text extends beyond the top or bottom edges of its bounding box. | <ul><li>Truncate</li><li>Overflow</li></ul> | `Truncate`

### Image Attributes

Applies to elements with an image component. The string that `image`s all take is the **NAME THE IMAGE WAS GIVEN WHEN YOU PUT IT IN THE IN-GAME ASSET MANAGER**.

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
image | Name of the image in the asset manager. | string | *(none)*
preserveAspect | If set, the image will not stretch beyond its original aspect ratio, potentially leaving gaps around the image. | [<span class="tag boo"></span>](#attribute-types) | *(varies)*
color | Color to tint the image, or a flat color to display if no image is given. | [<span class="tag xmlco"></span>](#attribute-types) | `clear` or `#FFFFFF`
type | Defines how the image is drawn. | <ul><li>Simple</li><li>Sliced</li><li>Filled</li><li>Tiled</li></ul> | *(varies)*
raycastTarget | If the element blocks clicks. | [<span class="tag boo"></span>](#attribute-types) | `true`

### Appearance Attributes

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
shadow | Defines the shadow color of this element. | [<span class="tag xmlco"></span>](#attribute-types) | *(none)*
shadowDistance | Defines the distance of the shadow for this element. | float(x) float(y) | `1 -1`
outline | Defines the outline color of this element. | [<span class="tag xmlco"></span>](#attribute-types) | *(none)*
outlineSize | Defines the size of this elements outline. | float(x) float(y) | `1 -1`

### Layout Element Attributes

These will only apply to elements within a layout group.

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
ignoreLayout | If this element ignores its parent's layout group behavior and treats it as a regular Panel. (This means it would obey regular position/size attributes.) | [<span class="tag boo"></span>](#attribute-types) | `false`
minWidth | Elements will not be sized thinner than this. | float | *(varies)*
minHeight | Elements will not be sized shorter than this. | float | *(varies)*
preferredWidth | If there is space after `minWidth`s are sized, then element widths are sized according to this. | float | *(varies)*
preferredHeight | If there is space after `minHeight`s are sized, then element heights are sized according to this. | float | *(varies)*
flexibleWidth | If there is additional space after `preferredWidth`s are sized, defines how much the element expands to fill the available horizontal space, relative to other elements. | float | *(varies)*
flexibleHeight | If there is additional space after `preferredHeights`s are sized, defines how much the element expands to fill the available vertical space, relative to other elements. | float | *(varies)*

!!!note "On Sizing Elements"
    Minimum and preferred sizes are defined in regular units, while the flexible sizes are defined in relative units. If any layout element has flexible size greater than zero, it means that all the available space will be filled out. The relative flexible size values of the siblings determines how big a proportion of the available space each sibling fills out. Most commonly, flexible width and height is set to just 0 or 1.

### Position/Size Attributes (Basic)

!!!important
    These attributes do not apply to elements that are direct children of layout groups. To size those elements see [Layout Element Attributes](#layout-element-attributes).

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
rectAlignment | The element's anchor and pivot point, relative to its parent element. | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `MiddleCenter`
width | The width of this element in pixels or as a percentage of the width of its parent. | float (fixed width) or a Percentage value | `100%`
height | The height of this element in pixels or as a percentage of the height of its parent. | float (fixed width) or a Percentage value | `100%`
offsetXY | An offset to the position of this element, e.g. a value of `-32 10` will cause this element to be 10 pixels up and 32 pixels to the left of where it would otherwise be. | float(x) float(y) | `0 0`

### Position/Size Attributes (Advanced)

These provide deeper access to Unity's [RectTransform](https://docs.unity3d.com/ScriptReference/RectTransform.html) properties.

!!!important
    Besides `rotation` and `scale`, these attributes do not apply to elements that are direct children of layout groups. To size those elements see [Layout Element Attributes](#layout-element-attributes).

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
anchorMin | The anchor point for the bottom-left corner of the element, where `0 0` is its parent's bottom-left corner and `1 1` is its parent's top-right corner. | float(x) float(y) | *(varies)*
anchorMax | The anchor point for the top-right corner of the element, where `0 0` is its parent's bottom-left corner and `1 1` is its parent's top-right corner. | float(x) float(y) | *(varies)*
sizeDelta | An offset to the size of the element, e.g. a value of `15 -20` will cause this element to be 15 pixels wider and 32 pixels shorter than what it would otherwise be. | float(x) float(y) | *(varies)*
pivot | The pivot point this element is positioned, rotated, and scaled around. `0 0` is the element's bottom-left corner and `1 1` is its top-right corner. | float(x) float(y) | `0.5 0.5`
position | An offset to the position of this element in 3D space. Z moves the element in and out. | float(x) float(y) float(z) | `0 0 0`
rotation | Rotates the element in 3D space. X and Y tilt it like a dish, Z turns it like a steering wheel. | float(x) float(y) float(z) | `0 0 0`
scale | Scales the component around its pivot. Note that this does not add more pixel detail, text with small font and other elements may appear pixelated or blurry. Z does not affect the thickness of the element (it is always flat), but does affect the transforms of its children. | float(x) float(y) float(z) | `1 1 1`
offsetMin | An offset in pixels from `anchorMin` to be used as the bottom-left corner of the element. | float(x) float(y) | *(varies)*
offsetMax | An offset in pixels from `anchorMax` to be used as the top-right corner of the element. | float(x) float(y) | *(varies)*

!!!warning "Mixing Attributes"
    Some [Advanced Position/Size Attributes](#positionsize-attributes-advanced) affect the same underlying properties as the [Basic Position/Size Attributes](#positionsize-attributes-basic) and other Advanced Position/Size Attributes. Using these overlapping attributes on the same element will cause one attribute to be effectively overwritten, and may result in unexpected behaviour.

!!!note "Elements in 3D Space"
    Moving elements in 3D space can achieve parallax and perspective effects, but elements later in the XML will always be drawn on top of elements earlier in the same XML, and will not occlude as other 3d objects would. To avoid any visual glitches, try to make sure unrelated UI elements can't be seen overlapping when viewed from most angles. Global UI has no perspective and is always 2D.

### Dragging Attributes

Allow users to move elements by clicking/dragging.

!!!note
    There is currently no reliable way to read the positions of elements, and dragged positions reset when the UI is reloaded.

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
allowDragging | Allows the element to be dragged around. <br>{>>Does not work on child elements of layout groups)<<} | [<span class="tag boo"></span>](#attribute-types) | `false`
restrictDraggingToParentBounds | If set, prevents the element from being dragged outside the bounding box of its parent. | [<span class="tag boo"></span>](#attribute-types) | `true`
returnToOriginalPositionWhenReleased | If this is set to true, then the element will return to its original position when it is released. | [<span class="tag boo"></span>](#attribute-types) | `true`

### Animation Attributes

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
showAnimation | Animation to play when `show()` is called for the element. | <ul><li>None</li><li>Grow</li><li>FadeIn</li><li>SlideIn_Left</li><li>SlideIn_Right</li><li>SlideIn_Top</li><li>SlideIn_Bottom</li></ul> | `None`
hideAnimation | Animation to play when `hide()` is called for the element. | <ul><li>None</li><li>Shrink</li><li>FadeOut</li><li>SlideOut_Left</li><li>SlideOut_Right</li><li>SlideOut_Top</li><li>SlideOut_Bottom</li></ul> | `None`
showAnimationDelay | Time in seconds to wait before playing this element's show animation. Useful for staggering the animations of multiple elements. | float | `0`
hideAnimationDelay | Time in seconds to wait before playing this element's hide animation. Useful for staggering the animations of multiple elements. | float | `0`
animationDuration | Time in seconds that show/hide animations take to play. | float | `0.25`

### Tooltip Attributes

Allow any element to have a tooltip (text that appears when the element is hovered over by the mouse).

Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Value
-- | -- | -- | --
tooltip | Text to display when the element is hovered over. | string | *(none)*
tooltipBorderColor | Color of the tooltip's border. | [<span class="tag xmlco"></span>](#attribute-types) | `#FFFFFF`
tooltipBackgroundColor | Color of the tooltip's background. | [<span class="tag xmlco"></span>](#attribute-types) | `rgba(0,0,0,0.62)`
tooltipBorderImage | Image used for the tooltip's border. See [Image Attributes](#image-attributes). | string |
tooltipBackgroundImage | Image used for the tooltip's background. See [Image Attributes](#image-attributes). | string |
tooltipTextColor | Color of the text within this tooltip. | [<span class="tag xmlco"></span>](#attribute-types) | `#FFFFFF`
tooltipPosition | Position of this tooltip in relation to the element. | <ul><li>Above</li><li>Below</li><li>Left</li><li>Right</li></ul> | `Right`
tooltipOffset | Distance in pixels that this tooltip will appear from the element. | float | `8`

### Event Attributes

Allows Lua scripting functions to be triggered by an element, through a variety of interactions. All elements have no events by default, listed below is the default value passed as the 2nd parameter to the triggered function.

See the [Input Elements](inputelements.md) page for how to interact with Lua scripting.


Attribute&nbsp;Name | Description | Type&nbsp;/&nbsp;Options | Default&nbsp;Argument
-- | -- | -- | --
onClick | Called when the mouse is pressed while over the element and then released while still over it. | string | The click button
onMouseEnter | Called when the pointer enters the boundary of the element. | string | `"-1"`
onMouseExit | Called when the pointer leaves the boundary of the element. | string | `"-1"`
onDrag | Called every frame if the element is being dragged and has moved that frame. | string | `nil`
onBeginDrag | Called once when the element starts being dragged. | string | `nil`
onEndDrag | Called once when the element stops being dragged and the mouse button is released. | string | `nil`
onMouseDown | Called when the mouse is pressed while over the element. | string | The click button
onMouseUp | Called when the mouse is released, if it had previously been pressed while over the element (no matter where the cursor currently is). | string | The click button
onSubmit | Called when the Enter/Return key is pressed on an [Input Element](inputelements.md). | string | The value of the input element

!!!note
    `onClick`, `onMouseDown` and `onMouseUp` all pass the click button. They hold digits, but their data type is **string**. The possible values are:

    - `"-1"`: Left mouse button
    - `"-2"`: Right mouse button
    - `"-3"`: Middle mouse button
    - `"1"`: Single touch
    - `"2"`: Double touch
    - `"3"`: Triple touch

    `onMouseEnter` and `onMouseExit` also pass click buttons, but the value is always `"-1"`.

---

## Usage

### Single Element Attributes

This is how you would assign attributes to a single element.

#### One Attribute

```xml
<Button onClick="test">Hello</Button>
```

#### Multiple Attributes

```xml
<Button onClick="test" allowDragging="true">Hello</Button>
```

#### Many Attributes

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
