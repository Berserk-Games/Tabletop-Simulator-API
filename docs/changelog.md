This is an ongoing list of scripting changes that have been implemented to scripting and Custom UI side of Tabletop Simulator.



######11/06/18 - v11.1

!!!info ""
    * Lua:
        * Added group(table). This allows you to group a table of objects, in the same way the "G" key would for a player! It returns a list of the grouped objects.
        * Added addDecal(table), getDecals(), and setDecals(table). Now scripting can add decals into the game world.
        * Added object.getJoints().
        * When a table of parameters for a joint is returned, it now includes joint_object_guid. This is the GUID for the object which is attached by the joint.
        * Added desired_position to the list of parameters returned by .getCustomObject() when it is used on a Jigsaw Puzzle piece. This parameter is the "solved" position for the piece.
        * New Time class added, used to easily fetch information like os.time(), but also other informations like time passed since last frame, total frames passed, etc.
        pingTable(vector) added to the Player class. Now a script can emulate a player pinging.
        * Added setComponentVar(componentName, varName, value) and getComponentVar(componentName, varName) as an object function. This allows you to access components that you have made part of your AssetBundle via scripting. For example, changing lights or colliders on the fly. These functions will also work on the components of default objects like "Collider" and "Light".




######11/06/18 - v11.0

!!!info ""
    * Lua:
        * Fog of War API elements added
            * `object.getFogOfWarReveal()` and `object.setFogOfWarReveal(table)` to access an Object's ability to reveal Fog of War.
            * `object.ignore_fog_of_war` member variable added (prevents object from being hidden)
        * Play Area
            * Change player area  with `Physics.play_area`
    * API Improvements
        * Knowledge Base link added to left nav bar.
        * Minor visual improvements
        * Footer returns


######08/17/18 - v10.9

