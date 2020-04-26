An RPGFigurine is an in-game Object of a figurine with built-in animations. It has its own class, RPGFigurine, with functions associated with it. This allows you to manipulate the special properties of these figurines.

##Function Summary

###Object Functions
These functions are called like this: `self.RPGFigurine.attack()`.

Function Name | Description | Return
-- | -- | --
<a class="anchor" id="attack"></a>attack() | Plays a random attack animation. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="changemode"></a>changeMode() | Changes the figurine's current mode. What the mode represents is based on the figurine. | [<span class="ret boo"></span>](types.md)
<a class="anchor" id="die"></a>die() | Plays the death animation or causes it to return to life. | [<span class="ret boo"></span>](types.md)

###Event Functions
These functions are called by the game whenever a figurine attacks or is attacked. See details for example usage.

Function Name | Description | &nbsp;
-- | -- | --:
onAttack([<span class="tag tab"></span>](types.md)&nbsp;hit_list) | Activates when an attack is performed by an identified RPGFigurine Object. | [<span class="i"></span>](#onattack)
onHit([<span class="tag obj"></span>](types.md)&nbsp;attacker) | Activates when an attack is performed on this RPGFigurine Object. | [<span class="i"></span>](#onattack)





---

##Function Details

###Event Function Details

####onAttack(...)

Activates when an attack is performed by an identified RPGFigurine Object. An attack is triggered via the context menu or pressing the appropriate number key. If another RPGFigurine is within its attack arch, then the function will be triggered with the figurine hit passed as a parameter.

!!!info "onAttack(hit_list)"
    * [<span class="tag tab"></span>](types.md)&nbsp;**hit_list**: A Table of RPGFigurine Object references within the reach of the attack.

``` Lua
-- Monitoring and announcing a cyclops attacks
function onLoad()
    cyclops = getObjectFromGUID("aaa111")

    function cyclops.RPGFigurine.onAttack(hit_list)
        for _, v in ipairs(hit_list) do
            print(v.getName() .. " was hit!")
        end
    end
end
```

---


####onHit(...)

Activates when an attack is performed on this RPGFigurine Object. An attack is triggered via the context menu or pressing the appropriate number key. If this RPGFigurine is within the attack radius, this function is triggered, passing a parameter of the Object which attacked.

!!!info "onHit(attacker)"
    * [<span class="tag obj"></span>](types.md)&nbsp;**attacker**: Reference to the RPGFigurine attacking the indicated RPGFigurine.

``` Lua
-- Monitoring and announcing a cyclops being hit
function onLoad()
    cyclops = getObjectFromGUID("aaa111")

    function cyclops.RPGFigurine.onHit(attacker)
        print(attacker.getName() .. " attacked the Cyclops!")
    end
end
```
