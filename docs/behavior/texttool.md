TextTool is a special Object type for creating text labels in the game instance. It is the same text that is created with the [text tool](https://kb.tabletopsimulator.com/game-tools/text-tool/). You call these functions like this: `self.TextTool.getFontColor()`.

##Function Summary

###Object Functions

Function Name | Description | Return
-- | -- | --
getFontColor()  {: #getfontcolor } | Returns Table of font Color. | [<span class="ret col"></span>](../types.md#color)
getFontSize()  {: #getfontsize } | Returns Int of the font size. | [<span class="ret int"></span>](../types.md)
getValue()  {: #getvalue } | Returns the current text. Works the same as Object's [getValue()](../object.md#getvalue). | [<span class="ret str"></span>](../types.md)
setFontColor([<span class="tag col"></span>](../types.md#color) font_color) {: #setfontcolor } | Sets font Color. | [<span class="ret boo"></span>](../types.md)
setFontSize([<span class="tag int"></span>](../types.md) font_size) {: #setfontsize } | Sets font size. | [<span class="ret boo"></span>](../types.md)
setValue([<span class="tag str"></span>](../types.md) text) {: #setvalue } | Sets the current text. Works the same as Object's [setValue(...)](../object.md#setvalue). | [<span class="ret boo"></span>](../types.md)
