By nesting elements within layouts/groupings, you are able to easily group elements together in-game. It allows for adjusting/moving them together, uniform padding and additional visual flair possibilities.

Each layout element has its own attributes specific to its type. Additionally, elements within a layout are subject to common [common layout element attributes](attributes.md#layout-element-attributes).

##Element Summary

###Layout Summary
Element Name | Description | &nbsp;
-- | -- | --
`#!xml <Panel></Panel>` | A "window" in which elements can be confined. | [<span class="i"></span>](#panel)
`#!xml <HorizontalLayout></HorizontalLayout>` | A horizontal row of elements. | [<span class="i"></span>](#horizontallayout)
`#!xml <VerticalLayout></VerticalLayout>` | A vertical column of elements. | [<span class="i"></span>](#verticallayout)
`#!xml <GridLayout></GridLayout>` | A grid of elements. | [<span class="i"></span>](#gridlayout)
`#!xml <TableLayout></TableLayout>` | A layout element based on HTML tables, allowing you to specify the position of elements in specific rows/columns. | [<span class="i"></span>](#tablelayout)
`#!xml <Row></Row>` | A row within a TableLayout. | [<span class="i"></span>](#row)
`#!xml <Cell></Cell>` | A cell within a TableLayout. | [<span class="i"></span>](#cell)


###Scroll View Summary
Element Name | Description | &nbsp;
-- | -- | --
`#!xml <HorizontalScrollView></HorizontalScrollView>` | A scrollable horizontal row of elements. | [<span class="i"></span>](#horizontalscrollview)
`#!xml <VerticalScrollView></VerticalScrollView>` | A scrollable vertical column of elements. | [<span class="i"></span>](#verticalscrollview)


---

##Layout Element Details

###Layout Details

####Panel
A "window" in which elements can be confined.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
padding | Specifies the padding for this panel. Please note that if padding is specified, the panel will function as a LayoutGroup (which it does not do by default). | float(left) float(right) float(top) float(bottom) | *(none)*

```xml
<Panel>
    <Text>Text contained within Panel</Text>
</Panel>
```

---


####HorizontalLayout
 A horizontal row of elements.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
padding |  | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
spacing | Spacing between child elements. | float | `0`
childAlignment |  | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `UpperLeft`
childForceExpandWidth |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
childForceExpandHeight |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`

```xml
<HorizontalLayout>
    <Button>Button One</Button>
    <Button>Button Two</Button>
    <Button>Button Three</Button>
</HorizontalLayout>
```

---


####VerticalLayout
A vertical column of elements.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
padding |  | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
spacing | Spacing between child elements. | float | `0`
childAlignment |  | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `UpperLeft`
childForceExpandWidth |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
childForceExpandHeight |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`

```xml
<VerticalLayout>
    <Button>Button One</Button>
    <Button>Button Two</Button>
    <Button>Button Three</Button>
</VerticalLayout>
```

---


####GridLayout
A grid of elements.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
padding |  | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
spacing | Spacing between child elements | float(x) float(y) | `0 0`
cellSize |  | float(x) float(y)	 | `100 100`
startCorner |  | <ul><li>UpperLeft</li><li>UpperRight</li><li>LowerLeft</li><li>LowerRight</li></ul> | `UpperLeft`
startAxis |  | <ul><li>Horizontal</li><li>Vertical</li></ul> | `Horizontal`
childAlignment |  | <ul><li>UpperLeft</li><li>UpperCenter</li><li>UpperRight</li><li>MiddleLeft</li><li>MiddleCenter</li><li>MiddleRight</li><li>LowerLeft</li><li>LowerCenter</li><li>LowerRight</li></ul> | `UpperLeft`
constraint |  | <ul><li>Flexible</li><li>FixedColumnCount</li><li>FixedRowCount</li></ul> | `Flexible`
constraintCount |  | integer | `2`

```xml
<GridLayout>
    <Button>Button One</Button>
    <Button>Button Two</Button>
    <Button>Button Three</Button>
</GridLayout>
```


---


####TableLayout
A layout element based on HTML tables, allowing you to specify the position of elements in specific rows/columns.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
padding |  | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
cellSpacing | Spacing between each cell. | float | `0`
columnWidths | (Optional) Explicitly set the width of each column. Use a value of 0 to auto-size a specific column.	 | float list - e.g. '32 0 0 32' | *(none)*
automaticallyAddColumns | If more cells are added to a row than are accounted for by columnWidths, should this TableLayout automatically add one or more new auto-sized entries (0) to columnWidths? | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
automaticallyRemoveEmptyColumns | If there are more entries in columnWidths than there are cells in any row, should this TableLayout automatically remove entries from columnWidths until their are no 'empty' columns? | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
autoCalculateHeight | If set to true, then the height of this TableLayout will automatically be calculated as the sum of each rows preferredHeight value. This option cannot be used without explicitly sized rows. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
useGlobalCellPadding | If set to true, then all cells will use this TableLayout's cellPadding value. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
cellPadding | Padding for each cell. | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
cellBackgroundImage | Image to use as the background for each cell.	| string | 
cellBackgroundColor | Color for each cells background. | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `rgba(1,1,1,0.4)`
rowBackgroundImage | Image to use as the background for each row. | string | 
rowBackgroundColor | Color to use for each rows background. | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `clear`

```xml
<TableLayout>
    <!-- Row 1 -->
    <Row>
        <Cell><Button>Button One</Button></Cell>
        <Cell><Button>Button Two</Button></Cell>
    </Row>
    <!-- Row 2 -->
    <Row>
        <Cell><Button>Button One</Button></Cell>
        <Cell><Button>Button Three</Button></Cell>
    </Row>
</TableLayout>
```

#####Row
A row within a TableLayout.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
preferredHeight | Sets the height for this row. Use a value of '0' to specify that this row should be auto-sized. | float | `0`
dontUseTableRowBackground | If set to true, then this row will ignore the tables' *rowBackgroundImage* and *rowBackgroundColor* values, allowing you to override those values for this row. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`

#####Cell
A cell within a TableLayout.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
columnSpan | __ | int | `1`
dontUseTableCellBackground | If set to true, then this cell will ignore the tables' *cellBackgroundImage* and values, allowing you to override those values for this cell. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
overrideGlobalCellPadding | If set to true, then this cell will ignore the tables' *cellPadding* value, allowing you to set unique cell padding for this cell. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
padding | 	Padding values to use for this cell if *overrideGlobalCellPadding* is set to true. | float(left) float(right) float(top) float(bottom) | `0 0 0 0`
childForceExpandWidth |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
childForceExpandHeight |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`

---


###Scroll View Details

####HorizontalScrollView
A scrollable horizontal row of elements. This is an [input element](inputelements.md).

A layout element such as a Panel, HorizontalLayout, GridLayout, or TableLayout can be used to position child elements within the Scroll View.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When a selection is made, its name is sent to a function with this name. | string | *(none)*
horizontal |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
vertical |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
movementType |  | <ul><li>Unrestricted</li><li>Elastic</li><li>Clamped</li></ul> | `Clamped`
elasticity |  | float | `0.1`
inertia |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
decelerationRate |  | float | `0.135`
scrollSensitivity |  | float | `1`
horizontalScrollbarVisibility |  | <ul><li>Permanent</li><li>AutoHide</li><li>AutoHideAndExpandViewport</li></ul> | `AutoHide`
verticalScrollbarVisibility |  | <ul><li>Permanent</li><li>AutoHide</li><li>AutoHideAndExpandViewport</li></ul> | *(none)*
noScrollbars | If set to true, then this scroll view will have no visible scrollbars. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
scrollbarBackgroundColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
scrollbarColors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
scrollbarImage |  | string | 

```xml
<HorizontalScrollView>
    <HorizontalLayout>
        <Panel>
            <Text>1</Text>
        </Panel>
        <Panel>
            <Text>2</Text>
        </Panel>
        <Panel>
            <Text>3</Text>
        </Panel>
        <Panel>
            <Text>4</Text>
        </Panel>
    </HorizontalLayout>
</HorizontalScrollView>
```


---


####VerticalScrollView
A scrollable vertical column of elements. This is an [input element](inputelements.md).

A layout element such as a Panel, HorizontalLayout, GridLayout, or TableLayout can be used to position child elements within the Scroll View.

Attribute Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Type&nbsp;/&nbsp;Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Default&nbsp;Value&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | -- | --
onValueChanged | When a selection is made, its name is sent to a function with this name. | string | *(none)*
horizontal |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
vertical |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
movementType |  | <ul><li>Unrestricted</li><li>Elastic</li><li>Clamped</li></ul> | `Clamped`
elasticity |  | float | `0.1`
inertia |  | [<span class="tag boo"></span>](attributes.md#attribute-types) | `true`
decelerationRate |  | float | `0.135`
scrollSensitivity |  | float | `1`
horizontalScrollbarVisibility |  | <ul><li>Permanent</li><li>AutoHide</li><li>AutoHideAndExpandViewport</li></ul> | *(none)*
verticalScrollbarVisibility |  | <ul><li>Permanent</li><li>AutoHide</li><li>AutoHideAndExpandViewport</li></ul> | `AutoHide`
noScrollbars | If set to true, then this scroll view will have no visible scrollbars. | [<span class="tag boo"></span>](attributes.md#attribute-types) | `false`
scrollbarBackgroundColor |  | [<span class="tag xmlco"></span>](attributes.md#attribute-types) | `#FFFFFF`
scrollbarColors |  | [<span class="tag xmlcb"></span>](attributes.md#attribute-types) | `#FFFFFF|#FFFFFF|#C8C8C8|rgba(0.78,0.78,0.78,0.5)`
scrollbarImage |  | string | 

```xml
<VerticalScrollView>
    <VerticalLayout>
        <Panel>
            <Text>1</Text>
        </Panel>
        <Panel>
            <Text>2</Text>
        </Panel>
        <Panel>
            <Text>3</Text>
        </Panel>
        <Panel>
            <Text>4</Text>
        </Panel>
    </VerticalLayout>
</VerticalScrollView>
```











---
