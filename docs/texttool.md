TextTool is a special Object type for creating text labels in the game instance. It is the same text that is created with the [text tool](http://berserk-games.com/knowledgebase/1958/). You call these functions like this: `self.TextTool.getFontColor()`.

##Function Summary

###Object Functions

Function Name | Description | Return 
-- | -- | -- 
getFontColor()  | Returns Table of font Color. | [<span class="ret col"></span>](intro#color)
getFontSize()  | Returns Int of the font size. | [<span class="ret int"></span>](intro#types)
getValue()  | Returns the current text. Works the same as Object's [getValue()](object#getvalue). | [<span class="ret str"></span>](intro#types)
setFontColor([<span class="tag col"></span>](intro#color)&nbsp;font_color) | Sets font Color. | [<span class="ret boo"></span>](intro#types)
setFontSize([<span class="tag int"></span>](intro#types)&nbsp;font_size) | Sets font size. | [<span class="ret boo"></span>](intro#types)
setValue([<span class="tag str"></span>](intro#types)&nbsp;text) | Sets the current text. Works the same as Object's [setValue(...)](object#setvalue). | [<span class="ret boo"></span>](intro#types)
