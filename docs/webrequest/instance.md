# Web Request Instance

Web request instances represent a singular in-progress, completed or failed web request. They are created via the [Web Request Manager](manager.md).

##Member Variables

Variable | Description | Type
-- | -- | :--
download_progress {: #download_progress } | Download percentage, represented as a number in the range 0-1. | [<span class="tag flo"></span>](../types.md)
error {: #error } | <p>Reason why the request failed to complete.</p><p>If the server responds with a [HTTP status code](#response_code) that represents a HTTP error (4xx/5xx), this is _not_ considered a request error.</p> | [<span class="tag str"></span>](../types.md)
is_error {: #is_error } | If the request failed due to an [error](#error). | [<span class="tag boo"></span>](../types.md)
is_done {: #is_done } | If the request completed _or failed_. If the request failed, [is_error](#is_error) will be set. | [<span class="tag boo"></span>](../types.md)
response_code {: #response_code } | Response [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). | [<span class="tag number"></span>](../types.md)
text {: #text } | Response body. | [<span class="tag str"></span>](../types.md)
upload_progress {: #upload_progress } | Upload percentage, represented as a number from 0-1. | [<span class="tag flo"></span>](../types.md)
url {: #url } | The request's target URL. If the request was redirected, this will still return the initial URL. | [<span class="tag str"></span>](../types.md)

##Functions {: data-toc-sort }

Function Name | Return | Description | &nbsp;
-- | -- | -- | --:
dispose() {: data-toc-child-of="functions" } | | <p>**Web requests are automatically disposed of after a request completes/fails.**</p><p>You may call this method to _try_ abort a request and dispose of it early.</p> |
getResponseHeader([<span class="tag str"></span>](../types.md) name) {: data-toc-label="getResponseHeader(...)" data-toc-child-of="functions" } | [<span class="ret str"></span>](../types.md) | Returns the value of the specified response header, or `nil` if no such header exists. |
getResponseHeaders() {: data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md)  | Returns the table of response headers. Keys and values are both [<span class="tag str"></span>](../types.md). |
