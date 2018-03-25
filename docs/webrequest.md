The static global WebRequest class allows you to interact with the web via get, post and put. This is a more advanced feature that allows you to store/retrieve data to/from an external database.

> Example Usage:`#!lua WebRequest.get(“https://www.google.com/”, self, “webRequestCallback”)`

##Member Variables

Like [Object member variables](object#member-variables), WebRequests have their own member variables.

A WebRequest is returned as part of a function, and these member variables are how your access its information.

Variable | Description | Type
-- | -- | :--
download_progress | Download percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](typeandclass)
error | Error text. | [<span class="tag str"></span>](typeandclass)
is_error | If there is an error with the WebRequest. | [<span class="tag boo"></span>](typeandclass)
is_done | If the WebRequest has finished. | [<span class="tag boo"></span>](typeandclass)
text | Returned data. | [<span class="tag flo"></span>](typeandclass)
upload_progress | Upload percentage, represented as a value from 0-1. | [<span class="tag flo"></span>](typeandclass)
url | The targeted URL. | [<span class="tag str"></span>](typeandclass)

---


##Function Summary
All functions return a WebRequest.

Function Name | Description | &nbsp; 
-- | -- | --:
get([<span class="tag str"></span>](typeandclass) url, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback) | Get data from the current URL. | [<span class="i"></span>](#get)
post([<span class="tag str"></span>](typeandclass) url,  [<span class="tag tab"></span>](typeandclass) form, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback) | Post the form to the URL. | [<span class="i"></span>](#post)
put([<span class="tag str"></span>](typeandclass) url,  [<span class="tag str"></span>](typeandclass) data, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback) | Post the data to the URL. | [<span class="i"></span>](#put)

---


##Function Details

###get(...)

Get data from the current URL.

!!!info "get([<span class="tag str"></span>](typeandclass) url, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback)"
    * [<span class="tag str"></span>](typeandclass) **url**: The url to pull data from.
    * [<span class="tag obj"></span>](typeandclass) **callback_owner**: The Object that the callback function will be called on. Global is also valid.
    * [<span class="tag str"></span>](typeandclass) **callback**: The name of the function to be called.

``` Lua
function onLoad()
    print("Web Request Called")
    WebRequest.get("https://www.google.com", Global, "webRequestCallback")
end

function webRequestCallback(webReturn)
    print("Web Request Returned")
    print("webReturn.is_done")
end
```

---


###post(...)

Post the form to the URL.

!!!info "post([<span class="tag str"></span>](typeandclass) url,  [<span class="tag tab"></span>](typeandclass) form, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback)"
    * [<span class="tag str"></span>](typeandclass) **url**: The url to pull post to.
    * [<span class="tag tab"></span>](typeandclass) **form**: The form of data to post.    
    * [<span class="tag obj"></span>](typeandclass) **callback_owner**: The Object that the callback function will be called on. Global is also valid.
    * [<span class="tag str"></span>](typeandclass) **callback**: The name of the function to be called.

---


###put(...)

Post the form to the URL.

!!!info "put([<span class="tag str"></span>](typeandclass) url,  [<span class="tag str"></span>](typeandclass) data, [<span class="tag obj"></span>](typeandclass) callback_owner, [<span class="tag str"></span>](typeandclass) callback)"
    * [<span class="tag str"></span>](typeandclass) **url**: The url to pull post to.
    * [<span class="tag str"></span>](typeandclass) **data**: The data string to post.    
    * [<span class="tag obj"></span>](typeandclass) **callback_owner**: The Object that the callback function will be called on. Global is also valid.
    * [<span class="tag str"></span>](typeandclass) **callback**: The name of the function to be called.
