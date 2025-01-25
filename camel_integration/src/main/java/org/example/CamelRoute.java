package org.example;

import org.apache.camel.Exchange;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.model.dataformat.JsonLibrary;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class CamelRoute extends RouteBuilder {

    @Override
    public void configure() throws Exception {

        from("file:/Users/Narek/Desktop/Uni/Master of Science/Sem2/SA4E/SA4E_2/xmas_prototype/scanned?noop=true")
            .routeId("scanned-wishes-route")

            // Logge den Dateinamen
            .log("Neue Datei gefunden: ${header.CamelFileName}")

            // Lese den Dateiinhalt explizit mit Java NIO
            .process(exchange -> {
                String filePath = exchange.getIn().getHeader(Exchange.FILE_PATH, String.class);
                String fileContent = new String(Files.readAllBytes(Paths.get(filePath))); // Dateiinhalt als String lesen

                // Setze Dateiinhalt in Header und Body
                exchange.getIn().setHeader("fileContentRaw", fileContent);

                Map<String, Object> bodyMap = new HashMap<>();
                bodyMap.put("wish", fileContent);
                bodyMap.put("status", 1);

                exchange.getIn().setBody(bodyMap);
            })

            // Logge den gelesenen Inhalt
            .log("Dateiinhalt (raw): ${header.fileContentRaw}")

            // Konvertiere Map zu JSON
            .marshal().json(JsonLibrary.Jackson)

            // Logge das JSON vor dem Senden
            .log("Nach JSON-Konvertierung: ${body}")

            // Setze Header und sende die Anfrage an XmasWishes
            .setHeader(Exchange.HTTP_METHOD, constant("POST"))
            .setHeader(Exchange.CONTENT_TYPE, constant("application/json"))
            .to("http://localhost:7887/wishes")

            // Abschließendes Log
            .log(">>> Datei zu XmasWishes gesendet: ${body}");
    }
}
