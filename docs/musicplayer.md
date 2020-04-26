MusicPlayer, a static global class, is the in-game music player. It allows you to control the music player in the same way that the in-game music player user interface does.

Example usage: `MusicPlayer.repeat_track = true`.

##Member Variables

Like [Object member variables](object.md#member-variables), MusicPlayer has its own member variables. They allow for direct access to the MusicPlayer's property information without a helping function. Some are read-only.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="repeat_track"></a>repeat_track | If the current audioclip should be repeated.  | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="shuffle"></a>shuffle | If the playlist should play shuffled. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="playlistIndex"></a>playlistIndex | Current index of the playlist. -1 if no playlist audioclip is playing. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="loaded"></a>loaded | If all players loaded the current audioclip. Read only. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="player_status"></a>player_status | The current state of the music player. Read only. <br/>Options: "Stop", "Play", "Loading", "Ready". | [<span class="tag str"></span>](types.md)


##Function Summary

###MusicPlayer Functions
Functions that interact with the in-game music player.

Function Name | Description | Return
-- | -- | --:
<a class="anchor" id="play"></a>play() | Plays currently loaded audioclip. Returns true if the music player is playing, otherwise returns false. | [<span class="ret boo"></span>](types.md)(#play)
<a class="anchor" id="pause"></a>pause() | Pauses currently playing audioclip. Returns true if the music player is paused, otherwise returns false. | [<span class="ret boo"></span>](types.md)(#pause)
<a class="anchor" id="skipForward"></a>skipForward() | Skips to the next audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false. | [<span class="ret boo"></span>](types.md)(#skipForward)
<a class="anchor" id="skipBack"></a>skipBack() | Skips to the beginning of the audioclip or if the play time is less than 3 seconds to the previous audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false. | [<span class="ret boo"></span>](types.md)(#skipBack)
<a class="anchor" id="getCurrentAudioclip"></a>getCurrentAudioclip() | Gets the currently loaded audioclip. | [<span class="ret tab"></span>](types.md)(#getCurrentAudioclip)
<a class="anchor" id="setCurrentAudioclip"></a>setCurrentAudioclip() | Sets the audioclip to be loaded. | [<span class="ret boo"></span>](types.md)(#setCurrentAudioclip)
<a class="anchor" id="getPlaylist"></a>getPlaylist() | Gets the current playlist. | [<span class="ret tab"></span>](types.md)(#getPlaylist)
<a class="anchor" id="setPlaylist"></a>setPlaylist() | Sets the current playlist. | [<span class="ret boo"></span>](types.md)(#setPlaylist)

---


##Function Details

####play()

[<span class="ret boo"></span>](types.md)&nbsp;Plays currently loaded audioclip. Returns true if the music player is playing, otherwise returns false.

``` Lua
--Example Usage
startLuaCoroutine(self, "PlayMusic")

--Plays currently loaded audioclip when everyone has loaded the audioclip.
function PlayMusic()
  --Wait for everyone to load the audioclip.
  while MusicPlayer.loaded == false do
      coroutine.yield(0)
  end

  --Play audioclip.
  MusicPlayer.play()

  return 1
end
```

---

####pause()

[<span class="ret boo"></span>](types.md)&nbsp;Pauses currently playing audioclip. Returns true if the music player is paused, otherwise returns false.

``` Lua
--Example Usage
startLuaCoroutine(self, "PauseMusic")

--Pauses the currently playing audioclip after 1000 frames.
function PauseMusic()
  --Wait 1000 frames
  for i=1,1000 do
    coroutine.yield(0)
  end

  --Pause audioclip
  MusicPlayer.pause()

  return 1
end
```

---

####skipForward()

[<span class="ret boo"></span>](types.md)&nbsp;Skips to the next audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false.

``` Lua
--Example Usage
MusicPlayer.skipForward()
```

---

####skipBack()

[<span class="ret boo"></span>](types.md)&nbsp;Skips to the beginning of the audioclip or if the play time is less than 3 seconds to the previous audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false.

``` Lua
--Example Usage
MusicPlayer.skipBack()
```

---

####getCurrentAudioclip()

[<span class="ret tab"></span>](types.md)&nbsp;Gets the currently loaded audioclip.

``` Lua
--Example Usage
currentAudioclip = MusicPlayer.getCurrentAudioclip()
```
``` Lua
--Example Returned Table
{url="Audioclip Url", title="Audioclip Title"}
```

---

####setCurrentAudioclip(...)

[<span class="ret boo"></span>](types.md)&nbsp;.Sets the audioclip to be loaded.

!!!info "setCurrentAudioclip(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the audioclip parameters.
        * [<span class="tag str"></span>](types.md) **parameters.url**: Url for the new audioclip.
        * [<span class="tag str"></span>](types.md) **parameters.title**: Title for the new audioclip.

``` Lua
--Example Usage
parameters =
{
	url="SOME URL HERE",
	title="SOME TITLE HERE"
}
MusicPlayer.setCurrentAudioclip(parameters)
```

---

####getPlaylist()

[<span class="ret tab"></span>](types.md)&nbsp;Gets the current playlist.

``` Lua
--Example Usage
playlist = MusicPlayer.getPlaylist()
```
``` Lua
--Example Returned Table
{
  {url="Audioclip Url 1", title="Audioclip Title 1"},
  {url="Audioclip Url 2", title="Audioclip Title 2"},
  {url="Audioclip Url 3", title="Audioclip Title 3"}
}
```

---

####setPlaylist(...)

[<span class="ret boo"></span>](types.md)&nbsp;.Sets the current playlist.

!!!info "setPlaylist(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the playlist parameters.
        * [<span class="tag tab"></span>](types.md) **parameters**: A Table containing the audioclip parameters.
            * [<span class="tag str"></span>](types.md) **parameters.url**: Url for the new audioclip.
            * [<span class="tag str"></span>](types.md) **parameters.title**: Title for the new audioclip.

``` Lua
--Example Usage
parameters =
{
  {url="SOME URL HERE 1",title="SOME TITLE HERE 1"},
  {url="SOME URL HERE 2",title="SOME TITLE HERE 2"},
  {url="SOME URL HERE 3",title="SOME TITLE HERE 3"}
}
MusicPlayer.setPlaylist(parameters)
```

---
