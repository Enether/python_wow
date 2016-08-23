"""
A Module that will take care of loading creatures that are in the Elwynn Forest zone
This is created so that we don't have to load the creatures every time we change zones AND
to have dead creatures stay dead, not be reloaded

the cs in cs_alive_monsters and similar names stands for Current Subzone
"""
from zones.zone import Zone, SubZone


class ElwynnForest(Zone):
    # the _map that shows us where we can go from our current subzone
    zone_map = {"Northshire Valley": ["Northshire Vineyards"],
                "Northshire Vineyards": ["Northshire Valley"]}
    zone_name = "Elwynn Forest"
    starter_subzone = "Northshire Valley"
    # dictionary that will hold the subzone class objects
    loaded_zones = {"Northshire Valley": None,
                    "Northshire Vineyards": None}

    def __init__(self):
        super().__init__()
        subzone_object = NorthshireValley(name="Northshire Valley", parent_zone_name=self.zone_name,
                                          zone_map=self.zone_map["Northshire Valley"])
        self.cs_alive_monsters, self.cs_monsters_guid_name_set = subzone_object.get_monsters()
        self.cs_alive_npcs, self.cs_npcs_guid_name_set = subzone_object.get_npcs()
        self.cs_available_quests = subzone_object.get_quests()
        self.cs_map = subzone_object.get_map_directions()
        self.curr_subzone = "Northshire Valley"
        self.loaded_zones["Northshire Valley"] = subzone_object

    def move_player(self, current_subzone: str, destination: str):
        """

        :param current_subzone: the subzone the character is in
        :param destination: the subzone he wants to go in
        :return: a boolean indicating if the move is possible
        """
        if current_subzone in self.zone_map.keys() and current_subzone == self.curr_subzone:

            if destination in self.zone_map[current_subzone] and destination in self.loaded_zones.keys():
                # Before moving:
                # update the information for our current in case we've killed monsters or done quests for example
                self._update_subzone_attributes(current_subzone)

                if not self.loaded_zones[destination]:  # if we don't have the destination's attributes loaded load them
                    self._load_zone(destination)

                self.curr_subzone = destination

                # We move, therefore update our attributes
                self._update_attributes(destination)
                return True

        else:
            raise Exception("The subzone is not in the zone_object!")

        return False

    def _load_zone(self, subzone: str):
        # if we have not loaded the zone before, we need to initialize it's class and put it in the loaded_zones
        if subzone == "Northshire Valley":
            self.loaded_zones[subzone] = NorthshireValley(name=subzone,
                                                          parent_zone_name=self.zone_name,
                                                          zone_map=self.zone_map[subzone])
        elif subzone == "Northshire Vineyards":
            self.loaded_zones[subzone] = NorthshireVineyards(name=subzone,
                                                             parent_zone_name=self.zone_name,
                                                             zone_map=self.zone_map[subzone])


class NorthshireValley(SubZone):
    pass


class NorthshireVineyards(SubZone):
    pass