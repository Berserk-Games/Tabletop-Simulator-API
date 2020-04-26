# Introduction

Welcome to **Lua Scripting** in Tabletop Simulator! Scripting is an advanced feature and it’s expected you already know something about it. However, for complete novices, check out this [beginners scripting guide to Lua](http://steamcommunity.com/sharedfiles/filedetails/?id=714904631) created by MrStump, to help you along the way.

![Demonstration Of Game](img/intro.gif)

A game is composed of one Global Script and zero to many Object Scripts. The Global Script is a script that lives in your game that can run background tasks and do general game management type functions. Object scripts are attached to an individual object. Objects are anything with a physical model in the game - chess piece, dice, decks, cards, bags, custom models, boards, etc. Both types of scripts can call the same functions, but Object scripts have access to a reference of the Object it is attached to with the `self` keyword.


## Resources

You are able to follow the links on the left side of the page for available tools to help utilize and learn the basics of scripting. When at the top of the page, you will see a link to the Lua API for documentation on all of the available Tabletop Simulator Lua functionality. Links on the right side of the page help navigate the article you are viewing.


## Writing Lua Scripts
The Lua code is written via our in-game code editor or via our [Official Plugin for the Atom Text Editor](atom.md). Lua scripts are stored in the .json file of the save game as a plain text string. There is no need for an external internet host for Lua scripts, everything is self-contained in your game’s save file. Workshop uploads work the same way.
