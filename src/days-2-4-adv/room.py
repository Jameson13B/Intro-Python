# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
  def __init__(self, name, description, items, is_light):
    self.name = name
    self.description = description
    self.itemList = items
    self.is_light = is_light