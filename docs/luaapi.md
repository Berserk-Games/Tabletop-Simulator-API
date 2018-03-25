In this section, you will find details on all events/classes/functions specific to Tabletop Simulator's Lua scripting. For more general information on how the scripting language of Lua works and what it does on its own, you can review the [online documentation](https://www.lua.org/docs.html). 

##GUID
A GUID is a unique 6-character [string](typeandclass) which can be used to identify in-game [Objects](object). GUIDs are automatically assigned when objects exist within the scene.

If an object is duplicated, it will sometimes have the same GUID for 1 frame before the engine assigns a new GUID to the newer Object. Objects in containers (bags/decks/etc) do not automatically get new GUIDs assigned to them in this way. Only once their contents are moved out into the scene.

???warning "Custom Deck Card GUIDs"
	When you first create a custom deck, all cards within the deck share the same GUID. If you need to reference individual GUIDs of cards, then the way to solve this is to lay out all cards from the deck at the same time to allow new GUIDs to be assigned by the game. [This tool](http://steamcommunity.com/sharedfiles/filedetails/?id=1180142950) can be used to simplify the process.
	
---


!!! note "TODO:"
	* Add more here on how this docu is set up
	* Link to the tutorial in the top message once I input it
	* Instructions on how to modify if they think changes are needed.
	
	
##In progress reference

[<span class="tag tab"></span>](typeandclass)&nbsp; 
[<span class="tag str"></span>](typeandclass)&nbsp; 
[<span class="tag int"></span>](typeandclass)&nbsp; 
[<span class="tag flo"></span>](typeandclass)&nbsp; 
[<span class="tag nil"></span>](typeandclass)&nbsp; 
[<span class="tag boo"></span>](typeandclass)&nbsp; 
[<span class="tag obj"></span>](typeandclass)&nbsp; 
[<span class="tag var"></span>](typeandclass)&nbsp; 
[<span class="tag vec"></span>](typeandclass#vector)&nbsp; 
[<span class="tag col"></span>](typeandclass#color)&nbsp; 


[<span class="ret tab"></span>](typeandclass)&nbsp; 
[<span class="ret str"></span>](typeandclass)&nbsp; 
[<span class="ret int"></span>](typeandclass)&nbsp; 
[<span class="ret flo"></span>](typeandclass)&nbsp; 
[<span class="ret nil"></span>](typeandclass)&nbsp; 
[<span class="ret boo"></span>](typeandclass)&nbsp; 
[<span class="ret obj"></span>](typeandclass)&nbsp;
[<span class="ret var"></span>](typeandclass)&nbsp; 
[<span class="ret vec"></span>](typeandclass#vector)&nbsp; 
[<span class="ret col"></span>](typeandclass#color)&nbsp; 
