package org.example;

import org.apache.camel.CamelContext;
import org.apache.camel.impl.DefaultCamelContext;

public class CamelMain {

    public static void main(String[] args) throws Exception {
        CamelContext context = new DefaultCamelContext();
        context.addRoutes(new CamelRoute());

        context.start();
        System.out.println("Camel is running. Press Ctrl+C to stop...");
        Thread.sleep(Long.MAX_VALUE);
        context.stop();
    }
}
