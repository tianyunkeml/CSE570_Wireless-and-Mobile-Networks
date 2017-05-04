function [ minValue ] = myMin( theArray )
%MYMIN Summary of this function goes here
%   Detailed explanation goes here
    theArray(find(theArray == 0)) = 10000;
    minValue = min(theArray);


end

