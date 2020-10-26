package me.summerfang.study;

import java.util.List;

import javax.management.Query;
import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

import me.summerfang.study.Warehouses;

public class AppWarehouse {
    private static final String PERSISTENCE_UNIT_NAME = "mytest";
    private static EntityManagerFactory factory;
    
    public static void main(String[] args) {
        factory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
        EntityManager em = factory.createEntityManager();
        // read the existing entries and write to console
        Query q = (Query) em.createQuery("select name from warehouses");
        List<Warehouses> todoList = ((javax.persistence.Query) q).getResultList();
        for (Warehouses todo : todoList) {
            System.out.println(todo);
        }
        System.out.println("Size: " + todoList.size());
    
        // create new todo
        // em.getTransaction().begin();
        // Warehouses todo = new Warehouses();
        // ((Object) todo).setName("This is a test");
        // em.persist(todo);
        // em.getTransaction().commit();
    
        // em.close();
    }
}

