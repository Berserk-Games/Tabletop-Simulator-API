You can spawn [custom Objects](https://kb.tabletopsimulator.com/custom-content/about-custom-objects/) and then provide the custom content for them after spawning them by calling [setCustomObject()](object.md#setcustomobject). {>>See setCustomObject for usage<<}

You can also use setCustomObject along with [reload()](object.md#reload) to modify an existing custom Object.

##Custom AssetBundle

* Custom_Assetbundle

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **assetbundle**: The path/url for the AssetBundle.
        * [<span class="tag str"></span>](types.md) **assetbundle_secondary**: The path/url for the secondary AssetBundle property.
            * {>>Optional, is not used by default.<<}
        * [<span class="tag int"></span>](types.md) **type**: An Int representing the Object's type.
            * {>>Optional, defaults to 0.<<}
                * **0**: Generic
                * **1**: Figurine
                * **2**: Dice
                * **3**: Coin
                * **4**: Board
                * **5**: Chip
                * **6**: Bag
                * **7**: Infinite bag
        * [<span class="tag int"></span>](types.md) **material**: An Int representing the Object's material.
            * {>>Optional, defaults to 0.<<}
                * **0**: Plastic
                * **1**: Wood
                * **2**: Metal
                * **3**: Cardboard

##Custom Board

* Custom_Board

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **image**: The path/url for the board.

##Custom Deck

* DeckCustom

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **face**: The path/url of the face cardsheet.
        * [<span class="tag str"></span>](types.md) **back**: The path/url of the back cardsheet or card back.
        * [<span class="tag boo"></span>](types.md) **unique_back**: If each card has a unique card back (via a cardsheet).
            * {>>Optional, defaults to false.<<}
        * [<span class="tag int"></span>](types.md) **width**: The number of columns on the cardsheet.
            * {>>Optional, defaults to 10.<<}
        * [<span class="tag int"></span>](types.md) **height**: The number of rows on the cardsheet.
            * {>>Optional, defaults to 7.<<}
        * [<span class="tag int"></span>](types.md) **number**: The number of cards on the cardsheet.
            * {>>Optional, defaults to 52.<<}
        * [<span class="tag boo"></span>](types.md) **sideways**: If the cards are horizontal instead of vertical.
            * {>>Optional, defaults to false.<<}
        * [<span class="tag boo"></span>](types.md) **back_is_hidden**: If cards have a special face that shows up when hidden in a hand zone.
            * {>>Optional, defaults to false.<<}

##Custom Dice

* Custom_Dice

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **image**: The path/url for the [custom die](http://berserk-games.com/knowledgebase/custom-dice/).
        * [<span class="tag int"></span>](types.md) **type**: The type of die, which determines its number of sides.
            * {>>Optional, defaults to 1.<<}
                * **0**: 4-sided
                * **1**: 6-sided
                * **2**: 8-sided
                * **3**: 10-sided
                * **4**: 12-sided
                * **5**: 20-sided

##Custom Figurine

* Figurine_Custom

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **image**: The path/url for the [custom figurine](http://berserk-games.com/knowledgebase/custom-figurines/).
        * [<span class="tag str"></span>](types.md) **image_secondary**: The path/url for the custom figurine's back.
            * {>>Optional, defaults to "image".<<}

##Custom Model

* Custom_Model

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **mesh**: The path/url for the .obj mesh used on the [custom model](http://berserk-games.com/knowledgebase/custom-models/).
        * [<span class="tag str"></span>](types.md) **diffuse**: The path/url for the diffuse image.
        * [<span class="tag str"></span>](types.md) **normal**: The path/url for the normals image.
            * {>>Optional, is not used by default.<<}
        * [<span class="tag str"></span>](types.md) **collider**: The path/url for the collider mesh.
            * {>>Optional, defaults to a generic box collider.<<}
        * [<span class="tag boo"></span>](types.md) **convex**: If the object model is convex.
            * {>>Optional, defaults to false.<<}
        * [<span class="tag int"></span>](types.md) **type**: An Int representing the Object's type.
            * {>>Optional, defaults to 0.<<}
                * **0**: Generic
                * **1**: Figurine
                * **2**: Dice
                * **3**: Coin
                * **4**: Board
                * **5**: Chip
                * **6**: Bag
                * **7**: Infinite bag
        * [<span class="tag int"></span>](types.md) **material**: An Int representing the Object's material.
            * {>>Optional, defaults to 0.<<}
                * **0**: Plastic
                * **1**: Wood
                * **2**: Metal
                * **3**: Cardboard
        * [<span class="tag flo"></span>](types.md) **specular_intensity**: The specular intensity.
            * {>>Optional, defaults to 0.1.<<}
        * [<span class="tag tab"></span>](types.md) **specular_color**: The specular [Color](types.md#color).
            * {>>Optional, defaults to {r=1, g=1, b=1}.<<}
        * [<span class="tag flo"></span>](types.md) **specular_sharpness**: The specular sharpness.
            * {>>Optional, defaults to 3.<<}
        * [<span class="tag flo"></span>](types.md) **freshnel_strength**: The freshnel strength.
            * {>>Optional, defaults to 0.1.<<}
        * [<span class="tag boo"></span>](types.md) **cast_shadows**: If the Object casts shadows.
            * {>>Optional, defaults to true.<<}

##Custom Tile

* Custom_Tile

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **image**: The path/url for the [custom tile](http://berserk-games.com/knowledgebase/custom-tiles/) image.
        * [<span class="tag int"></span>](types.md) **type**: Determines the shape of the tile.
            * {>>Optional, defaults to 0.<<}
                * **0**: Square/Rectangle
                * **1**: Hex
                * **2**: Circle
        * [<span class="tag str"></span>](types.md) **image_bottom**: The path/url for the bottom-side image.
            * {>>Optional, uses the top image by default.<<}
        * [<span class="tag flo"></span>](types.md) **thickness**: How thick the tile is.
            * {>>Optional, defaults to 0.5.<<}
        * [<span class="tag boo"></span>](types.md) **stackable**: If these tiles stack together into a pile.
            * {>>Optional, defaults to false.<<}

##Custom Token

* Custom_Token

!!!info "Custom Parameters"
    * [<span class="tag tab"></span>](types.md) **parameters**: A Table of parameters which determine the properties of the Object.
        * [<span class="tag str"></span>](types.md) **image**: The path/url for the [custom token](http://berserk-games.com/knowledgebase/custom-tokens/) image.
        * [<span class="tag flo"></span>](types.md) **thickness**: How thick the tile is.
            * {>>Optional, defaults to 0.2.<<}
        * [<span class="tag flo"></span>](types.md) **mege_distance**: How accurate the edges are to the image.
            * {>>Optional, defaults to 15.<<}
        * [<span class="tag boo"></span>](types.md) **stackable**: If these tiles stack together into a pile.
            * {>>Optional, defaults to false.<<}
