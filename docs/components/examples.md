!!!danger
	Component APIs are an advanced feature. An **understanding of how Unity works is required** to utilize them.

These examples are complete scripts which can placed on a regular Red Block.

!!!example
	Disable shadow receiving for an object.
    
	```lua
	function onLoad()
		-- Get the MeshRenderer of the block's GameObject
		local meshRenderer = self.getComponent("MeshRenderer")
		-- Disable its ability to have a shadow cast onto it by another Object
		meshRenderer.set("receiveShadows", false)
	end
	```

---

!!!example
	Disable an object's (box) collider. This will typically result in the object falling through the table.
    
	```lua
	function onLoad()
		-- Get the BoxCollider Component of the block's GameObject
		local boxCollider = self.getComponent("BoxCollider")
		-- Disable the BoxCollider Component
		boxCollider.set("enabled", false)
	end
	```

!!!example
	Disable audio for an object. The object will no longer make sound e.g. when picked up from or dropped on the table.
	Other objects may continue to make sound when colliding with this object.
    
	```lua
	function onLoad()
		-- Get the AudioSource Component of the block's GameObject
		local blockComp = self.getComponent("AudioSource")
		-- Mute it
		blockComp.set("mute", true)
	end
	```
