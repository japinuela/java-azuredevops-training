package com.nascorformacion.java_azuredevops_training;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class HealthController {

    private final GreetingService greetingService;

    public HealthController(GreetingService greetingService) {
        this.greetingService = greetingService;
    }

    @GetMapping("/health")
    public String health() {
        return "OK";
    }

    @GetMapping("/greeting")
    public String greeting(@RequestParam(required = false) String name) {
        return greetingService.buildGreeting(name);
    }
}