package me.summerfang.study;

import java.util.Date;

import com.fasterxml.jackson.annotation.JsonFormat;

import lombok.Getter;
import lombok.Setter;

public class User {
    @Setter
    @Getter
    private String firstName;
    private String lastName;

    @Setter
    @Getter
    private Date createDate = new Date();

    public User(String firstName, String lastName, Date createDate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.createDate = createDate;
    }

    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    public Date getDate() {
        return createDate;
    }
}
