
This page has information on each type of non-custom object, including the internal names used in the object's save data, which can be used in the `json.Name`, `data.Name`, and `type` fields of [`spawnObjectJSON()`](base.md#spawnobjectjson), [`spawnObjectData()`](base.md#spawnobjectdata), and [`spawnObject()`](base.md#spawnobject) respectively.

For Custom Objects, see [Custom Game Objects](custom-game-objects.md).

## Object Types

Each item listed below is treated as a unique object type. (ie. A red checker tinted black will not stack on top of a regular black checker.)

### Blocks

Name | Type | Description | Notes
-- | -- | -- | --
BlockRectangle {: #BlockRectangle } | `Block` | A blue rectangular prism. |
BlockSquare {: #BlockSquare } | `Block` | A red cube. |
BlockTriangle {: #BlockTriangle } | `Block` | A green triangular prism. |

### Boards

All boards spawn locked by default.

Name | Type | Description | Notes
-- | -- | -- | --
backgammon_board {: #backgammon_board } | `Board` | The fold-open board of Backgammon. | Includes snap-points along each triangle, totalling 120.
CardBot_Board {: #CardBot_Board } | `Board` | The main board and 4 player boards of CardBots, Build & Destroy. | Includes snap-points on each card and deck location, totally 79.
Checker_Board {: #Checker_Board } | `Board` | The 8x8 board of Checkers. | Includes snap-points on each grid square, totalling 64.
Chess_Board {: #Chess_Board } | `Board` | The 8x8 board of Chess. | Includes snap-points on each grid square, totalling 64.
Chinese_Checkers_Board {: #Chinese_Checkers_Board } | `Board` | The 6-pointed board of Sternhalma, or Chinese Checkers. | Includes snap-points on each indent, totalling 121.
Go_Board {: #Go_Board } | `Board` | The 9-starred board of Go. | Includes snap-points on each line intersection, totalling 361.
Pachisi_board {: #Pachisi_board } | `Board` | A 6-player Pachisi board. | Includes snap-points on each indent, totall 133.
reversi_board {: #reversi_board } | `Board` | The 8x8 board of Reversi. | Includes snap-points on each grid square, totalling 64.

### Cards

Name | Type | Description | Notes
-- | -- | -- | --
Card {: #Card } | `Card` | A blank card, standard playing card, or Cardbots card. |
Deck {: #Deck } | `Deck` | A deck of the 52 standard playing cards. | Shuffles immediately when spawned.
Deck_CardBot_Head {: #Deck_CardBot_Head } | `Deck` | A deck of the 10 head cards for CardBots, Build & Destroy. | Shuffles immediately when spawned.
Deck_CardBot_Main {: #Deck_CardBot_Main } | `Deck` | A deck of the 152 main cards for CardBots, Build & Destroy. | Shuffles immediately when spawned.

### Checkers

Name | Type | Description | Notes
-- | -- | -- | --
Checker_black {: #Checker_black } | `Checker` | A black checker with a crown emblem on the top side. |
Checker_red {: #Checker_red } | `Checker` | A red checker with a crown emblem on the top side. |
Checker_white {: #Checker_white } | `Checker` | A white checker with a crown emblem on the top side. |
Chinese_Checkers_Piece {: #Chinese_Checkers_Piece } | `Checker` | A marble for use in Sternhalma, or Chinese Checkers. |

### Chess Pieces

Name | Type | Description | Notes
-- | -- | -- | --
Chess_Bishop {: #Chess_Bishop } | `Chess` | A chrome Chess bishop. | Faces visually to the left.
Chess_King {: #Chess_King } | `Chess` | A chrome Chess king. |
Chess_Knight {: #Chess_Knight } | `Chess` | A chrome Chess knight. | Faces visually backward (a common chess practice).
Chess_Pawn {: #Chess_Pawn } | `Chess` | A chrome Chess pawn. |
Chess_Queen {: #Chess_Queen } | `Chess` | A chrome Chess queen. |
Chess_Rook {: #Chess_Rook } | `Chess` | A chrome Chess rook. |

### Chips

Name | Type | Description | Notes
-- | -- | -- | --
Chip_10 {: #Chip_10 } | `Chip` | A blue casino chip worth $10 | Faces visually to the left.
Chip_50 {: #Chip_50 } | `Chip` | A green casino chip worth $50 | Faces visually to the left.
Chip_100 {: #Chip_100 } | `Chip` | A red casino chip worth $100 | Faces visually to the left.
Chip_500 {: #Chip_500 } | `Chip` | A silver casino chip worth $500 | Faces visually to the left.
Chip_1000 {: #Chip_1000 } | `Chip` | A gold casino chip worth $1000 | Faces visually to the left.

### Dice

Name | Type | Description | Notes
-- | -- | -- | --
Die_4 {: #Die_4 } | `Dice` | A 4-sided die. |
Die_6 {: #Die_6 } | `Dice` | A 6-sided die with dots. |
Die_6_Rounded {: #Die_6_Rounded } | `Dice` | A 6-sided die with dots and rounded corners. |
Die_8 {: #Die_8 } | `Dice` | An 8-sided die. |
Die_10 {: #Die_10 } | `Dice` | A 10-sided die. |
Die_12 {: #Die_12 } | `Dice` | A 12-sided die. |
Die_20 {: #Die_20 } | `Dice` | A 20-sided die. |
Die_Piecepack {: #Die_Piecepack } | `Dice` | A wooden 6-sided die. |

### Dominos

Name | Type | Description | Notes
-- | -- | -- | --
Domino {: #Domino } | `Domino` | A blank domino. |
Mahjong_Coin {: #Mahjong_Coin } | `Domino` | A coin used in Mahjong. |
Mahjong_Stick {: #Mahjong_Stick } | `Domino` | A stick used in Mahjong. |
Mahjong_Tile {: #Mahjong_Tile } | `Domino` | A tile used in Mahjong. |

### Figurines

Name | Type | Description | Notes
-- | -- | -- | --
Figurine_Card_Bot {: #Figurine_Card_Bot } | `Figurine` | A rectangle-based figurine of a CardBot from CardBots, Build & Destroy. | Faces visually to the side.
Figurine_Kimi_Kat {: #Figurine_Kimi_Kat } | `Figurine` | A rectangle-based figurine of two sitting cats. |
Figurine_Knil {: #Figurine_Knil } | `Figurine` | A baseless figurine of a sword-wielding knight in full-plate armor. |
Figurine_Mara {: #Figurine_Mara } | `Figurine` | A baseless figurine of a bearded man in slacks. |
Figurine_Sir_Loin {: #Figurine_Sir_Loin } | `Figurine` | A rectangle-based figurine of a sword-wielding warrior with a shield on his back. | Faces visually backwards.
Figurine_Zeke {: #Figurine_Zeke } | `Figurine` | A baseless figurine of a cloaked character wielding a sword. |
Figurine_Zomblor {: #Figurine_Zomblor } | `Figurine` | A baseless figurine of a zombified riot-officer with knives for hands, wearing a skirt. |
Metal Ball {: #Metal-Ball } | `Figurine` | A metallic marble. | This object's internal name includes a space character and not an underline.
PlayerPawn {: #PlayerPawn } | `Figurine` | A small game piece representing a player. |

### Go Pieces

Name | Type | Description | Notes
-- | -- | -- | --
go_game_piece_black {: #go_game_piece_black } | `GoPiece` | A black Go stone. | Spawned from a [black Go bowl](#go_game_bowl_black).
go_game_piece_white {: #go_game_piece_white } | `GoPiece` | A white Go stone. | Spawned from a [white Go bowl](#go_game_bowl_white).
go_game_bowl_black {: #go_game_bowl_black } | `GoPiece` | A bowl that any number of [Black Go Stones](#go_game_piece_black) can be taken from and dropped back into. |
go_game_bowl_white {: #go_game_bowl_white } | `GoPiece` | A bowl that any number of [White Go Stones](#go_game_piece_white) can be taken from and dropped back into. |

### Graphics

Name | Description | Notes
-- | -- | --
3DText {: #3DText } | The text that the [Text Tool](https://kb.tabletopsimulator.com/game-tools/text-tool/) spawns. |

### Piecepack

Name | Type | Description | Notes
-- | -- | -- | --
PiecePack_Arms {: #PiecePack_Arms } | `Piecepack` | A wooden coin with a blue fleur-de-lis on the underside. |
PiecePack_Crowns {: #PiecePack_Crowns } | `Piecepack` | A wooden coin with a green crown on the underside. |
PiecePack_Moons {: #PiecePack_Moons } | `Piecepack` | A wooden coin with a black moon on the underside. |
PiecePack_Suns {: #PiecePack_Suns } | `Piecepack` | A wooden coin with a red sun on the underside. |

### RPG Figurines

Name | Type | Description | Notes
-- | -- | -- | --
rpg_BARGHEST {: #rpg_BARGHEST } | `rpgFigurine` | An animated figurine of a mythical barghest. |
rpg_BASILISK {: #rpg_BASILISK } | `rpgFigurine` | An animated figurine of a mythical basilisk (a.k.a. cockatrice). |
rpg_BEAR {: #rpg_BEAR } | `rpgFigurine` | An animated figurine of a bear. |
rpg_BLACK_DRAGON {: #rpg_BLACK_DRAGON } | `rpgFigurine` | An animated figurine of an eastern dragon. |
rpg_CENTAUR {: #rpg_CENTAUR } | `rpgFigurine` | An animated figurine of an armoured centaur. |
rpg_CERBERUS {: #rpg_CERBERUS } | `rpgFigurine` | An animated figurine of an infernal 3-headed dog. |
rpg_CHIMERA {: #rpg_CHIMERA } | `rpgFigurine` | An animated figurine of a mythical chimera. |
rpg_CRASC {: #rpg_CRASC } | `rpgFigurine` | An animated figurine of a one-eyed manta-like creature. |
rpg_CYCLOP {: #rpg_CYCLOP } | `rpgFigurine` | An animated figurine of a club-wielding cyclops. |
rpg_DARKNESS_WARLORD {: #rpg_DARKNESS_WARLORD } | `rpgFigurine` | An animated figurine of an armoured, morningstar-wielding orc. |
rpg_DRAGONIDE {: #rpg_DRAGONIDE } | `rpgFigurine` | An animated figurine of an armored humanoid lizard. |
rpg_EVIL_WATCHER {: #rpg_EVIL_WATCHER } | `rpgFigurine` | An animated figurine of a cycloptic scaled head with eye-stalks and bat-wings. |
rpg_GHOUL {: #rpg_GHOUL } | `rpgFigurine` | An animated figurine of an undead humanoid |
rpg_GIANT_VIPER {: #rpg_GIANT_VIPER } | `rpgFigurine` | An animated figurine of a large snake. |
rpg_GOBLIN {: #rpg_GOBLIN } | `rpgFigurine` | An animated figurine of a lightly-armored goblin with two knives. |
rpg_GOLEM {: #rpg_GOLEM } | `rpgFigurine` | An animated figurine of a large earthen golem. |
rpg_GRIFFON {: #rpg_GRIFFON } | `rpgFigurine` | An animated figurine of a mythical griffon. |
rpg_HYDRA {: #rpg_HYDRA } | `rpgFigurine` | An animated figurine of a large 3-headed lizard. |
rpg_KNIGHT {: #rpg_KNIGHT } | `rpgFigurine` | An animated figurine of a knight in full-plate armor wielding a sword and shield. |
rpg_KOBOLD {: #rpg_KOBOLD } | `rpgFigurine` | An animated figurine of a small helmeted humanoid. |
rpg_LIZARD_WARRIOR {: #rpg_LIZARD_WARRIOR } | `rpgFigurine` | An animated figurine of a sword-wielding lizard-like humanoid |
rpg_MAGE {: #rpg_MAGE } | `rpgFigurine` | An animated figurine of a staff-wielding mage. |
rpg_MANTICORA {: #rpg_MANTICORA } | `rpgFigurine` | An animated figurine of a mythical manticore. | This type is spelled with an A.
rpg_MUMMY {: #rpg_MUMMY } | `rpgFigurine` | An animated figurine of a living mummy. |
rpg_OGRE {: #rpg_OGRE } | `rpgFigurine` | An animated figurine of a large boiled humanoid. |
rpg_ORC {: #rpg_ORC } | `rpgFigurine` | An animated figurine of an axe-wielding orc. |
rpg_RANGER {: #rpg_RANGER } | `rpgFigurine` | An animated figurine of a bow-wielding ranger. |
rpg_RAT {: #rpg_RAT } | `rpgFigurine` | An animated figurine of a giant rat. |
rpg_SKELETON_KNIGHT {: #rpg_SKELETON_KNIGHT } | `rpgFigurine` | An animated figurine of an armored living skeleton. |
rpg_TEMPLATE {: #rpg_TEMPLATE } | `rpgFigurine` | The base of an RPG figurine. | It has the same animatable triggers as any other RPG Figurine, but no associated animations.
rpg_THIEF {: #rpg_THIEF } | `rpgFigurine` | An animated figurine of a cowled knife-wielding thief. |
rpg_TREE_ENT {: #rpg_TREE_ENT } | `rpgFigurine` | An animated figurine of a large tree creature. |
rpg_TROLL {: #rpg_TROLL } | `rpgFigurine` | An animated figurine of a large green humanoid. |
rpg_VAMPIRE {: #rpg_VAMPIRE } | `rpgFigurine` | An animated figurine of a large wingless bat. |
rpg_WARRIOR {: #rpg_WARRIOR } | `rpgFigurine` | An animated figurine of a stout, bearded, axe-wielding warrior in scale mail. |
rpg_WEREWOLF {: #rpg_WEREWOLF } | `rpgFigurine` | An animated figurine of a mythical werewolf. |
rpg_WOLF {: #rpg_WOLF } | `rpgFigurine` | An animated figurine of a mythical wolf. |
rpg_WYVERN {: #rpg_WYVERN } | `rpgFigurine` | An animated figurine of a mythical wyvern. |

### Tileset Pieces

Name | Type | Description | Notes
-- | -- | -- | --
Tileset_Barrel {: #Tileset_Barrel } | `Tileset` | A small barrel for use in RPG Tilesets. |
Tileset_Chair {: #Tileset_Chair } | `Tileset` | A small chair for use in RPG Tilesets. |
Tileset_Chest {: #Tileset_Chest } | `Tileset` | A small chest for use in RPG Tilesets. |
Tileset_Corner {: #Tileset_Corner } | `Tileset` | A floor tile with two walls for use in RPG Tilesets. |
Tileset_Floor {: #Tileset_Floor } | `Tileset` | A floor tile for use in RPG Tilesets. |
Tileset_Rock {: #Tileset_Rock } | `Tileset` | A small rock for use in RPG Tilesets. |
Tileset_Table {: #Tileset_Table } | `Tileset` | A small table for use in RPG Tilesets. |
Tileset_Tree {: #Tileset_Tree } | `Tileset` | A small tree for use in RPG Tilesets. |
Tileset_Wall {: #Tileset_Wall } | `Tileset` | A floor tile with a wall for use in RPG Tilesets. |

### Other

Name | Type | Description | Notes
-- | -- | -- | --
backgammon_piece_brown {: #backgammon_piece_brown } | `Backgammon Piece` | A brown Backgammon piece. |
backgammon_piece_white {: #backgammon_piece_white } | `Backgammon Piece` | A white Backgammon piece. |
Bag {: #Bag } | `Bag` | A pouch that objects can be stored in and taken from. |
Bowl {: #Bowl } | `Generic` | A wooden bowl that objects can be dropped in. | The bowl does not have an inventory, objects merely rest within it visually.
Calculator {: #Calculator } | `Calculator` | An interactive calculator. | Faces visually backwards.
Counter {: #Counter } | `Counter` | An interactive digital counter. |
Digital_Clock {: #Digital_Clock } | `Clock` | An interactive digital clock. |
Infinite_Bag {: #Infinite_Bag } | A pouch that any number of copies of a single object can be taken from and dropped back into. | An object must be put into the bag to become the source object.
Notecard {: #Notecard } | `Notecard` | An editable notecard. |
Quarter {: #Quarter } | `Coin` | An american quarter minted in 1942. | Spawns tails-up, facing to the right.
reversi_chip {: #reversi_chip } | `Generic` | A dual-colored Reversi chip. | Spawns white-side up.
Tablet {: #Tablet } | `Tablet` | A tablet that displays a webpage. |

### Zones

Name | Type | Description
-- | -- | --
FogOfWar {: #FogOfWar } | `Fog` | A [Fog of War Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#fog-of-war-zone).
FogOfWarTrigger {: #FogOfWarTrigger } | `FogOfWar` | A [Hidden Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#hidden-zone).
HandTrigger {: #HandTrigger } | `Hand` | A [Hand Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#hand-zone).
LayoutZone {: #LayoutZone } | `Layout` | A [Layout Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#layout-zone).
RandomizeTrigger {: #RandomizeTrigger } | `Randomize` | A [Randomize Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#randomize-zone).
ScriptingTrigger {: #ScriptingTrigger } | `Scripting` | A [Scripting Zone](https://kb.tabletopsimulator.com/game-tools/zone-tools/#scripting-zone).

## Spawnable Names

When using [`spawnObject()`](base.md#spawnobject), the `type` parameter can be any of the above object types, or any of the below names, which spawns an object of a certain type, and with certain properties different from default.

Alternate&nbsp;Name | Object | Differences
-- | -- | --
Arms Dice {: #Arms-Dice } | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `0`.
Backgammon Board {: #Backgammon-Board } | [`backgammon_board`](#backgammon_board) | Snaps to table level immediately upon spawn.
Barrel {: #Barrel } | [`Tileset_Barrel`](#Tileset_Barrel) | *(none)*
Bear {: #Bear } | [`rpg_BEAR`](#rpg_BEAR) | *(none)*
Bishop Cast Iron {: #Bishop-Cast-Iron } | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `1`.
Bishop Chrome {: #Bishop-Chrome } | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `0`.
Bishop Dark Wood {: #Bishop-Dark-Wood } | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `3`.
Bishop Light Wood {: #Bishop-Light-Wood } | [`Chess_Bishop`](#Chess_Bishop) | `MaterialIndex` of `2`.
Black Ball {: #Black-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `6`.
Black Checker {: #Black-Checker } | [`Checker_black`](#Checker_black) | *(none)*
Black Pawn {: #Black-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `8`.
Blue 10 {: #Blue-10 } | [`Chip_10`](#Chip_10) | *(none)*
Blue Ball {: #Blue-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `4`.
Blue Pawn {: #Blue-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `5`.
Blue Rectangle {: #Blue-Rectangle } | [`BlockRectangle`](#BlockRectangle) | *(none)*
Brown Backgammon {: #Brown-Backgammon } | [`backgammon_piece_brown`](#backgammon_piece_brown) | *(none)*
CardBot {: #CardBot } | [`Figurine_Card_Bot`](#Figurine_Card_Bot) | *(none)*
CardBots Head Deck {: #CardBots-Head-Deck } | [`Deck_CardBot_Head`](#Deck_CardBot_Head) | *(none)*
CardBots Main Deck {: #CardBots-Main-Deck } | [`Deck_CardBot_Main`](#Deck_CardBot_Main) | *(none)*
Chair {: #Chair } | [`Tileset_Chair`](#Tileset_Chair) | *(none)*
Checkers Board {: #Checkers-Board } | [`Checker_Board`](#Checker_Board) | Snaps to table level immediately upon spawn.
Chess Board {: #Chess-Board } | [`Chess_Board`](#Chess_Board) | Snaps to table level immediately upon spawn.
Chest {: #Chest } | [`Tileset_Chest`](#Tileset_Chest) | *(none)*
Chimera {: #Chimera } | [`rpg_CHIMERA`](#rpg_CHIMERA) | *(none)*
Chinese Checkers Board {: #Chinese-Checkers-Board } | [`Chinese_Checkers_Board`](#Chinese_Checkers_Board) | Snaps to table level immediately upon spawn.
Corner {: #Corner } | [`Tileset_Corner`](#Tileset_Corner) | *(none)*
Crowns Dice {: #Crowns-Dice } | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `1`.
Custom Board {: #Custom-Board } | [`Custom_Board`](custom-game-objects.md#custom-board) | Snaps to table level immediately upon spawn.
Custom Deck {: #Custom-Deck } | [`DeckCustom`](custom-game-objects.md#custom-deck) | *(none)*
Custom Figurine {: #Custom-Figurine } | [`Figurine_Custom`](custom-game-objects.md#custom-figurine) | *(none)*
Custom Model {: #Custom-Model } | [`Custom_Model`](custom-game-objects.md#custom-model) | *(none)*
Cyclops {: #Cyclops } | [`rpg_CYCLOP`](#rpg_CYCLOP) | *(none)*
D10 {: #D10 } | [`Die_10`](#Die_10) | `MaterialIndex` of `0`.
D10 Chrome {: #D10-Chrome } | [`Die_10`](#Die_10) | `MaterialIndex` of `1`, `AltSound` of `true`.
D12 {: #D12 } | [`Die_12`](#Die_12) | `MaterialIndex` of `0`.
D12 Chrome {: #D12-Chrome } | [`Die_12`](#Die_12) | `MaterialIndex` of `1`, `AltSound` of `true`.
D20 {: #D20 } | [`Die_20`](#Die_20) | `MaterialIndex` of `0`.
D20 Chrome {: #D20-Chrome } | [`Die_20`](#Die_20) | `MaterialIndex` of `1`, `AltSound` of `true`.
D4 {: #D4 } | [`Die_4`](#Die_4) | `MaterialIndex` of `0`.
D4 Chrome {: #D4-Chrome } | [`Die_4`](#Die_4) | `MaterialIndex` of `1`, `AltSound` of `true`.
D6 {: #D6 } | [`Die_6`](#Die_6) | `MaterialIndex` of `0`.
D6 Black {: #D6-Black } | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `0`.
D6 Blue {: #D6-Blue } | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `3`.
D6 Chrome {: #D6-Chrome } | [`Die_6`](#Die_6) | `MaterialIndex` of `1`, `AltSound` of `true`.
D6 Green {: #D6-Green } | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `2`.
D6 Red {: #D6-Red } | [`Die_6_Rounded`](#Die_6_Rounded) | `MaterialIndex` of `1`.
D8 {: #D8 } | [`Die_8`](#Die_8) | `MaterialIndex` of `0`.
D8 Chrome {: #D8-Chrome } | [`Die_8`](#Die_8) | `MaterialIndex` of `1`, `AltSound` of `true`.
Digital Clock {: #Digital-Clock } | [`Digital_Clock`](#Digital_Clock) | *(none)*
Dragonide {: #Dragonide } | [`rpg_DRAGONIDE`](#rpg_DRAGONIDE) | *(none)*
Evil Watcher {: #Evil-Watcher } | [`rpg_EVIL_WATCHER`](#rpg_EVIL_WATCHER) | *(none)*
Floor {: #Floor } | [`Tileset_Floor`](#Tileset_Floor) | *(none)*
Ghoul {: #Ghoul } | [`rpg_GHOUL`](#rpg_GHOUL) | *(none)*
Giant Rat {: #Giant-Rat } | [`rpg_RAT`](#rpg_RAT) | *(none)*
Giant Viper {: #Giant-Viper } | [`rpg_GIANT_VIPER`](#rpg_GIANT_VIPER) | *(none)*
Go Board {: #Go-Board } | [`Go_Board`](#Go_Board) | Snaps to table level immediately upon spawn.
GO Bowl Black {: #GO-Bowl-Black } | [`go_game_bowl_black`](#go_game_bowl_black) | *(none)*
GO Bowl White {: #GO-Bowl-White } | [`go_game_bowl_white`](#go_game_bowl_white) | *(none)*
GO Piece Black {: #GO-Piece-Black } | [`go_game_piece_black`](#go_game_piece_black) | *(none)*
GO Piece White {: #GO-Piece-White } | [`go_game_piece_white`](#go_game_piece_white) | *(none)*
Goblin {: #Goblin } | [`rpg_GOBLIN`](#rpg_GOBLIN) | *(none)*
Gold 1000 {: #Gold-1000 } | [`Chip_1000`](#Chip_1000) | *(none)*
Golem {: #Golem } | [`rpg_GOLEM`](#rpg_GOLEM) | *(none)*
Green 50 {: #Green-50 } | [`Chip_50`](#Chip_50) | *(none)*
Green Ball {: #Green-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `3`.
Green Pawn {: #Green-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `4`.
Green Triangle {: #Green-Triangle } | [`BlockTriangle`](#BlockTriangle) | *(none)*
Griffon {: #Griffon } | [`rpg_GRIFFON`](#rpg_GRIFFON) | *(none)*
Hydra {: #Hydra } | [`rpg_HYDRA`](#rpg_HYDRA) | *(none)*
Joker {: #Joker } | [`Card`](#Card) | `CardID` of `52`.
Kimi Kat {: #Kimi-Kat } | [`Figurine_Kimi_Kat`](#Figurine_Kimi_Kat) | *(none)*
King Cast Iron {: #King-Cast-Iron } | [`Chess_King`](#Chess_King) | `MaterialIndex` of `1`.
King Chrome {: #King-Chrome } | [`Chess_King`](#Chess_King) | `MaterialIndex` of `0`.
King Dark Wood {: #King-Dark-Wood } | [`Chess_King`](#Chess_King) | `MaterialIndex` of `3`.
King Light Wood {: #King-Light-Wood } | [`Chess_King`](#Chess_King) | `MaterialIndex` of `2`.
Knight Cast Iron {: #Knight-Cast-Iron } | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `1`.
Knight Chrome {: #Knight-Chrome } | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `0`.
Knight Dark Wood {: #Knight-Dark-Wood } | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `3`.
Knight Light Wood {: #Knight-Light-Wood } | [`Chess_Knight`](#Chess_Knight) | `MaterialIndex` of `2`.
Knight of Knil {: #Knight-of-Knil } | [`Figurine_Knil`](#Figurine_Knil) | *(none)*
Kobold {: #Kobold } | [`rpg_KOBOLD`](#rpg_KOBOLD) | *(none)*
Lizard Warrior {: #Lizard-Warrior } | [`rpg_LIZARD_WARRIOR`](#rpg_LIZARD_WARRIOR) | *(none)*
Loot Bag {: #Loot-Bag } | [`Bag`](#Bag) | *(none)*
Manticora {: #Manticora } | [`rpg_MANTICORA`](#rpg_MANTICORA) | *(none)*
Mara {: #Mara } | [`Figurine_Mara`](#Figurine_Mara) | *(none)*
Moons Dice {: #Moons-Dice } | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `2`.
Mummy {: #Mummy } | [`rpg_MUMMY`](#rpg_MUMMY) | *(none)*
Ogre {: #Ogre } | [`rpg_OGRE`](#rpg_OGRE) | *(none)*
Orange Pawn {: #Orange-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `2`.
Orc {: #Orc } | [`rpg_ORC`](#rpg_ORC) | *(none)*
Pachisi Board {: #Pachisi-Board } | [`Pachisi_board`](#Pachisi_board) | Snaps to table level immediately upon spawn.
Pawn Cast Iron {: #Pawn-Cast-Iron } | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `1`.
Pawn Chrome {: #Pawn-Chrome } | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `0`.
Pawn Dark Wood {: #Pawn-Dark-Wood } | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `3`.
Pawn Light Wood {: #Pawn-Light-Wood } | [`Chess_Pawn`](#Chess_Pawn) | `MaterialIndex` of `2`.
Pink Ball {: #Pink-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `5`.
Pink Pawn {: #Pink-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `7`.
Purple Pawn {: #Purple-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `6`.
Quarter {: #Quarter } | [`Quarter`](#Quarter) | *(none)*
Queen Cast Iron {: #Queen-Cast-Iron } | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `1`.
Queen Chrome {: #Queen-Chrome } | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `0`.
Queen Dark Wood {: #Queen-Dark-Wood } | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `3`.
Queen Light Wood {: #Queen-Light-Wood } | [`Chess_Queen`](#Chess_Queen) | `MaterialIndex` of `2`.
Random Card {: #Random-Card } | [`Card`](#Card) | Random `CardID` between `0` and `51` (inclusive).
Random Domino {: #Random-Domino } | [`Domino`](#Domino) | Random `MeshIndex` between `0` and `27` (inclusive).
Random Mahjong {: #Random-Mahjong } | [`Mahjong_Tile`](#Mahjong_Tile) | Random `MeshIndex` between `0` and `35` (inclusive).
Red 100 {: #Red-100 } | [`Chip_100`](#Chip_100) | *(none)*
Red Ball {: #Red-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `1`.
Red Checker {: #Red-Checker } | [`Checker_red`](#Checker_red) | *(none)*
Red Pawn {: #Red-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `1`.
Red Square {: #Red-Square } | [`BlockSquare`](#BlockSquare) | *(none)*
Reversi Board {: #Reversi-Board } | [`reversi_board`](#reversi_board) | Snaps to table level immediately upon spawn.
Reversi Chip {: #Reversi-Chip } | [`reversi_chip`](#reversi_chip) | *(none)*
Rock {: #Rock } | [`Tileset_Rock`](#Tileset_Rock) | *(none)*
Rook Cast Iron {: #Rook-Cast-Iron } | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `1`.
Rook Chrome {: #Rook-Chrome } | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `0`.
Rook Dark Wood {: #Rook-Dark-Wood } | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `3`.
Rook Light Wood {: #Rook-Light-Wood } | [`Chess_Rook`](#Chess_Rook) | `MaterialIndex` of `2`.
Silver 500 {: #Silver-500 } | [`Chip_500`](#Chip_500) | *(none)*
Sir Loin {: #Sir-Loin } | [`Figurine_Sir_Loin`](#Figurine_Sir_Loin) | *(none)*
Skeleton Knight {: #Skeleton-Knight } | [`rpg_SKELETON_KNIGHT`](#rpg_SKELETON_KNIGHT) | *(none)*
Standard Deck {: #Standard-Deck } | [`Deck`](#Deck) | *(none)*
Suns Dice {: #Suns-Dice } | [`Die_Piecepack`](#Die_Piecepack) | `MaterialIndex` of `3`.
Table {: #Table } | [`Tileset_Table`](#Tileset_Table) | *(none)*
Tree {: #Tree } | [`Tileset_Tree`](#Tileset_Tree) | *(none)*
Tree Ent {: #Tree-Ent } | [`rpg_TREE_ENT`](#rpg_TREE_ENT) | *(none)*
Troll {: #Troll } | [`rpg_TROLL`](#rpg_TROLL) | *(none)*
Vampire {: #Vampire } | [`rpg_VAMPIRE`](#rpg_VAMPIRE) | *(none)*
Wall {: #Wall } | [`Tileset_Wall`](#Tileset_Wall) | *(none)*
Werewolf {: #Werewolf } | [`rpg_WEREWOLF`](#rpg_WEREWOLF) | *(none)*
White Backgammon {: #White-Backgammon } | [`backgammon_piece_white`](#backgammon_piece_white) | *(none)*
White Ball {: #White-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `0`.
White Checker {: #White-Checker } | [`Checker_white`](#Checker_white) | *(none)*
White Pawn {: #White-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `0`.
Wolf {: #Wolf } | [`rpg_WOLF`](#rpg_WOLF) | *(none)*
Wyvern {: #Wyvern } | [`rpg_WYVERN`](#rpg_WYVERN) | *(none)*
Yellow Ball {: #Yellow-Ball } | [`Chinese_Checkers_Piece`](#Chinese_Checkers_Piece) | `MaterialIndex` of `2`.
Yellow Pawn {: #Yellow-Pawn } | [`PlayerPawn`](#PlayerPawn) | `MaterialIndex` of `3`.
Zeke Kodoku {: #Zeke-Kodoku } | [`Figurine_Zeke`](#Figurine_Zeke) | *(none)*
Zomblor {: #Zomblor } | [`Figurine_Zomblor`](#Figurine_Zomblor) | *(none)*
