package me.summerfang.study;

public class AccessDatabase extends MyDatabase{
    private MyDatabase db;

    public AccessDatabase(MyDatabase db) {
        this.db = db;
    }

    public String getAValue(String str) {
        if(db.query(str))
            return "OK";
        else
            return "False";
    }
}
