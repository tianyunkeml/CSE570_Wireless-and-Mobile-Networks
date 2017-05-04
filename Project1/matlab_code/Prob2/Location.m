function [ locMap ] = Location( idList, lat, long, rssi, freqList )
%LOCATION Summary of this function goes here
%   Detailed explanation goes here
    latMap = containers.Map();
    longMap = containers.Map();
    locMap = containers.Map();
    [m, n] = size(idList);
    for i = 1:m
        if rssi(i) == -51
            for j = 1:size(freqList,2)
                if strcmp(freqList{1,j},num2str(idList(i))) == 1
                    if isKey(latMap, num2str(idList(i)))
                        latMap(num2str(idList(i))) = [latMap(num2str(idList(i))), lat(i)];
                        longMap(num2str(idList(i))) = [longMap(num2str(idList(i))), long(i)];
                    else
                        latMap(num2str(idList(i))) = [lat(i)];
                        longMap(num2str(idList(i))) = [long(i)];
                    end
                end
            end
        end
    end
    for i = 1:size(freqList,2)
        avgLat = mean(latMap(freqList{i}));
        avgLong = mean(longMap(freqList{i}));
        locMap(freqList{i}) = [avgLat, avgLong];
    end
            
end

