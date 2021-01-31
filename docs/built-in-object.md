
This page has information on each type of non-custom object, including the internal names used in the object's save data, which can be used in the `json.Name`, `data.Name`, and `type` fields of [`spawnObjectJSON()`](base.md#spawnobjectjson), [`spawnObjectData()`](base.md#spawnobjectdata), and [`spawnObject()`](base.md#spawnobject) respectively.

For Custom Objects, see [Custom Game Objects](custom-game-objects.md).

## Object Types

Each item listed below is treated as a unique object type. (ie. A red checker tinted black will not stack on top of a regular black checker.)

### Blocks

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="BlockRectangle"></a>BlockRectangle | `Block` | A blue rectangular prism. |
<a class="anchor" id="BlockSquare"></a>BlockSquare | `Block` | A red cube. |
<a class="anchor" id="BlockTriangle"></a>BlockTriangle | `Block` | A green triangular prism. |

### Boards

All boards spawn locked by default.

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="backgammon_board"></a>backgammon_board | `Board` | The fold-open board of Backgammon. | Includes snap-points along each triangle, totalling 120.
<a class="anchor" id="CardBot_Board"></a>CardBot_Board | `Board` | The main board and 4 player boards of CardBots, Build & Destroy. | Includes snap-points on each card and deck location, totally 79.
<a class="anchor" id="Checker_Board"></a>Checker_Board | `Board` | The 8x8 board of Checkers. | Includes snap-points on each grid square, totalling 64.
<a class="anchor" id="Chess_Board"></a>Chess_Board | `Board` | The 8x8 board of Chess. | Includes snap-points on each grid square, totalling 64.
<a class="anchor" id="Chinese_Checkers_Board"></a>Chinese_Checkers_Board | `Board` | The 6-pointed board of Sternhalma, or Chinese Checkers. | Includes snap-points on each indent, totalling 121.
<a class="anchor" id="Go_Board"></a>Go_Board | `Board` | The 9-starred board of Go. | Includes snap-points on each line intersection, totalling 361.
<a class="anchor" id="Pachisi_board"></a>Pachisi_board | `Board` | A 6-player Pachisi board. | Includes snap-points on each indent, totall 133.
<a class="anchor" id="reversi_board"></a>reversi_board | `Board` | The 8x8 board of Reversi. | Includes snap-points on each grid square, totalling 64.

### Cards

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Card"></a>Card | `Card` | A blank card, standard playing card, or Cardbots card. |
<a class="anchor" id="Deck"></a>Deck | `Deck` | A deck of the 52 standard playing cards. | Shuffles immediately when spawned.
<a class="anchor" id="Deck_CardBot_Head"></a>Deck_CardBot_Head | `Deck` | A deck of the 10 head cards for CardBots, Build & Destroy. | Shuffles immediately when spawned.
<a class="anchor" id="Deck_CardBot_Main"></a>Deck_CardBot_Main | `Deck` | A deck of the 152 main cards for CardBots, Build & Destroy. | Shuffles immediately when spawned.

### Checkers

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Checker_black"></a>Checker_black | `Checker` | A black checker with a crown emblem on the top side. |
<a class="anchor" id="Checker_red"></a>Checker_red | `Checker` | A red checker with a crown emblem on the top side. |
<a class="anchor" id="Checker_white"></a>Checker_white | `Checker` | A white checker with a crown emblem on the top side. |
<a class="anchor" id="Chinese_Checkers_Piece"></a>Chinese_Checkers_Piece | `Checker` | A marble for use in Sternhalma, or Chinese Checkers. |

### Chess Pieces

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Chess_Bishop"></a>Chess_Bishop | `Chess` | A chrome Chess bishop. | Faces visually to the left.
<a class="anchor" id="Chess_King"></a>Chess_King | `Chess` | A chrome Chess king. |
<a class="anchor" id="Chess_Knight"></a>Chess_Knight | `Chess` | A chrome Chess knight. | Faces visually backward (a common chess practice).
<a class="anchor" id="Chess_Pawn"></a>Chess_Pawn | `Chess` | A chrome Chess pawn. |
<a class="anchor" id="Chess_Queen"></a>Chess_Queen | `Chess` | A chrome Chess queen. |
<a class="anchor" id="Chess_Rook"></a>Chess_Rook | `Chess` | A chrome Chess rook. |

