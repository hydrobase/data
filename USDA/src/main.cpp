// Robin Kalia
// robinkalia@berkeley.edu
// HydroBase
//
// main.cpp: Contains the interface to load data from a file in a map data structure


#include <iostream>
#include <stdio.h>

#include <stdint.h>

#include "DataMapper.h"

enum ERROR_CONSTANTS { ARGUMENT_ERROR = -2, LOGIC_ERROR = -1, NO_ERROR = 0 };

const int32_t DEBUG = 1;

int main(int argc, char* argv[])
{
    std::string plant_data_file;
    if (DEBUG) {
        plant_data_file = std::string("usda_plant2_filtered.csv");
    } else {
        if (argc != 2) {
            std::cout << "\n\tUsage:  ./datamapper <Data_File>\n\n";
            return ARGUMENT_ERROR;
        }
        
        plant_data_file = std::string(argv[1]);
    }

    std::ifstream file_stream(plant_data_file);
    if (!file_stream.is_open()) {
        std::cout << "\nError: Unable to open the file - " << plant_data_file << "\n\n";
        return LOGIC_ERROR;
    }

    DataMapper data_mapper;
    std::map<std::string, std::map<std::string, std::string> > plant_map;
    
    try {
        data_mapper.GenerateDataMap(file_stream, plant_map);
    } catch (const std::exception &ex) {
        std::cout << "\nCaught Error: " << ex.what() << std::endl;

        return LOGIC_ERROR;
    }

    return NO_ERROR;
}
