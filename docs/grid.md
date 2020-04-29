Grid, a static global class, controls the in-game grid. It allows you to manipulate the placement and appearance of the grid in the same way as the in-game interface.

Example usage: `Grid.show_lines = true`.

##Member Variables

Like [Object member variables](object.md#member-variables), Grid has its own member variables. They allow for direct access to the Grid's properties.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="type"></a>type | The type of the grid. 1 = Rectangles, 2 = Horizontal hexes, 3 = Vertical hexes.  | [<span class="tag int"></span>](types.md)
<a class="anchor" id="show_lines"></a>show_lines | Visibility of the grid lines. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="color"></a>color | Color of the grid lines. | [<span class="tag col"></span>](types.md)
<a class="anchor" id="opacity"></a>opacity | Opacity of the grid lines. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="thick_lines"></a>thick_lines | Thickness of the grid lines. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="offsetx"></a>offsetX | X offset of the grid origin. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="offsety"></a>offsetY | Y offset of the grid origin. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="sizex"></a>sizeX | Width of the grid cells. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="sizey"></a>sizeY | Height of the grid cells. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="snapping"></a>snapping | Method of snapping objects to the grid. 1 = Off, 2 = Lines, 3 = Center, 4 = Both. | [<span class="tag int"></span>](types.md)
