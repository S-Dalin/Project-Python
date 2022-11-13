# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:07:29 2022

@author: Lisa,Dalin,Deva,Wenyao
"""

from abc import ABC, abstractmethod
from enum import Enum
import pandas as pd
from pandas.io.formats.format import common_docstring

# Class Descriable
class Descriable(ABC):
    def __init__(self):
        pass 

    @staticmethod
    def describe():
        pass

#Class Unit
class Unit(Descriable):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def describle():
        pass


#INDICATOR Group in Enumerate     
class IndicatorGroup (Enum) : 
    PRICES = 1
    SUPPLY_AND_USE = 2 
    EXPORTS_AND_IMPORTS = 3
    TRANSPORTATION = 4
    ANIMAL_UNIT_INDEXES = 5
    QUANTITIES_FED = 6
    FEED_PRICE_RATIOS = 7

#COMMODITY Group in Enumerate     
class CommodityGroup (Enum) :
    ANIMAL_PROTEIN_FEEDS = 8
    BARLEY = 9
    BYPRODUCT_FEEDS = 10
    COARSE_GRAINS = 11
    CORN = 12
    ENERGY_FEEDS = 13
    FEED_GRAINS = 14
    GRAIN_PROTEIN_FEEDS = 15
    HAY = 16
    OATS = 17
    OTHER = 18
    PROCESSED_FEEDS = 19
    SORGHUM = 20

#Class Indicator ###
class Indicator(Descriable):
    def __init__(self, id : str, frequency : int, frequencyDesc : str, geogLocation : str, indicatorGroup : IndicatorGroup, unit : Unit) :
        self.id  = id #Attributé Public +
        self.__frequency = frequency #Attributs privés -, toujours avec __ en préfixe
        self.__frequencyDesc = frequencyDesc #Attributs privés -
        self.__geogLocation = geogLocation #Attributs privés -
        self.__indicatorGroup = indicatorGroup #Attributs privés -
        self.__unit = unit #Attributs privés -
        

#Class Commodity
class Commodity(Descriable):
    def __init__(self,group:CommodityGroup,id:int,name:str):
        self.id = id #Attributé Public +
        self.__name = name #Attributs privés -
        self.__group = group #Attributs privés -

#Class Measurement
class Measurement(Descriable):
    def __init__(self, id:int, year:int ,value:float,timeperiodId:int, timeperiodDesc:str, commodity:Commodity, indicator:Indicator):
        self.id = id #Attributé Public +
        self.__year = year 
        self.__value = value
        self.__timeperiodId = timeperiodId
        self.__timeperiodDesc = timeperiodDesc
        self.__commodity = commodity #Attributs privés -
        self.__indicator = indicator


#Class Volume
class Volume(Unit):
    def __init__(self,id: int, name: str = "Volume"):
        super().__init__()
        self.__id=id
        self.__name=name
    
    def describle():
        pass


#Class Price
class Price(Unit):
    def __init__(self,id: int, name: str = "Price"):
        super().__init__()
        self.__id=id
        self.__name=name

    def describle():
        pass

#When you initialize a child class in Python, you can call the super(). __init__() method. This initializes the parent class object into the child class. In addition to this, you can add child-specific information to the child object as well.

#Class Weight 
class Weight(Unit):
    def __init__(self, id: int,  multiplier: float,name: str = "Weight"):
        super().__init__()
        self.id = id 
        self.__multiplier = multiplier
        self.__name=name

    def describle():
        pass

#Class Surface
class Surface(Unit):
    def __init__(self, id: int, name: str = "Surface"):
        super().__init__()
        self.__id=id
        self.__name=name
    
    def describle():
        pass

#Class Count
class Count(Unit):
    def __init__(self, id: int, what: str, name: str = "Count"):
        super().__init__()
        self.id=id
        self.__name=name
        self.__what = what

    def describle():
        pass

#Class Ratio
class Ratio(Unit):
    def __init__(self, id: int, name: str = "Ratio"):
        super().__init__()
        self.id=id
        self.__name=name
       
    def describle():
        pass
    


# FoodCropFactory ###
class FoodCropFactory():
    def __init__(self):
        self.__unitsRegistry={}
        self.__indicatorsRegistry={}
        self.__commodityRegistry={}
        

    def createVolume(self, id:int, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Volume(id,name)
        return self.__unitsRegistry[id]

    def createPrice(self, id:int, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Price(id,name)
        return self.__unitsRegistry[id]

    def createWeight(self, id:int, weight:float, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Weight(id,weight,name)
        return self.__unitsRegistry[id]

    def createSurface(self, id:int, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Surface(id,name)
        return self.__unitsRegistry[id]

    def createCount(self, id:int,  what:str, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Count(id,what,name)
        return self.__unitsRegistry[id]

    def createRatio(self, id:int, name:str):
        if(not(id in self.__unitsRegistry)):
            self.__unitsRegistry[id] = Ratio(id,name)
        return self.__unitsRegistry[id]

    def createIndicator(self, id:int, frequency:int, freqDesc:str, geogLocation:str, indicatorGroup: IndicatorGroup, unit:Unit):
        if(not (id in self.__indicatorsRegistry)):
            self.__indicatorsRegistry[id] = Indicator(id,frequency,freqDesc,geogLocation,indicatorGroup,unit)
        return self.__indicatorsRegistry[id]

    def createCommodity(self , group:CommodityGroup , id:int, name:str):
        if(not (id in self.__commodityRegistry)):
            self.__commodityRegistry[id]=Commodity(group,id,name)
        return self.__commodityRegistry[id]

    def createMeasurement(self, id:int, year:int, value:float, timeperiodId:int, timeperiodDesc:str, commodity: Commodity, indicator:Indicator):
        return Measurement(id,year,value,timeperiodId,timeperiodDesc,commodity,indicator)



#Class FoodCropsDataset
class FoodCropsDataset(): 
    def __init__(self):
        self.__commodityGroupMeasurementIndex = {}
        self.__indicatorGroupMeasurement = {}
        self.__locationMeasurementIndex = {}
        self.__unitMeasurement = {}
        self.unitDictionary = {
            "Price" : ["Dollars"],
            "Weight" : ["ton","tons"],
            "Volume" : ["bushels","Bushels","bushel","Gallons","liters"],
            "Surface" : ["hectares","acres"],
            "Ratio" : ["Ratio"],
            "Count" : ["Index","Carloads","Cents","animal"]
        }
        self.factory = FoodCropFactory()

    def load(self, datasetPath:str):
        dataframe = pd.read_csv(datasetPath)
        for index,row in dataframe.iterrows():
            #Instantion d'un objet de la classe Commodity
            try:

                groupCommod = CommodityGroup[str(row['SC_GroupCommod_Desc']).replace(" ","_").upper()]
            except KeyError:
                groupCommod = CommodityGroup["OTHER"]
            commodity =  self.factory.createCommodity(groupCommod,row['SC_Commodity_ID'],row['SC_Commodity_Desc'])


            for key,value in self.unitDictionary.items():
                unitFound = False
                for item in value:
                    if item in str(row['SC_Unit_Desc']):
                        if(key == "Price"):
                            unit=self.factory.createPrice(row['SC_Unit_ID'],row['SC_Unit_Desc'])
                            unitFound=True
                            break
                        elif(key == "Weight"):
                            multiplier=1
                            for x in str(row['SC_Unit_Desc']).split():
                                if x.isdigit():
                                    multiplier=x
                            unit = self.factory.createWeight(row['SC_Unit_ID'],x,row['SC_Unit_Desc'])
                            unitFound = True
                            break
                        elif(key == "Volume"):
                            unit = self.factory.createVolume(row['SC_Unit_ID'],row['SC_Unit_Desc'])
                            unitFound = True
                            break
                        elif(key == "Surface"):
                            unit = self.factory.createSurface(row['SC_Unit_ID'],row['SC_Unit_Desc'])
                            unitFound = True
                            break
                        elif(key == "Ratio"):
                            unit = self.factory.createRatio(row['SC_Unit_ID'],row['SC_Unit_Desc'])
                            unitFound = True
                            break
                        elif(key == "Count"):
                            unit = self.factory.createCount(row['SC_Unit_ID'],"Il s'agit d'une grandeur sans unité permettant de connaitre le nombre ou la quantité",row['SC_Unit_Desc'])
                            unitFound = True
                            break
                if(unitFound):
                    break

            #Instantiation d'un objet de la classe Indicator 
            """
            Mais avant cela, on reformate correctement la valeur lue à partir du fichier .csv afin qu'elle corresponde au format des clés du dictionnaire IndicatorGroup
            """
            indicatorGroup = IndicatorGroup[str(row['SC_Group_Desc']).replace(" ","_").replace("-","_").upper()]
            indicator = self.factory.createIndicator(row['SC_Group_ID'],row['SC_Frequency_ID'],row['SC_Frequency_Desc'],row['SC_GeographyIndented_Desc'],indicatorGroup,unit)

            #Instantiation d'un Objet de type Measurement
            measurement = self.factory.createMeasurement(row['SC_Group_ID'],row['Year_ID'],row['Amount'],row['Timeperiod_ID'],row['Timeperiod_Desc'],commodity,indicator) 
            
            #Indexation de l'instance de measurement (nouvellement créée) par son CommodityGroup 
            measurementCommodityGroup=measurement._Measurement__commodity._Commodity__group
            if(not (measurementCommodityGroup in self.__commodityGroupMeasurementIndex)):
                self.__commodityGroupMeasurementIndex[measurementCommodityGroup]=[]  
            self.__commodityGroupMeasurementIndex[measurementCommodityGroup].append(measurement)

            #Indexation de l'instance de measurement (nouvellement créée) par son IndicatorGroup
            measurementIndicatorGroup=measurement._Measurement__indicator._Indicator__indicatorGroup
            if(not (measurementIndicatorGroup in self.__indicatorGroupMeasurement)):
                self.__indicatorGroupMeasurement[measurementIndicatorGroup]=[]  
            self.__indicatorGroupMeasurement[measurementIndicatorGroup].append(measurement) 

            #Indexation de l'instance de measurement (nouvellement créée) par sa zone géographique
            measurementGeogLocation=measurement._Measurement__indicator._Indicator__geogLocation
            if(not (measurementGeogLocation in self.__locationMeasurementIndex)):
                self.__locationMeasurementIndex[measurementGeogLocation]=[]  
            self.__locationMeasurementIndex[measurementGeogLocation].append(measurement)

            #Indexation de l'instance de measurement (nouvellement créée) par son unité
            #D'abord on vérifie dequel unité il s'agit
            if(isinstance(measurement._Measurement__indicator._Indicator__unit, Price)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Price__name
            elif(isinstance(measurement._Measurement__indicator._Indicator__unit, Volume)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Volume__name
            elif(isinstance(measurement._Measurement__indicator._Indicator__unit, Surface)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Surface__name
            elif(isinstance(measurement._Measurement__indicator._Indicator__unit, Ratio)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Ratio__name
            elif(isinstance(measurement._Measurement__indicator._Indicator__unit, Count)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Count__name
            elif(isinstance(measurement._Measurement__indicator._Indicator__unit, Weight)):
                measurementUnit = measurement._Measurement__indicator._Indicator__unit._Weight__name
  
            if(not (measurementUnit in self.__unitMeasurement)) :
                self.__unitMeasurement[measurementUnit]=[]  
            self.__unitMeasurement[measurementUnit].append(measurement)  
        
    
    def findMeasurement(self,comodityType: CommodityGroup, indicatorGroup : IndicatorGroup, geographicalLocation: str, unit: Unit):
        #result1 CommodityGroup
        result1 = [item for item in self.__commodityGroupMeasurementIndex[comodityType] ]

        #Intersection result1 and IndicatorGroup
        result2 = [item for item in result1 if item in self._Measurement__indicator[indicatorGroup]]

        #Intersection result2 and geographicalLocation
        result3 = [item for item in result2 if item in self._locationMeasurementIndex[geographicalLocation]]

        #Intersection result3 and unit
        resultFinal = [item for item in result3 if item.__unitMeasurement[unit.__name]]

        return resultFinal
    

if (__name__=="__main__"):

    foodCropsDataset=FoodCropsDataset()

    print("It will took sometimes")

    foodCropsDataset.load("FeedGrains.csv")

    print("\nyou are now can find with method \"findMeasurement\" !")