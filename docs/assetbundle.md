AssetBundle is a special [Object](object.md) type that has access to [custom AssetBundle](http://berserk-games.com/knowledgebase/assetbundles/) related functions like looping and trigger effects.

Example Usage: `self.AssetBundle.getLoopingEffects()`

##Function Summary

###Object Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="getloopingeffectindex"></a>getLoopingEffectIndex()  |  Index of the currently looping effect. Indexs starts at 0. | [<span class="ret int"></span>](types.md)
getLoopingEffects()  |  Returns a Table with the keys "index" and "name" for each looping effect. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#getloopingeffects)
getTriggerEffects()  |  Returns a Table with the keys "index" and "name" for each trigger effect. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#gettriggereffects)
<a class="anchor" id="playloopingeffect"></a>playLoopingEffect([<span class="tag int"></span>](types.md)&nbsp;index)  |  Starts playing a looping effect. Indexs starts at 0. | [<span class="ret nil"></span>](types.md) |
<a class="anchor" id="playtriggereffect"></a>playTriggerEffect([<span class="tag int"></span>](types.md)&nbsp;index)  |  Starts playing a trigger effect. Indexs starts at 0. | [<span class="ret nil"></span>](types.md) |

---

##Function Details

###getLoopingEffects()

[<span class="ret tab"></span>](types.md)&nbsp;Returns a Table with the keys "index" and "name" for each looping effect.

``` Lua
	-- Example usage
	effectTable = self.AssetBundle.getLoopingEffects()
```
``` Lua
	-- Example returned table
	{
		{index=0, name="Effect Name 1"},
		{index=1, name="Effect Name 2"},
	}
```

---


###getTriggerEffects()

[<span class="ret tab"></span>](types.md)&nbsp;Returns a Table with the keys "index" and "name" for each trigger effect.

``` Lua
	-- Example usage
	effectTable = self.AssetBundle.getTriggerEffects()
```
``` Lua
	-- Example returned table
	{
		{index=0, name="Effect Name 1"},
		{index=1, name="Effect Name 2"},
	}
```
