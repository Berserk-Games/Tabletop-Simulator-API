The AssetBundle behavior is present on Objects that were created from a
[custom AssetBundle](https://kb.tabletopsimulator.com/custom-content/custom-assetbundle/).

## Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
getLoopingEffectIndex() {: #getloopingeffectindex data-toc-label="" data-toc-child-of="function-details" } | [<span class="ret int"></span>](../types.md) | Index of the currently looping effect. Indexs starts at 0. |
getLoopingEffects() | [<span class="ret tab"></span>](../types.md) | Returns a Table with the keys "index" and "name" for each looping effect. | [:i:](#getloopingeffects)
getTriggerEffects() | [<span class="ret tab"></span>](../types.md) | Returns a Table with the keys "index" and "name" for each trigger effect. | [:i:](#gettriggereffects)
playLoopingEffect([<span class="tag int"></span>](../types.md) index) {: #playloopingeffect data-toc-label="playLoopingEffect(...)" data-toc-child-of="function-details" } | [<span class="ret nil"></span>](../types.md) | Starts playing a looping effect. Indexs starts at 0. |
playTriggerEffect([<span class="tag int"></span>](../types.md) index) {: #playtriggereffect data-toc-label="playTriggerEffect(...)" data-toc-child-of="function-details" } | [<span class="ret nil"></span>](../types.md) | Starts playing a trigger effect. Indexs starts at 0. |

---

## Function Details {: data-toc-sort }

### getLoopingEffects()

[<span class="ret tab"></span>](../types.md) Returns a Table with the keys "index" and "name" for each looping effect.

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

### getTriggerEffects()

[<span class="ret tab"></span>](../types.md) Returns a Table with the keys "index" and "name" for each trigger effect.

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
