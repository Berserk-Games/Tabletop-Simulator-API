In this section, you will find details on all events/classes/functions specific to Tabletop Simulator's Lua scripting. For more general information on how the scripting language of Lua works and what it does on its own, you can review the [Official Lua Documentation](https://www.lua.org/docs.html). 

##Using TTS Documentation

###Left Column
This is the top-level list of classes and other information needed when scripting with Lua in Tabletop Simulator. Event, Base and Object are the three pages you will use the most, with the rest referring to niche information you can access as you go. It is a good idea to familiarize yourself with the contents of those three pages in order to have a good high-level understanding of off what scripting is capable of doing.

###Right Column
The Table of Contents will lay out the contents of the page you are on. It always starts with high-level summary information first and, if needed, detailed information towards the bottom. The <span class="i"></span> next to a summary element will take you directly down to the relevant detailed explanation below.


##Growing TTS Documentation
This documentation is written via Markdown language and some custom CSS. The relevant files you can modify, as well as some detailed editing instructions, are listed on GitHub. You can make a pull request to made modifications/improvements that can be incorporated into this documentation.

Just click the link in the pencil icon in the top-right of an article, or visit the GitHub page for more information by clicking GitHub Source in the far upper right.

---


##TTS Terms

###GUID
In Tabletop Simulator, a GUID is a unique 6-character [string](intro#types) which can be used to identify in-game [Objects](object). GUIDs are automatically assigned when objects exist within the scene.

If an object is duplicated, it will sometimes have the same GUID for 1 frame before the engine assigns a new GUID to the newer Object. Objects in containers (bags/decks/etc) do not automatically get new GUIDs assigned to them in this way. Only once their contents are moved out into the scene.

???warning "Custom Deck Card GUIDs"
	When you first create a custom deck, all cards within the deck share the same GUID. If you need to reference individual GUIDs of cards, then the way to solve this is to lay out all cards from the deck at the same time to allow new GUIDs to be assigned by the game. [This tool](http://steamcommunity.com/sharedfiles/filedetails/?id=1180142950) can be used to simplify the process.

---


###Types

Type refers to the type of information. You do not need to declare the type in Lua, but in this API you will see them indicated. This is only so you know what kind of information is required in a given variable/parameter. This API utilizes the following types.

Tag | Type | Description | Example
-- | -- | -- | --
[<span class="tag nil"></span>](intro#types) | nil | No value. | `#!lua nil`
[<span class="tag int"></span>](intro#types) | int | Non-decimal value. | `#!lua 5`
[<span class="tag flo"></span>](intro#types) | float | Non-exact decimal value. | `#!lua 2.032`
[<span class="tag boo"></span>](intro#types) | bool | `true` or `false` value. | `#!lua true`
[<span class="tag str"></span>](intro#types) | string | A series of characters. | `#!lua "Hello."`
[<span class="tag tab"></span>](intro#types) | table | A container with keys and values. | `#!lua {["key"]="value", true, 5}`
[<span class="tag obj"></span>](intro#types) | object | An in-game physical Object. Can refer to Global. | `#!lua Global or self`
[<span class="tag pla"></span>](intro#types) | player | An in-game Player. | `#!lua Player["White"]`
[<span class="tag var"></span>](intro#types) | variable | Can possibly be some or any other type described above. | 


For more information what types are, you can refer to the relevant [Lua documentation](https://www.lua.org/manual/5.1/manual.html#2.2).


---

###Classes

Defining class requires further knowledge on object-oriented programming to really understand. However for the purposes of Tabletop Simulator Lua scripting, you can think of a class as a standard or collection that handles categories of objects.

####Object Classes
Associated with in-game Objects.

* [Clock](clock)
* [Counter](counter)
* [Object](object)
* [AssetBundle](assetbundle)
* [RPGFigurine](rpgfigurine)
* [TextTool](texttool)

####Static Classes
Associated with in-game properties and systems.

* [JSON](json)
* [Player](player)
* [Timer](timer)
* [WebRequest](webrequest)
* [Physics](physics)
* [Lighting](lighting)

For more information on what a class is, you can refer to the relevant [Lua Documentation](https://www.lua.org/pil/16.1.html).

---

###Special Standards

There are two Table types that are used often in Tabletop Simulator. They represent Vectors and Colors, and have special formatting rules to be understood by the many functions that utilize them.


####Color
Color is a type of Table that is used to define a color.

#####Keys

The Table will contain the keys `r`, `g`, `b`, `a` and/or `1`, `2`, `3`, `4`. The letter and numeric keys are duplicates of each other, and each represents a color or transparency.

Color | Letter Key | Number Key
--- | --- | ---
red | r | 1
green | g | 2
blue | b | 3
alpha | a | 4

As an example, an Object with a white color tint would return this table:
``` Lua
{
    r = 1,
    g = 1,
    b = 1,
    1 = 1,
    2 = 1,
    3 = 1,
}
```

Notice it does not contain the `a` or `4` keys. This is because currently only scripted buttons and scripted inputs utilize the alpha channel (transparency).

#####Mixed Keys

Only one type of key, number or letter, is required. If both a are present in a Table, the numeric key is ignored and only the **letter key** is used.

``` Lua
--Valid Table for red
{r=1, g=0, b=0}
--Valid Table for blue
{0, 0, 1}
--This Table would be red.
{r=1, g=0, b=0, 0, 0, 1}
```

#####Value

Values are between 0 and 1 for each key. If you are using RGB color that is in 0-255, you can use simple math to convert to the proper value.
``` Lua
--To display a color that is r=50, b=83, g=199
self.setColorTint({50/255, 83/255, 199/255})
```

---



####Vector
Vector is a type of Table that is used to define a position, rotation or direction. 
#####Keys
The Table will contain the keys `x`, `y`, `z` and/or `1`, `2`, `3`. The letter and numeric keys are duplicates of each other.

 Letter Key | Number Key
 --- | ---
 x | 1
 y | 2
 z | 3


As an example, An Object at coordinate X=5, Y=2, Z=-1 would return this table:
``` Lua
{
    x = 5,
    y = 2,
    z = -1,
    1 = 5,
    2 = 2,
    3 = -1,
}
```

#####Mixed Keys


Only one type of key, number or letter, is required. If both a are present in a Table, the numeric key is ignored and only the **letter key** is used.

``` Lua
--Valid Table for 1 to the right
{x=1, y=0, z=0}
--Valid Table for 1 unit forward
{0, 0, 1}
--This Table would be for 1 unit to the right.
{x=1, y=0, z=0, 0, 0, 1}
```

#####Value Range

The range of values depend on the type of Vector you are using.

Type | Description | Range
--- | --- | ---
Position | A point in space. | Any number within the bounds of the world.
Rotation | Angle, in degrees. | -180 to 180.
Direction | Vector direction. | -1 to 1.

#####Type Details

######Position

X is right/left, Y is up/down, Z is forward/back. A positional Vector can be either world or local. Most of Tabletop Simulator's functions use world positional Vectors.

Type | Description
-- | --
World | The center of the instance is `{x=0, y=0, z=0}`. That is usually near the tabletop's center.
Local | The center of the Object's model is `{x=0, y=0, z=0}`. The center of an Object is determined by the model's creator.

???tip "Conversion Between World/Local" 
     [positionToWorld(...)](object#positiontoworld) and [positionToLocal(...)](object#positiontolocal) can be used to convert between the two types.

######Rotation

X is pitch (nodding your head), Y is yaw (shaking you head), Z is roll (tilting your head).

######Direction

X is right/left, Y is up/down, Z is forward/back.
