The Custom UI system allows users to create custom UIs to support their game. The UI system is unique because the elements are created using a simple XML system. These UI elements can be created on screen using a Global UI or on individual in-game Objects.

##Core Features

There are 3 main pieces to the UI system.

* **Create Elements**
    * You are able to create individual elements and position them on the screen/object in a variety of ways.
* **Import Assets**
    * By clicking the button in the upper-right corner of the scripting window in-game, you open a menu that lets you upload/manage assets that can be utilized by the UI. When you save your table after uploading images here, they are saved forever.
* **Communicate with Lua**
    * Your scripts can be triggered by UI elements and your Lua scripts can also modify elements in the UI during gameplay.

---


##Getting Started

Once you load a saved table, click the Scripting button at the top of the screen. The traditional scripting window will now be visible, but you will also see a button labeled **UI**. Using this button, you can toggle back and forth between Lua scripting and UI XML. In this UI window you will input your XML. Once you are finished, click **Save & Play** in its upper-left hand corner and the save file will re-load with your changes applied to it.

If you do not see your UI elements appearing, it is possible your code has an error in it. Look down to the In-Game chat box for the error message It will indicate the line and character position the issue was discovered when trying to parse your code.

###Basics of XML

In the UI XML, you create **elements** and modify them with **attributes**. Each element is created using tags. Here is an element being created.

```xml
<Text>Displayed Text</Text>
```

Those elements can be modified with attributes to change how they look and, in some cases, function.

```xml
<Text fontSize="200">Bigger Displayed Text</Text>
```

Input types are able to communicate to a Lua script in-game.

```xml
<Button onClick="uibutton">Example Button</Button>
```

There are even organizational methods you can do to easily group these elements together.

!!!important
    The value for any attribute is **ALWAYS** in quotes. 
    
    **INCORRECT**: `#!xml <Text fontSize=200>Bigger Displayed Text</Text>`
    
    **CORRECT**: `#!xml <Text fontSize="200">Bigger Displayed Text</Text>`


###Example UI

Below you will find a variety of example projects to help you understand how the UI works.
* [Example Score Sheet](https://steamcommunity.com/sharedfiles/filedetails/?id=1415879101&searchtext=) By Gikerl
* [Example Splash Screen + Collapsible Die Roller](https://steamcommunity.com/sharedfiles/filedetails/?id=1393821479) by MrStump
* [Example Grid Menu](https://steamcommunity.com/sharedfiles/filedetails/?id=1382344471) by UnrealEd
* [Example Rulebook](https://steamcommunity.com/sharedfiles/filedetails/?id=1384145407) by UnrealEd

