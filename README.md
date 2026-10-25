# File Integrity Verification using Hash Functions

[![University](https://img.shields.io/badge/University-University%20of%20Ioannina-blue.svg)](https://www.uoi.gr)
[![Department](https://img.shields.io/badge/Department-Informatics%20%26%20Telecommunications-lightgrey.svg)](https://www.cs.uoi.gr/)
[![Course](https://img.shields.io/badge/Course-Systems%20Security-orange.svg)]()
[![Language](https://img.shields.io/badge/Language-Python-blueviolet.svg)]()

A Python-based cybersecurity tool designed to calculate cryptographic hashes and verify file integrity. The project supports multiple hashing algorithms and implements defenses against common cryptographic vulnerabilities, such as timing attacks.

---

## 📚 Table of Contents
1. [Overview](#-overview)
2. [Theoretical Background](#-theoretical-background)
3. [Security & Performance Optimizations](#-security--performance-optimizations)
4. [Getting Started & Execution](#-getting-started--execution)
5. [Author & Credits](#-author--credits)

---

## 🔍 Overview
File integrity ensures that a file has not been altered during transfer, storage, or processing. This program computes the digital "fingerprint" (hash) of a file using algorithms like **MD5, SHA-1, SHA-256, and SHA3-256**. By comparing a known hash with the current hash of a file, the system can instantly detect if even a single byte has been maliciously or accidentally modified.

---

## 📐 Theoretical Background
### Hash Functions
A hash function $h = H(M)$ maps a message $M$ of arbitrary length to a fixed-length hash value. It acts as an authenticator.
- **MD5:** Produces a 128-bit hash. Historically used for digital signatures but currently considered insecure due to collision vulnerabilities.
- **SHA-1 / SHA-256:** Part of the Secure Hash Algorithm family. SHA-256 produces a 256-bit hash and provides a high level of security (128-bit security strength).
- **SHA3-256:** The latest generation of hash functions, built on the Sponge Construction rather than the Merkle-Damgård structure used by its predecessors.

---

## 🛡️ Security & Performance Optimizations

### 1. Mitigating Timing Attacks
Timing attacks exploit the time variations in string comparisons to guess hashes byte-by-byte. This program utilizes `hmac.compare_digest()` for **constant-time comparison**, ensuring that the verification process does not leak information through response times.

### 2. Large File Handling (>1GB)
Loading massive files entirely into RAM causes memory overflow. The `calculate_file_hash` function utilizes a generator and a buffer to read files in **64KB chunks**. This specific chunk size provides an optimal balance between minimizing I/O system calls and maintaining low RAM consumption.

---

## 🚀 Getting Started & Execution
1. Ensure Python 3.x is installed.
2. Run the script: `python ntontouu.py`
3. **Menu Options:**
   - `[1]`: Calculate the hash of a file (choose between MD5, SHA-1, SHA-256, SHA3-256).
   - `[2]`: Verify integrity by providing the file path, the original hash, and the algorithm used.
   - `[3]`: Exit.
4. Use the provided `dokimi.txt` to test modifications and observe hash mismatches.

---

## 📝 Author & Academic Use
- **Student:** Maria Alexandra Ntontou (ΜΑΡΙΑ ΑΛΕΞΑΝΔΡΑ ΝΤΟΝΤΟΥ)
- **Student ID:** 2799
- **Institution:** University of Ioannina — Department of Informatics and Telecommunications
- **Course:** Systems Security (Ασφάλεια Συστημάτων) — 1st Assignment
