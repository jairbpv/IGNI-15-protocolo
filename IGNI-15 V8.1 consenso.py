    # IGNI-15 V8.1
    # Autor: Jair Olindino Bernardo Junior
    # Licença: MIT
    # Protocolo de Governança Distribuída

    # IGNI-15 V8.1 SUPREMA
# Autor: Jair Olindino Bernardo Junior
# Licença: MIT
# Protocolo de Governança Distribuída com Sistema de Alerta
# Data: 16/08/2026

import hashlib
import time
import json
from datetime import datetime

class SistemaAlerta:
    def __init__(self):
        self.logs = []
        self.niveis = {"INFO": "🟢", "ALERTA": "🟡", "CRITICO": "🔴", "CONSENSO": "👑"}
    
    def registrar(self, nivel, mensagem):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log = f"{self.niveis.get(nivel, '⚪')} [{timestamp}] {nivel}: {mensagem}"
        self.logs.append(log)
        print(log)
    
    def exportar_logs(self):
        return "\n".join(self.logs)

class NoIGI:
    def __init__(self, id_no, peso=1, reputacao=100):
        self.id = id_no
        self.peso = peso
        self.reputacao = reputacao
        self.ativo = True
        self.ultimo_acesso = time.time()

class IGNI15:
    def __init__(self):
        self.versao = "V8.1 SUPREMA"
        self.autor = "Jair Olindino Bernardo Junior"
        self.nos = {}
        self.blockchain = []
        self.alerta = SistemaAlerta()
        self.limiar_consenso = 0.67
        self.limiar_quorum = 0.51
        self.alerta.registrar("INFO", f"IGI-15 {self.versao} inicializado")
    
    def registrar_no(self, id_no, peso=1):
        """Registra nó com verificação de segurança"""
        if id_no in self.nos:
            self.alerta.registrar("ALERTA", f"Tentativa de duplicar nó: {id_no}")
            return False
        
        self.nos[id_no] = NoIGI(id_no, peso)
        self.alerta.registrar("INFO", f"Nó {id_no} registrado | Peso: {peso}")
        return True
    
    def propor_decisao(self, proposta, id_proponente):
        """Cria proposta com hash e timestamp"""
        if id_proponente not in self.nos:
            self.alerta.registrar("CRITICO", f"Proponente não autorizado: {id_proponente}")
            return None
        
        hash_proposta = hashlib.sha256(f"{proposta}{time.time()}".encode()).hexdigest()
        bloco = {
            "hash": hash_proposta,
            "proposta": proposta,
            "proponente": id_proponente,
            "timestamp": time.time(),
            "votos": {},
            "status": "votacao",
            "hash_anterior": self.blockchain[-1]["hash"] if self.blockchain else "0"
        }
        self.blockchain.append(bloco)
        self.alerta.registrar("INFO", f"Nova proposta: {hash_proposta[:12]}... por {id_proponente}")
        return hash_proposta
    
    def votar(self, hash_proposta, id_no, voto):
        """Voto ponderado com auditoria"""
        if id_no not in self.nos or not self.nos[id_no].ativo:
            self.alerta.registrar("ALERTA", f"Voto inválido de nó inativo: {id_no}")
            return False
        
        for bloco in self.blockchain:
            if bloco["hash"] == hash_proposta and bloco["status"] == "votacao":
                bloco["votos"][id_no] = {
                    "voto": voto,
                    "peso": self.nos[id_no].peso,
                    "timestamp": time.time()
                }
                self.alerta.registrar("INFO", f"Voto {voto} registrado: {id_no}")
                return True
        
        self.alerta.registrar("ALERTA", f"Proposta não encontrada: {hash_proposta[:8]}")
        return False
    
    def verificar_consenso(self, hash_proposta):
        """Verifica consenso 67% + quorum 51%"""
        for bloco in self.blockchain:
            if bloco["hash"] == hash_proposta:
                peso_total = sum(no.peso for no in self.nos.values() if no.ativo)
                peso_votante = sum(v["peso"] for v in bloco["votos"].values())
                peso_sim = sum(v["peso"] for v in bloco["votos"].values() if v["voto"] == "sim")
                
                quorum = peso_votante / peso_total if peso_total > 0 else 0
                percentual = peso_sim / peso_votante if peso_votante > 0 else 0
                
                if quorum < self.limiar_quorum:
                    self.alerta.registrar("ALERTA", f"Quorum insuficiente: {quorum*100:.1f}%")
                    return False
                
                if percentual >= self.limiar_consenso:
                    bloco["status"] = "aprovado"
                    self.alerta.registrar("CONSENSO", f"APROVADO com {percentual*100:.1f}% | Quorum: {quorum*100:.1f}%")
                    return True
                else:
                    self.alerta.registrar("INFO", f"Rejeitado: {percentual*100:.1f}%")
                    bloco["status"] = "rejeitado"
                    return False
        return False
    
    def detectar_anomalia(self):
        """Sistema de detecção de ataques e anomalias"""
        if len(self.nos) < 3:
            self.alerta.registrar("CRITICO", "Rede com menos de 3 nós ativos - Vulnerável")
        
        for bloco in self.blockchain[-5:]:
            if len(bloco["votos"]) == 0 and time.time() - bloco["timestamp"] > 3600:
                self.alerta.registrar("ALERTA", f"Proposta órfã detectada: {bloco['hash'][:8]}")
    
    def gerar_relatorio(self):
        """Relatório completo para auditoria"""
        return {
            "versao": self.versao,
            "autor": self.autor,
            "timestamp": datetime.now().isoformat(),
            "nos_ativos": len([n for n in self.nos.values() if n.ativo]),
            "total_propostas": len(self.blockchain),
            "aprovadas": len([b for b in self.blockchain if b["status"] == "aprovado"]),
            "hash_cadeia": hashlib.sha256(json.dumps(self.blockchain).encode()).hexdigest(),
            "logs": self.alerta.exportar_logs()
        }

# Inicialização IGNI-15 V8.1 SUPREMA
if __name__ == "__main__":
    print("="*60)
    print(f"  IGI-15 {IGNI15().versao} - PROTOCOLO ATIVO")
    print(f"  Autor: {IGNI15().autor}")
    print(f"  Sistema de Governança Distribuída + Alerta")
    print("="*60)
    
    igni = IGNI15()
    igni.detectar_anomalia()
    print("\nRede pronta. Aguardando nós e propostas...")
