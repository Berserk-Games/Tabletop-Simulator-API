Notes, a static global class, allows access to the on-screen notes and the notebook.

Example function call: `Notes.setNotes()`

##Function Summary

###Notebook Functions
Functions that interact with the in-game notebook tabs.

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
addNotebookTab([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Adds a notebook tab, returning its index. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#addnotebooktab)
editNotebookTab([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Edit an existing Tab in the notebook. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#editnotebooktab)
getNotebookTabs() | Returns Table containing data on all tabs in the notebook. | [<span class="ret tab"></span>](types.md) | [<span class="i"></span>](#getnotebooktabs)
removeNotebookTab([<span class="tag int"></span>](types.md)&nbsp;index) | Remove a notebook tab. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#removenotebooktab)

###Notes Functions
Functions that interact with the on-screen notes (lower right corner of screen).

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
<a class="anchor" id="getnotes"></a>getNotes() | Returns the contents of the on-screen notes section. | [<span class="ret str"></span>](types.md) |
setNotes([<span class="tag str"></span>](types.md)&nbsp;notes) | Replace the text in the notes window with the string. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#setnotes)

---


##Function Details


###Notebook Function Details

####addNotebookTab(...)

[<span class="ret int"></span>](types.md)&nbsp;Add a new notebook tab. If it failed to create a new tab, a -1 is returned instead. Indexes for notebook tabs begin at 0.

!!!info "addNotebookTab(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing spawning parameters.
		* [<span class="tag str"></span>](types.md) **parameters.title**: Title for the new tab.
		* [<span class="tag str"></span>](types.md) **parameters.body**: Text to place into the body of the new tab.
			* {>>Optional, defaults to an empty string<<}
		* [<span class="tag str"></span>](types.md) **parameters.color**: [Player Color](player.md) for the new tab's color.
			* {>>Optional, defaults to "Grey"<<}

``` Lua
parameters = {
	title = "New Tab",
	body = "Body text example.",
	color = "Grey"
}
Notes.addNotebookTab(parameters)
```

---


####editNotebookTab(...)

[<span class="ret boo"></span>](types.md)&nbsp;Edit an existing Tab in the notebook. Indexes for notebook tabs begin at 0.

!!!info "editNotebookTab(parameters)"
	* [<span class="tag tab"></span>](types.md) **parameters**: A Table containing instructions for the notebook edit.
		* [<span class="tag int"></span>](types.md) **parameters.index**: Index number for the tab.
		* [<span class="tag str"></span>](types.md) **parameters.title**: Title for the tab.
			* {>>Optional, defaults to the current title of the tab begin edited.<<}
		* [<span class="tag str"></span>](types.md) **parameters.body**: Text for the body for the tab.
			* {>>Optional, defaults to the current body of the tab begin edited.<<}
		* [<span class="tag str"></span>](types.md) **parameters.color**: [Player Color](player-color.md) for who the tab belongs to.
			* {>>Optional, defaults to the current color of the tab begin edited.<<}

``` Lua
params = {
	index = 5,
	title = "Edited Title",
	body = "This tab was edited via script.",
	color = "Grey"
}
Notes.editNotebookTab(params)
```

---


####getNotebookTabs()

[<span class="ret tab"></span>](types.md)&nbsp;Returns a Table containing data on all tabs in the notebook. Indexes for notebook tabs begin at 0.

``` Lua
--Example Usage
tabInfo = Notes.getNotebookTabs()
```
``` Lua
--Example Returned Table
{
	{index=0, title="", body="", color="Grey"},
	{index=1, title="", body="", color="Grey"},
	{index=2, title="", body="", color="Grey"},
}
```

---


####removeNotebookTab(...)

[<span class="ret boo"></span>](types.md)&nbsp;Remove a notebook tab. Notebook tab indexes begin at 0.

!!!info "removeNotebookTab(index)"
	* [<span class="tag int"></span>](types.md) **index**: Index for the tab to remove.

``` Lua
Notes.removeNotebookTab(0)
```

---





###Notes Function Details


####setNotes(...)

[<span class="ret boo"></span>](types.md)&nbsp;Replace the text in the notes window with the string. The notes is an area which displays text in the lower-left corner of the screen.

!!!info "setNotes(notes)"
	* [<span class="tag str"></span>](types.md) **notes**: What to place into the notes area.

``` Lua
Notes.setNotes("This appears in the notes section")
```

---
