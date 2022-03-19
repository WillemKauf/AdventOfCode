#include<omp.h>
#include<string>
#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include<map>

auto read_input(){
  std::ifstream in_file("input/input24.txt");
  std::string line;
  std::vector<std::string> input;
  while(std::getline(in_file, line)){
    std::istringstream iss(line);
    input.push_back(line);
  }
  return input;
}


int main(){
  auto input = read_input();
#pragma omp parallel for
  for(long i = 0; i < 99999999999999; ++i){//This is gonna take a while.
    std::map<std::string, int> regs {{"w", 0}, {"x", 0}, {"y", 0}, {"z", 0}};
    std::string num = std::to_string(i);
    auto number_of_zeros = 14 - num.length();
    num.insert(0, number_of_zeros, '0');
    std::size_t index = 0;
    for(const auto& line : input){
      if(line.substr(0, 3) == "inp"){
        const char w2 = num[index++];
        regs["w"] = std::atoi(&w2);
      }else if(line.substr(0,3) == "mul"){
        const std::string a = line.substr(4,1);
        const std::string b = line.substr(6,line.length()-6);
        if(regs.find(b) == regs.end()){
          regs[a] *= std::stoi(b);
        }else{
          regs[a] *= regs[b];
        }
      }else if(line.substr(0,3) == "div"){
        const std::string a = line.substr(4,1);
        const std::string b = line.substr(6,line.length()-6);
        if(regs.find(b) == regs.end()){
          regs[a] /= std::stoi(b);
        }else{
          regs[a] /= regs[b];
        }
      }else if(line.substr(0,3) == "mod"){
        const std::string a = line.substr(4,1);
        const std::string b = line.substr(6,line.length()-6);
        if(regs.find(b) == regs.end()){
          regs[a] %= std::stoi(b);
        }else{
          regs[a] %= regs[b];
        }
      }else if(line.substr(0,3) == "add"){
        const std::string a = line.substr(4,1);
        const std::string b = line.substr(6,line.length()-6);
        if(regs.find(b) == regs.end()){
          regs[a] += std::stoi(b);
        }else{
          regs[a] += regs[b];
        }
      }else if(line.substr(0,3) == "eql"){
        const std::string a = line.substr(4,1);
        const std::string b = line.substr(6,line.length()-6);
        if(regs.find(b) == regs.end()){
          if(regs[a] == std::stoi(b)){
            regs[a] = 1;
          }else{
            regs[a] = 0;
          }
        }else{
          if(regs[a] == regs[b]){
            regs[a] = 1;
          }else{
            regs[a] = 0;
          }
        }
      }
    }
    if(regs["z"] == 0){
      std::cout << num << '\n';
    }
  }
  return 0;
}
