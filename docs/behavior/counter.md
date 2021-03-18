The Counter behavior is present on the Counter object.

## Functions {: data-toc-sort }

Function Name | Return | Description
-- | -- | --
clear() {: #clear data-toc-label="clear()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Resets Counter to 0.
decrement() {: #decrement data-toc-label="decrement()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Reduces Counter's value by 1.
getValue() {: #getvalue data-toc-label="getValue()" data-toc-child-of="functions" } | [<span class="ret int"></span>](../types.md) | Returns Counter's current value. This function behaves the same as [Object's getValue()](../object.md#getvalue).
increment() {: #increment data-toc-label="increment()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Increases Counter's value by 1.
setValue() {: #setvalue data-toc-label="setValue()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Sets the current value of the Counter. This function behaves the same as [Object's setValue()](../object.md#setvalue).

!!!example
    Increment a counter's value.
    ```lua
    object.Counter.increment()
    ```
