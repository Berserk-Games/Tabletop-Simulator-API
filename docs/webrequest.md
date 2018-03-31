The static global WebRequest class allows you to interact with the web via get, post and put. This is a more advanced feature that allows you to store/retrieve data to/from an external database.

> Example Usage:`#!lua WebRequest.get(“https://www.google.com/”, self, “webRequestCallback”)`

##Member Variables

Like [Object member variables](object#member-variables), WebRequests have their own member variables.

A WebRequest is returned as part of a function, and these member variables are how your access its information.

Variable | Description | Type
-- | -- | :--
@download_progress | Download percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](intro#types)
@error | Error text. | [<span class="tag str"></span>](intro#types)
@is_error | If there is an error with the WebRequest. | [<span class="tag boo"></span>](intro#types)
@is_done | If the WebRequest has finished. | [<span class="tag boo"></span>](intro#types)
@text | Returned data. | [<span class="tag flo"></span>](intro#types)
@upload_progress | Upload percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](intro#types)
@url | The targeted URL. | [<span class="tag str"></span>](intro#types)


##Function Summary
All functions return a WebRequest.

Function Name | Description | &nbsp;
-- | -- | --:
get([<span class="tag str"></span>](intro#types)&nbsp;url, [<span class="tag obj"></span>](intro#types)&nbsp;callback_owner, [<span class="tag str"></span>](intro#types)&nbsp;callback) | Get data from the current URL. | [<span class="i"></span>](#get)
post([<span class="tag str"></span>](intro#types)&nbsp;url,  [<span class="tag tab"></span>](intro#types)&nbsp;form, [<span class="tag obj"></span>](intro#types)&nbsp;callback_owner, [<span class="tag str"></span>](intro#types)&nbsp;callback) | Post the form to the URL. | [<span class="i"></span>](#post)
put([<span class="tag str"></span>](intro#types)&nbsp;url,  [<span class="tag str"></span>](intro#types)&nbsp;data, [<span class="tag obj"></span>](intro#types)&nbsp;callback_owner, [<span class="tag str"></span>](intro#types)&nbsp;callback) | Post the data to the URL. | [<span class="i"></span>](#put)

---


##Function Details

###get(...)

Get data from the current URL.

!!!info "get(url, callback_owner, callback)"
    * [<span class="tag str"></span>](intro#types) **url**: The url to pull data from.
    * [<span class="tag obj"></span>](intro#types) **callback_owner**: The Object that the callback function will be called on.
        * {>>Global, self or any Object reference are all valid targets.<<}
    * [<span class="tag str"></span>](intro#types) **callback**: The name of the function to be called.

``` Lua
function onLoad()
    print("Web Request Called")
    WebRequest.get("https://www.google.com", Global, "webRequestCallback")
end

function webRequestCallback(webReturn)
    print("Web Request Returned")
    print(webReturn.is_done)
end
```

---


###post(...)

Post the form to the URL.

!!!info "post(url, form, callback_owner, callback)"
    * [<span class="tag str"></span>](intro#types) **url**: The url to pull post to.
    * [<span class="tag tab"></span>](intro#types) **form**: The form of data to post.    
    * [<span class="tag obj"></span>](intro#types) **callback_owner**: The Object that the callback function will be called on.
        * {>>Global, self or any Object reference are all valid targets.<<}
    * [<span class="tag str"></span>](intro#types) **callback**: The name of the function to be called.

---


###put(...)

Post the form to the URL.

!!!info "put(url, data, callback_owner, callback)"
    * [<span class="tag str"></span>](intro#types) **url**: The url to pull post to.
    * [<span class="tag str"></span>](intro#types) **data**: The data string to post.    
    * [<span class="tag obj"></span>](intro#types) **callback_owner**: The Object that the callback function will be called on.
        * {>>Global, self or any Object reference are all valid targets.<<}
    * [<span class="tag str"></span>](intro#types) **callback**: The name of the function to be called.
