package org.example;

/*设计一个线程安全的懒汉式单例类  DatabaseConnection ，该类模拟一个数据库连接。这个类应该具有以下功能：
获取实例：提供一个静态方法  getInstance() ，用于获取  DatabaseConnection  的唯一实例。
连接数据库：提供一个实例方法  connect() ，模拟连接到数据库，并返回连接成功的消息。
断开连接：提供一个实例方法  disconnect() ，模拟断开与数据库的连接，并返回断开成功的消息。
线程安全：确保在多线程环境下， getInstance()  方法能够正确返回唯一的实例。*/

import java.util.Scanner;

//创建一个饿汉式单例类，获取连接
public class DatabaseConnection {
    private static DatabaseConnection databaseConnection;
    private DatabaseConnection(){}
    public static DatabaseConnection getInstance(){
        if(databaseConnection == null){
            databaseConnection=new DatabaseConnection();
        }
        return databaseConnection;
    }

    public void connect(){
        Scanner scanner=new Scanner(System.in);
        System.out.print("Connect successful!!\n");
    }

    public void disconnect(){
        Scanner scanner=new Scanner(System.in);
        System.out.print("Broken connect!!\n");
    }
}
