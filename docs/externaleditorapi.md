This page describes how our [Official Atom Plugin](atom) API works so that you can write your own plugin for your text editor of choice if Atom does not suit your needs. The plugin communicates with Tabletop Simulator via two localhost TCP connections - one for each system acting as a server and the other as a client and vice versa. All communication messages are JSON.

##Tabletop Simulator as the Server

!!!note ""
	TTS listens for incoming localhost TCP connections on port 39999.


###Get Lua Scripts

Atom sends a JSON message with an ID of 0.

```JSON
{
    "messageID": 0
}
```

TTS sends back a JSON message with an ID of 0 and an array of the Lua Scripts.

```JSON
{
    "messageID": 0,
    "scriptStates": [
        {
            "name": "Global",
            "guid": "-1",
            "script": "..."
        },
        {
            "name": "BlackJack Dealer's Deck",
            "guid": "a0b2d5",
            "script": "..."
        },
    ]
}
```


###Save & Play

Atom sends a JSON message with an ID of 1 and an array of the Lua Scripts.

```JSON
{
    "messageID": 1,
    "scriptStates": [
        {
            "guid": "-1",
            "script": "..."
        },
        {
            "guid": "a0b2d5",
            "script": "..."
        },
    ]
}
```


##Atom as the Server

!!!note ""
	Atom listens for incoming localhost TCP connections on port 39998.

###Pushing New Object

When clicking on "Lua Editor" in the right click contextual menu in-game for an Object that doesn't have a Lua Script yet, it will try to open a new tab in Atom for this Object before falling back to the in-game editor if Atom is not running. TTS sends a JSON message with an ID of 0 and the new Object.

```JSON
{
    "messageID": 0,
    "scriptStates": [
        {
            "name": "Chess Pawn",
            "guid": "db3f06",
            "script": ""
        }
    ]
}
```


###Loading a New Game

When loading a new game in TTS, TTS will automatically send all the Lua Scripts from the new game to Atom. TTS sends a JSON message with an ID of 1 and an array of the Lua Scripts.

```JSON
{
    "messageID": 1,
    "scriptStates": [
        {
            "name": "Global",
            "guid": "-1",
            "script": "..."
        },
        {
            "name": "BlackJack Dealer's Deck",
            "guid": "a0b2d5",
            "script": "..."
        },
    ]
}
```


###Print/Debug Messages

TTS sends all print() messages to Atom to be displayed in Atom's console (ctrl + alt + i). TTS sends a JSON message with an ID of 2 and the message.

```JSON
{
    "messageID": 2,
    "message": "Hit player! White"
}
```


###Error Messages

TTS sends all Lua error messages to Atom to be displayed in Atom's console *(ctrl + alt + i)*. TTS sends a JSON message with an ID of 3 and the error message.

```JSON
{
    "messageID": 3,
    "error": "chunk_0:(36,4-8): unexpected symbol near 'deck'",
    "guid": "-1",
    "errorMessagePrefix": "Error in Global Script: "
}
```
