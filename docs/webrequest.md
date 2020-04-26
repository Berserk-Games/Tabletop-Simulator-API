The static global WebRequest class allows you to interact with the web via get, post and put. This is a more advanced feature that allows you to store/retrieve data to/from an external database.

> Example Usage:`#!lua WebRequest.get(“https://www.google.com/”, self, “webRequestCallback”)`

##Member Variables

Like [Object member variables](object.md#member-variables), WebRequests have their own member variables.

A WebRequest is returned as part of a function, and these member variables are how your access its information.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="download_progress"></a>download_progress | Download percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="error"></a>error | Error text. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="is_error"></a>is_error | If there is an error with the WebRequest. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="is_done"></a>is_done | If the WebRequest has finished. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="text"></a>text | Returned data. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="upload_progress"></a>upload_progress | Upload percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="url"></a>url | The targeted URL. | [<span class="tag str"></span>](types.md)


##Function Summary
All functions return a WebRequest.

Function Name | Description | &nbsp;
-- | -- | --:
get([<span class="tag str"></span>](types.md)&nbsp;url, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Get data from the current URL. | [<span class="i"></span>](#get)
post([<span class="tag str"></span>](types.md)&nbsp;url,  [<span class="tag tab"></span>](types.md)&nbsp;form, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Post the form to the URL. | [<span class="i"></span>](#post)
put([<span class="tag str"></span>](types.md)&nbsp;url,  [<span class="tag str"></span>](types.md)&nbsp;data, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Post the data to the URL. | [<span class="i"></span>](#put)

---


##Function Details

###get(...)

Get data from the current URL.

!!!info "get(url, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to pull data from.
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

``` Lua
function onLoad()
    print("Web Request Called")
    WebRequest.get("https://www.google.com", function(a) webRequestCallback(a) end)
end

function webRequestCallback(webReturn)
    print("Web Request Returned")
    print(webReturn.is_done)
end
```

---


###post(...)

Post the form to the URL.

!!!info "post(url, form, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to pull post to.
    * [<span class="tag tab"></span>](types.md) **form**: The form of data to post.    
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

---


###put(...)

Post the data to the URL.

!!!info "put(url, data, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to pull post to.
    * [<span class="tag str"></span>](types.md) **data**: The data string to post.    
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}
