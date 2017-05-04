package com.example.yunketian.homework1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import java.io.FileNotFoundException;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.io.FileWriter;
import java.lang.Thread;

import android.view.View;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        WifiManager wifi_service = (WifiManager)getSystemService(WIFI_SERVICE);
//        WifiInfo wifiInfo = wifi_service.getConnectionInfo();

        final Button startButton = (Button) findViewById(R.id.startButton);

        startButton.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v){
                for(int i = 0; i < 20; i++) {
                    try {
                        FileWriter writer = new FileWriter("/data/data/com.example.yunketian.homework1/RSSI_Record" + String.valueOf(i) + ".txt");
                        for (int j = 0; j < 60; j++) {
                            try {
                                WifiManager wifi_service = (WifiManager)getSystemService(WIFI_SERVICE);
                                WifiInfo wifiInfo = wifi_service.getConnectionInfo();
                                Thread.sleep(3 * 1000);
                                String rssiValue = String.valueOf(wifiInfo.getRssi());
                                writer.write(rssiValue + "\n");
                            } catch (InterruptedException e) {
                            }
                            catch (UnsupportedEncodingException e) {
                            }
                        }
                        writer.close();
                    } catch (FileNotFoundException e) {
                        e.printStackTrace();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

//                for (int j = 0; j < 1200; j++) {
//                    try {
//                        Thread.sleep(3 * 1000);
//                        String rssiValue = new String();
//                        rssiValue.valueOf(wifiInfo.getRssi());
//                        fos.write(rssiValue.getBytes("UTF-8"));
//                    }catch (InterruptedException e)
//                    {
//                    }
//                    catch (UnsupportedEncodingException e)
//                    {
//                    }
//                }
//                fos.close();
                }
            }
        });
//        stopButton.setOnClickListener(new Button.OnClickListener() {
//            public void onClick(View v){
//                try {
//                    fos.close();
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//        });
    }
}
