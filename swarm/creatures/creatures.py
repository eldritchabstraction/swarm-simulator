import json
import pdb

class Creature():
    def __init__(self, json_creature, creature):
        # all creatures can either mine meat or territory
        self.meat_mine = int(json_creature["meat_mine"])
        self.terr_mine = int(json_creature["terr_mine"])
        self.meat_cost = int(json_creature["meat_cost"])
        self.quantity = int(json_creature["quantity"])
        self.type = str(creature)

    def __str__(self):
        return "Creature type: %s\nQuantity: %d" % (self.type, self. quantity)

class Swarm():
    def __init__(self):
        # when you initialize a swarm, you should get a table of creatures and their respective quantities
        f = open("creatures.json", "r")
        # eldr: we've got the root object in the json definition
        root = json.load(f)
        f.close()

        # create a list of creature objects
        self.creatures = []
        for creature in root["creatures"]:
            self.creatures.append(Creature(root["creatures"][creature], creature))

    def __str__(self):
        return_string = ""
        for creature in self.creatures:
            return_string = return_string + creature.__str__() + "\n"
        return return_string

def test():
    # instantiate a swarm
    print Swarm()

if __name__ == "__main__":
    test()