These are display-type elements for the UI. They cannot send information to any Lua scripts.

Each element has its own attributes specific to its type that work in addition to the [common attributes](attributes.md#common-attributes).

##Element Summary

Element Name | Description | &nbsp;
-- | -- | --
`#!xml <Text></Text>` | Adds basic text. | [<span class="i"></span>](#text)
`#!xml <Image></Image>` | Adds an image. | [<span class="i"></span>](#image)
`#!xml <ProgressBar></ProgressBar>` | Displays a progress bar which can be updated dynamically via script. | [<span class="i"></span>](#progressbar)

---

##Element Details

###Text

Adds basic text. This tag supports Rich Text as shown in the example below.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type / Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
text | This can be used to determine the text that appears. It can also be modified externally by the script. | string | *(none)*
alignment | | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | MiddleCenter
color | | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#323232`
fontStyle | | <ul><li>Normal</li><li>Bold</li><li>Italic</li><li>BoldItalic</li></ul> | `Normal`
fontSize | | float | `14`
resizeTextForBestFit | Resize text to fit? | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
resizeTextMinSize | Minimum font size | float | `10`
resizeTextMaxSize | Maximum font size | float | `40`
horizontalOverflow | | <ul><li>Wrap</li><li>Overflow</li></ul> | `Overflow`
verticalOverflow | | <ul><li>Truncate</li><li>Overflow</li></ul> | `Truncate`

Example:
```xml
<!-- Standard Text element -->
<Text>Some Text</Text>

<!-- Rich Text -->
<Text>
    This text is <b>Bold</b>, <i>Italic</i>, 
    and <textcolor color="#00FF00">Green</textcolor>.    
    This text is <textsize size="18">Larger</textsize>.
</Text>
```

---


###Image

Adds an image.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
image | The name of the file in the asset manager (upper right corner of the scripting window in-game). | string | *(none)*
color |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
type | Image Type | <ul><li>Simple</li><li>Sliced</li><li>Filled</li><li>Tiled</li></ul> | `Simple`
raycastTarget | Should this image block clicks from passing through it? | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`

---


###ProgressBar

Displays a progress bar which can be updated dynamically via script.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type / Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
image | Background Image | (path to image) | *(none)*
color | Background Color | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
fillImage | Fill Image | string | *(none)*
fillImageColor | Fill Color | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
percentage | Percentage to Display | float | `0`
showPercentageText | Is the percentage text displayed? | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
percentageTextFormat | Format to use for the percentage text | string | `0.00`
textColor | Percentage Text Color | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#000000`
textShadow | Percentage Text Shadow Color | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textOutline | Percentage Text Outline Color  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | *(none)*
textAlignment | Percentage Text Alignment | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `MiddleCenter`

---
