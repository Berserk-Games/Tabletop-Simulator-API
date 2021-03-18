The Browser behavior is present on the Tablet Object.

!!!example
    Instruct a Tablet Object to load the Tabletop Simulator homepage.
    ```lua
    object.Browser.url = "https://tabletopsimulator.com"
    ```

## Member Variables

Variable | Type | Description
-- | -- | --
url {: #url } | [<span class="tag str"></span>](../types.md) | URL which currently wants to display.
pixel_width {: #pixel_width } | [<span class="tag int"></span>](../types.md) | The pixel width the browser is virtually rendering to.
