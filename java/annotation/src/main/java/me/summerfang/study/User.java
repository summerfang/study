package me.summerfang.study;

import java.util.Date;

import com.fasterxml.jackson.annotation.JsonFormat;

import lombok.Getter;
import lombok.Setter;

public class User {

    @Getter
    @Setter
    private String firstName;

    @Getter
    @Setter
    private String lastName;

    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date createDate;

    public User(String firstName, String lastName, Date createDate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.createDate = createDate;
    }
}
