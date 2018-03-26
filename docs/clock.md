The clock is an in-game Object which either tells time or acts as a timer. It has its own class, Clock, with functions/members associated with it. This allows you to manipulate the special properties of a clock.

Example Usage: `self.Clock.pauseStart()`

> * **Clock Modes:**
>       * **Current Time**: Displays the current time of the host.
>       * **Stopwatch**: Displays a running count up.
>       * **Timer**: Displays a countdown and beeps once complete.

##Member Variables

Like [Object member variables](object#member-variables), Clocks have their own member variable.

Variable | Description | Type
-- | -- | :--
paused | If the clock timer is paused. | [<span class="tag boo"></span>](intro#types)

---

##Function Summary

###Object Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getValue() | Current time in stopwatch or timer mode. Clock mode returns 0. This function acts the same as [Object's getValue()](object#getvalue). | [<span class="ret int"></span>](intro#types)
pauseStart() | Pauses/resumes a Clock in stopwatch or timer mode. | [<span class="ret boo"></span>](intro#types)
setValue(Int seconds) | Switches clock to timer and sets countdown time. This function acts the same as [Object's setValue()](object#setvalue). | [<span class="ret boo"></span>](intro#types) | [<span class="i"></span>](#setvalue)
showCurrentTime() | Switches clock to display current time. It will clear any stopwatch or timer. | [<span class="ret boo"></span>](intro#types)
startStopwatch() | Switches clock to stopwatch, setting time to 0. It will reset time if already in stopwatch mode. | [<span class="ret boo"></span>](intro#types)

---

##Function Details

###setValue(...)

[<span class="ret boo"></span>](intro#types)&nbsp;Set the timer to display a number of seconds. This function acts the same as [Object's setValue()](object#setvalue). If the Clock is not in timer mode, it will be switched. If it is in timer mode, it will be paused and the remaining time will be changed. This will not start the countdown on its own.


!!!info "setValue(seconds)"
    * [<span class="tag int"></span>](intro#types) **seconds**: How many seconds will be counted down.
    
``` Lua
self.Clock.setValue(30)
```
