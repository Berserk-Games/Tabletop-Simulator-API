Color is a type of Table that is used to define RGBA values for tinting. R for red, G for green, B for blue and A for alpha (transparency)

Besides the functions listed below, other classes can be used to manipulate colors as well.

Example Usage: `#!lua orange = Color(1, 0, 0):lerp(Color(1, 1, 0), 0.5)`

Check [Manipulation examples](#manipulation-examples) for more detailed usage.

!!!tip
    Vector and Color are the first classes to be defined in pure Lua. This means you **have** to use colon operator (e.g. `col:lerp()`) to call member functions, not the dot operator. Failing to do so will fail with cryptic error messages displayed.

##Constructors summary

!!!tip
    Every place that returns a coordinate table, like `#!lua obj.getColorTint()`, serves a Color class instance already - you do not have to explicitly construct it.
    When constructing Color instances, the `.new` part can be omitted, making e.g. `#!lua Color(1, 0.5, 0.75)` equivalent to `#!lua Color.new(1, 0.5, 0.75)`.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
Color([<span class="tag flo"></span>](types.md)&nbsp;r, [<span class="tag flo"></span>](types.md)&nbsp;g, [<span class="tag flo"></span>](types.md)&nbsp;b) | Return a color with specified (r, g, b) components. | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#colornew)
Color([<span class="tag flo"></span>](types.md)&nbsp;r, [<span class="tag flo"></span>](types.md)&nbsp;g, [<span class="tag flo"></span>](types.md)&nbsp;b, [<span class="tag flo"></span>](types.md)&nbsp;a) | Return a color with specified (r, g, b, a) components. | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#colornew)
Color([<span class="tag tab"></span>](types.md)&nbsp;t) | Return a color with r&#47;g&#47;b&#47;a <!-- (Not work in 12.3.5) or 1&#47;2&#47;3&#47;4 --> components from source table<!-- (r&#47;g&#47;b&#47;a first)-->. | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#colornew)
Color.new(...) | Same as Color(...). | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#colornew)
Color.fromString([<span class="tag str"></span>](types.md)&nbsp;colorStr) | Return a color from a color string ('Red', 'Green' etc), capitalization ignored. | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#colorfromstring)
Color.Blue | Shorthand for Color.fromString('Blue'), works for all [Player](player-color.md) and [added colors](#coloradd), capitalization ignored. Also return the color name. | [<span class="ret col"></span>](types.md)[<span class="ret str"></span>](types.md) | [<span class="i"></span>](#colorblue)

<!--
This function exist but in version 12.3.5 she is not working.

Color.fromHex([<span class="tag str"></span>](types.md)&nbsp;hexStr) | Return a color from a hex representation string ('#ff112233', 'ff1122'), hash sign and alpha are optional. | [<span class="ret col"></span>](types.md)
-->


###Constructors examples

```lua
function onLoad()
    local red = Color.new(1, 0, 0)
    local green = Color(0, 1, 0) -- same as Color.new(0, 1, 0)

    local orangePlayer = Color.fromString("Orange")
    local purplePlayer = Color.Purple
end
```

---

##Element access summary

In addition to accessing color components by their numeric indices (1, 2, 3, 4) and textual identifiers (r, g, b, a), the following methods may also be utilized.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
setAt([<span class="tag str"></span>](types.md)&nbsp;k, [<span class="tag flo"></span>](types.md)&nbsp;value) | Sets a component to value and returns self. | [<span class="ret sel"></span>](types.md#vector)  | [<span class="i"></span>](#setat)
set([<span class="tag flo"></span>](types.md)&nbsp;r, [<span class="tag flo"></span>](types.md)&nbsp;g, [<span class="tag flo"></span>](types.md)&nbsp;b, [<span class="tag flo"></span>](types.md)&nbsp;a) | Sets `r`, `g`, `b`, `a` components to given values and returns self, alpha is optional| [<span class="ret sel"></span>](types.md#vector) | [<span class="i"></span>](#set)
get() | Returns `r`, `g`, `b`, `a` components as four separate values. | [<span class="ret flo"></span>](types.md)<br>[<span class="ret flo"></span>](types.md)<br>[<span class="ret flo"></span>](types.md)<br>[<span class="ret flo"></span>](types.md) | [<span class="i"></span>](#get)
copy() | Returns a separate Color with identical component values. | [<span class="ret col"></span>](types.md#vector) | [<span class="i"></span>](#copy)

!!!tip
    Before `Color` was introduced, color tables contained separate values under 1, 2, 3, 4 and r, g, b, a keys, with letter keys taking precedence when they were different. This is no longer the case, and using letter and numerical keys is equivalent. However, when iterating over Color components you have to use `pairs` and only letter keys will be read there.

###Element access examples

```lua
function onLoad()
    local col = Color(0, 0.5, 0.75)
    col.r = 1 -- set the first component
    col[2] = 0.25 -- set the second component
    col:setAt('b', 1) -- set the third component

    print(col:get()) --> same as print(col.r, col.g, col.b, col.a)

    for colorCode, value in pairs(col) do
        print(colorCode .. "="..value) --> r=1 then g=0.25 then b=1 and finally a=1
    end

    col:copy():setAt('a', 0.5)
    print(col.a) --> 1, because we only changed 'a' on a copy
end
```

---


##Arithmetics summary

Color also allows you to use arithmetic operators to performs basic operations:

Operator | Description | Return | &nbsp;
-- | -- | -- | --
[<span class="tag col"></span>](types.md)&nbsp;one == [<span class="tag col"></span>](types.md)&nbsp;two | Return true if both colors identical or within a small margin of each other, false otherwise. See also [color:equals()](#equals). | [<span class="tag boo"></span>](types.md)
tostring([<span class="tag col"></span>](types.md)&nbsp;col) | Return a string description of a color. | [<span class="tag str"></span>](types.md)

###Arithmetics examples

```lua
function onLoad()
	local col = Color({r = 0.118, g = 0.53, b = 1})
    print(col == Color.blue) --> true

    -- Color : Blue { r = 0.118, g = 0.53, b = 1, a = 1}
    tostring(Color(0.118, 0.53, 1))

    --> Color : { r = 0.3, g = 0.5, b = 1, a = 1}
    tostring(Color({r = 0.3, g = 0.5, b = 1}))
end
```

---

##Methods summary

###Methods not modifying self

Method Name | Description | Return | &nbsp;
-- | -- | -- | --:
col:toHex([<span class="tag boo"></span>](types.md)&nbsp;includeAlpha) | Returns a hex string for `col`, boolean parameter `includeAlpha`. | [<span class="ret str"></span>](types.md) | [<span class="i"></span>](#tohex)
col:toString([<span class="tag flo"></span>](types.md)&nbsp;tolerance) | Returns a color string if matching this instance, nil otherwise, optional numeric `tolerance` param. | [<span class="ret str"></span>](types.md) | [<span class="i"></span>](#tostring)
col:equals([<span class="tag col"></span>](types.md)&nbsp;otherCol, [<span class="tag flo"></span>](types.md)&nbsp;num) | Returns true if `otherCol` same as `col`, false otherwise, optional numeric tolerance param. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#equals)
col:lerp([<span class="tag col"></span>](types.md)&nbsp;otherCol, [<span class="tag flo"></span>](types.md)&nbsp;num) | Return a color some part of the way between `col` and `otherCol`, numeric arg [0, 1] is the fraction. | [<span class="ret col"></span>](types.md) | [<span class="i"></span>](#lerp)
col:dump([<span class="tag str"></span>](types.md)&nbsp;prefix) | Return a string description of a color with an optional `prefix`. | [<span class="ret str"></span>](types.md)<br>[<span class="ret flo"></span>](types.md) | [<span class="i"></span>](#dump)

###Other methods
Method Name | Description | Return | &nbsp;
-- | -- | -- | --:
Color.list | Returns a table of all color strings. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#colorlist)
Color.Add([<span class="tag str"></span>](types.md)&nbsp;name, [<span class="tag col"></span>](types.md)&nbsp;yourColor) | Add your own color definition to the class. | [<span class="ret nil"></span>](types.md) | [<span class="i"></span>](#coloradd)

---

##Constructors details

###Color.new(...)

[<span class="ret col"></span>](types.md)&nbsp;Return a color with specified components.

!!!info "Color.new(r, g, b)"
    * [<span class="tag flo"></span>](types.md) **r**: Red component between 0 and 1.
    * [<span class="tag flo"></span>](types.md) **g**: Green component between 0 and 1.
    * [<span class="tag flo"></span>](types.md) **b**: Blue component between 0 and 1.

!!!info "Color.new(r, g, b, a)"
    * [<span class="tag flo"></span>](types.md) **r**: Red component between 0 and 1.
    * [<span class="tag flo"></span>](types.md) **g**: Green component between 0 and 1.
    * [<span class="tag flo"></span>](types.md) **b**: Blue component between 0 and 1.
    * [<span class="tag flo"></span>](types.md) **a**: Alpha component between 0 and 1.

!!!info "Color.new(t)"
    * [<span class="tag tab"></span>](types.md) **t**: The table should use the `r`, `g`, `b` and `a` index. <br>By default the value is 0 for color and 1 for alpha.


``` Lua
local red = Color.new(1, 0, 0)
local green = Color(0, 1, 0) -- same as Color.new(0, 1, 0)
local river = Color(52 / 255, 152 / 255, 219 / 255, 160 / 255)
local teal = Color({ r = 0.129, g = 0.694, b = 0.607})
```

!!!info
	If you want to use value between 0 and 255 you should divide them by 255 before construct the object.


###Color.fromString(...)

[<span class="ret col"></span>](types.md)&nbsp;Return a color from a color string ('Red', 'Green' etc), capitalization ignored.

!!!info "Color.fromString(colorStr)"
    * [<span class="tag str"></span>](types.md) **colorStr**: Any [Player Color](player-color.md) or color added with [Color.Add](#coloradd).

``` Lua
local col = Color.fromString("Blue")
print(col) --> Color: Blue { r = 0.118, g = 0.53, b = 1, a = 1 }
```

###Color.Blue

[<span class="ret col" style="margin-right:5px;"></span>](types.md)
[<span class="ret str"></span>](types.md)&nbsp;Return a color from a color string ('Red', 'Green' etc).

Any [Player Color](player-color.md) or color added with [Color.Add](#coloradd).

``` Lua
local color, name = Color.Blue
print(color) -- Color: Blue { r = 0.118, g = 0.53, b = 1, a = 1 }
print(name) -- Blue

local color, name = Color.Red
print(color) -- Color: Red { r = 0.856, g = 0.1, b = 0.094, a = 1 }
print(name) -- Red
```

---

##Element access details

###setAt(...)

[<span class="ret sel"></span>](types.md)&nbsp;Update one component of the color and returning self.

!!!info "setAt(key, num)"
    * [<span class="tag int"></span>](types.md) **key**: Index of component (1, 2, 3 or 4 for r, g, b or a).
    * [<span class="tag flo"></span>](types.md) **num**: New value.

``` Lua
col = Color.Blue
col:setAt(1, 128 / 255):setAt('a', 0.5)
print(col) --> Color: { r = 0.501961, g = 0.53, b = 1, a = 0.5 }
```

###set(...)

[<span class="ret sel"></span>](types.md)&nbsp;Update all components of the vector and returning self.

Providing a nil value makes it ignore that argument.

!!!info "set(r, g, b)"
    * [<span class="tag flo"></span>](types.md) **r**: New value of Red component.
    * [<span class="tag flo"></span>](types.md) **g**: New value of Green component.
    * [<span class="tag flo"></span>](types.md) **b**: New value of Blue component.

!!!info "set(r, g, b, a)"
    * [<span class="tag flo"></span>](types.md) **r**: New value of Red component.
    * [<span class="tag flo"></span>](types.md) **g**: New value of Green component.
    * [<span class="tag flo"></span>](types.md) **b**: New value of Blue component.
    * [<span class="tag flo"></span>](types.md) **a**: New value of Alpha component.

``` Lua
col = Color.black
col:set(41 / 255, 128 / 255, 185 / 255)
print(col) --> Color: { r = 0.160784, g = 0.501961, b = 0.72549, a = 1 }
```

###get()

[<span class="ret flo" style="margin-right:5px;"></span>](types.md)
[<span class="ret flo" style="margin-right:5px;"></span>](types.md)
[<span class="ret flo" style="margin-right:5px;"></span>](types.md)
[<span class="ret flo"></span>](types.md)&nbsp;Returns `r`, `g`, `b`, `a` components as four separate values.

``` Lua
col = Color.Blue
r, g, b, a = col:get()
print(r + g + b + a) --> 2.648
```

###copy()

[<span class="ret col"></span>](types.md)&nbsp;Copy self into a new Color and return it.

``` Lua
col1 = Color(1, 0.5, 0.75)
col2 = col1:copy()
col1:set(0.75, 1, 0.25)
print(col1) --> Color: { r = 0.75, g = 1, b = 0.25, a = 1 }
print(col2) --> Color: { r = 1, g = 0.5, b = 0.75, a = 1 }
```


##Methods details

###Methods not modifying self

####toHex(...)

[<span class="ret str"></span>](types.md)&nbsp;Returns a hex string representation of self.

!!!info "toHex(includeAlpha)"
    * [<span class="tag boo"></span>](types.md) **includeAlpha**: Include or not the `a` value. (Default true)

``` Lua
print(Color.blue:toHex()) -- 1e87ffff
print(Color.blue:toHex(true)) -- 1e87ffff
print(Color.blue:toHex(false)) -- 1e87ff
```

####toString(...)

[<span class="ret str"></span>](types.md)&nbsp;Returns a color string if matching this instance, nil otherwise, optional numeric `tolerance` param.

!!!info "toString(tolerance)"
    * [<span class="tag flo"></span>](types.md) **tolerance**: Numeric `tolerance`, by default 0.01.

``` Lua
print(Color( 0.118, 0.53, 1):toString()) -- Blue
```

####equals(...)

[<span class="ret boo"></span>](types.md)&nbsp;Returns true if `otherCol` same as self, false otherwise, optional numeric `tolerance` param.

!!!info "equals(otherCol, tolerance)"
    * [<span class="tag col"></span>](types.md) **otherCol**: The color to compare with.
    * [<span class="tag flo"></span>](types.md) **tolerance**: Numeric `tolerance`, by default 0.01.

``` Lua
print(Color( 0.118, 0.53, 1):equals(Color.Blue:copy())) -- true
print(Color( 0.118, 0.53, 1) == Color.Blue) -- true

print(Color( 0.118, 0.53, 1):equals(Color.Blue)) -- Throw errors
```

####lerp(...)

[<span class="ret col"></span>](types.md)&nbsp;Return a color some part of the way between self and `otherCol`, numeric arg [0, 1] is the fraction.

!!!info "lerp(otherCol, fraction)"
    * [<span class="tag col"></span>](types.md) **otherCol**: The color to compare with.
    * [<span class="tag flo"></span>](types.md) **fraction**: Numeric `fraction`.

``` Lua
local pink = Color.Red:lerp(Color.White, 0.5)
print(pink) -- Color: { r = 0.928, g = 0.55, b = 0.547, a = 1 }
```

####dump(...)

[<span class="ret str" style="margin-right:5px;"></span>](types.md)
[<span class="ret flo"></span>](types.md)&nbsp;Return string describing self, optional string prefix.

!!!info "dump(prefix)"
    * [<span class="tag str"></span>](types.md) **prefix**: The prefix of return string.

!!!warning
    This function returns one extra float that will be displayed in print function. This value is returned by the last gsub used in internal function.

``` Lua
col = Color.Blue
str = col:dump('Prefix')
print(str) --> Prefix: Blue { r = 0.118, g = 0.53, b = 1, a = 1 }
print(col:dump('Prefix')) --> Prefix: Blue { r = 0.118, g = 0.53, b = 1, a = 1 } 2
print(Color.dump(col, 'Prefix')) --> Prefix: Blue { r = 0.118, g = 0.53, b = 1, a = 1 }	2
```

###Other methods


####Color.list

[<span class="ret tab"></span>](types.md)&nbsp;Returns a table of all color strings.


``` Lua
data = Color.list
-- Same as
data = {
    [1] => "White",
    [2] => "Brown",
    [3] => "Red",
    [4] => "Orange",
    [5] => "Yellow",
    [6] => "Green",
    [7] => "Teal",
    [8] => "Blue",
    [9] => "Purple",
    [10] => "Pink",
    [11] => "Grey",
    [12] => "Black"
}

```

####Color.Add(...)

[<span class="ret nil"></span>](types.md)&nbsp;Add your own color definition to the class.

!!!info "dump(name, yourColor)"
    * [<span class="tag str"></span>](types.md) **name**: The name of the color.
    * [<span class="tag col"></span>](types.md) **yourColor**: The color value.

``` Lua
Color.Add("River", Color(52 / 255, 152 / 255, 219 / 255))
local color, name = Color.River
print(color) -- Color: River { r = 0.203922, g = 0.596078, b = 0.858824, a = 1 }
print(name) -- River
```

---

##Manipulation examples

Tint all object in scene in orange.
```lua
function onLoad()
    local red = Color.Red
    local green = Color.Green

    -- Get a color between red and green
    local yellow = red:lerp(green, 0.5)

    -- Make the color brighter
    yellow:set(yellow.r * 1.5, yellow.g * 1.5, yellow.b * 1.5)

    -- Get a color between yellow and red
    local orange = yellow:lerp(Color.Red, 0.5)

    -- Iterate through all scene objects and set the color tint to orange
    for k, obj in pairs(getAllObjects()) do
        obj.setColorTint(orange)
    end
end
```

Tint all object in a random color.
```lua
function onLoad()
    -- Iterate through all scene objects and generate a random color
    for k, obj in pairs(getAllObjects()) do
        local colorA = getRandomColor()
        local colorB = getRandomColor()

        color = colorA:lerp(colorB, math.random(0, 1))

        -- Make the color darker or brighter
        local factor = math.random(1, 2)
        color:set(color.r * factor, color.g * factor, color.b * factor)

        -- Apply the color to object
        obj.setColorTint(color)
    end
end

function getRandomColor()
    local r = math.random(0, 255)
    local g = math.random(0, 255)
    local b = math.random(0, 255)
    return Color(r / 255, g / 255, b / 255)
end
```



