## Available scripting methods

### In-Game Lua Editor
You can access the in-game Lua Editor by clicking on **Scripting** on the top bar or by right clicking on an object, choosing Scripting, and then selecting Lua Editor from the contextual menu. In the Lua Editor, the tabs on the left of the editor let you switch between the Global and the Object scripts. Once your Lua code is written, you can use the *Save and Play* button to commit your changes to your save file and reload for quick iteration. *Save and Play* will only commit your script changes, any changes made that weren't scripting will be lost.

The advantage of this method is it requires no additional setup. However it lacks many features included in some of the other options.

![Overview](img/overview1.png)


### Official Atom Plugin
The preferred method of writing Lua scripts is using our Official Plugin for the Atom Text Editor. It has all of the functionality of the in-game editor plus line numbers, syntax highlighting, autocomplete, and a modern look. [Click here for setup instructions.](atom.md)

![Aton Plugin](img/overview2.png)


### External Editor API
It is also possible to edit inside of other envionments which are not officially supported. Using the External Editor API it is possible to work in other enviornments (like Notepad++).

!!! warning
	This method does not, by default, include many features that Atom provides, like auto-completion of Tabletop Simulator functions/class members.


###For further information
* [Official Lua Website](http://www.lua.org/home.html)
* [MoonSharp](http://www.moonsharp.org/)


##Example Mods
* [BlackJack](http://steamcommunity.com/sharedfiles/filedetails/?id=620967608)
* [Chess Clock](http://steamcommunity.com/sharedfiles/filedetails/?id=659350499)
* [Roulette](http://steamcommunity.com/sharedfiles/filedetails/?id=659349425)
* [Interactable](http://steamcommunity.com/sharedfiles/filedetails/?id=737574536)
