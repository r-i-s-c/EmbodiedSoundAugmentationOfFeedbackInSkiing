using UnityEngine;
using System.Runtime.InteropServices;

public class ValueInput : MonoBehaviour {

	#region WebSocketJSLib Implement
	[DllImport("__Internal")]
	private static extern void InitWebSocket();
	#endregion

	[HideInInspector] public Values values;

	void Start () 
	{
		InitWebSocket();
	}

	void UpdateValues(string str) //connection to websocket client
	{
		values = JsonUtility.FromJson<Values>(str);
		//values.ConvertToTwoDP();
	}

	public class Values
	{
		public float s1RotX;
		public float s1RotY;
		public float s2RotX;
		public float s2RotY;
		public float s3RotX;
		public float s3RotY;

		public void ConvertToInt()
		{
			s1RotX = (int) s1RotX;
			s1RotY = (int) s1RotY;
			s2RotX = (int) s2RotX;
			s2RotY = (int) s2RotY;
			s3RotX = (int) s3RotX;
			s3RotY = (int) s3RotY;
		}

		public void ConvertToTwoDP()
		{
			s1RotX = Mathf.Round(s1RotX * 100f) / 100f;
			s1RotY = Mathf.Round(s1RotY * 100f) / 100f;
			s2RotX = Mathf.Round(s2RotX * 100f) / 100f;
			s2RotY = Mathf.Round(s2RotY * 100f) / 100f;
			s3RotX = Mathf.Round(s3RotX * 100f) / 100f;
			s3RotY = Mathf.Round(s3RotY * 100f) / 100f;
		}
	}
}

