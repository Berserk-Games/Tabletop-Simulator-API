Timer is a statis global class which provides methods for executing other functions after a delay and/or repeatedly. Each Timer is tracked by a unique "identifier" string. You call these functions like this: `Timer.destroy(...)`.

!!!Warning
    The "identifiers" are shared between Global and all Object scripts, so each Timer must have a unique name.

##Function Summary

Function Name | Description | Return | &nbsp; 
-- | -- | -- | --:
create([<span class="tag tab"></span>](typeandclass) parameters) | Creates a Timer. It will auto-delete once its repetitions have been completed. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#create)
destroy([<span class="tag str"></span>](typeandclass) identifier) | Destroys a Timer. | [<span class="ret boo"></span>](typeandclass) | [<span class="i"></span>](#destroy)

---


##Function Details

###create(...)

[<span class="ret boo"></span>](typeandclass)&nbsp; Creates a Timer. It will auto-delete once its repetitions have been completed.

!!!info "create([<span class="tag tab"></span>](typeandclass)&nbsp; parameters)"
    * [<span class="tag_tab"></span>](typeandclass)&nbsp; **parameters**: A Table containing the information used to start the Timer.
        * [<span class="tag str"></span>](typeandclass)&nbsp; **identifier**: Timer's name, used to destroy it. Must be unique within all other scripts.
        * [<span class="tag str"></span>](typeandclass)&nbsp; **function_name**: Name of function to trigger when time is reached.
        * [<span class="tag obj"></span>](typeandclass)&nbsp; **function_owner**: Where the function from function_name exists.
            * {>>Optional, defaults to the calling Object.<<}
        * [<span class="tag tab"></span>](typeandclass)&nbsp; **parameters**: Table containing any data that will be passed to the function.
            * {>>Optional, will not be used by default.<<}
        * [<span class="tag flo"></span>](typeandclass)&nbsp; **delay**: Length of time before the function is triggered.
            * {>>Optional, defaults to 0.<<}
            * {>>0 results in a delay of 1 frame before the triggered function activates.<<}
        * [<span class="tag int"></span>](typeandclass)&nbsp; **repetitions**: Number of times the countdown repeats.
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

[<span class="ret boo"></span>](typeandclass)&nbsp; Destroys a Timer. A timer, if it completes its number of repetitions, will automatically destroy itself.

!!!info "destroy([<span class="tag str"></span>](typeandclass)&nbsp; identifier)"
    * [<span class="tag str"></span>](typeandclass)&nbsp; **identifier**: The unique identifier for the timer you want to destroy.
