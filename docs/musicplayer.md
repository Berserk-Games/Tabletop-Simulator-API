`MusicPlayer` is a static global class which allows you to control the in-game music playback i.e. the in-game "Music" menu.

##Member Variables

Like [Object member variables](object.md#member-variables), MusicPlayer has its own member variables. They allow for direct access to the MusicPlayer's property information without a helping function. Some are read-only.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="loaded"></a>loaded | If all players loaded the current audioclip. Read only. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="player_status"></a>player_status | The current state of the music player. Read only. <br/>Options: "Stop", "Play", "Loading", "Ready". | [<span class="tag str"></span>](types.md)
<a class="anchor" id="playlistIndex"></a>playlistIndex |  <p>[<span class="tag deprecated"></span>](intro.md#deprecated) _Use [playlist_index](#playlist_index)_.</p>Current index of the playlist. `-1` if no playlist audioclip is playing. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="playlist_index"></a>playlist_index | Current index of the playlist. `-1` if no playlist audioclip is playing. | [<span class="tag int"></span>](types.md)
<a class="anchor" id="repeat_track"></a>repeat_track | If the current audioclip should be repeated.  | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="shuffle"></a>shuffle | If the playlist should play shuffled. | [<span class="tag boo"></span>](types.md)

##Function Summary

Functions that interact with the in-game music player.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
getCurrentAudioclip() | Gets the currently loaded audioclip. | [<span class="ret tab"></span>](types.md)| [:i:](#getcurrentaudioclip)
getPlaylist() | Gets the current playlist. | [<span class="ret tab"></span>](types.md)| [:i:](#getplaylist)
pause() | Pauses currently playing audioclip. Returns true if the music player is paused, otherwise returns false. | [<span class="ret boo"></span>](types.md)| [:i:](#pause)
play() | Plays currently loaded audioclip. Returns true if the music player is playing, otherwise returns false. | [<span class="ret boo"></span>](types.md) | [:i:](#play)
setCurrentAudioclip() | Sets the audioclip to be loaded. | [<span class="ret boo"></span>](types.md)| [:i:](#setcurrentaudioclip)
setPlaylist() | Sets the current playlis
skipBack() | Skips to the beginning of the audioclip or if the play time is less than 3 seconds to the previous audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false. | [<span class="ret boo"></span>](types.md)| [:i:](#skipback)
skipForward() | Skips to the next audioclip in playlist if possible. Returns true if skip was successful, otherwise returns false. | [<span class="ret boo"></span>](types.md)| [:i:](#skipforward) | [<span class="ret boo"></span>](types.md)| [:i:](#setplaylist)

---

##Function Details

####getCurrentAudioclip()

[<span class="ret tab"></span>](types.md)&nbsp;Gets the currently loaded audioclip.

!!!info "Returned table"
	* [<span class="tag tab"></span>](types.md) Table describing the current audioclip.
		* [<span class="tag str"></span>](types.md) **url**: The URL of the current audioclip.
		* [<span class="tag str"></span>](types.md) **title**: The title of the current audioclip.

!!!example
    Print the title of the current audioclip.
    ``` Lua
    local clip = MusicPlayer.getCurrentAudioclip()
    print("Currently playing '" .. clip.title .. "'")
    ```

---

####getPlaylist()

[<span class="ret tab"></span>](types.md)&nbsp;Gets the current playlist.

!!!info "Returned table"
	* [<span class="tag tab"></span>](types.md) Playlist table, consisting of zero or more audioclip sub-tables.
        * [<span class="tag tab"></span>](types.md) Sub-table describing each audioclip.
            * [<span class="tag str"></span>](types.md) **url**: The URL of the current audioclip.
            * [<span class="tag str"></span>](types.md) **title**: The title of the current audioclip.

!!!example
    Print the track number and title of each audioclip making up the playlist.
    ``` Lua
    local playlist = MusicPlayer.getPlaylist()
    for i, clip in ipairs(playlist) do
        print(i .. " - " .. clip.title)
    end
    ```

---

####pause()

[<span class="ret boo"></span>](types.md)&nbsp;Pause the current audioclip.

Returns `true` if the music player is/was paused, otherwise `false`.

!!!example
    Pause the current track.
    ``` Lua
    MusicPlayer.pause()
    ```

---

####play()

[<span class="ret boo"></span>](types.md)&nbsp;Plays the current audioclip.

Returns `true` if the music player is/was playing, otherwise `false`.

!!!example
    Play the current track.
    ``` Lua
    MusicPlayer.play()
    ```

---

####setCurrentAudioclip(...)

[<span class="ret boo"></span>](types.md)&nbsp;.Sets/loads the specified audioclip.

!!!info "setCurrentAudioclip(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A table describing an audioclip.
        * [<span class="tag str"></span>](types.md) **url**: The URL of the audioclip.
        * [<span class="tag str"></span>](types.md) **title**: The title of the audioclip.

!!!example
    Set the current track.
    ``` Lua
    MusicPlayer.setCurrentAudioclip({
        url = "https://domain.example/path/to/clip.mp3",
        title = "Example"
    })
    ```

---

####setPlaylist(...)

[<span class="ret boo"></span>](types.md)&nbsp;Sets the current playlist.

!!!info "setPlaylist(parameters)"
    * [<span class="tag tab"></span>](types.md) **parameters**: A table containing zero or more audioclip sub-tables.
        * [<span class="tag tab"></span>](types.md) Sub-table describing each audioclip.
            * [<span class="tag str"></span>](types.md) **parameters.url**: The URL of an audioclip.
            * [<span class="tag str"></span>](types.md) **parameters.title**: The title of an audioclip.

!!!example
    Set the current playlist to include three pieces of music.
    ``` Lua
    MusicPlayer.setCurrentAudioclip({
        {
            url = "https://domain.example/path/to/clip.mp3",
            title = "Example"
        },
        {
            url = "https://domain.example/path/to/clip2.mp3",
            title = "Example #2"
        },
        {
            url = "https://domain.example/path/to/clip3.mp3",
            title = "Example #3"
        }
    })
    ```

---

####skipBack()

[<span class="ret boo"></span>](types.md)&nbsp;Skips to the beginning of the audioclip or if the play time is less than 3 seconds to the previous audioclip in playlist if possible.

Returns `true` if skip was successful, otherwise returns `false`.

!!!example
    Skip backwards to either the beginning of the audioclip, or the prior audioclip in the playlist.
    ``` Lua
    MusicPlayer.skipBack()
    ```

---

####skipForward()

[<span class="ret boo"></span>](types.md)&nbsp;Skips to the next audioclip in the current playlist. If the current
audioclip is the last of the playlist, loops around to the first audioclip in the playlist.


Returns `true` if skip was successful, otherwise returns `false`.


!!!example
    Skip to the next audioclip.
    ``` Lua
    MusicPlayer.skipForward()
    ```

---
