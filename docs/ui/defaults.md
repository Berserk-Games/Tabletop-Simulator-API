The Default element allows you to set default values for UI elements. Primarily this will be used to set styles and the like, but there is no restriction on what default values you can set.

Defaults can be applied to all instances of a particular tag type, or only those of a particular class (as set by the class attribute). Please note that elements may use more than one class (separated by spaces).

As with its HTML counterpart (CSS), XmlLayout Defaults are applied in a cascading fashion. This means that an element will always use the most recent value for an attribute - for example, if an element implements a class, it will use the attribute values defined by that class except when the element itself also defines those attributes (attributes defined on the element will always take precedence).

Defaults tags can be placed anywhere in the Xml document, but will only apply to elements after it.

**Example:**
```xml
<Defaults>
    <!-- Set the default color and font size for all Text elements -->
    <Text color="#DDDDDD" fontSize="16" />
    
    <!-- Set the default color for all Text elements using the 'darker' class -->
    <Text class="darker" color="#AAAAAA" />    
</Defaults>

<!-- This text's color will be "#DDDDDD" and its font size will be "16" -->
<Text>Text</Text>

<!-- This text's color will be "#AAAAAA" and its font size will be "16" -->
<Text class="darker">Text</Text>

<!-- Set the default border and text color for all tooltips -->
<Tooltip tooltipBorderColor="rgb(1,1,1)" tooltipTextColor="rgb(1,1,1)" />
```
