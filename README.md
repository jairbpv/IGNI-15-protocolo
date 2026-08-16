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

[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
[Status](https://img.shields.io/badge/Status-V8.1%20SUPREMA-green.svg)
[Version](https://img.shields.io/badge/Protocolo-LIMIAR-red.svg)

# IGNI-15-protocolo

**Protocolo de Governança Distribuída IGNI-15 V8.1 SUPREMA**

Autor: **Jair Olindino Bernardo Junior**

O IGNI-15 é um protocolo de consenso distribuído projetado para governança transparente, segura e escalável. Inspirado nos princípios do LIMIAR, ele utiliza blockchain para garantir imutabilidade e auditabilidade das decisões.

[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
[Status](https://img.shields.io/badge/Status-V8.1%20SUPREMA-green.svg)

# IGNI-15-protocolo

**Protocolo de Governança Distribuída IGNI-15 V8.1 SUPREMA**

Autor: **Jair Olindino Bernardo Junior**

O IGNI-15 é um protocolo de consenso distribuído projetado para governança transparente, segura e escalável. Inspirado nos princípios do LIMIAR, ele utiliza blockchain para garantir imutabilidade e auditabilidade das decisões.

## 🚀 Como Usar

```bash
git clone https://github.com/jairbpv/IGNI-15-protocolo.git
python IGNI-15_V8.1_consenso.py