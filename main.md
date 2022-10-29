# Methodologie pentest

## <1> reconaisance

```bash
sans accer : 
	nmap -A -p- -v <ip>
	verifier les vertion sur expoit db
	il faut tout noter
	dirb <url> -X
	on peut preciser un aliace d'ip dasn /var/hosts
	plus pousser que nmap enume4linux pour scaner une machin

avec accer:
	/etc/shadow
	sudo -l
	LinPEAS enumeration de vecteur d'elevation de privileg
```

## <2> attaque

```bash
smbclien -> smb
hydra -> force brut sur plain de truc (a aprofondir)

une fois l'accet obtenus on revienb a l'etape 1
```

