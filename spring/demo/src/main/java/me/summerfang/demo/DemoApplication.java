package me.summerfang.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@GetMapping("/hello")
	public String hello(@RequestParam(value = "name", defaultValue = "World") String name, @RequestParam(value = "greeting", defaultValue="") String greeting){
		return String.format("Hello %s! %s", name, greeting);
	}

	@GetMapping("/greeting")
	public String greeting(@RequestParam(value = "greeting", defaultValue = "The world is beatuiful") String greeting) {
		return String.format("%s", greeting);
	}
}
