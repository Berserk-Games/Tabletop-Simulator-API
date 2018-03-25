In this section, you will find details on all events/classes/functions specific to Tabletop Simulator's Lua scripting. For more general information on how the scripting language of Lua works and what it does on its own, you can review the [Official Lua Documentation](https://www.lua.org/docs.html). 

##Using TTS Documentation
On each class/type page (column to the left) there is a summary of information at the top of the page and more detailed data towards the end of the page. You can use the Table of Contents (column to the right) to navigate between various sections.

The <span class="i"}</span> next to a summary element will take you directly down to the relevant detailed explanation.

##Growing TTS Documentation
This documentation is written via Markdown language and some custom CSS. The relevant files you can modify, as well as some detailed editing instructions, are listed on GitHub. You can make a pull request to made modifications/improvements that can be incorporated into this documentation.

##TTS Terms

###GUID
In Tabletop Simulator, a GUID is a unique 6-character [string](typeandclass) which can be used to identify in-game [Objects](object). GUIDs are automatically assigned when objects exist within the scene.

If an object is duplicated, it will sometimes have the same GUID for 1 frame before the engine assigns a new GUID to the newer Object. Objects in containers (bags/decks/etc) do not automatically get new GUIDs assigned to them in this way. Only once their contents are moved out into the scene.

???warning "Custom Deck Card GUIDs"
	When you first create a custom deck, all cards within the deck share the same GUID. If you need to reference individual GUIDs of cards, then the way to solve this is to lay out all cards from the deck at the same time to allow new GUIDs to be assigned by the game. [This tool](http://steamcommunity.com/sharedfiles/filedetails/?id=1180142950) can be used to simplify the process.
	
###Types

See 

###Classes
