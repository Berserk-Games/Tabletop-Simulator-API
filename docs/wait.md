The `Wait` class is a static global class which allows you to schedule code (functions) to be executed later on.

!!!important
    Please note that `Wait` does _not_ pause Lua script execution, _because that would freeze Tabletop Simulator!_ The
    next line of code after a `Wait` function call will always be executed immediately.

##Function Summary

Function Name | Description | Return | &nbsp;
-- | -- | -- | --
condition([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag fun"></span>](types.md#function)&nbsp;conditionFunc, [<span class="tag flo"></span>](types.md)&nbsp;timeout, [<span class="tag fun"></span>](types.md#function)&nbsp;timeoutFunc) | Schedules a function to be executed after the specified condition has been met. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#condition)
frames([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag int"></span>](types.md)&nbsp;numberFrames) | Schedules a function to be executed after the specified number of frames have elapsed. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#frames)
stop([<span class="tag int"></span>](types.md)&nbsp;id) | Cancels a Wait-scheduled function. | [<span class="ret boo"></span>](types.md) | [<span class="i"></span>](#stop)
stopAll() | Cancels all Wait-scheduled functions. | | [<span class="i"></span>](#stopall)
time([<span class="tag fun"></span>](types.md#function)&nbsp;toRunFunc, [<span class="tag flo"></span>](types.md)&nbsp;seconds, [<span class="tag int"></span>](types.md)&nbsp;repetitions) | Schedules a function to be executed after the specified amount of time (in seconds) has elapsed. | [<span class="ret int"></span>](types.md) | [<span class="i"></span>](#time)

---

##Function Details

###condition(...)

[<span class="ret int"></span>](types.md)&nbsp;Schedules a function to be executed after the specified condition has been met.

The return value is a unique ID that may be used to [stop](#stop) the scheduled function before it runs.

!!!info "condition(toRunFunc, conditionFunc, timeout, timeoutFunc)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to be executed after the specified condition is met.
    * [<span class="tag fun"></span>](types.md#function) **conditionFunc**: The function that will be executed repeatedly, until it returns `true` (or the `timeout` is reached).
    * [<span class="tag flo"></span>](types.md) **timeout**: The amount of time (in seconds) that may elapse before the scheduled function is cancelled.
        * {>>Optional, defaults to never timing out.<<}
    * [<span class="tag fun"></span>](types.md#function) **timeoutFunc**: The function that will be executed if the timeout is reached.
        * {>>Optional<<}

`conditionFunc` will be executed (possibly several times) until it returns `true`, at which point the
scheduled function (`toRunFunc`) will be executed, and `conditionFunc` will no longer be executed again.

Optionally, a `timeout` and `timeoutFunc` may be specified. If `conditionFunc` does not return `true` before the specified
timeout (seconds) has elapsed, then the scheduled function is cancelled i.e. will not be called. If a `timeoutFunc` is
provided, then it will be called when the timeout is reached.

!!!example
    Roll a die, and wait until it comes to rest.
    ``` Lua
    die.randomize() -- Roll a die
    Wait.condition(
        function() -- Executed after our condition is met
            if die.isDestroyed() then
                print("Die was destroyed before it came to rest.")
            else
                print(die.getRotationValue() .. " was rolled.")
            end
        end,
        function() -- Condition function
            return die.isDestroyed() or die.resting
        end
    )
    ```

!!!example
    Launch an object into the air with a random impulse and wait until it comes to rest.
    However, if it's taking too long (more than two seconds), give up waiting.
    ``` Lua
    local upwardImpulse = math.random(5, 25)
    object.addForce({0, upwardImpulse, 0})
    Wait.condition(
        function()
            if object.isDestroyed() then
                print("Object was destroyed before it came to rest.")
            else
                print("The object came to rest in under two seconds.")
            end
        end,
        function()
            return object.isDestroyed() or object.resting
        end,
        2, -- second timeout
        function() -- Executed if our timeout is reached
            print("Took too long to come to rest.")
        end
    )
    ```

---

###frames(...)

[<span class="ret int"></span>](types.md)&nbsp;Schedules a function to be executed after the specified number of frames
have elapsed.

The return value is a unique ID that may be used to [stop](#stop) the scheduled function before it runs.

!!!info "frames(toRunFunc, frameCount)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to be executed after the specified number of frames have elapsed.
    * [<span class="tag int"></span>](types.md) **numberFrames**: The number of frames that must elapse before `toRunFunc` is executed.
        * {>>Optional, defaults to `1`.<<}

!!!example
    Prints "Hello!" after 60 frames have elapsed.
    ``` Lua
    Wait.frames(
        function()
            print("Hello!")
        end,
        60
    )
    ```
    It's a matter of personal preference, but it's quite common to see the above compacted into one line, like:
    ``` Lua
    Wait.frames(function() print("Hello!") end, 60)
    ```

!!!example "Advanced Example"
    <p>Prints "1", "2", "3", "4", "5", waiting 60 frames before each printed number.</p>
    <p>Note that the scheduled function, upon execution, will reschedule itself unless `count` has reached 5.</p>
    ``` Lua
    local count = 1
    local function printAndReschedule()
        print(count)

        if count < 5 then
            count = count + 1
            Wait.frames(printAndReschedule, 60)
        end
    end

    Wait.frames(printAndReschedule, 60)
    ```

---

###stop(...)

[<span class="ret boo"></span>](types.md)&nbsp;Cancels a Wait-scheduled function.

!!!info "stop(id)"
    * [<span class="tag int"></span>](types.md) **id**: A wait ID (returned from `Wait` scheduling functions).

!!!example
    Schedules two functions: one that says "Hello!", and one that says "Goodbye!". However, the latter is stopped before
    it has a chance to execute i.e. We'll see "Hello!" printed, but we _won't_ see "Goodbye!"
    ``` Lua
    Wait.time(function() print("Hello!") end, 1)
    local goodbyeId = Wait.time(function() print("Goodbye!") end, 2)
    Wait.stop(goodbyeId)
    ```

---

###stopAll(...)

Cancels all Wait-scheduled functions.

!!!warning
    You should be extremely careful using this function. Generally you should cancel individual scheduled functions with
    [stop](#stop) instead.

!!!example
    Schedules two functions: one that says "Hello!", and one that says "Goodbye!". However, _both_ are stopped before
    either has the chance to execute.
    ``` Lua
    Wait.time(function() print("Hello!") end, 1)
    Wait.time(function() print("Goodbye!") end, 2)
    Wait.stopAll()
    ```

---

###time(...)

[<span class="ret int"></span>](types.md)&nbsp;Schedules a function to be executed after the specified amount of time
(in seconds) has elapsed.

The return value is a unique ID that may be used to [stop](#stop) the scheduled function before it runs.

!!!info "time(toRunFunc, seconds, repetitions)"
    * [<span class="tag fun"></span>](types.md#function) **toRunFunc**: The function to be executed after the specified amount of time has elapsed.
    * [<span class="tag flo"></span>](types.md) **seconds**: The amount of time that must elapse before `toRunFunc` is executed.
    * [<span class="tag int"></span>](types.md) **repetitions**: Number of times `toRunFunc` will be (re)scheduled. `-1` is infinite repetitions.
        * {>>Optional, defaults to `1`.<<}

`repetitions` is optional and defaults to `1`. When `repetitions` is a positive number, `toRunFunc` will execute for the
specified number of repetitions, with the specified time delay before and between each execution. When `repetitions` is
`-1`, `toRunFunc` will be re-scheduled indefinitely (i.e. infinite repetitions).

!!!example
    Prints "Hello!" after 1 second has elapsed.
    ``` Lua
    Wait.time(
        function()
            print("Hello!")
        end,
        1
    )
    ```
    It's a matter of personal preference, but it's quite common to see the above compacted into one line, like:
    ``` Lua
    Wait.time(function() print("Hello!") end, 1)
    ```

!!!example
    Prints "1", "2", "3", "4", "5", waiting 1 second before each printed number.
    ``` Lua
    local count = 1
    Wait.time(
        function()
            print(count)
            count = count + 1
        end,
        1, -- second delay
        5 -- repetitions
    )
    ```

---
