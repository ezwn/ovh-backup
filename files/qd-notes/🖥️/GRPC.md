# grpc

```mermaid
sequenceDiagram
    participant Client
    participant RequestTopic
    participant ResponseTopic
    participant LLMService

    Note over Client,LLMService: Le client produit un message requête (prompt)

    Client->>RequestTopic: Production d'une requête

    Note over Client,LLMService: Un LLMService consomme, traite et produit la réponse
    
    LLMService->>RequestTopic: Récupération de la requête
    RequestTopic-->>LLMService: Requête consommée
    LLMService->>LLMService: Traitement (appel de l'API du LLM)
    LLMService->>ResponseTopic: Production de la réponse

    Note over Client,LLMService: La réponse est consommée

    Client->>ResponseTopic: Un client récupère la réponse
    ResponseTopic-->>Client: Réponse consommée


```

## Modes

* Unary
* LLMService streaming
* Client streaming
* Bidirectional streaming

## JS tools

* grpc
* @grpc/proto-loader: generator

[https://youtu.be/Yw4rkaTc0f8?list=PL12XW6i6zqKsK3nax9AYFYuTlEgzH7zCh\&t=2001](https://youtu.be/Yw4rkaTc0f8?list=PL12XW6i6zqKsK3nax9AYFYuTlEgzH7zCh\&t=2001)

[https://grpc.io/docs/what-is-grpc/core-concepts/](https://grpc.io/docs/what-is-grpc/core-concepts/)
