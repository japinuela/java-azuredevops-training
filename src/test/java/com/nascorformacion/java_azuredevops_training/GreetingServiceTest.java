package com.nascorformacion.java_azuredevops_training;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class GreetingServiceTest {

    private final GreetingService service = new GreetingService();

    @Test
    void shouldReturnGreetingWithName() {
        assertEquals("Hola, Juan", service.buildGreeting("Juan"));
    }

    @Test
    void shouldReturnDefaultGreetingWhenNameIsEmpty() {
        assertEquals("Hola, mundo", service.buildGreeting(""));
    }
}
