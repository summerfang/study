package me.summerfang.study;

import javax.persistence.*;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "warehouses")
public class Warehouses {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id")
    private int id;
    
    @Getter
    @Setter
    @Column(name = "name")
    private String name;

    @Column(name = "capacity")
    private Float capacity;
}
