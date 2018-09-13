using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

	public float speed;
	private Rigidbody ball;

	void Start() {
		ball = GetComponent<Rigidbody>();
	}
	
	void FixedUpdate () {
		float moveX = Input.GetAxis("Horizontal");
        float moveZ = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(moveX, 0.0f, moveZ);
        ball.AddForce(movement*speed);
	}
}
