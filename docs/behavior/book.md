The Book behavior is present on Custom PDF Objects. The Book behaviour allows you to manipulate the displayed PDF.

## Member Variables

Variable | Type | Description
-- | -- | :--
page_offset {: #page_offset } | [<span class="tag int"></span>](../types.md) | The page numbers displayed in the Custom PDF UI are offset by this amount.

!!! info
    For example, if `page_offset` were set to 10, the first page in the UI would be 11, rather than 1. Negative numbers are accepted, and useful if a rule book contains a front cover, index etc. within the PDF file.

## Function Summary

Function Name | Return | Description  | &nbsp;
-- | -- | -- | --
clearHighlight() {: #clearhighlight data-toc-label="clearHighlight()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Clears the current highlight.
getPage([<span class="tag boo"></span>](../types.md) offsetPageNumbering)  | [<span class="ret int"></span>](../types.md) | Gets the current page of the PDF. | [:i:](#getpage)
setHighlight([<span class="tag flo"></span>](../types.md) x1, [<span class="tag flo"></span>](../types.md) y1, [<span class="tag flo"></span>](../types.md) x2, [<span class="tag flo"></span>](../types.md) y2) | [<span class="ret boo"></span>](../types.md) | Set highlight box on current page.| [:i:](#sethighlight)
setPage([<span class="tag int"></span>](../types.md) page, [<span class="tag boo"></span>](../types.md) offsetPageNumbering) | [<span class="ret boo"></span>](../types.md) | Set current page.| [:i:](#setpage)

---

## Function Details {: data-toc-sort }

#### getPage(...)

[<span class="ret int"></span>](../types.md) Gets the current page of the PDF.

!!! info "getPage(offsetPageNumbering)"
	  * [<span class="tag boo"></span>](../types.md) **offsetPageNumbering**: Indicates whether or not [page_offset](#page_offset) should be applied to the page number returned.
        * {>>Optional, defaults to `false`.<<}
---

#### setHighlight(...)

[<span class="ret boo"></span>](../types.md) Draws a highlight rectangle on the popout mode of the PDF at the given coordinates. Coordinates (0,0) are the lower left corner of the PDF, while coordinates (1,1) are the upper right corner.

!!! info "setHighlight(x1, y1, x2, y2)"
    * [<span class="tag flo"></span>](../types.md) **x1**: x coordinate of the rectangle's left side.
    * [<span class="tag flo"></span>](../types.md) **y1**: y coordinate of the rectangle's bottom side.
    * [<span class="tag flo"></span>](../types.md) **x2**: x coordinate of the rectangle's right side.
    * [<span class="tag flo"></span>](../types.md) **y2**: y coordinate of the rectangle's top side.

!!!example
    Highlight the upper right quarter of a PDF.
    ```lua
    object.Book.setHighlight(0.5, 0.5, 1, 1)
    ```

---

#### setPage(...)

[<span class="ret boo"></span>](../types.md) Sets the current page of the PDF. Returns true if the page was succesfully set, false if the page number was invalid.

!!! info "setPage(page, offsetPageNumbering)"
    * [<span class="tag int"></span>](../types.md) **page**: The new page number.
    * [<span class="tag boo"></span>](../types.md) **offsetPageNumbering**: Indicates whether or not [page_offset](#page_offset) should be applied to the page number set.
        * {>>Optional, defaults to `false`.<<}
