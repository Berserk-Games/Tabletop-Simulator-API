Component is a unique collection of functions and member variables. They interact directly with the Unity properties of the objects that Tabletop Simulator is composed of. This means that a level of understanding of how Unity works is required to utilize these commands.

!!!warning
	In other words, this is a highly advanced feature and this API is only able to teach you the basic commands to utilize it.

##General Concepts
Every object in a "room" of Tabletop Simulator is a **GameObject**. Some sort of entity which exists within the scene. When a room is created, the GameObjects are loaded and initiated into the Lua script system. This is why, if you spawn a block and then run `print(self)` on it, it will print `BlockSquare(Clone) (LuaGameObjectScript)` into the chat. `BlockSquare(Clone)` is the GameObject, while `(LuaGameObjectScript)` is the Lua scripting system.

GameObjects themselves contain many variables called **Components**. These can be the Collider, Transform, Mesh, etc that compose a GameObject, telling Unity how to render it. The component functions allow you to directly access the GameObjects and Components that make up any object in Tabletop Simulator, including your own AssetBundles. This means you can attach all manner of components (lights, sounds, and a lot more) and then control them.

Finally, each Component has **Vars**, variables which you can modify to change how that Component effects the GameObject. The best way to explain this more clearly is with a few examples.

##General Examples
The specific functions will be covered further down this page. These examples are scripts placed on a regular red block.

###Disable Receiving Shadows
```Lua
function onLoad()
	-- Get the MeshRenderer of the block's GameObject
	local blockComp = self.getComponent("MeshRenderer")
	-- Disable its ability to have a shadow cast onto it by another Object
	blockComp.set("receiveShadows", false)
end
```

###Modify Object's Collider
```Lua
function onLoad()
	-- Get the BoxCollider Component of the block's GameObject
	local blockComp = self.getComponent("BoxCollider")
	-- Now lets make its collider disappear
	blockComp.set("enabled", false)
	-- Watch the block fall through the world and vanish
	-- The system deletes it once it falls too far
end
```

###Completly Silence an Object
```Lua
function onLoad()
	-- Get the AudioSource Component of the block's GameObject
	local blockComp = self.getComponent("AudioSource")
	-- Mute it
	blockComp.set("mute", true)
	-- Now it makes no sound when impacting anything.
end
```

And these examples are only scraping the surface of what these functions can do. It essentially gives you near-full access to anything an object in Unity is capable of.

---

##Commands

###Object and GameObject Commands
These can be used on either a regular in-game Object or an in-game Objects `GameObject`.

Command Name | Description | Return&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | --
<a class="anchor" id="getcomponent"></a>getComponent([<span class="tag str"></span>](types.md)&nbsp;name) | Obtains a component reference from an Object, by name. | **Component**
<a class="anchor" id="getcomponents"></a>getComponents([<span class="tag str"></span>](types.md)&nbsp;optional_name) | Returns all components on a game object. The name is an optional component name to narrow results with. | **Component** in [<span class="ret tab"></span>](types.md)
<a class="anchor" id="name"></a>name | Returns the name of the given Object or GameObject. | [<span class="ret str"></span>](types.md)


###GameObject Children Commands
When you access an in-game Object normally with Lua, it is always the "parent" object. Other objects can be "attached" to that parent object as a child object. You are able to access those children with these commands.

Command Name | Description | Return&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | --
<a class="anchor" id="getcomponentinchildren"></a>getComponentInChildren([<span class="tag str"></span>](types.md)&nbsp;name) | Obtains a component reference from a child GameObject, by name. | **Component**
<a class="anchor" id="getcomponentsinchildren"></a>getComponentsInChildren([<span class="tag str"></span>](types.md)&nbsp;optional_name) | Returns all components of all child GameObjects attached to this parent Object. The name is an optional component name to narrow results with. | **Component** in [<span class="ret tab"></span>](types.md)
<a class="anchor" id="getchild"></a>getChild([<span class="tag str"></span>](types.md)&nbsp;name) | Obtains a reference to the GameObject of a child object. The name is the name of the GameObject. | **GameObject**
<a class="anchor" id="getchildren"></a>getChildren() | Returns a list of all GameObjects attached under the parent GameObject. | **GameObject** in [<span class="ret tab"></span>](types.md)

###Component Commands
These commands are used on the Components of objects to find or modify the values of their variables. The values will depend on which variable is being changed. They are usually System.Int32 (an Integer), System.Boolean (a Bool) or UnityEngine.Vector3 (a Vector). These are all used on Components.

Command Name | Description | Return&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
-- | -- | --
<a class="anchor" id="game_object"></a>game_object | Returns the GameObject the component is on. | **GameObject**
<a class="anchor" id="get"></a>get([<span class="tag str"></span>](types.md)&nbsp;varName) | Obtains the value of a given Variable on a Component. | [<span class="ret var"></span>](types.md)
<a class="anchor" id="get"></a>getVars() | Obtains a table containing Variable names along with the type of value they take. | [<span class="ret tab"></span>](types.md)
<a class="anchor" id="set"></a>set([<span class="tag str"></span>](types.md)&nbsp;varName, [<span class="tag var"></span>](types.md)&nbsp;value) | Sets a value to a Variable on the Component | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="name"></a>name | Returns the name of the given Object or GameObject. | [<span class="ret str"></span>](types.md)
