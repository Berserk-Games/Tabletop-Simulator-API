This is an ongoing list of scripting changes that have been implemented to scripting side of Tabletop Simulator.

######5/9/18 - v10.5 Hotfix 2

!!!info ""
    * Custom UI:
        * Added UI.show(id) and UI.hide(id) for disabling and enabling ui with animations.
        * Now support the Image tag for custom images. 
        * Supports overriding the look of the UI using this custom image support.
        * Fixed visibility attribute not working correctly on elements with no id attribute or layout tag.
        * Fixed offsetXY set/getAttribute() not working.
        * Added Tooltip attribute for all objects

######5/7/18 - v10.5

!!!info ""
    * Addition of XML Custom UI and associated documentation as part of this documentation.
    * onSearchStart/onSearchEnd/onObjectSearchStart/onObjectSearchEnd added to Events.
    * The log() command's "label" and "tag" parameters were reversed to `log(object, label, tags)`
    * Scripted object button changes
        * The click_function of scripted object buttons now passes an argument for alt_click. This allows determining if anything besides left click was used on the button (like right click)
        * hover_color and press_color added as optional parameters
    * getJSON() and spawnObjectJSON() created.
    * Turns global static class added
        * Member variables for controlling how turns work
        * New event trigger for player turns beginning (onPlayerTurn)
        * Devalued previous onPlayerTurn events
    * Changelog moved under Getting Started due to the fact that it applies to the UI API as well as the scripting API. But I guess you figured that out already, didn't ya.
    * Added getJSON and spawnObjectJSON to Object/Base, respectively.
    

######3/26/18 - v10.4 Hotfix 2

!!!info ""
    * New Tabletop Simulator Scripting Documentation is created.
