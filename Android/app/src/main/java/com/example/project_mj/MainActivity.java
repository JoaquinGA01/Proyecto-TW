package com.example.project_mj;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

import org.json.JSONException;
import org.json.JSONObject;
import org.w3c.dom.Text;

import java.io.IOException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;


public class MainActivity extends AppCompatActivity {

    private Button loginButton;
    private EditText editTextEmail;
    private EditText editTextPassword;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editTextEmail = findViewById(R.id.editTextEmail);
        editTextPassword = findViewById(R.id.editTextPassword);
        loginButton = findViewById(R.id.buttonLogin);
        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Obtener los datos del formulario de inicio de sesión
                String email = editTextEmail.getText().toString();
                String password = editTextPassword.getText().toString();

                // Crear un objeto JSON con los datos de inicio de sesión
                JSONObject json = new JSONObject();
                try {
                    json.put("email", email);
                    json.put("password", password);
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                // Crear una instancia del cliente OkHttp
                OkHttpClient client = new OkHttpClient();

                // Definir el tipo de contenido como JSON
                MediaType mediaType = MediaType.parse("application/json; charset=utf-8");

                // Crear el cuerpo de la solicitud POST con los datos JSON
                RequestBody requestBody = RequestBody.create(json.toString(), mediaType);

                // Crear la solicitud POST
                Request request = new Request.Builder()
                        .url("http://192.168.0.15:8000/api/personas/getAll-Movil/")
                        .post(requestBody)
                        .build();

                try {
                    // Enviar la solicitud POST y obtener la respuesta
                    Response response = client.newCall(request).execute();

                    // Comprobar el código de respuesta
                    if (response.isSuccessful()) {
                        // La solicitud fue exitosa
                        Intent intent = new Intent(MainActivity.this, HomeActivity.class);
                        startActivity(intent);
                    } else {
                        // La solicitud no fue exitosa
                        // Manejar el caso de error según tus necesidades
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });


        // Agrega el código para manejar el evento "Forgot Password" si es necesario
    }
}
