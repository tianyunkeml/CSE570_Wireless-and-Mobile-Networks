noise1 = indoor_rssi - floor(mean(indoor_rssi));
noise2 = outdoor_rssi - floor(mean(outdoor_rssi));


histfit(noise2, 10);

