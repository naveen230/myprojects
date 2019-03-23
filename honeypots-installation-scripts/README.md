# Installation scripts for Cowrie and Dionaea honeypots

## What is a honeypot?

In computer terminology, a honeypot is a computer security mechanism set to detect, deflect, or, in some manner, counteract attempts at unauthorized use of information systems. Generally, a honeypot consists of data (for example, in a network site) that appears to be a legitimate part of the site, but is actually isolated and monitored, and that seems to contain information or a resource of value to attackers, who are then blocked. This is similar to police sting operations, colloquially known as "baiting," a suspect

![wikipedia-img](https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Honeypot_diagram.jpg/220px-Honeypot_diagram.jpg)

Source: Wikipedia

## What is Cowrie?

Cowrie is a medium interaction SSH and Telnet honeypot designed to log brute force attacks and the shell interaction performed by the attacker.
Cowrie is developed by Michel Oosterhof

Official repository: https://github.com/cowrie/cowrie

## What is Dionea?

Dionaea's intention is to trap malware exploiting vulnerabilities exposed by services offerd to a network, the ultimate goal is gaining a copy of the malware.

Official Documentation: https://dionaea.readthedocs.io/en/latest/introduction.html#

Official repository: https://github.com/DinoTools/dionaea

## Testing

These scripts are tested on Ubuntu Mate LTS 16.04 with Raspberry Pi 3. All the dependencies required are installed using the script.

## Usage

1) Clone the repository
2) cd into the folder
3) chmod u+x *.sh (Makes scripts executable)
4) ./cowrie.sh
5) ./dionaea.sh

Run as sudo if errors occured.





