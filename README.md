# Taller de Hacking Web edición 2026 - Soy QB1t 
![Workshop](https://img.shields.io/badge/_Workshop-Web_Hacking_2026-red?style=for-the-badge&logo=hackthebox&logoColor=white)
![Level](https://img.shields.io/badge/🎯_Level-Intermediate-orange?style=for-the-badge&logo=htb&logoColor=white)
![Sessions](https://img.shields.io/badge/⚡_Sessions-10_Modules-blue?style=for-the-badge&logo=python&logoColor=white)
![Topics](https://img.shields.io/badge/🔥_Topics-SQLi|XSS|SSRF|API-red?style=for-the-badge)
![Tools](https://img.shields.io/badge/🛠️_Tools-Burp|Python|Docker-black?style=for-the-badge&logo=linux&logoColor=white)
![Status](https://img.shields.io/badge/📦_Status-Active_Labs-green?style=for-the-badge)
![License](https://img.shields.io/badge/⚖️_License-Educational_Only-yellow?style=for-the-badge)


Este repositorio contiene el material técnico, metodologías y laboratorios del taller. El contenido está diseñado para el estudio sistemático de vulnerabilidades modernas, desde fallos en la capa de datos hasta vectores emergentes en infraestructura y modelos de lenguaje.

##  ¿Que es ese taller?

El taller se enfoca en metodologías de explotación, técnicas de evasión y análisis de arquitecturas actuales. Cada módulo incluye recursos técnicos, payloads de campo y laboratorios de práctica.

##  ¿Que vamos estudiar?

|Sesión|Tópicos Principales|Vectores y Metodologías|
|---|---|---|
|**01**|Server-side Injection I|Análisis de motores relacionales vs. documentales (SQLi/NoSQLi), manipulación de drivers y bypass de lógica de autenticación.|
|**02**|Server-side Injection II|Remote Code Execution (RCE) vía OS Command Injection y técnicas de evasión de filtros en Path Traversal/LFI.|
|**03**|Client-side Attacks|Explotación avanzada de XSS (DOM, Reflected, Stored) y desincronización de estado mediante CSRF.|
|**04**|Broken Trust|Auditoría de controles de acceso (IDOR), escalamiento de privilegios y análisis de fallos en la lógica de negocio.|
|**05**|Input/Output Handling|Manipulación de flujos de entrada mediante Server-Side Request Forgery (SSRF) y explotación de XML External Entity (XXE).|
|**06**|Files & Templates|Bypass de validaciones en File Upload (Polyglots) y explotación de Server-Side Template Injection (SSTI).|
|**07**|API Security|Análisis de seguridad en implementaciones REST y GraphQL. Ataques a la integridad y algoritmos de JWT.|
|**08**|Modern Attacks|Explotación de condiciones de carrera (Race Conditions) y vectores de ataque sobre implementaciones de Web LLM.|
|**09**|Infrastructure & Cache|Vulnerabilidades en la capa de transporte: HTTP Request Smuggling y configuraciones erróneas de CORS.|
|**10**|The Dark Side|Análisis de Deserialización Insegura y resolución de entorno controlado integrador (Final Boss Lab).|

## 📂 Estructura del Repositorio

- `/presentaciones`: Methodology Decks en formato HTML para cada sesión.
    
- `/cheat-sheets`: Hojas de referencia rápida con payloads probados en campo.
    
- `/guias`: Documentación técnica autodidacta y guías de remediación.
    
- `/scripts`: Herramientas en Python para la automatización de vectores específicos.
    

## 🛠️ Requisitos Sugeridos

- **Burp Suite Professional/Community** (Intruder & Repeater).
    
- **Python 3.x** (Automatización de scripts).
    
- **Docker** (Despliegue de entornos controlados).
    

## ⚠️ Disclaimer

Este repositorio tiene fines exclusivamente educativos. El acceso a sistemas informáticos sin autorización previa es un delito.
