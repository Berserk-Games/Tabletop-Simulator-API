The Custom PDF is a type in-game Spawnable Object that renders a PDF from a URL. It has its own class, Book, with functions/members associated with it. This allows you to manipulate the special properties of a Custom PDF.

Example Usage: `obj.Book.setPage(1, false)`

##Member Variables

Like [Object member variables](object.md#member-variables), Books have their own member variables.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="page_offset"></a>page_offset | The page numbers displayed in the Custom PDF UI are offset by this amount. | [<span class="tag int"></span>](types.md)

!!! info
    For example, if `page_offset` were set to 10, the first page in the UI would be 11, rather than 1. Negative numbers are accepted, and useful if a rule book contains a front cover, index etc. within the PDF file.

##Function Summary

###Object Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
<a class="anchor" id="getpage"></a>getPage([<span class="tag boo"></span>](types.md)&nbsp;offsetPageNumbering) | Gets the current page of the PDF. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#getpage)
<a class="anchor" id="setpage"></a>setPage([<span class="tag int"></span>](types.md)&nbsp;page, [<span class="tag boo"></span>](types.md)&nbsp;offsetPageNumbering) | Set current page. | [<span class="ret boo"></span>](types.md)| [<span class="i"></span>](#setpage)
<a class="anchor" id="sethighlight"></a>setHighlight([<span class="tag flo"></span>](types.md)&nbsp;x1, [<span class="tag flo"></span>](types.md)&nbsp;y1, [<span class="tag flo"></span>](types.md)&nbsp;x2, [<span class="tag flo"></span>](types.md)&nbsp;y2) | Set highlight box on current page. | [<span class="ret boo"></span>](types.md) |  [<span class="i"></span>](#sethighlight)
<a class="anchor" id="clearhighlight"></a>clearHighlight() | Clears the current highlight. | [<span class="ret boo"></span>](types.md)

---

##Function Details

####getPage(...)

[<span class="ret int"></span>](types.md)&nbsp;Gets the current page of the PDF.

!!! info "getPage(offsetPageNumbering)"
	  * [<span class="tag boo"></span>](types.md) **offsetPageNumbering**: Indicates whether or not [page_offset](#page_offset) should be applied to the page number returned.
        * {>>Optional, defaults to `false`.<<}
---

####setPage(...)

[<span class="ret boo"></span>](types.md)&nbsp;Sets the current page of the PDF. Returns true if the page was succesfully set, false if the page number was invalid.

!!! info "setPage(page, offsetPageNumbering)"
    * [<span class="tag int"></span>](types.md) **page**: The new page number.
    * [<span class="tag boo"></span>](types.md) **offsetPageNumbering**: Indicates whether or not [page_offset](#page_offset) should be applied to the page number set.
        * {>>Optional, defaults to `false`.<<}


---

####setHighlight(...)

[<span class="ret boo"></span>](types.md)&nbsp;Draws a highlight rectangle on the popout mode of the PDF at the given coordinates. Coordinates (0,0) are the lower left corner of the PDF, while coordinates (1,1) are the upper right corner.

!!! info "setHighlight(x1, y1, x2, y2)"
    * [<span class="tag flo"></span>](types.md) **x1**: x coordinate of the rectangle's left side.
    * [<span class="tag flo"></span>](types.md) **y1**: y coordinate of the rectangle's bottom side.
    * [<span class="tag flo"></span>](types.md) **x2**: x coordinate of the rectangle's right side.
    * [<span class="tag flo"></span>](types.md) **y2**: y coordinate of the rectangle's top side.

``` Lua
-- Sets highlight of upper right quarter of the pdf
self.Book.setHighlight(0.5, 0.5, 1, 1)
```

!!! bug
    setHighlight() will do nothing if you try to draw a highlight twice in a row at the same coordinates, even if you call clearHighlight() or reload() on the object in between calls to setHighlight().
