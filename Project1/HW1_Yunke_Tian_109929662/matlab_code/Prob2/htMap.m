m = size(cell_tower_id,1);

freqList = FindFreqTower(cell_tower_id);
% minLat = 1000;
% minLong = 1000;
% maxLat = -1000;
% maxLong = -1000;
minLat = myMin(latitude);
maxLat = myMax(latitude);
minLong = myMin(longitude);
maxLong = myMax(longitude);
% for i = 1:size(freqList, 2)
%     num_id = str2double(freqList{i});
%     corrInd = find(cell_tower_id == num_id);
%     minLat = min(minLat, myMin(latitude(corrInd)));
%     maxLat = max(maxLat, myMax(latitude(corrInd)));
%     minLong = min(minLong, myMin(longitude(corrInd)));
%     maxLong = max(maxLong, myMax(longitude(corrInd)));
% end
metersPerLat = 111052;
metersPerLong = 84241;
gridHeight = floor(metersPerLat * (maxLat - minLat));
gridWidth = floor(metersPerLong * (maxLong - minLong));
htmap = zeros(gridHeight + 1, gridWidth + 1);
htmap = htmap - 120;
for i = 1:size(cell_tower_rssi,1)
    sign = 0;
    for j = 1:size(freqList,2)
        if strcmp(freqList{1, j},num2str(cell_tower_id(i))) == 1
            sign = 1;
            break;
        end
    end
    if sign == 1 && latitude(i) ~= 0 && longitude(i) ~= 0
        h_offset = 1 + floor(metersPerLat * (latitude(i) - minLat));
        w_offset = 1 + floor(metersPerLong * (longitude(i) - minLong));
        htmap(h_offset, w_offset) = cell_tower_rssi(i);
    end
end
img = 2 * (120 + htmap);
image(img);

