// Robin Kalia
// robinkalia@berkeley.edu
// HydroBase
//
// DataMapper.h: Class for converting USDA filtered data to a vector of Map data structure

#ifndef _HYDROBASE_DATA_USDA_DATAMAPPER_H
#define _HYDROBASE_DATA_USDA_DATAMAPPER_H

#include <iostream>

#include <fstream>

#include <vector>
#include <string>
#include <map>
#include <tuple>


class DataMapper {
private:
    

public:
    DataMapper();
    ~DataMapper();

    void GenerateDataMap(std::ifstream &file_stream, std::map<std::string, std::map<std::string, std::string> > &plant_map);
};

#endif      // _HYDROBASE_DATA_USDA_DATAMAPPER_H
