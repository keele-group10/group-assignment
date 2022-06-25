# group-assignment

## Infrastructure Diagram

Proposed Google Cloud Platform infrastructure, inspired by [13 Sample Architectures](https://cloud.google.com/blog/products/application-development/13-popular-application-architectures-for-google-cloud).

This is quite generic, and could easily be translated to an AWS or Azure option.

Note that any potential external services (IAM, payment) are not included in the diagram.

![Infrastructure Diagram](./diagrams/bmi2_gcp_architecture_proposal.png)

## This is smaller heading

Here's a graph:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### an even smaller heading

Here's a sequence diagram:

```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/> prevail...
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```
