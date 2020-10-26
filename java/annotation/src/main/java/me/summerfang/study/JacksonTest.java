package me.summerfang.study;

import java.io.IOException;
import java.text.ParseException;
// import java.text.SimpleDateFormat;
import java.util.Date;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JacksonTest {
    public static void main(String args[]) throws IOException, ParseException {
        ObjectMapper mapper = new ObjectMapper();
        // SimpleDateFormat simpleDateFormat = new SimpleDateFormat("dd-MM-yyyy");
        // Date date = simpleDateFormat.parse("20-12-1984");

        Student student = new Student(1, new Date());
        String jsonString = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(student);
        String jsstr = mapper.writeValueAsString(student);
        System.out.println(jsstr);

        System.out.println(jsonString);
    }
}

class Student {
    public int id;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd-MM-yyyy")
    public Date birthDate;

    Student(int id, Date birthDate) {
        this.id = id;
        this.birthDate = birthDate;
    }
}