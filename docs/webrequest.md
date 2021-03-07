The static global WebRequest class allows you to interact with the web via get, post and put. This is a more advanced feature that allows you to store/retrieve data to/from an external database.

> Example Usage:`#!lua WebRequest.get(“https://www.google.com/”, function(a) webRequestCallback(a) end)`

##Member Variables

Like [Object member variables](object.md#member-variables), WebRequests have their own member variables.

A WebRequest is returned as part of a function, and these member variables are how your access its information.

Variable | Description | Type
-- | -- | :--
<a class="anchor" id="download_progress"></a>download_progress | Download percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="error"></a>error | Error text. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="is_error"></a>is_error | If there is an error with the WebRequest. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="is_done"></a>is_done | If the WebRequest has finished. | [<span class="tag boo"></span>](types.md)
<a class="anchor" id="response_code"></a>response_code | The response code of the WebRequest. | [<span class="tag int"></span>](#types.md)
<a class="anchor" id="text"></a>text | Returned data. | [<span class="tag str"></span>](types.md)
<a class="anchor" id="upload_progress"></a>upload_progress | Upload percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](types.md)
<a class="anchor" id="url"></a>url | The targeted URL. | [<span class="tag str"></span>](types.md)


##Function Summary

###Class Functions

Function Name | Description | Return | &nbsp;
-- | -- | -- | --:
getResponseHeader([<span class="tag str"></span>](types.md)&nbsp;name) | Returns the value of a header in the response. | [<span class="ret str"></span>](types.md) | 
getResponseHeaders() | Returns a table of the headers of the response. | [<span class="ret tab"></span>](types.md) | 

###Direct Class Functions

All functions return a WebRequest.

Function Name | Description | &nbsp;
-- | -- | --:
custom([<span class="tag str"></span>](types.md)&nbsp;url, [<span class="tag str"></span>](types.md)&nbsp;method, [<span class="tag boo"></span>](types.md)&nbsp;download, [<span class="tag str"></span>](types.md)&nbsp;data, [<span class="tag tab"></span>](types.md)&nbsp;headers, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | A more complex version of the other WebRequest Functions. | [<span class="i"></span>](#custom)
delete([<span class="tag str"></span>](types.md)&nbsp;url, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Deletes data at the current URL. | [<span class="i"></span>](#delete)
get([<span class="tag str"></span>](types.md)&nbsp;url, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Get data from the current URL. | [<span class="i"></span>](#get)
head([<span class="tag str"></span>](types.md)&nbsp;url, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Get the headers that would be returned if a get request was made to the current URL. | [<span class="i"></span>](#head)
post([<span class="tag str"></span>](types.md)&nbsp;url,  [<span class="tag tab"></span>](types.md)&nbsp;form, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Post the form to the URL. | [<span class="i"></span>](#post)
put([<span class="tag str"></span>](types.md)&nbsp;url,  [<span class="tag str"></span>](types.md)&nbsp;data, [<span class="tag fun"></span>](types.md#function)&nbsp;callback_function) | Post the data to the URL. | [<span class="i"></span>](#put)

---


##Function Details


###custom(...)

Sends a request to the URL with the supplied information.

!!!info "custom(url, method, download, data, headers, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to send a request to.
    * [<span class="tag str"></span>](types.md) **method**: The HTTP method to use. (`GET`, `POST`, etc.)
    * [<span class="tag boo"></span>](types.md) **download**: Whether to download the returned resource?
    * [<span class="tag str"></span>](types.md) **data**: The data string to send.
    * [<span class="tag tab"></span>](types.md) **headers**: The headers to send with your request.
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

---

###delete(...)

Deletes data at the current URL.

!!!info "delete(url, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to delete a resource at.   
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

---

###get(...)

Get data from the current URL.

!!!info "get(url, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to get data from.
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
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


###head(...)

Get the headers that would be returned if a get request was made to the current URL.

!!!info "head(url, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to get headers from.
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

---


###post(...)

Post the form to the URL.

!!!info "post(url, form, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to post to.
    * [<span class="tag tab"></span>](types.md) **form**: The form of data to post.    
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}

---


###put(...)

Put the data to the URL.

!!!info "put(url, data, callback_function)"
    * [<span class="tag str"></span>](types.md) **url**: The url to put to.
    * [<span class="tag str"></span>](types.md) **data**: The data string to put.    
    * [<span class="tag fun"></span>](types.md#function) **callback_function**: The function that will be triggered.
        * {>>Optional, but you will get no data back from the get if it isn't used.<<}
