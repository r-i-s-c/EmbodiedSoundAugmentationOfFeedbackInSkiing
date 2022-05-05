//using System.Collections;
//using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Info : MonoBehaviour
{
    [SerializeField] private Text soundText;
    [SerializeField] private Text sensor1Text;
    [SerializeField] private Text sensor2Text;
    [SerializeField] private Text sensor3Text;
    [SerializeField] private ValueInput input;
    [SerializeField] private SoundObject soundObj1;
    [SerializeField] private SoundObject soundObj2;

    void Update()
    {
        soundText.text = "obj1 sound on: " + (soundObj1.soundIsOn).ToString() + "\n" +  
                         "obj2 sound on: " + (soundObj2.soundIsOn).ToString();
        sensor1Text.text = "s1RotX: " + (input.values.s1RotX).ToString() + "\n" + 
                           "s1RotY: " + (input.values.s1RotY).ToString();
        sensor2Text.text = "s2RotX: " + (input.values.s2RotX).ToString() + "\n" + 
                           "s2RotY: " + (input.values.s2RotY).ToString();
        sensor3Text.text = "s3RotX: " + (input.values.s3RotX).ToString() + "\n" + 
                           "s3RotY: " + (input.values.s3RotY).ToString();
                           
    } 
}
