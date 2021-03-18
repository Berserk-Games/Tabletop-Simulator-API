Grid, a static global class, controls the in-game grid. It allows you to manipulate the placement and appearance of the grid in the same way as the in-game interface.

Example usage: `Grid.show_lines = true`.

##Member Variables

Variable | Description | Type
-- | -- | :--
type {: #type } | The type of the grid. 1 = Rectangles, 2 = Horizontal hexes, 3 = Vertical hexes.  | [<span class="tag int"></span>](types.md)
show_lines {: #show_lines } | Visibility of the grid lines. | [<span class="tag boo"></span>](types.md)
color {: #color } | Color of the grid lines. | [<span class="tag col"></span>](types.md)
opacity {: #opacity } | Opacity of the grid lines. | [<span class="tag flo"></span>](types.md)
thick_lines {: #thick_lines } | Thickness of the grid lines. false = Thin, true = Thick. | [<span class="tag boo"></span>](types.md)
snapping {: #snapping } | Method of snapping objects to the grid. 1 = Off, 2 = Lines, 3 = Center, 4 = Both. | [<span class="tag int"></span>](types.md)
offsetX {: #offsetx } | X offset of the grid origin. | [<span class="tag flo"></span>](types.md)
offsetY {: #offsety } | Y offset of the grid origin. | [<span class="tag flo"></span>](types.md)
sizeX {: #sizex } | Width of the grid cells. | [<span class="tag flo"></span>](types.md)
sizeY {: #sizey } | Height of the grid cells. | [<span class="tag flo"></span>](types.md)
