package com.nascorformacion.java_azuredevops_training;
import org.springframework.stereotype.Service;

@Service
public class GreetingService {

    public String buildGreeting(String name) {
        if (name == null || name.isBlank()) {
            return "Hola, mundo";
        }
        return "Buenos días, " + name + "!";
    }
}