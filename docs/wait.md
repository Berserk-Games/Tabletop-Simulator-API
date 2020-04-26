The Wait class is a static global class which deals with triggering a specified function after some form of delay. It is how you can add pauses into your code while you wait for something, like waiting for a deck to finish forming after using putObject.

Example usage: `Wait.frames(functionName, 60)`

!!!tip
    This is the first Class to use functions as parameters. To help, detailed examples are included for each usage. For more details, you can check out the [Function section](types.md#function) of the Introduction page.

##Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
condition([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag fun"></span>](types.md#function)&nbsp;conditionFunc, [<span class="tag flo"></span>](types.md)&nbsp;timeout, [<span class="tag fun"></span>](types.md#function)&nbsp;timeoutFunc) | Activates a function when a given function returns `true` or activates a different function if a timeout occurs. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#condition)
frames([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag int"></span>](types.md)&nbsp;frameCount) | Activates a function after a set number of frames. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#frames)
stop([<span class="tag int"></span>](types.md)&nbsp;id) | Stops a currently running Wait function. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#stop)
time([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag flo"></span>](types.md)&nbsp;time, [<span class="tag int"></span>](types.md)&nbsp;repetitions) | Activates a function after a set amount of time has passed. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#time)

---

##Function Details

###condition(...)

[<span class="ret int"></span>](types.md)&nbsp;Activates a function when a given function returns `true` or activates a different function if a timeout occurs.

> The returned value is an ID which can be used with [stop](#stop) to cancel the function at any time.

!!!info "condition(toRunFunc, conditionFunc, timeout, timeoutFunc)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to activate once the condition is met.
    * [<span class="tag fun"></span>](types.md#function) **conditionFunc**: The function that is watched until it returns `true`.
    * [<span class="tag flo"></span>](types.md) **timeout**: The amount of time, in seconds, before this function gives up checking the condition function.
        * {>>Optional, defaults to never timing out.<<}
    * [<span class="tag fun"></span>](types.md#function) **timeoutFunc**: The function that that triggers if the timeout amount is met.
        * {>>Optional, defaults to no function being triggered if a timeout happens.<<}

Example without a timeout:
``` Lua
--Watches a die until it comes to rest, then print its result
function onLoad()
    --Roll a die, using its GUID
    local die = getObjectFromGUID("555555")
    die.roll()

    --Function that will be watched until it becomes true
    local rollWatch = function() return die.resting end
    --Function that will be run once the above condition becomes true
    local rollEnd = function() print(die.getRotationValue()) end

    --Plug those two functions into the Wait function
    Wait.condition(rollEnd, rollWatch)
end
```

Example with a timeout, written differently:
``` Lua
--Watches a die until it comes to rest, then print its result
function onLoad()
    --Roll a die, using its GUID
    local die = getObjectFromGUID("a5b5ac")
    die.roll()

    --Activate the wait condition, passing parameters to exterior functions
    Wait.condition(
        function() printResult(die.getRotationValue()) end,
        function() return checkResting(die) end,
        2,
        function() printResult("Too Slow!") end
    )
end

--Prints the roll result, runs when wait condition is met
--It is also used in case of timeout to print that timeout message.
function printResult(number)
    print(number)
end

--Checks if the object is resting
function checkResting(target)
    return target.resting
end
```


---


###frames(...)

[<span class="ret int"></span>](types.md)&nbsp;Activates a function after a set number of frames. The amount of time this takes is based off the Host's FPS. The higher their FPS, the faster this will trigger.

> The returned value is an ID which can be used with [stop](#stop) to cancel the function at any time.

!!!info "frames(toRunFunc, frameCount)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to activate once the condition is met.
    * [<span class="tag int"></span>](types.md) **frameCount**: The number of frames to wait before activating the above function.

``` Lua
function onLoad()
	--Built-in functions with parameters can be called directly
	--This is done by wrapping the function within `function()` and `end`
	Wait.frames(function() print("One") end, 60)

	--You can also call custom functions you have made yourself
	--Pass them any parameters you wish
	Wait.frames(function() sayTwo("Two") end, 120)

	--If you aren't passing any parameters to the function, you can shorten it
	Wait.frames(sayThree, 180)
end

--Has its parameter passed to it
function sayTwo(s) print(s) end

--Does not have any parameters passed to it
function sayThree() print("Three") end
```

---


###stop(...)
[<span class="ret boo"></span>](types.md)&nbsp;Stops a currently running Wait function. The only way to obtain these ID numbers is to get them from the return value of a Wait function.

!!!info "stop(id)"
    * [<span class="tag int"></span>](types.md) **id**: The index number assigned by the game to every Wait function (besides stop).

``` Lua
function onLoad()
    --This would print the message after 5 seconds
    id = Wait.time(function() print("This won't print") end, 5)
    --Except it is stopped immediately
    Wait.stop(id)
end
```

---


###time(...)
[<span class="ret int"></span>](types.md)&nbsp;Activates a function after a set amount of time has passes.

> The returned value is an ID which can be used with [stop](#stop) to cancel the function at any time.

!!!info "time(toRunFunc, time)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to activate once the amount of time has passed.
    * [<span class="tag flo"></span>](types.md) **time**: The amount of time before the function is triggered.
    * [<span class="tag int"></span>](types.md) **repetitions**: Number of times the timer will be repeated.
        * {>>Optional, defaults to 0.<<}
        * {>>Using -1 causes it to loop indefinitely unless stopped.<<}

Example (basic usage):
``` Lua
function onLoad()
	Wait.time(|| print("One"), 1)

	Wait.time(function() saySomething("Two") end, 2)

	Wait.time(sayThree, 3)
end

function saySomething(something)
    print(something)
end

function sayThree()
    print("Three")
end
```

---
