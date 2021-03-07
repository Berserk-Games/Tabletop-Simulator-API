`Time`, not to be confused with the deprecated [Timer](timer.md) class, is a static global class which provides access
to Unity's time information.


!!!example "Example Usage"
    ```lua
    Time.time
    ```

###Member Variables

Function Name | Description | Return
-- | -- | --
<a class="anchor" id="time"></a>time | The current time. Works like `os.time()` but is more accurate. Read only. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="delta_time"></a>delta_time | The amount of time since the last frame. Read only. | [<span class="ret flo"></span>](types.md)
<a class="anchor" id="fixed_delta_time"></a>fixed_delta_time | The interval (in seconds) between physics updates. Read only. | [<span class="ret flo"></span>](types.md)
