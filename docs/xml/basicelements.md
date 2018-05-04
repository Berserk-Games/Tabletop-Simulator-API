These are display-type elements for the UI. They cannot send information to any Lua scripts.

##Element Summary

Element Name | Description | &nbsp;
-- | -- | --
`#!xml <Text></Text>` | Adds basic text. | [<span class="i"></span>](#text)
`#!xml <RawImage></RawImage>` | Loads an image from those that were uploaded to the UI assets. | [<span class="i"></span>](#image)
`#!xml <ProgressBar></ProgressBar>` | Displays a progress bar which can be updated dynamically via script. | [<span class="i"></span>](#progressbar)

---

##Element Details

###Text

Adds basic text.


Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type / Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
alignment | | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> |
color | | color | `#323232`
fontStyle | | <ul><li>Normal</li><li>Bold</li><li>Italic</li><li>BoldItalic</li></ul> | `Normal`
fontSize | | float | `14`
resizeTextForBestFit | Resize text to fit? | bool | `false`
resizeTextMinSize | Minimum font size | float | `10`
resizeTextMaxSize | Maximum font size | float | `40`
horizontalOverflow | | <ul><li>Wrap</li><li>Overflow</li></ul> | `Overflow`
verticalOverflow | | <ul><li>Truncate</li><li>Overflow</li></ul> | `Truncate`

###RawImage

Displays an image from those that were uploaded to the UI assets.

!!!Tip
    To upload an image, with the scripting window open, click on the "Custom UI Assets" button in the upper right.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type / Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
texture | | string | none )
color | | color | `#FFFFFF`
type | Image Type | <ul><li>Simple</li><li>Sliced</li><li>Filled</li><li>Tiled</li></ul> | `Simple`
raycastTarget | Will the element block clicks? | bool | `true`


###ProgressBar

Displays a progress bar which can be updated dynamically via script.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type / Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
image | Background Image | (path to image) | none
color | Background Color | color | `#FFFFFF`
fillImageColor | Fill Color | color | `#FFFFFF`
percentage | Percentage to Display | float | `0`
showPercentageText | Is the percentage text displayed? | bool | `true`
percentageTextFormat | Format to use for the percentage text | string | `0.00`
textColor | Percentage Text Color | color | `#000000`
textShadow | Percentage Text Shadow Color | color | none
textOutline | Percentage Text Outline Color  | color | none
textAlignment | Percentage Text Alignment | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `MiddleCenter`
