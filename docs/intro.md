In this section, you will find details on all events/classes/functions specific to Tabletop Simulator's Lua scripting. For more general information on how the scripting language of Lua works and what it does on its own, you can review the [Official Lua Documentation](https://www.lua.org/docs.html).

##Using TTS Documentation

###Left Column
This is the top-level list of classes and other information needed when scripting with Lua in Tabletop Simulator. Event, Base and Object are the three pages you will use the most, with the rest referring to niche information you can access as you go. It is a good idea to familiarize yourself with the contents of those three pages in order to have a good high-level understanding of what scripting is capable of doing.

###Right Column
The Table of Contents will lay out the contents of the page you are on. It always starts with high-level summary information first and, if needed, detailed information towards the bottom. The <span class="i"></span> next to a summary element will take you directly down to the relevant detailed explanation below.


##Growing TTS Documentation
This documentation is written via Markdown language and some custom CSS. The relevant files you can modify, as well as some detailed editing instructions, are listed on GitHub. You can make a pull request to made modifications/improvements that can be incorporated into this documentation.

Just click the link in the pencil icon in the top-right of an article, or visit the GitHub page for more information by clicking GitHub Source in the far upper right.

---


##TTS Terms

###Object
An in-game physical Object that currently exists in the scene. If an Object is placed inside of a bag/deck/etc, it stops existing and is no longer in the scene until it is pulled back out.

###Player
A person in the game. Each Player is assigned a color, with spectators being "Grey". If you are attempting to identify a Player, you would use the color of the seat they are in to do so.

###Global Script
The Global script, which is a script that is not attached to any particular Object. It is always present during a game.

###Object Script
A script that is attached to an in-game Object, and is saved as part of it. This is similar to any other property like its scale or tint. Some functions ask for an Object reference in order to attempt to run a function on it. In these cases, Global (exactly as written here) is also a valid Object reference.

###GUID
In Tabletop Simulator, a GUID is a unique 6-character [string](types.md)&nbsp;which can be used to identify in-game [Objects](object.md). GUIDs are automatically assigned when objects exist within the scene.

If an object is duplicated, it will sometimes have the same GUID for 1 frame before the engine assigns a new GUID to the newer Object. Objects in containers (bags/decks/etc) do not automatically get new GUIDs assigned to them in this way. Only once their contents are moved out into the scene.

???warning "Custom Deck Card GUIDs"
	When you first create a custom deck, all cards within the deck share the same GUID. If you need to reference individual GUIDs of cards, then the way to solve this is to lay out all cards from the deck at the same time to allow new GUIDs to be assigned by the game. [This tool](http://steamcommunity.com/sharedfiles/filedetails/?id=1180142950) can be used to simplify the process.

---



---

###Classes

Defining classes requires further knowledge of object-oriented programming to really understand. However for the purposes of Tabletop Simulator Lua scripting, you can think of a class as a standard or collection that handles categories of objects.

####Object Classes
Associated with in-game Objects.

* [Clock](clock.md)
* [Counter](counter.md)
* [Object](object.md)
* [AssetBundle](assetbundle.md)
* [RPGFigurine](rpgfigurine.md)
* [TextTool](texttool.md)

####Static Classes
Associated with in-game properties and systems.

* [JSON](json.md)
* [Player](player.md)
* [WebRequest](webrequest.md)
* [Physics](physics.md)
* [Lighting](lighting.md)
* [Turns](turns.md)
* [Notes](notes.md)
* [UI](ui.md)
* [Wait](wait.md)
* [Web Request](webrequest.md)

For more information on what a class is, you can refer to the relevant [Lua Documentation](https://www.lua.org/pil/16.1.html).

---
