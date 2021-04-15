The LayoutZone behavior is present on [Layout Zones](https://kb.tabletopsimulator.com/game-tools/zone-tools/#layout-zone).

## Functions {: data-toc-sort }

Function Name | Return | Description
-- | -- | --
getOptions() {: #getoptions data-toc-label="getOptions()" data-toc-child-of="functions" } | [<span class="ret tab"></span>](../types.md) | Returns the layout zones [options](#options).
layout() {: #layout data-toc-label="layout()" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Causes the layout zone to (re)layout.
setOptions([<span class="tag tab"></span>](../types.md) options) {: #setoptions data-toc-label="setOptions(...)" data-toc-child-of="functions" } | [<span class="ret boo"></span>](../types.md) | Sets the layout zone's [options](#options). If an option is not included in the table, then the zone's value for that option will remain unchanged.

!!!example
    Log a layout zone's options.
    ```lua
    log(zone.LayoutZone.getOptions())
    ```

## Options

Layout zone option tables may contain the following properties.

Name | Type | Description
-- | -- | --
allow_swapping {: #allow_swapping } | [<span class="tag boo"></span>](../types.md) | When moving an object from one full group to another, the object you drop on will be moved to the original group.
alternate_direction {: #alternate_direction } | [<span class="tag boo"></span>](../types.md) | Objects added to a group will be aligned up or right, different from the preceding object in the group.  Used, for example, in trick-taking games to make counting easier.
cards_per_deck {: #cards_per_deck } | [<span class="tag int"></span>](../types.md) | Sets the size of decks made by the layout zone when it combines newly added cards.
combine_into_decks {: #combine_into_decks } | [<span class="tag boo"></span>](../types.md) | Whether cards added to the zone should be combined into decks.  You may specify the number of cards per deck.
direction {: #direction } | [<span class="tag int"></span>](../types.md) | The directions the groups in the zone expand into.  This will determine the origin corner.
horizontal_group_padding {: #horizontal_group_padding } | [<span class="tag flo"></span>](../types.md) | How much horizontal space is inserted between groups.
horizontal_spread {: #horizontal_spread } | [<span class="tag flo"></span>](../types.md) | How far each object in a group is moved horizontally from the previous object.
instant_refill {: #instant_refill } | [<span class="tag boo"></span>](../types.md) | When enabled, if ever a group is picked up or removed the rest of the layout will trigger to fill in the gap
manual_only {: #manual_only } | [<span class="tag boo"></span>](../types.md) | The zone will not automatically lay out objects: it must be triggered manually.
max_objects_per_group {: #max_objects_per_group } | [<span class="tag int"></span>](../types.md) | Each group in the zone may not contain more than this number of objects.
max_objects_per_new_group {: #max_objects_per_new_group } | [<span class="tag int"></span>](../types.md) | When new objects are added to a zone, they will be gathered into groups of this many objects.
meld_direction {: #meld_direction } | [<span class="tag int"></span>](../types.md) | The direction the objects within a group will expand into.
meld_reverse_sort {: #meld_reverse_sort } | [<span class="tag boo"></span>](../types.md) | When enabled the sort order inside a group is reversed
meld_sort {: #meld_sort } | [<span class="tag int"></span>](../types.md) | How groups are sorted internally.
meld_sort_existing {: #meld_sort_existing } | [<span class="tag boo"></span>](../types.md) | When enabled all groups will be sorted when laid out, rather than only newly added groups.
new_object_facing {: #new_object_facing } | [<span class="tag int"></span>](../types.md) | Determines whether newly added objects are turned face-up or face-down.
randomize {: #randomize } | [<span class="tag boo"></span>](../types.md) | Objects will be randomized whenever they are laid out
split_added_decks {: #split_added_decks } | [<span class="tag boo"></span>](../types.md) | Decks added to the zone will be split into their individual cards.
sticky_cards {: #sticky_cards } | [<span class="tag boo"></span>](../types.md) | When picked up, cards above the grabbed card will also be lifted.
trigger_for_face_down {: #trigger_for_face_down } | [<span class="tag boo"></span>](../types.md) | Face-Down objects dropped on zone will be laid out.
trigger_for_face_up {: #trigger_for_face_up } | [<span class="tag boo"></span>](../types.md) | Face-Up objects dropped on zone will be laid out.
trigger_for_non_cards {: #trigger_for_non_cards } | [<span class="tag boo"></span>](../types.md) | Non-card objects dropped on zone will be laid out
vertical_group_padding {: #vertical_group_padding } | [<span class="tag flo"></span>](../types.md) | How much vertical space is inserted between groups.
vertical_spread {: #vertical_spread } | [<span class="tag flo"></span>](../types.md) | How far each object in a group is moved vertically from the previous object.
