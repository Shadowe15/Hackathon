# Capture The Flag (CTF) Challenges – Hackathon Series

Welcome to the repository hosting two beginner-friendly cybersecurity Capture The Flag challenges designed for hands-on learning and fun.

---

## Challenge 1: DNS Leak (Forensics)

### Overview
During a security incident simulation, sensitive data has been covertly leaked from a compromised machine via DNS queries. Your job is to analyze the provided network capture file and extract the secret flag hidden inside suspicious DNS queries.

### File Provided
- `dns_leak_big_troll_ctf.pcap` — A large network traffic capture with thousands of DNS queries.

### Objectives
- Use Wireshark or similar tools to filter DNS queries.
- Search for unusual subdomains.
- Reconstruct the base64-encoded flag from fragmented DNS subdomains.
- Decode the base64 string to reveal the flag.

### Flag Format
flag{dns_c4n_l34k_5ecrets}

### Tools Recommended
- Wireshark / tshark
- Command line utilities: grep, base64
- Text editor

---

## Challenge 2: Matryoshka JPG (Steganography / Forensics)

### Overview
Bombardino killed Tralalero and got away, but now he needs help from his allies at PES to hide secret information safely.
 Instead of sending normal messages, Bombardino stuffed his secrets—layer upon layer—inside a single image like a Matryoshka doll.

Your mission is to outsmart Bombardino by peeling back each hidden layer, cracking the password-protected archives, and uncovering the final flag. Just be prepared for some PES-inspired trolling in the image metadata!

### File Provided
- `Bombardino_crocodilo.jpg` — A JPEG image with appended password-protected ZIP archives.

### Objectives
- Identify hidden data inside the image using `binwalk` or similar forensic tools.
- Extract nested ZIP archives, find and apply the password (hint: check image metadata).
- Retrieve the secret flag inside the deepest archive.

### Flag Format
flag{n3st3d_st3g0_succ3ss}

### Tools Recommended
- binwalk
- unzip
- exiftool
- strings

---

## How to Run the Challenges

### DNS Leak
1. Open the .pcap file in Wireshark.
2. Filter DNS queries: `dns.flags.response == 0`
3. Extract and base64-decode the payload.

### Matryoshka JPG
1. Analyze image metadata for hints: `exiftool Bombardino_crocodilo.jpg`
2. Detect embedded files: `binwalk Bombardino_crocodilo.jpg`
3. Unzip password-protected archives using discovered password.

