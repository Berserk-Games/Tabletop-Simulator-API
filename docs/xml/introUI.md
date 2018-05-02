The Custom UI system allows users to create custom UIs to support their game. The UI system is unique because the elements are created using a simple XML system.

##Core Features
Each element is created using a simple series of tags.

```xml
<Text>Displayed Text</Text>
```

Those tags can be modified with attributes to change how they look and, in some cases, function.

```xml
<Text fontSize=200>Bigger Displayed Text</Text>
```

Input types are able to communicate to a Lua script in-game.

```xml
<Button onClick="uibutton">Example Button</Button>
```

There are even organizational methods you can do to easily group these elements together.

##Getting Started

Once you load a saved table, click the Scripting button at the top of the screen. The traditional scripting window will now be visible, but you will also see a green tab labeled **UI**. Clicking that will open a blank window. In this box you will input your XML. Once you are finished, click **Save & Play** in its upper-left hand corner and the save file will re-load with your changes applied to it.

If you do not see your UI elements appearing, it is possible your code has an error in it. Look down to the In-Game chat box for the error message It will indicate the line and character position the issue was discovered when trying to parse your code.

##Basics of XML

XML is a very straight-forward language. You use tags to indicate what information goes together, and you can modify those tags to modify how their contents are handled. The basics can be picked up with only a few example scripts to point the wait. 

If you would like to read more about the language then W3 has a[very good general walkthrough here](https://www.w3schools.com/xml/default.asp). This is NOT a tutorial on how to use XML within Tabletop Simulator specifically.

##TODO:
Add place for defaults

- UI API:
  - Introduction: xml/introUI.md
  - Basic Elements: xml/basicelements.md
  - Input Elements: xml/inputelements.md
  - Layout/Grouping: xml/layoutgrouping.md
  - Advanced Attributes: xml/advancedattributes.md
  - Scripting Integration: xml/scriptingintegration.md
