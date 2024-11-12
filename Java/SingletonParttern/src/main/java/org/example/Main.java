package org.example;

public class Main {
    public static void main(String[] args){
        DatabaseConnection databaseConnection;
        databaseConnection=DatabaseConnection.getInstance();
        databaseConnection.connect();
        databaseConnection.disconnect();
    }
}