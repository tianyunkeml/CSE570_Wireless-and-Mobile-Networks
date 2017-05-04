function rank = FindFreqTower( idList )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    countMap = containers.Map();
    [m, n] = size(idList);
    for i = 1:m
        id = num2str(idList(i));
        if not(isKey(countMap, id))
            countMap(id) = 1;
        else
            countMap(id) = countMap(id) + 1;
        end
    end
    rank = cell(1,6);
    corrValue = zeros(1,6);
    keySet = keys(countMap);
    [mm, nn] = size(keySet);
    for i = 1:nn
        thisCount = countMap(keySet{i});
        if thisCount > min(corrValue)
            ind = find(corrValue == min(corrValue));
            ind = ind(1);
            rank{1, ind} = keySet{i};
            corrValue(ind) = thisCount;
        end
    end
end

