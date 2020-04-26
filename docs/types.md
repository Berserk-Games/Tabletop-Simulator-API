Type refers to the type of information being used. You do not need to declare a type in Lua, but in this API you will see them indicated. This is only so you know what kind of information is required in a given variable/parameter. This API utilizes the following types.

##Common Standards

Tag | Type | Description | Example
-- | -- | -- | --
[<span class="tag nil"></span>](types.md)&nbsp;| nil | No value. | `#!lua nil`
[<span class="tag int"></span>](types.md)&nbsp;| int | Non-decimal value. | `#!lua 5`
[<span class="tag flo"></span>](types.md)&nbsp;| float | Non-exact decimal value. | `#!lua 2.032`
[<span class="tag boo"></span>](types.md)&nbsp;| bool | `true` or `false` value. | `#!lua true`
[<span class="tag str"></span>](types.md)&nbsp;| string | A series of characters. | `#!lua "Hello."`
[<span class="tag tab"></span>](types.md)&nbsp;| table | A container with keys and values. | `#!lua {["key"]="value", true, 5}`
[<span class="tag obj"></span>](types.md)&nbsp;| object | An in-game physical Object. Sometimes Global. | `#!lua Global or self`
[<span class="tag pla"></span>](types.md)&nbsp;| player | An in-game Player. | `#!lua Player["White"]`
[<span class="tag var"></span>](types.md)&nbsp;| variable | A combination of other types. |

You will also see tags for Color, Vector, and Function. See below for more info.