### Chips

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Chip_10"></a>Chip_10 | `Chip` | A blue casino chip worth $10 | Faces visually to the left.
<a class="anchor" id="Chip_50"></a>Chip_50 | `Chip` | A green casino chip worth $50 | Faces visually to the left.
<a class="anchor" id="Chip_100"></a>Chip_100 | `Chip` | A red casino chip worth $100 | Faces visually to the left.
<a class="anchor" id="Chip_500"></a>Chip_500 | `Chip` | A silver casino chip worth $500 | Faces visually to the left.
<a class="anchor" id="Chip_1000"></a>Chip_1000 | `Chip` | A gold casino chip worth $1000 | Faces visually to the left.

### Dice

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Die_4"></a>Die_4 | `Dice` | A 4-sided die. |
<a class="anchor" id="Die_6"></a>Die_6 | `Dice` | A 6-sided die with dots. |
<a class="anchor" id="Die_6_Rounded"></a>Die_6_Rounded | `Dice` | A 6-sided die with dots and rounded corners. |
<a class="anchor" id="Die_8"></a>Die_8 | `Dice` | An 8-sided die. |
<a class="anchor" id="Die_10"></a>Die_10 | `Dice` | A 10-sided die. |
<a class="anchor" id="Die_12"></a>Die_12 | `Dice` | A 12-sided die. |
<a class="anchor" id="Die_20"></a>Die_20 | `Dice` | A 20-sided die. |
<a class="anchor" id="Die_Piecepack"></a>Die_Piecepack | `Dice` | A wooden 6-sided die. |

### Dominos

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Domino"></a>Domino | `Domino` | A blank domino. |
<a class="anchor" id="Mahjong_Coin"></a>Mahjong_Coin | `Domino` | A coin used in Mahjong. |
<a class="anchor" id="Mahjong_Stick"></a>Mahjong_Stick | `Domino` | A stick used in Mahjong. |
<a class="anchor" id="Mahjong_Tile"></a>Mahjong_Tile | `Domino` | A tile used in Mahjong. |

### Figurines

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Figurine_Card_Bot"></a>Figurine_Card_Bot | `Figurine` | A rectangle-based figurine of a CardBot from CardBots, Build & Destroy. | Faces visually to the side.
<a class="anchor" id="Figurine_Kimi_Kat"></a>Figurine_Kimi_Kat | `Figurine` | A rectangle-based figurine of two sitting cats. |
<a class="anchor" id="Figurine_Knil"></a>Figurine_Knil | `Figurine` | A baseless figurine of a sword-wielding knight in full-plate armor. |
<a class="anchor" id="Figurine_Mara"></a>Figurine_Mara | `Figurine` | A baseless figurine of a bearded man in slacks. |
<a class="anchor" id="Figurine_Sir_Loin"></a>Figurine_Sir_Loin | `Figurine` | A rectangle-based figurine of a sword-wielding warrior with a shield on his back. | Faces visually backwards.
<a class="anchor" id="Figurine_Zeke"></a>Figurine_Zeke | `Figurine` | A baseless figurine of a cloaked character wielding a sword. |
<a class="anchor" id="Figurine_Zomblor"></a>Figurine_Zomblor | `Figurine` | A baseless figurine of a zombified riot-officer with knives for hands, wearing a skirt. |
<a class="anchor" id="Metal-Ball"></a>Metal Ball | `Figurine` | A metallic marble. | This object's internal name includes a space character and not an underline.
<a class="anchor" id="PlayerPawn"></a>PlayerPawn | `Figurine` | A small game piece representing a player. |

