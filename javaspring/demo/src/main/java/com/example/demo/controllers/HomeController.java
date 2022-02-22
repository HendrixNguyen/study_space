package com.example.demo.controllers;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HomeController {
    @GetMapping("/hello" )
    public String helloYou(@RequestParam(value = "", defaultValue = "default") String name) {
        return String.format("Hello %s", name);
    };
}
