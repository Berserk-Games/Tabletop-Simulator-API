Physics, a static global class, allows access to casts and gravity. Physics casts are a way to detect Objects. You call these functions like this: `Physics.getGravity()`. This class also allows you to access elements of the environment.

For more information on physics casts in Unity, [refer to the Unity documentation](https://docs.unity3d.com/ScriptReference/Physics.html) under BoxCast/RayCast/SphereCast.



##Member Variable Summary

###Member Variables
These are variables that affect elements of the environment. It allows you to both read and write values.

Read example: `print(Physics.play_area)` Write Example = `Physics.play_area = 0.5`

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="play_area"></a>play_area | The play area being used (ie. how far from middle you can get). Values from 0 - 1. Default is 0.5 | [<span class="tag flo"></span>](types.md) <a class="anchor" id="angular_drag"></a>


---








##Function Summary

###Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
cast([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Returns Table containing information on hit Objects. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#cast)
<a class="anchor" id="getgravity"></a>getGravity() | Returns directional Vector of the direction gravity is pulling. | [<span class="ret vec"></span>](types.md#vector) |
<a class="anchor" id="setgravity"></a>setGravity([<span class="tag vec"></span>](types.md#vector)&nbsp;direction) | Sets the direction gravity gravity pulls. | [<span class="ret boo"></span>](types.md)






---


##Function Details

###cast(...)

[<span class="ret tab"></span>](types.md)&nbsp;Returns Table containing information on hit Objects. There are three kinds of casts:

Type | Description
--- | ---
Ray | A line.
Box | A cube, rectangle, plane.
Sphere | A round ball. You cannot make ovals.

It draws the imaginary cast, then moves the rap/box/sphere along that path instantly. The debug Bool in the parameters allows you to see this shape, to aid in setup, but the visual is not instant (due to that making it pointless, if you can't see it).

!!!Warning
    Physics casts are somewhat expensive. When running 30+ at once it will cause your game to stutter and/or crash. Do not overuse.

!!!info "cast(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters used to guide the function.
        * [<span class="tag vec"></span>](types.md#vector) **parameters.origin**: Position of the starting point.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](types.md#vector) **parameters.direction**: A direction for the cast to move in.
            * {>>Optional, but cast is motionless without a direction.<<}
        * [<span class="tag int"></span>](types.md) **parameters.type**: The type of cast. {>>1 = Ray, 2 = Sphere, 3= Box<<}
            * {>>Optional, defaults to 1.<<}
        * [<span class="tag vec"></span>](types.md#vector) **parameters.size**: Size of the cast shape. Sphere/Box only.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag vec"></span>](types.md#vector) **parameters.orientation**: Rotation of the cast shape. Box only.
            * {>>Optional, defaults to {x=0, y=0, z=0}.<<}
        * [<span class="tag flo"></span>](types.md) **parameters.max_distance**: How far the cast will travel.
            * {>>Optional, defaults to infinity. Won't move without direction.<<}
        * [<span class="tag boo"></span>](types.md) **parameters.debug**: If the cast is visualized for the user.
            * {>>Optional, defaults to false.<<}

!!!info "Returned Table of Hit Objects"
    * [<span class="tag tab"></span>](types.md) **table**: A numerically indexed Table, one entry for each hit Object. Entries are in the order of being hit.
        * [<span class="tag vec"></span>](types.md#vector) **table.point**: Position the cast impacted the Object.
        * [<span class="tag vec"></span>](types.md#vector) **table.normal**: The surface normal of the impact point.
        * [<span class="tag flo"></span>](types.md) **table.distance**: Distance between cast origin and impact point.
        * [<span class="tag obj"></span>](types.md) **table.hit_object**: An Object reference to the Object hit by the cast.

``` Lua
-- Example usage
-- This function, when called, returns a table of hit data
function findHitsInRadius(pos, radius)
    local radius = (radius or 1)
    local hitList = Physics.cast({
        origin       = pos,
        direction    = {0,1,0},
        type         = 2,
        size         = {radius,radius,radius},
        max_distance = 0,
        debug        = true,
    })

    return hitList
end
```

``` Lua
-- Example returned Table
{
    {
        point = {x=0,y=0,z=0},
        normal = {x=1,0,0},
        distance = 4,
        hit_object = objectreference1,
    },
    {
        point = {x=1,y=0,z=0},
        normal = {x=2,0,0},
        distance = 5,
        hit_object = objectreference2,
    },
}
```
