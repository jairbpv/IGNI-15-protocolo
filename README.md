# IGNI-15-protocolo
Protocolo Governança Distribuidada IGNI-15 V8.1 Autor: Jair Olindino Bernardo Junior.
# IGNI-15 V8.1 SUPREMA
## Protocolo de Governança Distribuída com Sistema de Alerta

**Autor:** Jair Olindino Bernardo Junior  
**Data de Lançamento:** 16/08/2026  
**Licença:** MIT

### Sobre
IGI-15 V8.1 é um protocolo de governança distribuída projetado para tomada de decisão em rede com segurança, auditoria e transparência. 
Utiliza sistema de consenso ponderado, blockchain encadeado e monitoramento em tempo real para garantir integridade das decisões.

### Características Principais
- **Sistema de Consenso 67% + Quorum 51%**: Segurança dupla para validação


- **Sistema de Alerta**: Logs em tempo real com níveis INFO, ALERTA, CRITICO e CONSENSO
- **Blockchain Encadeado**: Auditoria
 completa e rastreabilidade
- **Detecção de Anomalias**: Identifica nós
 vulneráveis e propostas órfãs
- **Votação Ponderada**: Peso e reputação por nó

### Como Usar
```python
igni = IGNI15()
igni.registrar_no("no_01", peso=2)
hash_prop = igni.propor_decisao("Aprovar nova regra", "no_01")
igni.votar(hash_prop, "no_02", "sim")
igni.verificar_consenso(hash_prop)



---
**Autor:** Jair Olindino Bernardo Junior  
**Lançado em:** 16/08/2026 - Palhoça, SC - Brasil  
**Licença:** MIT

*"Governança sem centralização. Poder distribuído com responsabilidade."*
