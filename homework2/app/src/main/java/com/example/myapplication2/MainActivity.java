package com.example.myapplication2;

import android.os.Bundle;

import android.os.Bundle;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.ImageView;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.CheckBox;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private TextView text1; // TextView 멤버 변수 선언
    private Switch chkAgree;
    private TextView text2;
    private RadioGroup rGroup1;
    private RadioButton rdoAnd12;
    private RadioButton rdoAnd13;
    private RadioButton rdoAnd14;
    private ImageView imgAnd ;

    private Button button1;
    private Button button2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main); // XML 파일의 이름에 맞게 변경하세요.

        setTitle("안드로이드 버전 보기");

        text1 = (TextView) findViewById(R.id.Text1);
        chkAgree = (Switch) findViewById(R.id.ChkAgree);

        text2 = (TextView) findViewById(R.id.Text2);
        rGroup1 = (RadioGroup) findViewById(R.id.RGroup1);
        rdoAnd12 = (RadioButton) findViewById(R.id.RdoAnd12);
        rdoAnd13 = (RadioButton) findViewById(R.id.RdoAnd13);
        rdoAnd14 = (RadioButton) findViewById(R.id.RdoAnd14);

        imgAnd = (ImageView) findViewById(R.id.ImgAnd);

        button1 = (Button) findViewById(R.id.button1);


        chkAgree.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (chkAgree.isChecked()) {
                    text2.setVisibility(View.VISIBLE);
                    rGroup1.setVisibility(View.VISIBLE);
                    imgAnd.setVisibility(View.VISIBLE);
                } else {
                    text2.setVisibility(View.INVISIBLE);
                    rGroup1.setVisibility(View.INVISIBLE);
                    imgAnd.setVisibility(View.VISIBLE);
                }
            }
        });

        rGroup1.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                // checkedId는 현재 선택된 RadioButton의 ID입니다.

                System.out.println("선택된 RadioButton ID: " + checkedId);

                if (checkedId == R.id.RdoAnd12)
                    imgAnd.setImageResource(R.drawable.and12);
                else if (checkedId == R.id.RdoAnd13)
                    imgAnd.setImageResource(R.drawable.and13);
                else if (checkedId == R.id.RdoAnd14)
                    imgAnd.setImageResource(R.drawable.and14);
            }
        });


        // "종료" 버튼 클릭 이벤트 처리
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish(); // 현재 액티비티 종료
            }
        });

        // "처음으로" 버튼 클릭 이벤트 처리
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 스위치 비활성화
                chkAgree.setChecked(false);

                // 텍스트뷰, 라디오그룹, 이미지뷰 초기 상태로 설정
                text2.setVisibility(View.INVISIBLE);
                rGroup1.setVisibility(View.INVISIBLE);
                imgAnd.setVisibility(View.INVISIBLE);

                // 라디오 버튼 선택 해제
                rGroup1.clearCheck();
            }
        });
    }
}