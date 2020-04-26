Time (not to be confused with the devalued Timer class) is a static global class which provides access to Unity's time information.

> Example Usage: `Time.time`

###Member Variables
All of the member variables of time are read only.

Function Name | Description | Return
-- | -- | --
<a class="anchor" id="time"></a>time  | Returns the current time. Works like `os.time()` but is more accurate. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="delta_time"></a>delta_time  | Returns the amount of time since the last frame. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="fixed_time"></a>fixed_time  | Returns a number like `time` does, but using Fixed updates. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="fixed_delta_time"></a>fixed_delta_time  | Returns a number like `delta_time` does, but using Fixed updates. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="frame_count"></a>frame_count  | Returns the amount of total frames since the scene began. | [<span class="ret flo"></span>](types.md)
