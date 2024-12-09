# Domain Model

This document describes the initial domain model concepts and relationships used within the ModelMates repository. It serves as a starting point, providing a common language and structure for representing various business, application, and infrastructure elements.

## Overview

Our domain model is built around a **graph-based** representation, where **nodes** represent entities and **edges** represent relationships. We aim for a flexible model that can be extended as needed. Initially, we define a few key entity types and relationships, focusing on common scenarios found in business and IT landscapes.

## Entities

| Entity Type         | Description                                                                                  | Example                             | Common Attributes             |
|---------------------|----------------------------------------------------------------------------------------------|-------------------------------------|-------------------------------|
| **BusinessCapability** | Represents a high-level ability or function of the organization                           | "Order Management", "Customer Care"  | `id`, `name`, `description`   |
| **BusinessProcess**  | A defined sequence of activities that fulfill a specific business goal                      | "Order-to-Cash", "Onboarding Process"| `id`, `name`, `description`   |
| **Actor**            | A role, person, or organizational unit involved in business processes or operations          | "Customer", "Sales Department"       | `id`, `name`, `description`   |
| **Application**      | A software application or system that supports business capabilities or processes            | "OrderService", "UserService"        | `id`, `name`, `description`, possibly `version` |
| **DataStore**        | A data storage component such as a database, file system, or data lake                      | "CustomerDB", "OrderDB"              | `id`, `name`, `description`, possibly `db_type` |

**Note:** Additional entity types (e.g., `Node` for infrastructure, `Device` for hardware) may be introduced later as the model evolves.

## Relationships

| Relationship  | Description                                                       | Example                                 |
|---------------|-------------------------------------------------------------------|-----------------------------------------|
| **depends_on** | One entity requires another entity to function                    | `Application(OrderService) depends_on DataStore(CustomerDB)` |
| **part_of**    | One entity is a constituent of another entity                     | `BusinessProcess(Order-to-Cash) part_of BusinessCapability(Order Management)` |
| **responsible_for** | An Actor is responsible or accountable for another entity    | `Actor(Sales Department) responsible_for BusinessCapability(Order Management)` |
| **implements** | An Application supports or realizes a BusinessCapability or Process | `Application(UserService) implements BusinessProcess(Onboarding Process)` |
| **connects_to** | Entities are technically connected or integrated (often used for IT components) | `Application(OrderService) connects_to Application(UserService)` |

**Note:** These initial relationships are generic. We might refine or add more specific relationship types (e.g., `hosts`, `runs_on`, `involves`) as we explore different domains or notations.

## Attributes

Each entity typically includes a minimal set of attributes:

- `id`: A unique identifier (e.g., a UUID or a human-readable key)
- `name`: A human-readable name
- `description`: A short description of the entity’s purpose or function

Additional attributes may be introduced as needed. For instance, an `Application` might have a `version` attribute, or a `DataStore` might specify `db_type` or `capacity`.

## Extensibility

This domain model is a starting point. We anticipate extending it in several ways:

- Introducing additional entity types (e.g., `Node`, `Device`, `ServiceLevelAgreement`, `Interface`).
- Adding domain-specific attributes or relations (e.g., `hosts`, `runs_on`, `belongs_to`).
- Mapping these entities and relationships to standardized modeling notations like ArchiMate, UML, BPMN, or ERD.

As the project evolves, we will revisit and refine this domain model to ensure it supports the use cases and visualizations we aim to provide.

---

This initial domain model outlines the basic entities and relationships we will work with. It does not represent a final standard; rather, it’s a living, flexible starting point that will grow as ModelMates matures.
