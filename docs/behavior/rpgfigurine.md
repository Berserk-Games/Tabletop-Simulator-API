The RPGFigurine behavior is present on Objects that are figurines with built-in animations i.e. RPG Kit objects.

## Callback Members

These are `RPGFigurine` member variable which can be assigned a function that will be executed in response to an even
occurring.

Member Name | Description | &nbsp;
-- | -- | --
onAttack([<span class="tag tab"></span>](../types.md) hitObjects) | Executed when an attack is performed by the RPGFigurine Object. | [:i:](#onattack)
onHit([<span class="tag obj"></span>](../types.md) attacker) | Executed when the RPGFigurine Object is attacked. | [:i:](#onattack)

## Functions {: data-toc-sort }

Function Name | Return | Description
-- | -- | --
attack() {: #attack data-toc-label="attack()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Plays a random attack animation.
changeMode() {: #changemode data-toc-label="changeMode()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Changes the figurine's current mode. What the mode represents is based on the figurine.
die() {: #die data-toc-label="die()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Plays the death animation or causes it to return to life.

!!!example
    Make an RPG figurine attack.
    ```lua
    object.RPGFigurine.attack()
    ```
---

## Callback Member Details

### onAttack(...)

Executed when an attack is performed by the RPGFigurine Object.

An attack is triggered via the context menu or by pressing the appropriate number key. If another RPGFigurine is within
its attack arc, then [onHit](#onhit) will be executed on the other figurine.

!!!info "onAttack(hitObjects)"
    * [<span class="tag tab"></span>](../types.md) **hitObjects**: A table of RPGFigurine Objects within the reach of the attack.

!!!example
    Assign an `onAttack` callback that prints the name of each object attacked.
    ```lua
    function object.RPGFigurine.onAttack(hitObjects)
        for _, v in ipairs(hitObjects) do
            print(v.getName() .. " was hit!")
        end
    end
    ```

---


### onHit(...)

Executed when the RPGFigurine Object is hit by another attacking RPGFigure Object.

An attack is triggered via the context menu or by pressing the appropriate number key. If this RPGFigurine Object is
within the attack radius of an attacker, this function will be executed.

!!!info "onHit(attacker)"
    * [<span class="tag obj"></span>](../types.md) **attacker**: The RPGFigurine Object performing the attack.

!!!example
    Assign an `onHit` callback that prints the name of the object that performed the attack.
    ```lua
    function object.RPGFigurine.onHit(attacker)
        print(attacker.getName() .. " attacked the Cyclops!")
    end
    ```
