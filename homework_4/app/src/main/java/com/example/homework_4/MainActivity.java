package com.example.homework_4;

import android.app.TabActivity;
import android.os.Bundle;
import android.widget.TabHost;
import android.widget.ImageView; // ImageView import 추가
import android.view.View; // View.VISIBLE import 추가

@SuppressWarnings("deprecation")
public class MainActivity extends TabActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TabHost tabHost= getTabHost();

        TabHost.TabSpec tabSpecSong = tabHost.newTabSpec("SONG").setIndicator("강아지");
        tabSpecSong.setContent(R.id.tabSong); // 수정된 부분
        tabHost.addTab(tabSpecSong);

        TabHost.TabSpec tabSpecArtist = tabHost.newTabSpec("ARTIST").setIndicator("고양이");
        tabSpecArtist.setContent(R.id.tabArtist); // 수정된 부분
        tabHost.addTab(tabSpecArtist);

        TabHost.TabSpec tabSpecAlbum = tabHost.newTabSpec("ALBUM").setIndicator("햄스터");
        tabSpecAlbum.setContent(R.id.tabAlbum); // 수정된 부분
        tabHost.addTab(tabSpecAlbum);

        tabHost.setCurrentTab(0);

        tabHost.setOnTabChangedListener(new TabHost.OnTabChangeListener() {
            @Override
            public void onTabChanged(String tabId) {
                // 선택한 탭의 ID를 확인하여 해당하는 이미지를 표시
                switch (tabId) {
                    case "SONG":
                        // Song 탭 이미지 표시
                        ImageView imageViewSong = findViewById(R.id.imageViewSong);
                        imageViewSong.setVisibility(View.VISIBLE);
                        ImageView imageViewArtist = findViewById(R.id.imageViewArtist);
                        imageViewArtist.setVisibility(View.GONE);
                        ImageView imageViewAlbum = findViewById(R.id.imageViewAlbum);
                        imageViewAlbum.setVisibility(View.GONE);
                        break;
                    case "ARTIST":
                        // Artist 탭 이미지 표시
                        imageViewArtist = findViewById(R.id.imageViewArtist);
                        imageViewArtist.setVisibility(View.VISIBLE);
                        imageViewSong = findViewById(R.id.imageViewSong);
                        imageViewSong.setVisibility(View.GONE);
                        imageViewAlbum = findViewById(R.id.imageViewAlbum);
                        imageViewAlbum.setVisibility(View.GONE);
                        break;
                    case "ALBUM":
                        // Album 탭 이미지 표시
                        imageViewAlbum = findViewById(R.id.imageViewAlbum);
                        imageViewAlbum.setVisibility(View.VISIBLE);
                        imageViewSong = findViewById(R.id.imageViewSong);
                        imageViewSong.setVisibility(View.GONE);
                        imageViewArtist = findViewById(R.id.imageViewArtist);
                        imageViewArtist.setVisibility(View.GONE);
                        break;
                    default:
                        break;
                }
            }
        });
    }
}