using UnityEngine;

public class SoundObject : MonoBehaviour
{
    [SerializeField] private ValueInput input;
    [SerializeField] private float speed;
    [SerializeField] private int sensorNum;
    [HideInInspector] public bool soundIsOn; 
    private AudioSource audiosrc;

    void Start()
    {
        audiosrc = GetComponent<AudioSource>();
        soundIsOn = audiosrc.isPlaying;
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.E))
            audiosrc.Play();
        else if (Input.GetKeyDown(KeyCode.R))
            audiosrc.Stop();

        soundIsOn = audiosrc.isPlaying;

        if (sensorNum == 1)
            gameObject.transform.position = new Vector3(input.values.s1RotY * speed, transform.position.y, 
                                                        transform.position.z);
        else if (sensorNum == 2)
            gameObject.transform.position = new Vector3(input.values.s2RotY * speed, transform.position.y, 
                                                        transform.position.z);
    }
}

