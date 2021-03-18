The Clock behavior is present on the Digital Clock object.

## Clock Modes

* **Current Time**: Displays the current time of the host.
* **Stopwatch**: Displays a running count up.
* **Timer**: Displays a countdown and beeps once complete.

## Member Variables

Variable | Type | Description
-- | -- | :--
paused {: #paused } | [<span class="tag boo"></span>](../types.md) | If the clock timer is paused.

---

## Function Summary

Function Name | Return | Description | &nbsp;
-- | -- | -- | --:
getValue() {: #getvalue data-toc-label="getValue()" data-toc-child-of="function-details" } | [<span class="ret int"></span>](../types.md) | Current time in stopwatch or timer mode. Clock mode returns 0. This function acts the same as [Object's getValue()](../object.md#getvalue).
pauseStart() {: #pausestart data-toc-label="pauseStart()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Pauses/resumes a Clock in stopwatch or timer mode.
setValue([<span class="tag int"></span>](../types.md) seconds) | [<span class="ret boo"></span>](../types.md) | Switches clock to timer and sets countdown time. This function acts the same as [Object's setValue()](../object.md#setvalue). | [:i:](#setvalue)
showCurrentTime() {: #showcurrenttime data-toc-label="showCurrentTime()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Switches clock to display current time. It will clear any stopwatch or timer.
startStopwatch() {: #startstopwatch data-toc-label="startStopwatch()" data-toc-child-of="function-details" } | [<span class="ret boo"></span>](../types.md) | Switches clock to stopwatch, setting time to 0. It will reset time if already in stopwatch mode.

---

## Function Details {: data-toc-sort }

### setValue(...)

[<span class="ret boo"></span>](../types.md) Set the timer to display a number of seconds. This function acts the same as [Object's setValue()](../object.md#setvalue). If the Clock is not in timer mode, it will be switched. If it is in timer mode, it will be paused and the remaining time will be changed. This will not start the countdown on its own.


!!!info "setValue(seconds)"
    * [<span class="tag int"></span>](../types.md) **seconds**: How many seconds will be counted down.

``` Lua
self.Clock.setValue(30)
```
