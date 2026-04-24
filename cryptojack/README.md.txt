# Cyber Range: Cryptojacking & Endpoint Forensics Simulator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📖 Overview
This project is an educational **Attack-Defense Simulator** designed for Digital Forensics and Incident Response (DFIR) and Security Operations Center (SOC) training. It provides a localized, three-phase Cyber Range environment to demonstrate a resource-exhaustion (Cryptojacking) attack lifecycle, from initial infection to endpoint detection and registry forensics.

## ✨ Features
The simulation is divided into a multi-tabbed Graphical User Interface (GUI), representing different stages of the incident response lifecycle:

* **Phase 1: Red Team (Infection)** * Simulates the execution of a trojanized software installer.
  * Establishes hidden persistence via Windows Registry Run keys (`HKCU\...\Run`).
* **Phase 2: Blue Team (Endpoint EDR)** * Simulates a live hardware monitor (CPU usage tracking).
  * Automated EDR heuristics that detect and suspend unauthorized processes communicating with known mining pool IPs.
* **Phase 3: DFIR Sandbox (Forensics)** * Static analysis tool for scanning simulated registry hives.
  * Extracts and flags persistent malicious Autorun entries for analyst remediation.

## 🚀 Installation & Usage

This project is built entirely using Python's standard library. No external dependencies are required.

**1. Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/cryptojacking-simulator.git](https://github.com/YOUR_USERNAME/cryptojacking-simulator.git)
cd cryptojacking-simulator