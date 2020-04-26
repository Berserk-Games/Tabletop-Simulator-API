Timer is a static global class which provides methods for executing other functions after a delay and/or repeatedly. Each Timer is tracked by a unique "identifier" string.

> Example Usage: `Timer.destroy(...)`

!!!warning "Important Tip"
    The "identifiers" are shared between Global and all Object scripts, so each Timer must have a unique name.

##Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
create([<span class="tag tab"></span>](types.md)&nbsp;parameters) | Creates a Timer. It will auto-delete once its repetitions have been completed. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#create)
destroy([<span class="tag str"></span>](types.md)&nbsp;identifier) | Destroys a Timer. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#destroy)

---


##Function Details

###create(...)

[<span class="ret boo"></span>](types.md)&nbsp;Creates a Timer. It will auto-delete once its repetitions have been completed.

!!!info "create(parameters)"
    * [<span class="tag_tab"></span>](types.md) **parameters**: A Table containing the information used to start the Timer.
        * [<span class="tag str"></span>](types.md) **identifier**: Timer's name, used to destroy it. Must be unique within all other scripts.
        * [<span class="tag str"></span>](types.md) **function_name**: Name of function to trigger when time is reached.
        * [<span class="tag obj"></span>](types.md) **function_owner**: Where the function from function_name exists.
            * {>>Optional, defaults to the calling Object.<<}
        * [<span class="tag tab"></span>](types.md) **parameters**: Table containing any data that will be passed to the function.
            * {>>Optional, will not be used by default.<<}
        * [<span class="tag flo"></span>](types.md) **delay**: Length of time before the function is triggered.
            * {>>Optional, defaults to 0.<<}
            * {>>0 results in a delay of 1 frame before the triggered function activates.<<}
        * [<span class="tag int"></span>](types.md) **repetitions**: Number of times the countdown repeats.
            * {>>Optional, defaults to 1.<<}
            * {>>Use 0 for infinite repetitions.<<}

``` Lua
function onLoad()
    dataTable = {welcome="Hello World!"}
    Timer.create({
        identifier     = "A Unique Name",
        function_name  = "fiveAfterOne",
        parameters     = dataTable,
        delay          = 1,
        repetitions    = 5,
    })
end

function fiveAfterOne(params)
    print(params.welcome)
end
```

!!!tip
    If your timer is on an Object, a good way to establish a unique identifier for it is to use the item's GUID!

---


###destroy(...)

[<span class="ret boo"></span>](types.md)&nbsp;Destroys a Timer. A timer, if it completes its number of repetitions, will automatically destroy itself.

!!!info "destroy(identifier)"
    * [<span class="tag str"></span>](types.md) **identifier**: The unique identifier for the timer you want to destroy.
