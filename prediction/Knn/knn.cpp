#include "utils.hpp"
#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

    int main(){


        tuple<vector<pair<string, vector<float>>>, vector<int>> dataset = read_csv("../datasets/dataset.csv");
        vector<pair<string, vector<float>>> test_dataset = read_test_csv("../datasets/test.csv");
        vector<pair<string, vector<float>>> values = get<0>(dataset);
        vector<int> team_number_dataset = get<1>(dataset);
        int columns = values.size();
        int n_lines_dataset = values.at(0).second.size();
        int n_test_lines = test_dataset.at(0).second.size();
        vector<vector<float>> dataset_values(n_lines_dataset, vector<float> (columns, 0)),
            test_lines(n_lines_dataset, vector<float> (columns, 0));

        vector<int> team_number_test(n_test_lines, 0);  
        vector<float> line(columns, 0);

        for(int i = 0; i < n_lines_dataset; i++)
        {   
            for(int j = 1; j < columns; j++)
            {
                dataset_values[i][j-1] = values[j].second[i];
                test_lines[i][j-1] = test_dataset[j].second[i];
            }
        }
        for(int i = 0; i < n_test_lines; i++)
        {
            line = test_lines[i];
            int prediction = nearest_neighbour(line, dataset_values);
            team_number_test[i] = team_number_dataset[prediction];
        }
        write_csv(test_dataset, team_number_test, "../datasets/new_dataset.csv");
        
        
        return 0;
    }