### Go Pieces

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="go_game_piece_black"></a>go_game_piece_black | `GoPiece` | A black Go stone. | Spawned from a [black Go bowl](#go_game_bowl_black).
<a class="anchor" id="go_game_piece_white"></a>go_game_piece_white | `GoPiece` | A white Go stone. | Spawned from a [white Go bowl](#go_game_bowl_white).
<a class="anchor" id="go_game_bowl_black"></a>go_game_bowl_black | `GoPiece` | A bowl that any number of [Black Go Stones](#go_game_piece_black) can be taken from and dropped back into. |
<a class="anchor" id="go_game_bowl_white"></a>go_game_bowl_white | `GoPiece` | A bowl that any number of [White Go Stones](#go_game_piece_white) can be taken from and dropped back into. |

### Piecepack

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="PiecePack_Arms"></a>PiecePack_Arms | `Piecepack` | A wooden coin with a blue fleur-de-lis on the underside. |
<a class="anchor" id="PiecePack_Crowns"></a>PiecePack_Crowns | `Piecepack` | A wooden coin with a green crown on the underside. |
<a class="anchor" id="PiecePack_Moons"></a>PiecePack_Moons | `Piecepack` | A wooden coin with a black moon on the underside. |
<a class="anchor" id="PiecePack_Suns"></a>PiecePack_Suns | `Piecepack` | A wooden coin with a red sun on the underside. |

### RPG Figurines

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="rpg_BARGHEST"></a>rpg_BARGHEST | `rpgFigurine` | An animated figurine of a mythical barghest. |
<a class="anchor" id="rpg_BASILISK"></a>rpg_BASILISK | `rpgFigurine` | An animated figurine of a mythical basilisk (a.k.a. cockatrice). |
<a class="anchor" id="rpg_BEAR"></a>rpg_BEAR | `rpgFigurine` | An animated figurine of a bear. |
<a class="anchor" id="rpg_BLACK_DRAGON"></a>rpg_BLACK_DRAGON | `rpgFigurine` | An animated figurine of an eastern dragon. |
<a class="anchor" id="rpg_CENTAUR"></a>rpg_CENTAUR | `rpgFigurine` | An animated figurine of an armoured centaur. |
<a class="anchor" id="rpg_CERBERUS"></a>rpg_CERBERUS | `rpgFigurine` | An animated figurine of an infernal 3-headed dog. |
<a class="anchor" id="rpg_CHIMERA"></a>rpg_CHIMERA | `rpgFigurine` | An animated figurine of a mythical chimera. |
<a class="anchor" id="rpg_CRASC"></a>rpg_CRASC | `rpgFigurine` | An animated figurine of a one-eyed manta-like creature. |
<a class="anchor" id="rpg_CYCLOP"></a>rpg_CYCLOP | `rpgFigurine` | An animated figurine of a club-wielding cyclops. |
<a class="anchor" id="rpg_DARKNESS_WARLORD"></a>rpg_DARKNESS_WARLORD | `rpgFigurine` | An animated figurine of an armoured, morningstar-wielding orc. |
<a class="anchor" id="rpg_DRAGONIDE"></a>rpg_DRAGONIDE | `rpgFigurine` | An animated figurine of an armored humanoid lizard. |
<a class="anchor" id="rpg_EVIL_WATCHER"></a>rpg_EVIL_WATCHER | `rpgFigurine` | An animated figurine of a cycloptic scaled head with eye-stalks and bat-wings. |
<a class="anchor" id="rpg_GHOUL"></a>rpg_GHOUL | `rpgFigurine` | An animated figurine of an undead humanoid |
<a class="anchor" id="rpg_GIANT_VIPER"></a>rpg_GIANT_VIPER | `rpgFigurine` | An animated figurine of a large snake. |
<a class="anchor" id="rpg_GOBLIN"></a>rpg_GOBLIN | `rpgFigurine` | An animated figurine of a lightly-armored goblin with two knives. |
<a class="anchor" id="rpg_GOLEM"></a>rpg_GOLEM | `rpgFigurine` | An animated figurine of a large earthen golem. |
<a class="anchor" id="rpg_GRIFFON"></a>rpg_GRIFFON | `rpgFigurine` | An animated figurine of a mythical griffon. |
<a class="anchor" id="rpg_HYDRA"></a>rpg_HYDRA | `rpgFigurine` | An animated figurine of a large 3-headed lizard. |
<a class="anchor" id="rpg_KNIGHT"></a>rpg_KNIGHT | `rpgFigurine` | An animated figurine of a knight in full-plate armor wielding a sword and shield. |
<a class="anchor" id="rpg_KOBOLD"></a>rpg_KOBOLD | `rpgFigurine` | An animated figurine of a small helmeted humanoid. |
<a class="anchor" id="rpg_LIZARD_WARRIOR"></a>rpg_LIZARD_WARRIOR | `rpgFigurine` | An animated figurine of a sword-wielding lizard-like humanoid |
<a class="anchor" id="rpg_MAGE"></a>rpg_MAGE | `rpgFigurine` | An animated figurine of a staff-wielding mage. |
<a class="anchor" id="rpg_MANTICORA"></a>rpg_MANTICORA | `rpgFigurine` | An animated figurine of a mythical manticore. | This type is spelled with an A.
<a class="anchor" id="rpg_MUMMY"></a>rpg_MUMMY | `rpgFigurine` | An animated figurine of a living mummy. |
<a class="anchor" id="rpg_OGRE"></a>rpg_OGRE | `rpgFigurine` | An animated figurine of a large boiled humanoid. |
<a class="anchor" id="rpg_ORC"></a>rpg_ORC | `rpgFigurine` | An animated figurine of an axe-wielding orc. |
<a class="anchor" id="rpg_RANGER"></a>rpg_RANGER | `rpgFigurine` | An animated figurine of a bow-wielding ranger. |
<a class="anchor" id="rpg_RAT"></a>rpg_RAT | `rpgFigurine` | An animated figurine of a giant rat. |
<a class="anchor" id="rpg_SKELETON_KNIGHT"></a>rpg_SKELETON_KNIGHT | `rpgFigurine` | An animated figurine of an armored living skeleton. |
<a class="anchor" id="rpg_TEMPLATE"></a>rpg_TEMPLATE | `rpgFigurine` | The base of an RPG figurine. | It has the same animatable triggers as any other RPG Figurine, but no associated animations.
<a class="anchor" id="rpg_THIEF"></a>rpg_THIEF | `rpgFigurine` | An animated figurine of a cowled knife-wielding thief. |
<a class="anchor" id="rpg_TREE_ENT"></a>rpg_TREE_ENT | `rpgFigurine` | An animated figurine of a large tree creature. |
<a class="anchor" id="rpg_TROLL"></a>rpg_TROLL | `rpgFigurine` | An animated figurine of a large green humanoid. |
<a class="anchor" id="rpg_VAMPIRE"></a>rpg_VAMPIRE | `rpgFigurine` | An animated figurine of a large wingless bat. |
<a class="anchor" id="rpg_WARRIOR"></a>rpg_WARRIOR | `rpgFigurine` | An animated figurine of a stout, bearded, axe-wielding warrior in scale mail. |
<a class="anchor" id="rpg_WEREWOLF"></a>rpg_WEREWOLF | `rpgFigurine` | An animated figurine of a mythical werewolf. |
<a class="anchor" id="rpg_WYVERN"></a>rpg_WYVERN | `rpgFigurine` | An animated figurine of a mythical wyvern. |

### Tileset Pieces

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="Tileset_Barrel"></a>Tileset_Barrel | `Tileset` | A small barrel for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Chair"></a>Tileset_Chair | `Tileset` | A small chair for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Chest"></a>Tileset_Chest | `Tileset` | A small chest for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Corner"></a>Tileset_Corner | `Tileset` | A floor tile with two walls for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Floor"></a>Tileset_Floor | `Tileset` | A floor tile for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Rock"></a>Tileset_Rock | `Tileset` | A small rock for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Table"></a>Tileset_Table | `Tileset` | A small table for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Tree"></a>Tileset_Tree | `Tileset` | A small tree for use in RPG Tilesets. |
<a class="anchor" id="Tileset_Wall"></a>Tileset_Wall | `Tileset` | A floor tile with a wall for use in RPG Tilesets. |

### Other

Name | Tag | Description | Notes
-- | -- | -- | --
<a class="anchor" id="backgammon_piece_brown"></a>backgammon_piece_brown | `Backgammon Piece` | A brown Backgammon piece. |
<a class="anchor" id="backgammon_piece_white"></a>backgammon_piece_white | `Backgammon Piece` | A white Backgammon piece. |
<a class="anchor" id="Bag"></a>Bag | `Bag` | A pouch that objects can be stored in and taken from. |
<a class="anchor" id="Bowl"></a>Bowl | `Generic` | A wooden bowl that objects can be dropped in. | The bowl does not have an inventory, objects merely rest within it visually. 
<a class="anchor" id="Calculator"></a>Calculator | `Calculator` | An interactive calculator. | Faces visually backwards.
<a class="anchor" id="Counter"></a>Counter | `Counter` | An interactive digital counter. |
<a class="anchor" id="Digital_Clock"></a>Digital_Clock | `Clock` | An interactive digital clock. |
<a class="anchor" id="Infinite_Bag"></a>Infinite_Bag | A pouch that any number of copies of a single object can be taken from and dropped back into. | An object must be put into the bag to become the source object. 
<a class="anchor" id="Notecard"></a>Notecard | `Notecard` | An editable notecard. |
<a class="anchor" id="Quarter"></a>Quarter | `Coin` | An american quarter minted in 1942. | Spawns tails-up, facing to the right.
<a class="anchor" id="reversi_chip"></a>reversi_chip | `Generic` | A dual-colored Reversi chip. | Spawns white-side up.
<a class="anchor" id="Tablet"></a>Tablet | `Tablet` | A tablet that displays a webpage. |

### Scripting

Name | Description | Notes
-- | -- | --
<a class="anchor" id="ScriptingTrigger"></a>ScriptingTrigger | A Scripting Zone. |
<a class="anchor" id="FogOfWarTrigger"></a>FogOfWarTrigger | A [Hidden Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#hidden-zone) |
<a class="anchor" id="FogOfWar"></a>FogOfWar | A [Fog of War Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone) |
<a class="anchor" id="3DText"></a>3DText | The text that the [Text Tool](https://kb.tabletopsimulator.com/game-tools/text-tool/) spawns. |

## Spawnable Names

When using [`spawnObject()`](base.md#spawnobject), the `type` parameter can be any of the above object types, or any of the below names, which spawns an object of a certain type, and with certain properties different from default.

Alternate&nbsp;Name | Object | Differences
-- | -- | --
<a class="anchor" id="Arms-Dice"></a>Arms Dice | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `0`.
<a class="anchor" id="Backgammon-Board"></a>Backgammon Board | [`backgammon_board`](#backgammon_board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Barrel"></a>Barrel | [`Tileset_Barrel`](#Tileset_Barrel) | *(none)*
<a class="anchor" id="Bear"></a>Bear | [`rpg_BEAR`](#rpg_BEAR) | *(none)*
<a class="anchor" id="Bishop-Cast-Iron"></a>Bishop Cast Iron | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `1`.
<a class="anchor" id="Bishop-Chrome"></a>Bishop Chrome | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `0`.
<a class="anchor" id="Bishop-Dark-Wood"></a>Bishop Dark Wood | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `3`.
<a class="anchor" id="Bishop-Light-Wood"></a>Bishop Light Wood | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `2`.
<a class="anchor" id="Black-Ball"></a>Black Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `6`.
<a class="anchor" id="Black-Checker"></a>Black Checker | [`Checker_black`](#Checker_black) | *(none)*
<a class="anchor" id="Black-Pawn"></a>Black Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `8`.
<a class="anchor" id="Blue-10"></a>Blue 10 | [`Chip_10`](#Chip_10) | *(none)*
<a class="anchor" id="Blue-Ball"></a>Blue Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `4`.
<a class="anchor" id="Blue-Pawn"></a>Blue Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `5`.
<a class="anchor" id="Blue-Rectangle"></a>Blue Rectangle | [`BlockRectangle`](#BlockRectangle) | *(none)*
<a class="anchor" id="Brown-Backgammon"></a>Brown Backgammon | [`backgammon_piece_brown`](#backgammon_piece_brown) | *(none)*
<a class="anchor" id="CardBot"></a>CardBot | [`Figurine_Card_Bot`](#Figurine_Card_Bot) | *(none)*
<a class="anchor" id="CardBots-Head-Deck"></a>CardBots Head Deck | [`Deck_CardBot_Head`](#Deck_CardBot_Head) | *(none)*
<a class="anchor" id="CardBots-Main-Deck"></a>CardBots Main Deck | [`Deck_CardBot_Main`](#Deck_CardBot_Main) | *(none)*
<a class="anchor" id="Chair"></a>Chair | [`Tileset_Chair`](#Tileset_Chair) | *(none)*
<a class="anchor" id="Checkers-Board"></a>Checkers Board | [`Checker_Board`](#Checker_Board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Chess-Board"></a>Chess Board | [`Chess_Board`](#Chess_Board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Chest"></a>Chest | [`Tileset_Chest`](#Tileset_Chest) | *(none)*
<a class="anchor" id="Chimera"></a>Chimera | [`rpg_CHIMERA`](#rpg_CHIMERA) | *(none)*
<a class="anchor" id="Chinese-Checkers-Board"></a>Chinese Checkers Board | [`Chinese_Checkers_Board`](#Chinese_Checkers_Board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Corner"></a>Corner | [`Tileset_Corner`](#Tileset_Corner) | *(none)*
<a class="anchor" id="Crowns-Dice"></a>Crowns Dice | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `1`.
<a class="anchor" id="Custom-Board"></a>Custom Board | [`Custom_Board`](#Custom_Board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Custom-Deck"></a>Custom Deck | [`DeckCustom`](#DeckCustom) | *(none)*
<a class="anchor" id="Custom-Figurine"></a>Custom Figurine | [`Figurine_Custom`](#Figurine_Custom) | *(none)*
<a class="anchor" id="Custom-Model"></a>Custom Model | [`Custom_Model`](#Custom_Model) | *(none)*
<a class="anchor" id="Cyclops"></a>Cyclops | [`rpg_CYCLOP`](#rpg_CYCLOP) | *(none)*
<a class="anchor" id="D10"></a>D10 | [`Die_10`](#Die_10) | `MaterialIndex` of `0`.
<a class="anchor" id="D10-Chrome"></a>D10 Chrome | [`Die_10`](#Die_10) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="D12"></a>D12 | [`Die_12`](#Die_12) | `MaterialIndex` of `0`.
<a class="anchor" id="D12-Chrome"></a>D12 Chrome | [`Die_12`](#Die_12) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="D20"></a>D20 | [`Die_20`](#Die_20) | `MaterialIndex` of `0`.
<a class="anchor" id="D20-Chrome"></a>D20 Chrome | [`Die_20`](#Die_20) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="D4"></a>D4 | [`Die_4`](#Die_4) | `MaterialIndex` of `0`.
<a class="anchor" id="D4-Chrome"></a>D4 Chrome | [`Die_4`](#Die_4) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="D6"></a>D6 | [`Die_6`](#Die_6) | `MaterialIndex` of `0`.
<a class="anchor" id="D6-Black"></a>D6 Black | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `0`.
<a class="anchor" id="D6-Blue"></a>D6 Blue | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `3`.
<a class="anchor" id="D6-Chrome"></a>D6 Chrome | [`Die_6`](#Die_6) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="D6-Green"></a>D6 Green | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `2`.
<a class="anchor" id="D6-Red"></a>D6 Red | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `1`.
<a class="anchor" id="D8"></a>D8 | [`Die_8`](#Die_8) | `MaterialIndex` of `0`.
<a class="anchor" id="D8-Chrome"></a>D8 Chrome | [`Die_8`](#Die_8) | `MaterialIndex` of `1`, `AltSound` of `true`.
<a class="anchor" id="Digital-Clock"></a>Digital Clock | [`Digital_Clock`](#Digital_Clock) | *(none)*
<a class="anchor" id="Dragonide"></a>Dragonide | [`rpg_DRAGONIDE`](#rpg_DRAGONIDE) | *(none)*
<a class="anchor" id="Evil-Watcher"></a>Evil Watcher | [`rpg_EVIL_WATCHER`](#rpg_EVIL_WATCHER) | *(none)*
<a class="anchor" id="Floor"></a>Floor | [`Tileset_Floor`](#Tileset_Floor) | *(none)*
<a class="anchor" id="Ghoul"></a>Ghoul | [`rpg_GHOUL`](#rpg_GHOUL) | *(none)*
<a class="anchor" id="Giant-Rat"></a>Giant Rat | [`rpg_RAT`](#rpg_RAT) | *(none)*
<a class="anchor" id="Giant-Viper"></a>Giant Viper | [`rpg_GIANT_VIPER`](#rpg_GIANT_VIPER) | *(none)*
<a class="anchor" id="Go-Board"></a>Go Board | [`Go_Board`](#Go_Board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="GO-Bowl-Black"></a>GO Bowl Black | [`go_game_bowl_black`](#go_game_bowl_black) | *(none)*
<a class="anchor" id="GO-Bowl-White"></a>GO Bowl White | [`go_game_bowl_white`](#go_game_bowl_white) | *(none)*
<a class="anchor" id="GO-Piece-Black"></a>GO Piece Black | [`go_game_piece_black`](#go_game_piece_black) | *(none)*
<a class="anchor" id="GO-Piece-White"></a>GO Piece White | [`go_game_piece_white`](#go_game_piece_white) | *(none)*
<a class="anchor" id="Goblin"></a>Goblin | [`rpg_GOBLIN`](#rpg_GOBLIN) | *(none)*
<a class="anchor" id="Gold-1000"></a>Gold 1000 | [`Chip_1000`](#Chip_1000) | *(none)*
<a class="anchor" id="Golem"></a>Golem | [`rpg_GOLEM`](#rpg_GOLEM) | *(none)*
<a class="anchor" id="Green-50"></a>Green 50 | [`Chip_50`](#Chip_50) | *(none)*
<a class="anchor" id="Green-Ball"></a>Green Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `3`.
<a class="anchor" id="Green-Pawn"></a>Green Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `4`.
<a class="anchor" id="Green-Triangle"></a>Green Triangle | [`BlockTriangle`](#BlockTriangle) | *(none)*
<a class="anchor" id="Griffon"></a>Griffon | [`rpg_GRIFFON`](#rpg_GRIFFON) | *(none)*
<a class="anchor" id="Hydra"></a>Hydra | [`rpg_HYDRA`](#rpg_HYDRA) | *(none)*
<a class="anchor" id="Joker"></a>Joker | [`Card`](#Card) | `CardID` of `52`.
<a class="anchor" id="Kimi-Kat"></a>Kimi Kat | [`Figurine_Kimi_Kat`](#Figurine_Kimi_Kat) | *(none)*
<a class="anchor" id="King-Cast-Iron"></a>King Cast Iron | [`Chess_King`](#Chess_King) | `MaterialIndex` of `1`.
<a class="anchor" id="King-Chrome"></a>King Chrome | [`Chess_King`](#Chess_King) | `MaterialIndex` of `0`.
<a class="anchor" id="King-Dark-Wood"></a>King Dark Wood | [`Chess_King`](#Chess_King) | `MaterialIndex` of `3`.
<a class="anchor" id="King-Light-Wood"></a>King Light Wood | [`Chess_King`](#Chess_King) | `MaterialIndex` of `2`.
<a class="anchor" id="Knight-Cast-Iron"></a>Knight Cast Iron | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `1`.
<a class="anchor" id="Knight-Chrome"></a>Knight Chrome | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `0`.
<a class="anchor" id="Knight-Dark-Wood"></a>Knight Dark Wood | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `3`.
<a class="anchor" id="Knight-Light-Wood"></a>Knight Light Wood | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `2`.
<a class="anchor" id="Knight-of-Knil"></a>Knight of Knil | [`Figurine_Knil`](#Figurine_Knil) | *(none)*
<a class="anchor" id="Kobold"></a>Kobold | [`rpg_KOBOLD`](#rpg_KOBOLD) | *(none)*
<a class="anchor" id="Lizard-Warrior"></a>Lizard Warrior | [`rpg_LIZARD_WARRIOR`](#rpg_LIZARD_WARRIOR) | *(none)*
<a class="anchor" id="Loot-Bag"></a>Loot Bag | [`Bag`](#Bag) | *(none)*
<a class="anchor" id="Manticora"></a>Manticora | [`rpg_MANTICORA`](#rpg_MANTICORA) | *(none)*
<a class="anchor" id="Mara"></a>Mara | [`Figurine_Mara`](#Figurine_Mara) | *(none)*
<a class="anchor" id="Moons-Dice"></a>Moons Dice | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `2`.
<a class="anchor" id="Mummy"></a>Mummy | [`rpg_MUMMY`](#rpg_MUMMY) | *(none)*
<a class="anchor" id="Ogre"></a>Ogre | [`rpg_OGRE`](#rpg_OGRE) | *(none)*
<a class="anchor" id="Orange-Pawn"></a>Orange Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `2`.
<a class="anchor" id="Orc"></a>Orc | [`rpg_ORC`](#rpg_ORC) | *(none)*
<a class="anchor" id="Pachisi-Board"></a>Pachisi Board | [`Pachisi_board`](#Pachisi_board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Pawn-Cast-Iron"></a>Pawn Cast Iron | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `1`.
<a class="anchor" id="Pawn-Chrome"></a>Pawn Chrome | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `0`.
<a class="anchor" id="Pawn-Dark-Wood"></a>Pawn Dark Wood | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `3`.
<a class="anchor" id="Pawn-Light-Wood"></a>Pawn Light Wood | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `2`.
<a class="anchor" id="Pink-Ball"></a>Pink Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `5`.
<a class="anchor" id="Pink-Pawn"></a>Pink Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `7`.
<a class="anchor" id="Purple-Pawn"></a>Purple Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `6`.
<a class="anchor" id="Quarter"></a>Quarter | [`Quarter`](#Quarter) | *(none)*
<a class="anchor" id="Queen-Cast-Iron"></a>Queen Cast Iron | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `1`.
<a class="anchor" id="Queen-Chrome"></a>Queen Chrome | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `0`.
<a class="anchor" id="Queen-Dark-Wood"></a>Queen Dark Wood | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `3`.
<a class="anchor" id="Queen-Light-Wood"></a>Queen Light Wood | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `2`.
<a class="anchor" id="Random-Card"></a>Random Card | [`Card`](#Card) | Random `CardID` between `0` and `51` (inclusive).
<a class="anchor" id="Random-Domino"></a>Random Domino | [`Domino`](#Domino) | Random `MeshIndex` between `0` and `27` (inclusive).
<a class="anchor" id="Random-Mahjong"></a>Random Mahjong | [`Mahjong_Tile`](#Mahjong_Tile) | Random `MeshIndex` between `0` and `35` (inclusive).
<a class="anchor" id="Red-100"></a>Red 100 | [`Chip_100`](#Chip_100) | *(none)*
<a class="anchor" id="Red-Ball"></a>Red Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `1`.
<a class="anchor" id="Red-Checker"></a>Red Checker | [`Checker_red`](#Checker_red) | *(none)*
<a class="anchor" id="Red-Pawn"></a>Red Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `1`.
<a class="anchor" id="Red-Square"></a>Red Square | [`BlockSquare`](#BlockSquare) | *(none)*
<a class="anchor" id="Reversi-Board"></a>Reversi Board | [`reversi_board`](#reversi_board) | Snaps to table level immediately upon spawn.
<a class="anchor" id="Reversi-Chip"></a>Reversi Chip | [`reversi_chip`](#reversi_chip) | *(none)*
<a class="anchor" id="Rock"></a>Rock | [`Tileset_Rock`](#Tileset_Rock) | *(none)*
<a class="anchor" id="Rook-Cast-Iron"></a>Rook Cast Iron | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `1`.
<a class="anchor" id="Rook-Chrome"></a>Rook Chrome | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `0`.
<a class="anchor" id="Rook-Dark-Wood"></a>Rook Dark Wood | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `3`.
<a class="anchor" id="Rook-Light-Wood"></a>Rook Light Wood | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `2`.
<a class="anchor" id="Silver-500"></a>Silver 500 | [`Chip_500`](#Chip_500) | *(none)*
<a class="anchor" id="Sir-Loin"></a>Sir Loin | [`Figurine_Sir_Loin`](#Figurine_Sir_Loin) | *(none)*
<a class="anchor" id="Skeleton-Knight"></a>Skeleton Knight | [`rpg_SKELETON_KNIGHT`](#rpg_SKELETON_KNIGHT) | *(none)*
<a class="anchor" id="Standard-Deck"></a>Standard Deck | [`Deck`](#Deck) | *(none)*
<a class="anchor" id="Suns-Dice"></a>Suns Dice | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `3`.
<a class="anchor" id="Table"></a>Table | [`Tileset_Table`](#Tileset_Table) | *(none)*
<a class="anchor" id="Tree"></a>Tree | [`Tileset_Tree`](#Tileset_Tree) | *(none)*
<a class="anchor" id="Tree-Ent"></a>Tree Ent | [`rpg_TREE_ENT`](#rpg_TREE_ENT) | *(none)*
<a class="anchor" id="Troll"></a>Troll | [`rpg_TROLL`](#rpg_TROLL) | *(none)*
<a class="anchor" id="Vampire"></a>Vampire | [`rpg_VAMPIRE`](#rpg_VAMPIRE) | *(none)*
<a class="anchor" id="Wall"></a>Wall | [`Tileset_Wall`](#Tileset_Wall) | *(none)*
<a class="anchor" id="Werewolf"></a>Werewolf | [`rpg_WEREWOLF`](#rpg_WEREWOLF) | *(none)*
<a class="anchor" id="White-Backgammon"></a>White Backgammon | [`backgammon_piece_white`](#backgammon_piece_white) | *(none)*
<a class="anchor" id="White-Ball"></a>White Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `0`.
<a class="anchor" id="White-Checker"></a>White Checker | [`Checker_white`](#Checker_white) | *(none)*
<a class="anchor" id="White-Pawn"></a>White Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `0`.
<a class="anchor" id="Wolf"></a>Wolf | [`rpg_WOLF`](#rpg_WOLF) | *(none)*
<a class="anchor" id="Wyvern"></a>Wyvern | [`rpg_WYVERN`](#rpg_WYVERN) | *(none)*
<a class="anchor" id="Yellow-Ball"></a>Yellow Ball | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `2`.
<a class="anchor" id="Yellow-Pawn"></a>Yellow Pawn | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `3`.
<a class="anchor" id="Zeke-Kodoku"></a>Zeke Kodoku | [`Figurine_Zeke`](#Figurine_Zeke) | *(none)*
<a class="anchor" id="Zomblor"></a>Zomblor | [`Figurine_Zomblor`](#Figurine_Zomblor) | *(none)*
