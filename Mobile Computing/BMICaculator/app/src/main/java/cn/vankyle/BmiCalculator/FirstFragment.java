package cn.vankyle.BmiCalculator;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import android.widget.EditText;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;
import cn.vankyle.bmiCaculator.R;

public class FirstFragment extends Fragment {

    private EditText WeightInput;
    private  EditText HeightInput;
    private TextView BmiOutput;


    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_first, container, false);
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        view.findViewById(R.id.button_first).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NavHostFragment.findNavController(FirstFragment.this)
                        .navigate(R.id.action_FirstFragment_to_SecondFragment);
            }
        });
        WeightInput=view.findViewById(R.id.BodyWeightInput);
        HeightInput=view.findViewById(R.id.BodyHeightInput);
        BmiOutput=view.findViewById(R.id.BmiValue);
        view.findViewById(R.id.bmiCalculateButton).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view1) {
                System.out.println("calculate button has been clicked!");
                double inputedHeithValue = Double.valueOf(HeightInput.getText().toString());
                double inputedWeightValue = Double.valueOf(WeightInput.getText().toString());
                double bmiResult=inputedWeightValue/((inputedHeithValue/100)*(inputedHeithValue/100));
                BmiOutput.setText(String.valueOf(bmiResult));
            }
        });

    }

}