> For more information on a type, you can read below or refer to the relevant [Lua documentation](https://www.lua.org/manual/5.1/manual.html#2.2).

---

##Special Standards

Some types need to be used in specific ways. For Color and Vector, they are Tables that are used often in Tabletop Simulator. They represent Vectors and Colors, and their contents must be formatted a certain way to be utilized correctly.

For Functions, they are used when a delay is required within a running script that have specific requirements.

###Color
<span class="tag col"></span> Color is a type of Table that is used to define RGB values for tinting.

####Keys

The Table will contain the keys `r`, `g`, `b`, `a` and/or `1`, `2`, `3`, `4`. The letter and numeric keys are duplicates of each other, and each represents a color or transparency.

Color | Letter Key | Number Key
:--: | :--: | :--:
red | r | 1
green | g | 2
blue | b | 3
alpha | a | 4

As an example, an Object with a white color tint would return this table:
``` Lua
{
    r=1, g=1, b=1,
    1=1, 2=1, 3=1,
}
```

Notice it does not contain the `a` or `4` keys. This is because currently only scripted buttons and scripted inputs utilize the alpha channel (transparency).

####Mixed Keys

Only one type of key, number or letter, is required. If both a are present in a Table, the numeric key is ignored and only the **letter key** is used.

``` Lua
--Valid Table for red
{r=1, g=0, b=0}
--Valid Table for blue
{0, 0, 1}
--This Table would be red.
{r=1, g=0, b=0, 0, 0, 1}
```

####Value

Values are between 0 and 1 for each key. If you are using RGB color that is in 0-255, you can use simple math to convert to the proper value.
``` Lua
--To display a color that is r=50, b=83, g=199
self.setColorTint({50/255, 83/255, 199/255})
```

####Strings

You are also able to use a String in place of a color table. Using a [Player Color](player-color.md) will automatically fill in that value. It works with any of the 12 color names, as they are written on the [Player Color](player-color.md) page.

Example: `printToAll("Test", "Green")`

---

###Vector
<span class="tag vec"></span> Vector is a type of Object with x, y, and z coordinates that is used to define a position, rotation or direction.

You can use the [Vector](vector.md) class to manipulate vectors.

Example: `#!lua target = Vector(1, 0, 0) + Vector(0, 2, 0):normalized()`

####Keys
The Table will contain the keys `x`, `y`, `z` and/or `1`, `2`, `3`. The letter and numeric keys are equivalent.

 Letter Key | Number Key
 :--: | :--:
 x | 1
 y | 2
 z | 3

As an example, An Object at coordinate X=5, Y=2, Z=-1 would return this [`Vector`](vector.md):
``` Lua
{
    x=5, y=2, z=-1,
}
```

####Mixed Keys

Before [`Vector`](vector.md) was introduced, coordinate tables contained separate values under 1, 2, 3 and x, y, z keys, with letter keys taking precedence when they were different. This is no longer the case, and using letter and numerical keys is equivalent. However, when iterating over Vector components you have to use `pairs` and only letter keys will be read there.

####Value Range

The range of values depend on the type of Vector you are using.

Type | Description | Range
--- | --- | ---
Position | A point in space. | Any number within the bounds of the world.
Rotation | Angle, in degrees. | -180 to 180.
Direction | Vector direction. | -1 to 1.

####Type Details

#####Position

X is right/left, Y is up/down, Z is forward/back. A positional Vector can be either world or local. Most of Tabletop Simulator's functions use world positional Vectors.

Type | Description
-- | --
World | The center of the instance is `{x=0, y=0, z=0}`. That is usually near the tabletop's center.
Local | The center of the Object's model is `{x=0, y=0, z=0}`. The center of an Object is determined by the model's creator.

???tip "Conversion Between World/Local"
     [positionToWorld(...)](object.md#positiontoworld) and [positionToLocal(...)](object.md#positiontolocal) can be used to convert between the two types.

#####Rotation

X is pitch (nodding your head), Y is yaw (shaking your head), Z is roll (tilting your head).

#####Direction

X is right/left, Y is up/down, Z is forward/back.

---


###Function
<span class="tag fun"></span> A function is a section of code that can be run when triggered. In Lua, you are able to pass (use as a parameter) functions. Some elements in Tabletop Simulator can be passed functions to perform some action with, like triggering it after a delay.

####Usage
To pass a function, first you must create the function. There are multiple ways to do this:

``` Lua
--Create it on-the-fly
function() print("Like This") end

--Create it with a variable name
anyFuncName = function() print("Like This") end

--Create it with a variable name that can also be passed parameters
function anyFuncName(printString)
	print(printString)
end
```

!!!warning
	You need to pass a function, not a result of a function. So this **will not** work:
	``` Lua
	Wait.frames(print("Ding"), 80)
	```
	Instead, make the print the result of a function running:
	``` Lua
	Wait.frames(function() print("Ding") end, 80)
	```

---


####Example

As an example, here is [Wait.frames(...)](wait.md#frames) used 3 times. It waits a set number of frames and then activates a given function:

``` Lua
function onLoad()
	--Built-in functions with parameters can be called directly
	--This is done by wrapping the function within `function()` and `end`
	Wait.frames(function() print("One") end, 60)

	--You can also call custom functions you have made yourself
	--Pass them any parameters you wish
	Wait.frames(function() sayTwo("Two") end, 120)

	--If you aren't passing any parameters to the function, you can shorten it
	Wait.frames(sayThree, 180)
end

--Has its parameter passed to it
function sayTwo(s) print(s) end

--Does not have any parameters passed to it
function sayThree() print("Three") end
```

---


####Lambda-Style Expressions
You are able to replace `function()` and `end` with `||`, allowing for much shorter functions.

#####Important Tips
You create a `|`, on a standard keyboard, by holding shift and pressing the key above enter (backslash).

`||` only work for one line. So if you intend to use a multi-line function, lambda-style will not be an option.

When using `||` for a conditional function with `Wait.condition(returnFunc, conditionalFunc)`, you do not need to include return.

If a parameter is passed to the return function, like with `callback_function` from `spawnObject(...)`, you can put a variable between the `||` characters to represent it. See the next section for an example.

#####Lambda-Style Example

Without Lambda-style:
``` Lua
function onLoad()
    --Spawn a deck with a callback function that triggers once deck spawns
    --Also, pass a reference to the spawned object
    spawnObject({
        type = "Deck",
        callback_function = function(obj) printCardCount(obj) end
    })

    --Print after 1 second
	Wait.time(function() print("One Second") end, 1)

    --Trigger a function after 2 seconds and send a parameter
    Wait.time(function() printString("Two Seconds") end, 2)
end

function printCardCount(deck)
    cardList = deck.getObjects()
    print(#cardList .. " cards.")
end

function printString(s)
    print(s)
end
```

With Lambda-style:
``` Lua
function onLoad()
    --Spawn a deck with a callback function that triggers once deck spawns
    --Also, pass a reference to the spawned object
    spawnObject({
        type = "Deck",
        callback_function = |obj| printCardCount(obj)
    })

    --Print after 1 second
	Wait.time(|| print("One Second"), 1)

    --Trigger a function after 2 seconds and send a parameter
    Wait.time(|| printString("Two Seconds"), 2)
end

function printCardCount(deck)
    cardList = deck.getObjects()
    print(#cardList .. " cards.")
end

function printString(s)
    print(s)
end
```



---
