# ifndef UTILS_CSV_H
# define UTILS_CSV_H

#include <fstream>
#include <sstream>
#include <iostream>
#include <utility>
#include <vector>
#include <tuple>
#include <math.h>
#include <limits>
#include <algorithm>

using namespace std;

float
norm_vector(vector<float> arr)
{
    float norm = 0;
    for(int i = 0; i < arr.size(); i++)
    {
        norm = norm + pow(arr[i], 2);
    }

    return (float)sqrt(norm);
}

tuple<vector<pair<string, vector<float>>>, vector<int>> read_csv(string filename)
{
    ifstream dataset(filename);

    // Create a vector of <string, int vector> pairs to store the result
    vector<pair<string, vector<float>>> result;
    vector<int> name, name_team;
    string line, colname;
    float val;
    if(dataset.good())
    {
        // Extract the first line in the file
        getline(dataset, line);

        // Create a stringstream from line
        stringstream ss(line);
        
        if(ss.peek() == ',') ss.ignore();
        // Extract each column name
        while(getline(ss, colname, ',')){
            // Initialize and add <colname, in            cout << colname << endl;t vector> pairs to result
            result.push_back({colname, vector<float> {}});
        }
    }
    int size = result.size();
    // Read data, line by line
    while(getline(dataset, line))
    {
        // Create a stringstream of the current line
        stringstream ss(line);
        
        // Keep track of the current column index
        int index = 0;
        
        // Extract each integer
        while(index < size){
            ss >> val;
            // Add the current integer to the 'index' column's values vector
            result.at(index).second.push_back(val);
            
            // If the next token is a comma, ignore it and move on
            if(ss.peek() == ',') ss.ignore();
            
            // Increment the column index
            index++;
        }
        ss >> val;
        name.push_back((int)val);
    }

    // Close file
    dataset.close();
    return make_tuple(result, name);
}

vector<pair<string, vector<float>>> read_test_csv(string filename)
{
    ifstream dataset(filename);

    // Create a vector of <string, int vector> pairs to store the result
    vector<pair<string, vector<float>>> result;
    string line, colname;
    float val;
    if(dataset.good())
    {
        // Extract the first line in the file
        getline(dataset, line);

        // Create a stringstream from line
        stringstream ss(line);
        
        // if(ss.peek() == ',') ss.ignore();
        // Extract each column name
        while(getline(ss, colname, ',')){
            // Initialize and add <colname, in            cout << colname << endl;t vector> pairs to result
            result.push_back({colname, vector<float> {}});
        }
    }
    int size = result.size();
    // Read data, line by line
    while(getline(dataset, line))
    {
        // Create a stringstream of the current line
        stringstream ss(line);
        
        // Keep track of the current column index
        int index = 0;
        
        // Extract each integer
        while(index < size){
            ss >> val;
            // Add the current integer to the 'index' column's values vector
            result.at(index).second.push_back(val);
            
            // If the next token is a comma, ignore it and move on
            if(ss.peek() == ',') ss.ignore();
            
            // Increment the column index
            index++;
        }
    }

    // Close file
    dataset.close();
    return result;
}

void
write_csv(vector<pair<string, vector<float>>> result,
    vector<int> name, string filename)
{
    ofstream output(filename);

    for(int j = 0; j < result.size(); j++)
    {
        output << result.at(j).first;
        if(j != result.size() - 1) 
            output << ","; // No comma at end of line
    }
    output << "\n";
    
    //Send data to the stream
    for(int i = 0; i < result.at(0).second.size(); ++i)
    {
        for(int j = 0; j < result.size(); ++j)
        {
            if(j < result.size() - 1){
                output << result.at(j).second.at(i); 
                output << ","; 
            }
            else
                output << name.at(i);
        }
        output << endl;
    }
    
    // Close the file
    output.close();
}

int
nearest_neighbour(vector <float> line, vector<vector<float>> dataset)
{
    int index_best;
    int better_distance = numeric_limits<int>::max();
    vector<float> diff(line.size()); 
    for(int i = 0; i < dataset.size(); i++)
    {
        transform(line.begin(), line.end(), dataset[i].begin(), diff.begin(), minus<float>());
        float norm = norm_vector(diff);
        if(norm < better_distance)
        {
            better_distance = norm;
            index_best = i;
        }   
        
    }
    return index_best;
}
# endif