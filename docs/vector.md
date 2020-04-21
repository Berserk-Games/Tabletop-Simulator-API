Representation of 3D vectors and points.

This structure is used to pass 3D positions and directions around. It also contains functions for doing common vector operations.

Besides the functions listed below, other classes can be used to manipulate vectors and points as well.

Example Usage: `target = Vector(1, 0, 0) + Vector(0, 1, 0)`

Check [Manipulation examples](#manipulation-examples) for more detailed usage.

!!!tip
    Vector and Color are the first classes to be defined in pure Lua. This means you **have** to use colon operator (e.g. `pos:angle()`) to call member functions, not the dot operator. Failing to do so will fail with cryptic error messages displayed.

##Constructors summary

!!!tip
    Every place that returns a coordinate table, like `obj.getPosition()`, serves a Vector class instance already - you do not have to explicitly construct it.
    When constructing Vector instances, the `.new` part can be omitted, making e.g. `Vector(1, 2, 3)` equivalent to `Vector.new(1, 2, 3)`.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
Vector([<span class="tag flo"></span>](/types)&nbsp;x, [<span class="tag flo"></span>](/types)&nbsp;y, [<span class="tag flo"></span>](/types)&nbsp;z) | Return a vector with specified (x, y, z) components. | [<span class="ret vec"></span>](/types)
Vector([<span class="tag tab"></span>](/types)&nbsp;v) | Return a vector with x&#47;y&#47;z or 1&#47;2&#47;3 components from source table (x&#47;y&#47;z first). | [<span class="ret vec"></span>](/types)
Vector.new(...) | Same as Vector(...). | [<span class="ret vec"></span>](/types)

###Constructors examples

```lua
function onLoad()
    local vec1 = Vector.new(0.5, 1, 1.5)
    local vec2 = Vector(1, -1, 0) -- same as Vector.new(1, -1, 0)

    print(Vector.between(vec1, vec2)) --> Vector: {0.5, -2. -1.5}
    print(Vector.max(vec1, vec2)) --> Vector: {1, 1. 1.5}
    print(Vector.min(vec1, vec2)) --> Vector: {0.5, -1. -0}
end
```

---

##Element access summary

Apart from being able to access elements using x, y, z and 1, 2, 3 keys directly, following methods directly modify vector components.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
[setAt](#setat)([<span class="tag str"></span>](/types)&nbsp;k, [<span class="tag flo"></span>](/types)&nbsp;value) | Sets a component to value and returns self. | [<span class="tag vec"></span>](/types#vector) 
[set](#set)([<span class="tag flo"></span>](/types)&nbsp;x, [<span class="tag flo"></span>](/types)&nbsp;y, [<span class="tag flo"></span>](/types)&nbsp;z) | Sets `x`, `y`, `z` components to given values and returns self. Providing a nil value makes it ignore that argument. | [<span class="tag vec"></span>](/types#vector) 
[get](#get)() | Returns `x`, `y`, `z` components as three separate values. | [<span class="tag flo"></span>](/types), [<span class="tag flo"></span>](/types), [<span class="tag flo"></span>](/types)
[copy](#copy)() | Returns a separate Vector with identical component values. | [<span class="tag vec"></span>](/types#vector)

!!!tip
    Before `Vector` was introduced, coordinate tables contained separate values under 1, 2, 3 and x, y, z keys, with letter keys taking precedence when they were different. This is no longer the case, and using letter and numerical keys is equivalent. However, when iterating over Vector components you have to use `pairs` and only letter keys will be read there.

###Element access examples

```lua
function onLoad()
    local vec = Vector(1, 2, 3)
    vec.x = 2 -- set the first component
    vec[2] = 4 -- set the second component
    vec:setAt('z', 6) -- set the third component

    print(vec:get()) --> same as print(vec.x, vec.y, vec.z)

    for axis, value in pairs(vec) do
        print(axis .. "="..value) --> x=2 then y=4 and finally z=6
    end

    vec:copy():setAt('x', - 11)
    print(vec.x) --> 2, because we only changed 'x' on a copy
end
```

---

##Methods summary


###Static methods summary

Method Name | Description | Return | &nbsp;
-- | -- | -- | --:
[Vector.equals](#vectorequals)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2, [<span class="tag flo"></span>](/types)&nbsp;margin) | Returns true if two vectors are approximately equal. The `margin` argument is optional and defaults to tolerating a difference of ~0.03 in both vector magnitude. | [<span class="tag boo"></span>](/types)
[Vector.min](#vectormin)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Returns a vector that is made from the smallest components of two vectors. | [<span class="tag vec"></span>](/types)
[Vector.max](#vectormax)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Returns a vector that is made from the largest components of two vectors. | [<span class="tag vec"></span>](/types)
[Vector.between](#vectorbetween)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Return a vector pointing from vec1 to vec2. | [<span class="tag vec"></span>](/types)
[Vector.lerp](#vectorlerp)([<span class="tag vec"></span>](/types)&nbsp;p1, [<span class="tag vec"></span>](/types)&nbsp;p2, [<span class="tag flo"></span>](/types)&nbsp;t) | Linearly interpolates between two points. Numeric arg [0, 1] is the fraction. | [<span class="tag vec"></span>](/types)
[Vector.cross](#vectorcross)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Return a cross-product vector of two vectors. | [<span class="tag vec"></span>](/types)
[Vector.dot](#vectordot)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Return a dot product of two vectors. | [<span class="tag flo"></span>](/types)
[Vector.angle](#vectorangle)([<span class="tag vec"></span>](/types)&nbsp;vec1, [<span class="tag vec"></span>](/types)&nbsp;vec2) | Return an angle between two vectors, in degrees [0, 180]. | [<span class="tag flo"></span>](/types)
[Vector.distance](#vectordistance)([<span class="tag vec"></span>](/types)&nbsp;p1, [<span class="tag vec"></span>](/types)&nbsp;p2) | Returns distance between two points. | [<span class="tag flo"></span>](/types)
[Vector.sqrDistance](#vectorsqrdistance)([<span class="tag vec"></span>](/types)&nbsp;p1, [<span class="tag vec"></span>](/types)&nbsp;p2) | Returns squared distance between two points. | [<span class="tag flo"></span>](/types)


!!!tip
    All static methods can be call like other method with this format:
    
    ``` Lua
	vec1:method(vec2, args)
	```

###Arithmetics methods summary
Method Name | Description | Return | &nbsp;
-- | -- | -- | --:
vec:[add](#add)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Adds components of otherVec to self. | [<span class="tag vec"></span>](/types)
vec:[sub](#sub)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Subtracts components of otherVec from self. | [<span class="tag vec"></span>](/types)
vec:[inverse](#inverse)() | Multiply self-components by -1. | [<span class="tag vec"></span>](/types)
vec:[scale](#scale)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Multiplies self-components by corresponding components from otherVec. | [<span class="tag vec"></span>](/types)
vec:[scale](#scale)([<span class="tag flo"></span>](/types)&nbsp;num) | Multiplies self-components by a numeric factor. | [<span class="tag vec"></span>](/types)
vec:[clamp](#clamp)([<span class="tag flo"></span>](/types)&nbsp;num) | If self-magnitude is higher than provided limit, scale self-down to match it. | [<span class="tag vec"></span>](/types)
vec:[normalize](#normalize)() | Makes this vector have a magnitude of 1. | [<span class="tag vec"></span>](/types)
vec:[project](#project)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Make self into projection on another vector. | [<span class="tag vec"></span>](/types)
vec:[projectOnPlane](#projectonplane)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Project self on a plane defined through a normal vector arg. | [<span class="tag vec"></span>](/types)
vec:[reflect](#reflect)([<span class="tag vec"></span>](/types)&nbsp;otherVec) | Reflect self over a plane defined through a normal vector arg. | [<span class="tag vec"></span>](/types)
vec:[moveTowards](#movetowards)([<span class="tag vec"></span>](/types)&nbsp;otherVec, [<span class="tag flo"></span>](/types)&nbsp;num) | Move self towards another vector, but only up to a provided distance limit. | [<span class="tag vec"></span>](/types)
vec:[rotateTowards](#rotatetowards)([<span class="tag vec"></span>](/types)&nbsp;target, [<span class="tag flo"></span>](/types)&nbsp;maxAngle) | Rotate self towards another vector, but only up to a provided angle limit. | [<span class="tag vec"></span>](/types)
vec:[rotateTowardsUnit](#rotatetowardsunit)([<span class="tag vec"></span>](/types)&nbsp;target, [<span class="tag flo"></span>](/types)&nbsp;maxAngle) | Same as rotateTowards, but only works correctly if `target` Vector is normalized. Less expensive than `rotateTowards`. | [<span class="tag vec"></span>](/types)
vec:[rotateOver](#rotateover)([<span class="tag str"></span>](/types)&nbsp;axis, [<span class="tag flo"></span>](/types)&nbsp;angle) | Rotate a Vector `angle` degres over given `axis` (can be `'x'`, `'y'`, `'z'`) and return self. | [<span class="tag vec"></span>](/types)

!!!tip
    Numerous methods of Vector will return the same vector instance to allow easy "chaining". That way you can do more complex processing without saving an intermediate result in a variable, like e.g. `vec:setAt('y', 0):scale(0.5):rotateOver('y', 90)`.
	
    All arithmetic methods can be used as static: 

    ``` Lua
    target = Vector(1, 2, 3)
    vec = Vector.rotateTowards(vec, target, 6)
    ```

Vector also allows you to use arithmetic operators to performs basic operations:

Operator | Description | Return | &nbsp;
-- | -- | -- | --
[<span class="tag vec"></span>](/types)&nbsp;one + [<span class="tag vec"></span>](/types)&nbsp;two | Returns a new Vector that is a sum of `one` and `two` | [<span class="tag vec"></span>](/types#vector) 
[<span class="tag vec"></span>](/types)&nbsp;one - [<span class="tag vec"></span>](/types)&nbsp;two | Returns a new Vector that is a difference of `one` and `two` | [<span class="tag vec"></span>](/types#vector) 
[<span class="tag vec"></span>](/types)&nbsp;one * [<span class="tag flo"></span>](/types)&nbsp;factor | Returns a new Vector that is `one` with each component multiplied by the factor. | [<span class="tag vec"></span>](/types#vector) 
[<span class="tag vec"></span>](/types)&nbsp;one == [<span class="tag vec"></span>](/types)&nbsp;two | Returns a boolean whether `one` and `two` are very similar to each other (less than ~0.03 difference in magnitude) | [<span class="tag boo"></span>](/types)

####Arithmetics and operators examples

```lua
function onLoad()
    local vec = Vector(1, 2, 3)
    vec:add(Vector(3, 2, 1)) --> vec is now {4, 4, 4}
    vec:sub(Vector(1, 0, 1)) --> vec is now {3, 4, 3}
    
    local another = vec + Vector(-1, -2, -1) --> another is {2, 2, 2}, vec remains unchanged

    print(another:equals(Vector(1, 2, 3))) --> false
    print(another == Vector(2, 2, 2)) --> true
    print(another == Vector(1.99, 2.01, 2)) --> true, small differences are tolerated
end
```

###Property methods summary
Method Name | Description | Return | &nbsp;
-- | -- | -- | --:
vec:[magnitude](#magnitude)() | Returns the length of this vector. | [<span class="tag flo"></span>](/types)
vec:[sqrMagnitude](#sqrmagnitude)() | Returns the squared length of this vector. | [<span class="tag flo"></span>](/types)
vec:[string](#string)([<span class="tag str"></span>](/types)&nbsp;prefix) | Return string describing self, optional string prefix. | [<span class="tag str"></span>](/types)
vec:[normalized](#normalized)() | Return a new vector that is normalized (length 1) version of self. | [<span class="tag vec"></span>](/types)
vec:[orthoNormalize](#orthonormalize)() | Return three normalized vectors perpendicular to each other, first one being in the same dir as self. | [<span class="tag vec"></span>](/types)&nbsp;base, [<span class="tag vec"></span>](/types)&nbsp;normal, [<span class="tag vec"></span>](/types)&nbsp;binormal
vec:[orthoNormalize](#orthonormalize)([<span class="tag vec"></span>](/types)&nbsp;binormalPlanar) | Same as vec:orthoNormalize(), but second vector is guranteed to be on a self-binormalPlanar plane. | [<span class="tag vec"></span>](/types)&nbsp;base, [<span class="tag vec"></span>](/types)&nbsp;normal, [<span class="tag vec"></span>](/types)&nbsp;binormal
vec:[heading](#heading)([<span class="tag str"></span>](/types)&nbsp;axis) | Returns an angle (In degrees) of rotation of Vector over a given `axis` (can be `'x'`, `'y'`, `'z'`). | [<span class="tag flo"></span>](/types)

---

##Methods details

###Static methods details

####Vector.equals(...)

[<span class="ret boo"></span>](/types)&nbsp;Returns true if two vectors are approximately equal.
The `margin` argument is optional and defaults to tolerating a difference of `~0.03` in both vector magnitude.

!!!info "Vector.equals(vec1, vec2, margin)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.
    * [<span class="tag flo"></span>](/types) **margin**: (Optional) Numeric tolerance.

``` Lua
vec1 = Vector(1, 2, 3.10)
vec2 = Vector(1, 2, 3.15)
print(Vector.equals(vec1, vec2)) --> false
print(Vector.equals(vec1, vec2, 0.01)) --> true
```

####Vector.min(...)

[<span class="ret vec"></span>](/types)&nbsp;Returns a vector that is made from the smallest components of two vectors.

!!!info "Vector.min(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 3, 2)
print(Vector.min(vec1, vec2)) --> Vector: { 1, 2, 2 }
```

####Vector.max(...)

[<span class="ret vec"></span>](/types)&nbsp;Returns a vector that is made from the largest components of two vectors.

!!!info "Vector.max(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 3, 2)
print(Vector.max(vec1, vec2)) --> Vector: { 4, 3, 3 }
```

####Vector.between(...)

[<span class="ret vec"></span>](/types)&nbsp;Return a vector pointing from vec1 to vec2.

!!!info "Vector.between(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 3, 2)
print(Vector.between(vec1, vec2)) --> Vector: { 3, 1, -1 }
```

####Vector.lerp(...)

[<span class="ret vec"></span>](/types)&nbsp;Linearly interpolates between two points.

Interpolates between the points a and b by the interpolant t. The parameter t is clamped to the range [0, 1]. This is most commonly used to find a point some fraction of the way along a line between two endpoints (e.g. to move an object gradually between those points).

The value returned equals (b - a) * t. When t = 0 returns a. When t = 1 returns b. When t = 0.5 returns the point midway between a and b.

!!!info "Vector.lerp(p1, p2)"
    * [<span class="tag vec"></span>](/types) **p1**: First point.
    * [<span class="tag vec"></span>](/types) **p2**: Second point.
    * [<span class="tag flo"></span>](/types) **t**: Fraction.

``` Lua
p1 = Vector(1, 2, - 4)
p2 = Vector(1, 2, 4)
print(Vector.lerp(p1, p2, 0.25)) --> Vector: { 1, 2, -2 }
```

####Vector.cross(...)

[<span class="ret vec"></span>](/types)&nbsp;Return a cross-product vector of two vectors.

The cross product of two vectors results in a third vector which is perpendicular to the two input vectors. The result's magnitude is equal to the magnitudes of the two inputs multiplied together and then multiplied by the sine of the angle between the inputs. You can determine the direction of the result vector using the "left hand rule".

!!!info "Vector.cross(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 3, 2)
print(Vector.cross(vec1, vec2)) --> Vector: { -5, 10, -5 }
print(Vector.cross(vec2, vec1)) --> Vector: {-5, -10, 5 }
```

####Vector.dot(...)

[<span class="ret flo"></span>](/types)&nbsp;Return the dot product of two vectors.

The dot product is a float value equal to the magnitudes of the two vectors multiplied together and then multiplied by the cosine of the angle between them.

For normalized vectors Dot returns 1 if they point in exactly the same direction, -1 if they point in completely opposite directions and zero if the vectors are perpendicular.

!!!info "Vector.dot(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(0, 1, 2)
vec2 = Vector(0, 2, 4)
print(Vector.dot(vec1, vec2)) --> 10
print(Vector.dot(vec1:normalized(), vec2:normalized())) --> 1
```

####Vector.angle(...)

[<span class="ret flo"></span>](/types)&nbsp;Returns the angle in degrees between two vectors.

The angle returned is the unsigned angle between the two vectors. This means the smaller of the two possible angles between the two vectors is used. The result is never greater than 180 degrees.

!!!info "Vector.angle(vec1, vec2)"
    * [<span class="tag vec"></span>](/types) **vec1**: First vector.
    * [<span class="tag vec"></span>](/types) **vec2**: Second vector.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 3, 2)
print(Vector.angle(vec1, vec2)) --> 37.43
```

####Vector.distance(...)

[<span class="ret flo"></span>](/types)&nbsp;Returns distance between two points.

!!!info "Vector.distance(p1, p2)"
    * [<span class="tag vec"></span>](/types) **p1**: First point.
    * [<span class="tag vec"></span>](/types) **p2**: Second point.

``` Lua
p1 = Vector(1, 2, 3)
p2 = Vector(4, 3, 2)
print(Vector.distance(p1, p2)) --> 3.32
print((p1 - p2):magnitude())  --> 3.32
```

####Vector.sqrDistance(...)

[<span class="ret flo"></span>](/types)&nbsp;Returns squared distance between two points.

!!!info "Vector.sqrDistance(p1, p2)"
    * [<span class="tag vec"></span>](/types) **p1**: First point.
    * [<span class="tag vec"></span>](/types) **p2**: Second point.

``` Lua
p1 = Vector(1, 2, 3)
p2 = Vector(4, 3, 2)
print(Vector.sqrDistance(p1, p2)) --> 11
```

###Arithmetics methods details

####setAt(...)

[<span class="ret vec"></span>](/types)&nbsp;Update one component of the vector and returning self.

!!!info "setAt(key, num)"
    * [<span class="tag int"></span>](/types) **key**: Index of component (1, 2 or 3 for x, y or z).
    * [<span class="tag flo"></span>](/types) **num**: New value.

``` Lua
vec = Vector(1, 2, 3)
vec:setAt(1, 4):setAt('y', 3)
print(vec) --> Vector: { 4, 3, 3 }
```

####set(...)

[<span class="ret vec"></span>](/types)&nbsp;Update all components of the vector and returning self.

!!!info "set(x, y, z)"
    * [<span class="tag flo"></span>](/types) **x**: New value of X component.
    * [<span class="tag flo"></span>](/types) **y**: New value of Y component.
    * [<span class="tag flo"></span>](/types) **z**: New value of Z component.

``` Lua
vec = Vector(1, 2, 3)
vec:set(4, 3, 2)
print(vec) --> Vector: { 4, 3, 2 }
```

####add(...)

[<span class="ret vec"></span>](/types)&nbsp;Adds components of otherVec to self and returning self.

!!!info "add(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The vector to add.

``` Lua
vec = Vector(1, 2, 3)
otherVec = Vector(4, 5, 6)
vec:add(otherVec)
print(vec) --> Vector: { 5, 7, 9 }

-- Same as
vec = Vector(1, 2, 3)
otherVec = Vector(4, 5, 6)
vec = vec + otherVec
print(vec) --> Vector: { 5, 7, 9 }
```

####sub(...)

[<span class="ret vec"></span>](/types)&nbsp;Subtracts components of otherVec from self and returning self.

!!!info "sub(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The vector to subtracts.

``` Lua
vec = Vector(1, 2, 3)
otherVec = Vector(6, 5, 4)
vec:sub(otherVec)
print(vec) --> Vector: { -5, -3, -1 }

-- Same as
vec = Vector(1, 2, 3)
otherVec = Vector(6, 5, 4)
vec = vec - otherVec
print(vec) --> Vector: { -5, -3, -1 }
```
####inverse()

[<span class="ret vec"></span>](/types)&nbsp;Multiply self-components by -1.

``` Lua
vec = Vector(1, 2, 3)
vec:inverse()
print(vec) --> Vector: { -1, -2, -3 }
```

####scale(...)

[<span class="ret vec"></span>](/types)&nbsp;Multiplies self-components by corresponding components from otherVec.

Every component in the result is a component of vec multiplied by the same component of otherVec or by a number factor.

!!!info "scale(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The vector to scale.

!!!info "scale(num)"
    * [<span class="tag flo"></span>](/types) **num**: The numeric factor.

``` Lua
vec = Vector(1, 2, 3)
otherVec = Vector(2, 3, 4)
vec:scale(otherVec)
print(vec) --> Vector: { 2, 6, 12 }
vec:scale(2)
print(vec) --> Vector: { 4, 12, 24 }
```

####clamp(...)

[<span class="ret vec"></span>](/types)&nbsp;If self-magnitude is higher than provided limit, scale self-down to match it.

!!!info "clamp(num)"
    * [<span class="tag flo"></span>](/types) **num**: The numeric max magnitude.

``` Lua
vec = Vector(1, 2, 3)
vec:clamp(2)
print(vec) --> Vector: { 0.53, 1.07, 1.60 }
```

####normalize()

[<span class="ret vec"></span>](/types)&nbsp;Makes this vector have a magnitude of 1.

When normalized, a vector keeps the same direction but its length is 1.0.

Note that this function will change the current vector. If you want to keep the current vector unchanged, use [normalized()](#normalized) method.

``` Lua
vec = Vector(1, 2, 3)
vec:normalize()
print(vec) --> Vector: { 0.27, 0.53, 0.80 }
```

####project(...)

[<span class="ret vec"></span>](/types)&nbsp;Make self into projection on another vector.

To understand vector projection, imagine that `otherVec` is resting on a line pointing in its direction. Somewhere along that line will be the nearest point to the tip of vector. The projection is just `otherVec` rescaled so that it reaches that point on the line.

!!!info "project(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The normal vector.

``` Lua
vec = Vector(2, 1, 4)
vec:project(Vector(1, - 2, 1))
print(vec) --> Vector: { 0.67, -1.3, 0.67 }
```

####projectOnPlane(...)

[<span class="ret vec"></span>](/types)&nbsp;Projects a vector onto a plane defined by a normal orthogonal to the plane.

A Vector stores the position of the given `vec` in 3d space. A second Vector is given by `otherVec` and defines a direction from a plane towards vector that passes through the origin. Vector.projectOnPlane uses the two Vector values to generate the position of vector in the `otherVec` direction, and return the location of the Vector on the plane.

!!!info "projectOnPlane(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The plane normal vector.

``` Lua
vec = Vector(2, 1, 4)
vec:projectOnPlane(Vector(1, - 2, 1))
print(vec) --> Vector: { 1.33, 2.33, 3.33 }
```

####reflect(...)

[<span class="ret vec"></span>](/types)&nbsp;Make self into reflection on another vector.

The `otherVec` vector defines a plane (a plane's normal is the vector that is perpendicular to its surface). The `vec` vector is treated as a directional arrow coming in to the plane. The returned value is a vector of equal magnitude to `vec` but with its direction reflected.


!!!info "reflect(otherVec)"
    * [<span class="tag vec"></span>](/types) **otherVec**: The normal vector.

``` Lua
vec = Vector(1, 2, 3)
vec:reflect(Vector(4, 3, 2))
print(vec) --> Vector: { -3.41, -1.31, 0.79 }
```

####moveTowards(...)

[<span class="ret vec"></span>](/types)&nbsp;Move self towards another vector, but only up to a provided distance limit.

!!!info "moveTowards(otherVec, num)"
    * [<span class="tag vec"></span>](/types) **target**: The position to move towards.
    * [<span class="tag flo"></span>](/types) **num**: The distance limit.

``` Lua
vec = Vector(1, 2, 3)
vec:moveTowards(Vector(4, 3, 2), 0.5)
print(vec) --> Vector: { 1.45, 2.15, 2.85 }
```

####rotateTowards(...)

[<span class="ret vec"></span>](/types)&nbsp;Rotate self towards another vector, but only up to a provided angle limit.

This function is similar to [moveTowards()](#movetowards) except that the vector is treated as a direction rather than a position. The current vector will be rotated round toward the target direction by an angle of `maxAngle`, although it will land exactly on the target rather than overshoot. If the magnitudes of current and target are different, then the magnitude of the result will be linearly interpolated during the rotation. If a negative value is used for `maxAngle`, the vector will rotate away from target until it is pointing in exactly the opposite direction, then stops.

!!!info "rotateTowards(target, maxAngle)"
    * [<span class="tag vec"></span>](/types) **target**: The position to rotate towards.
    * [<span class="tag flo"></span>](/types) **maxAngle**: The maximum angle in **degree** allowed for this rotation.

``` Lua
vec = Vector(1, 2, 3)
vec:rotateTowards(Vector(4, 3, 2), 45)
print(vec) --> Vector: { 2.78, 2.08, 1.39 }
```

####rotateTowardsUnit(...)

[<span class="ret vec"></span>](/types)&nbsp;Same as [rotateTowards()](#rotatetowards), but only works correctly if `target` Vector is normalized. Less expensive than `rotateTowards()`.

!!!info "rotateTowardsUnit(target, maxAngle)"
    * [<span class="tag vec"></span>](/types) **target**: The position to rotate towards.
    * [<span class="tag flo"></span>](/types) **maxAngle**: The maximum angle in **degree** allowed for this rotation.

``` Lua
vec = Vector(1, 2, 3)
vec:rotateTowardsUnit(Vector(4, 3, 2):normalized(), 45)
print(vec) --> Vector: { 3.29, 0.87, -1.55 }
```

####rotateOver(...)

[<span class="ret vec"></span>](/types)&nbsp;Rotate a Vector `angle` degrees over given `axis` (can be `'x'`, `'y'`, `'z'`) and return self.

!!!info "rotateOver(axis, angle)"
    * [<span class="tag vec"></span>](/types) **axis**: The axis to rotate around.
    * [<span class="tag flo"></span>](/types) **angle**: The angle in **degree** for this rotation.

``` Lua
vec = Vector(3, 2, 3)
vec:rotateOver('y', 45)
print(vec) --> Vector: { 4.24, 2, 0 }
```

###Property methods details

####get()

[<span class="ret flo" style="margin-right:5px;"></span>](/types)
[<span class="ret flo" style="margin-right:5px;"></span>](/types)
[<span class="ret flo"></span>](/types)&nbsp;Returns `x`, `y`, `z` components as three separate values.

``` Lua
vec = Vector(1, 2, 3)
x, y, z = vec:get()
print(x + y + z) --> 6
```
####copy()

[<span class="ret vec"></span>](/types)&nbsp;Copy self into a new vector and return it.

``` Lua
vec1 = Vector(1, 2, 3)
vec2 = vec1:copy()
vec1:set(4, 3, 2)
print(vec1) --> Vector { 4, 3, 2 }
print(vec2) --> Vector { 1, 2, 3 }
```

####magnitude()

[<span class="ret flo"></span>](/types)&nbsp;Returns the length of this vector.

``` Lua
vec = Vector(1, 2, 3)
print(vec:magnitude()) --> 3.74 (sqrt of 14)
```

####sqrMagnitude()

[<span class="ret flo"></span>](/types)&nbsp;Returns the squared length of this vector.

``` Lua
vec = Vector(1, 2, 3)
print(vec:sqrMagnitude()) --> 14
```

####string(...)

[<span class="ret str"></span>](/types)&nbsp;Return string describing self, optional string prefix.

!!!info "string(prefix)"
    * [<span class="tag str"></span>](/types) **prefix**: The prefix of return string.

``` Lua
vec = Vector(1, 2, 3)
str = vec:string('Prefix')
print(str) --> Prefix: { 1, 2, 3 }
print(vec:string('Prefix')) --> Prefix: { 1, 2, 3 }0
```

!!!warning
    This function returns one extra float that will be displayed in print function.

####normalized()

[<span class="ret vec"></span>](/types)&nbsp;Return a new vector that is normalized (length 1) version of self.

``` Lua
vec = Vector(1, 2, 3)
print(vec:normalized()) --> Vector: { 0.27, 0.53, 0.80}
```

####orthoNormalize(...)

[<span class="ret vec" style="margin-right:5px;"></span>](/types)
[<span class="ret vec" style="margin-right:5px;"></span>](/types)
[<span class="ret vec"></span>](/types)&nbsp;Return three normalized vectors perpendicular to each other, first one being in the same direction as self. If `binormalPlaner` is provided, the second vector is guaranteed to be on a self-binormalPlanar plane.

!!!info "orthoNormalize(binormalPlanar)"
    * [<span class="tag vec"></span>](/types) **binormalPlanar**: (optional) The vector for binormal planar.


``` Lua
vec = Vector(0, 0, 2)
base, normal, binormal = vec:orthoNormalize(Vector(0, 1, 0))
print(base) --> Vector: { 0, 0, 1}
print(normal) --> Vector: { -1, 0, 0}
print(binormal) --> Vector: { 0, -1, 0}
```

####heading(...)

[<span class="ret flo"></span>](/types)&nbsp;Returns an angle (In degrees) of rotation of Vector over a given `axis` (can be `'x'`, `'y'`, `'z'`).

!!!info "heading(axis)"
    * [<span class="tag str"></span>](/types) **axis**: Can be `'x'`, `'y'`, `'z'`.

``` Lua
vec = Vector(1, 2, 3)
angle = vec:heading('z')
print(angle) --> 26.57
```

---

##Manipulation examples

Moving an object towards a target position in small steps
```lua
function onLoad()
    local obj = assert(getObjectFromGUID('555555'), 'Object not found!')
    obj.lock()

    local current =  Vector(10, 5, 0) -- obj starting position
    local target =   Vector(-10, 5, 0) -- obj destination
    local movementType = 'linear' -- try with 'spherical' or 'asymptotic' to see how other methods work

    -- We want out movement stretched over time, a Wait will do it periodically
    local waitID
    waitID = Wait.time(
        function()
            -- move the current postion towards destination

            if movementType == 'linear' then
                -- simple linear movement, 1 unit at a time
                current:moveTowards(target, 1)
            elseif movementType == 'spherical' then
                -- rotate towards target, 10 degress at a time
                current:rotateTowards(target, 5)
            elseif movementType == 'asymptotic' then
                -- move quarter of the way towards target (take note that lerp does not modify current directly)
                current = current:lerp(target, 0.25)
            end

            obj.setPositionSmooth(current, true, true)

            -- if we reached the destination, stop this timer
            if current == target then
                Wait.stop(waitID)
                broadcastToAll('Finished!', {0, 1, 0})
            end
        end,
        0.5,  -- repeats every half second
        -1  -- indefinitely, until stopped because we reached destination
    )
end
```
