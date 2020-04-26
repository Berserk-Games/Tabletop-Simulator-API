The static global JSON class provides the ability to encode/decode data into JSON strings. This is largely used by the [onSave()](event.md#onsave) event function, but has other potential applications as well. The JSON class can be used on any String, Int, Float or Table. You call these functions like this: `JSON.encode(...)`.

!!!warning
    This class **does not** work with Object references. Use the Object's GUID instead.



##Function Summary

###Object Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
decode([<span class="tag str"></span>](types.md)&nbsp;json_string) | Value obtained from the encoded string. Can return a number, string or Table. | [<span class="ret var"></span>](types.md) | [<span class="i"></span>](#decode)
encode([<span class="tag var"></span>](types.md)&nbsp;data) | Encodes data from a number, string or Table into a JSON string. | [<span class="ret str"></span>](types.md) | [<span class="i"></span>](#encode)
encode_pretty([<span class="tag var"></span>](types.md)&nbsp;data) | Same as encode(...) but this version is slightly less efficient but is easier to read. | [<span class="ret str"></span>](types.md) | [<span class="i"></span>](#encode_pretty)

---


##Function Details

###decode(...)

[<span class="ret var"></span>](types.md)&nbsp;Value obtained from the encoded string. Can return a number, string or Table.

!!!info "decode(json_string)"
    * [<span class="tag str"></span>](types.md) **json_string**: A String that is decoded, generally created by encode(...) or encode_pretty(...).

``` Lua
coded = JSON.encode("Test")
print(coded) --Prints "Test"
decoded = JSON.decode(coded)
print(decoded) --Prints Test
```

---


###encode(...)

[<span class="ret str"></span>](types.md)&nbsp;Encodes data from a number, string or Table into a JSON string.

!!!info "encode(data)"
    * [<span class="tag var"></span>](types.md) **data**: A Var, either String, Int, Float or Table, to encode as a string.

---


###encode_pretty(...)

[<span class="ret str"></span>](types.md)&nbsp;Encodes data from a number, string or Table into a JSON string. This version is slightly less efficient but is easier to read.

!!!info "encode_pretty(data)"
    * [<span class="tag var"></span>](types.md) **data**: A Var, either String, Int, Float or Table, to encode as a string.
