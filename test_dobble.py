from unittest import TestCase
from double_generator import kartenlistenersteller, uberpruefe, uberpruefe_2

class Doublekartenchecker(TestCase):
    def test_jedes_icon_nur_einmal(self):
        try:
            lischte = [[1,2,3,4,5,6,7], [2,8,9,10,11,12,13], [3,8,14,16,17,18,19]]
            uberpruefe(lischte)
        except:
            self.fail()

    def test_keis_Item_stimmt(self):
        try:
            lischte = [[1,81,3,4,5,6,7], [2,8,9,10,11,12,13], [91,78,14,16,17,18,19]]
            uberpruefe(lischte)
        except(Warning):
            pass
        else:
            self.fail()

    def test_zwei_Item_stimmt(self):
        try:
            lischte = [[1,2,3,4,5,6,7], [2,1,9,10,11,12,13], [91,78,14,16,17,18,19]]
            uberpruefe(lischte)
        except(Warning):
            pass
        else:
            self.fail()

    def test_jedes_icon_nur_einmal_2(self):
        try:
            lischte = [[1,2,3,4,5,6,7], [2,8,9,10,11,12,13], [3,8,14,16,17,18,19]]
            uberpruefe_2(lischte)
        except:
            self.fail()

    def test_keis_Item_stimmt_2(self):
        try:
            lischte = [[1,81,3,4,5,6,7], [2,8,9,10,11,12,13], [91,78,14,16,17,18,19]]
            uberpruefe_2(lischte)
        except(Warning):
            pass
        else:
            self.fail()

    def test_zwei_Item_stimmt_2(self):
        try:
            lischte = [[1,2,3,4,5,6,7], [2,1,9,10,11,12,13], [91,78,14,16,17,18,19]]
            uberpruefe_2(lischte)
        except(Warning):
            pass
        else:
            self.fail()

