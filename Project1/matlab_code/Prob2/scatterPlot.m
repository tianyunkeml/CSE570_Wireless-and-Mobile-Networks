locmap = Location(cell_tower_id, latitude, longitude, cell_tower_rssi, freqList);
models = cell(1, 6);

for i = 1: size(freqList,2)
    theInd = find(cell_tower_id == str2double(freqList{i}));
    zeroInd = find(latitude == 0);
    interInd = intersect(theInd, zeroInd);
    for k = 1:size(interInd, 1)
        theInd(find(theInd == interInd(k))) = [];
    end
    rssi_s = cell_tower_rssi(theInd);
    lat_s = latitude(theInd);
    long_s = longitude(theInd);
    l = size(theInd, 1);
    logDis = zeros(1,l);
    center = locmap(freqList{i});
    for j = 1:l
        dist = haversine(lat_s(j), long_s(j), center(1), center(2));
        logDis(j) = log10(dist);
    end
    models{1, i} = LinearModel.fit(logDis, rssi_s);
    scatter(logDis, rssi_s);
    true;
end
        
    
    