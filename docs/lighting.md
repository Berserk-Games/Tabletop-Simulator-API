Lighting, a static global class, is the in-game light of the map. It allows you to modify the lighting of the instance in the same way that the [in-game lighting menu](https://kb.tabletopsimulator.com/host-guides/lighting/) does. You call these functions like this: `Lighting.apply()`.

For more information on lighting in Unity, [refer to the Unity documentation](https://docs.unity3d.com/Manual/LightingOverview.html).

!!!example
    Make the lighting _bright_ red.
    ```lua
    Lighting.light_intensity = 2
    Lighting.setLightColor({r = 1, g = 0.6, b = 0.6})
    Lighting.apply()
    ```

##Member Variables

Variable | Type | Description
-- | -- | --
ambient_intensity {: #ambient_intensity } | [<span class="tag flo"></span>](types.md) | The strength of the ambient light. Range = 0 to 4.
ambient_type {: #ambient_type } | [<span class="tag int"></span>](types.md) | The source of ambient light. 1 = background, 2 = gradient.
light_intensity {: #light_intensity } | [<span class="tag flo"></span>](types.md) | The strength of the directional light shining down in the scene. Range = 0 to 4.
lut_contribution {: #lut_contribution } | [<span class="tag flo"></span>](types.md) | How much the LUT contributes to the light.
lut_index {: #lut_index } | [<span class="tag int"></span>](types.md) | The LUT index of the light.
lut_url {: #lut_url } | [<span class="tag str"></span>](types.md) | The URL of the LUT.
reflection_intensity {: #reflection_intensity } | [<span class="tag flo"></span>](types.md) | The strength of the reflections from the background. Range = 0 to 1.

##Function Summary

###Functions {: data-toc-sort }

Function Name | Return | Description
-- | -- | --
apply() {: #apply data-toc-label="apply()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](types.md) | Applies pending changes made via the Lighting class.
getAmbientEquatorColor() {: #getambientequatorcolor data-toc-label="getAmbientEquatorColor()" data-toc-child-of="functions" } | [<span class="ret col"></span>](types.md#color) | Returns Color Table of the gradient equator. Not used if `ambient_type = 1`.
getAmbientGroundColor() {: #getambientgroundcolor data-toc-label="getAmbientGroundColor()" data-toc-child-of="functions" } | [<span class="ret col"></span>](types.md#color) | Returns Color Table of the gradient ground. Not used if `ambient_type = 1`.
getAmbientSkyColor() {: #getambientskycolor data-toc-label="getAmbientSkyColor()" data-toc-child-of="functions } | [<span class="ret col"></span>](types.md#color) | Returns Color Table of the gradient sky. Not used if `ambient_type = 1`.
getLightColor() {: #getlightcolor data-toc-label="getLightColor()" data-toc-child-of="functions" } | [<span class="ret col"></span>](types.md#color) | Returns Color Table of the directional light, which shines straight down on the table.
setAmbientEquatorColor([<span class="tag col"></span>](types.md#color) tint) {: #setambientequatorcolor data-toc-label="setAmbientEquatorColor(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](types.md) | Sets the color of the gradient equator. Not used if `ambient_type = 1`.
setAmbientGroundColor([<span class="tag col"></span>](types.md#color) tint) {: #setambientgroundcolor data-toc-label="setAmbientGroundColor(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](types.md) | Sets the color of the gradient ground. Not used if `ambient_type = 1`.
setAmbientSkyColor([<span class="tag col"></span>](types.md#color) tint) {: #setambientskycolor data-toc-label="setAmbientSkyColor(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](types.md) | Sets the color of the gradient sky. Not used if `ambient_type = 1`.
setLightColor([<span class="tag col"></span>](types.md#color) tint) {: #setlightcolor data-toc-label="setLightColor(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](types.md) | Sets the color of the directional light, which shines straight down on the table.

---
