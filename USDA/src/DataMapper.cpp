// Robin Kalia
// robinkalia@berkeley.edu
// HydroBase
//
// DataMapper.cpp: Definition of methods and data memebers of the DataMapper Class

#include "DataMapper.h"

#include <sstream>
#include <string.h>
#include <stdint.h>

DataMapper::DataMapper()
{

}


DataMapper::~DataMapper()
{

}


void DataMapper::GenerateDataMap(std::ifstream &file_stream, std::map<std::string, std::map<std::string, std::string> > &plant_map)
{
    plant_map.clear();
    std::vector<std::string> plant_attributes;

    std::string line, item, token;
    std::getline(file_stream, line);

    char *pch = NULL;
    pch = strtok(strdup(line.c_str()),",");
    int32_t token_count = -1;

    while (pch != NULL)
    {
        if (token_count >= 0) {
            token = std::string(pch);
            plant_attributes.push_back(token);
        }

        pch = strtok(NULL, ",");
        ++token_count;
    }

    while(std::getline(file_stream, line))
    {
        pch = strtok(strdup(line.c_str()), ",");
        if (pch != NULL)    item = std::string(pch); 
        
        int32_t token_count = -1;
        std::map<std::string, std::string> item_value_map;
        while (pch != NULL)
        {
            if (token_count >= 0) {
                token = std::string(pch);
                item_value_map.insert(std::pair<std::string, std::string>(plant_attributes[token_count],token));
            }

            pch = strtok(NULL, ",");
            ++token_count;
        }
        
        std::pair<std::string, std::map<std::string, std::string> > plant_item(item, item_value_map);
        plant_map.insert(plant_item);
    }
}