!!!info ""
    * Lua:
        * Updates to the new Wait class
            * Added repetitions to Wait.time to better emulate Timer. Wait.time(func, time, number_repetitions).
                * Using -1 will cause infinite repetitions
            * Improvements to stop() so it should work more as expected.
        * Returns from getObject and getStates improved to a common standard, includes:
            * Name and Nickname
            * Description
            * Lua Script and Lua Script State
        * New Object functions:
            * `obj.drop()` causes the item, if held by a player, to be dropped.
            * `setHiddenFrom(players)` Hides objects from a specific player/players. Uses "hand zone" hiding.
            * `setInvisibleTo(players)` Hides objects from a specific player/players. Uses "hidden zone" hiding.
            * `attachHider(...)` and `attachInvisibleHider(...)` are more advanced version of setHiddenFrom and setInvisibleTo, there to help handle complex situations easily.
        * Old Object Functions (with new features!)
            * `setRotationValues()` now allows you to start a name/value with a # and it won't display the value in the tooltip.
            * `randomize(color)` Now an optional string can be added so that onObjectRandomized will trigger, indicating that player color triggered it.
        * New base function:
            * `get/setVectorLines()` Allows for lines to be placed via scripting using the new vector line tools`
        * New Spawnable object: Custom Decks!
            * Technically this was added before, but now it works and is documented!
            * Spawn using spawnObject then set it using setCustomObject
        * Clarifications to the Object class
            * Some functions, let setSnapPoints or call, work on both Object and Global.
            * To highlight which Object functions can be directed at the game world, they have been broken out on the Object page into a "Global Functions" section.
        * New Object member Variables
            * `use_rotation_value_flip` can be used to modify which direction objects flip.
            * `is_face_down` determines if an object's "face" is pointed down (like with cards). The face is the direction that faces the positive Y value.
            * `hide_when_face_down` hides an Object when it is face-down. Objects are hidden like if in a hidden zone. The face is the direction that faces the positive Y value.
        * New Event
            * `onObjectEnterContainer` has long been a requested event, and it is now available!






######7/9/18 - v10.8

!!!info ""
    * Lua:
        * putObject() now returns an Object.
            * Using it to combine two cards will return an object reference to the newly formed deck
            * Using it to put an object into a container/stack/deck will return the container/stack/deck it was made part of
        * New class: **Notes**
            * Contains notebook and set/getNotes functions
            * Devalued the old "Base" versions of these functions
                * {>>This means they are not in the documentation but will, for legacy reasons, still function.<<}
        * New class: **Wait**
            * This new class allows you to easily trigger functions after some form of delay
            * Contains frames, time, condition, and stop functions
            * Devalued Timer class entirely
                * {>>This means Timer is removed from documentation but, for legacy reasons, still functions.<<}
        * New Object functions:
            * **obj.cut(int)** - Cuts a deck at the given card index
            * **obj.split(int)** - Splits a deck in a number of stacks
            * **obj.getRotationValue** - Returns the current rotationValue of an object (see: gizmo tool)
                * This function existed previously, but was not documented.
        * New Event functions:
            * **onObjectPeeked(player, object)** - Triggers when peek is used by a player
            * **onPeek(player)** - Triggers when a specific object is peeked
            * **onRandomize(player)** - Triggers when randomize (R) is used on an object.
        * Player Color strings convert automatically
            * Example: printToAll("Hello", "Green")
        * Snap points created on objects use Vectors local to the Object, rather than global
            * This applies to both position and rotation
        * Fix for optional parameters of spawnObjectJSON()
        * New Object Member Variables
            * loading_custom - Indicates if the assets of a custom element are being loaded.
            * spawning - Indicates if any object is currently in the process of spawning.
                * These are helpful to determine if elements are loaded into the game fully
                * Especially useful with the new Wait class!
        * Callback Changes
            * Callback methods are being devalued (still work, but not documented)
            * Being replaced with callback_function which directly triggers a function at the same time a callback would have been triggered.
            * Done with takeObject, spawnObject(s) and webRequest(s).
    * Custom UI:
        * New Lua function:
            * **UI.setValue(string id, string value)** - Updates the value that appears within element tags {>>(ex: <Text>THIS</Text>)<<}
            * **UI.getValue(string id)** - Obtains the value that appears within element tags {>>(ex: <Text>THIS</Text>)<<}
            * Both support Rich Text!
        * New InputField attribute
            * **placeholder** - Greyed out text that appears in the input if there is no text present.
        * New Lua Function:
            * **get/setCustomAssets()** - Allows you to obtain custom UI assets uploaded to the UI Assets window. Works on global or on object's assets.


######6/18/18 - v10.7

!!!info ""
    * Custom UI:
        * Visibility attribute now supports admin, host, and team names.
        * Clicking button won't block your hotkeys anymore.
        * Added getXmlTable() setXmlTable().
        * Fixed onValueChanged recursive event loop.
        * Fixed setAttribute() not working if it thought there wasn't a change.
        * Fixed not being able to setXml() with an empty string.
        * Fix support for RichText in Get/SetXmlTable().
        * Fixed zombie Xml UI when opening File Browser.
    * Lua:
        * Added Player.getAvailableColors() and Player.getColors().
        * Added SetSnapPoints() and GetSnapPoints().
        * Added JointTo().
        * Lots of scripting improvements to make it easier to convert between Lua Tables and C# types.
        * Fixed Hotseat crash when using scripting input fields.
        * Fixed camera triggering scripting zone.
        * Fixed Turns.getNextColor() returning name instead of color.



######5/30/18 - v10.6.1

!!!info ""
    * Custom UI:
        * Added getXmlTable() and setXmlTable() for dealing with Xml easier with Lua tables.
        * Changed setXml() from changing the actual Xml for the save file so everything is runtime changes only.
        * Changed getXml() to return the current Xml string including any runtime changes from setAttribute().
        * Fixed event recursion causing a potential lock up.
        * Fixed setXml() not working with empty string.
    * Lua:
        * Added a 'debug_external_api' console command to show logging for external api messages.
        * Fixed logging an empty table throwing null.

######5/25/18 - v10.6

!!!info ""
    * Custom UI:
        * 3D UI added for objects (simialar to createButton/Input)
            * Each object can have its own assets (images)
            * Point scripting towards an object UI with `object.UI.setAttribute(...)`
            * Events called from an object's UI will automatically go to that object's Script. To override that feature and send it to Global, use `Global/functionName` for the attribute's name.
        * `UI.getXml()` and `UI.setXml()` added:
            * Allows for dynamic UI creation from a string
            * This OVERWRITES THE CURRENT XML on the target Global/object!!!
        * Click sounds added for inputs
        * Text universal attributes outlined in attributes section
        * setLookingForPlayers() added.
        * FIXED: Player colors now match TTS colors. For example, "red" is now equivalent to the player color red exactly.
        * FIXED: Dragging is improved so the element doesn't snap to its rectAlignment when dragged.
        * FIXED: When changing active attribute from script visibility would sometimes not work correctly



######5/9/18 - v10.5.1

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
