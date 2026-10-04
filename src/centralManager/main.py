# Central Manager for Oxyohan OS
# 0.0.0.1a
# Criado por JohnzinOmochain

import os
import sys
import subprocess
import time

# Mantem o programa aberto
session = True

def menuserviceMgr():
  print("========================================")
  print("|           Service Manager            |")
  print("|      Criado por JohnzinOmochain      |")
  print("========================================")
  
def userserviceMgr():
  print("========================================")
  print("|            User Manager              |")
  print("|      Criado por JohnzinOmochain      |")
  print("========================================")

def verificar_root():
  """Garante que o script está sendo executado como root."""
  if os.geteuid() != 0:
    print(
        "Erro 102 - Você não tem permissão de root (Use sudo python3 main.py)"
    )
    sys.exit(1)
verificar_root()

#Limpa a tela do terminal
def limpar_tela():
  os.system("clear" if os.name == "posix" else "cls")

#pausa
def pausar():
  input("\nPressione [Enter] para continuar...")

# Lets see Partit
def ver_particoes():
  limpar_tela()
  print("=== Partições Disponíveis (lsblk) ===")
  subprocess.run(["lsblk", "-f"])
  pausar()
  
def versionYeah():
  limpar_tela()
  try:
    subprocess.run(["sudo", "fastfetch"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o fastfetch", file=sys.stderr)
    pausar()
  print(subprocess.run(["uname", "-a"], check=True))
  pausar()
  
def yamatest():
  limpar_tela()
  print("Não implementado...")
  pausar()
  
def cfdisk():
  try:
    subprocess.run(["sudo", "cfdisk"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o cfdisk", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o cfdisk não foi encontrado", file=sys.stderr)
    pausar()
    
def btop():
  try:
    subprocess.run(["sudo", "btop"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o btop", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o btop não foi encontrado", file=sys.stderr)
    pausar()
    
def htop():
  try:
    subprocess.run(["sudo", "htop"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o htop", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o htop não foi encontrado", file=sys.stderr)
    pausar()
    
def nmtui():
  try:
    subprocess.run(["sudo", "nmtui"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o nmtui", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o nmtui não foi encontrado", file=sys.stderr)
    pausar()
    
def nano():
  try:
    subprocess.run("nano", check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o nano", file=sys.stderr)
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o nano não foi encontrado", file=sys.stderr)
    
def pingYeah():
  try:
    subprocess.run(["ping", "-c", "3", "8.8.8.8"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o ping", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o ping não foi encontrado", file=sys.stderr)
    pausar()
    
def XorgInit():
  try:
    subprocess.run("startx", check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o Xorg", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o Xorg não foi encontrado", file=sys.stderr)
    pausar()
    
# Service Manager
def systemctl():
  limpar_tela()
  menuserviceMgr()
  print("1 - Voltar ao Início")
  print("2 - Ver Status dos Servicos")
  print("3 - Parar um servico")
  print("4 - Forcar a parada de um servico")
  print("5 - Iniciar um servico")
  print("6 - Reiniciar um servico")
  print("7 - Listar os Serviços ATIVOS no momento")
  
  inpush = input('-> ')
  
  if inpush == "1":
    sess = False
  elif inpush == "2":
    ctlStatus()
  elif inpush == "3":
    ctlStop()
  elif inpush == "4":
    ctlFkl()
  elif inpush == "5":
    ctlStart()
  elif inpush == "6":
    ctlRes()
  elif inpush == "7":
    listAct()
  else:
    print("Comando não detectado")
    
def ctlStatus():
  try:
    subprocess.run(["systemctl", "status"], check=True)
    systemctl()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o SystemCtl", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o SystemCtl não foi encontrado", file=sys.stderr)
    pausar()
    
def listAct():
  try:
    limpar_tela()
    subprocess.run(["systemctl", "list-units", "--type=service", "--state=running", "--no-pager"], check=True)
    pausar()
    systemctl()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o SystemCtl", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o SystemCtl não foi encontrado", file=sys.stderr)
    pausar()
    
def ctlStop():
  limpar_tela()
  print("==== Parar um serviço ====")
  print("Digite o servico (NÃO precisa colocar '.service' no final)")
  stopser = input('-> ').strip()
  
  checar_existencia1 = subprocess.run(
    ["systemctl", "list-unit-files", f"{stopser}.service"],
    stdout=subprocess.PIPE, # Captura a saída de texto
    stderr=subprocess.DEVNULL,
    text=True
  )
  
  if stopser not in checar_existencia1.stdout or not stopser:
    print(f"\nErro 201 - O serviço '{stopser}' não foi encontrado no sistema!")
    print("Verifique se você digitou o nome correto: (ex: docker, nginx, bluetooth).")
    pausar()
    return
  
  if stopser.upper() == "Q":
    return
  else:
    try:
      subprocess.run(["sudo", "systemctl", "stop", stopser], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
      print("\n Processo parado com sucesso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 202 - Você digitou errado ou não foi possivel parar o processo")
      pausar()
      
def ctlStart():
  limpar_tela()
  print("==== Iniciar um serviço ====")
  print("Digite o servico (NÃO precisa colocar '.service' no final)r")
  stopsta = input('-> ').strip()
  
  checar_existencia2 = subprocess.run(
    ["systemctl", "list-unit-files", f"{stopsta}.service"],
    stdout=subprocess.PIPE, # Captura a saída de texto
    stderr=subprocess.DEVNULL,
    text=True
  )
  
  if stopsta not in checar_existencia2.stdout or not stopsta:
    print(f"\nErro 201 - O serviço '{stopsta}' não foi encontrado no sistema!")
    print("Verifique se você digitou o nome correto: (ex: docker, nginx, bluetooth).")
    pausar()
    return
  
  if stopsta.upper() == "Q":
    return
  else:
    try:
      subprocess.run(["sudo", "systemctl", "start", stopsta], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
      print("\n Processo iniciado com sucesso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 202 - Você digitou errado ou não foi possivel iniciar o processo porque provavelmente já foi iniciado")
      pausar()
      
def ctlRes():
  limpar_tela()
  print("==== Reiniciar um serviço ====")
  print("Digite o servico (NÃO precisa colocar '.service' no final)")
  stopres = input('-> ').strip()
  
  checar_existencia3 = subprocess.run(
    ["systemctl", "list-unit-files", f"{stopres}.service"],
    stdout=subprocess.PIPE, # Captura a saída de texto
    stderr=subprocess.DEVNULL,
    text=True
  )
  
  if stopres not in checar_existencia3.stdout or not stopres:
    print(f"\nErro 201 - O serviço '{stopres}' não foi encontrado no sistema!")
    print("Verifique se você digitou o nome correto: (ex: docker, nginx, bluetooth).")
    pausar()
    return
  
  if stopres.upper() == "Q":
    return
  else:
    try:
      subprocess.run(["sudo", "systemctl", "restart", stopres], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
      print("\n Processo reiniciado com sucesso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 202 - Você digitou errado ou não foi possivel reiniciar o processo")
      pausar()
      
def ctlFkl():
  limpar_tela()
  print("==== FORÇAR a parada um serviço ====")
  print("⚠️  Isso força a parada imediata do processo. Então use COM MODERACÃO PRA NÃO F**** o sistema")
  print("Digite o servico (NÃO precisa colocar '.service' no final)")
  stopfkl = input('-> ').strip()
  
  checar_existencia4 = subprocess.run(
    ["systemctl", "list-unit-files", f"{stopfkl}.service"],
    stdout=subprocess.PIPE, # Captura a saída de texto
    stderr=subprocess.DEVNULL,
    text=True
  )
  
  if stopfkl not in checar_existencia4.stdout or not stopfkl:
    print(f"\nErro 201 - O serviço '{stopfkl}' não foi encontrado no sistema!")
    print("Verifique se você digitou o nome correto: (ex: docker, nginx, bluetooth).")
    pausar()
    return
  
  if stopfkl.upper() == "Q":
    return
  else:
    try:
      subprocess.run(["sudo", "systemctl", "kill", stopfkl], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
      print("\n Processo parado a FORÇA (Kill) com sucesso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 202 - Você digitou errado ou não foi possivel reiniciar o processo")
      pausar()

def verificar_integridade():
  """Funcionalidade extra: Verificação rápida de espaço em disco e pacotes."""
  limpar_tela()
  print("=== Informações e Diagnóstico do Oxyohan ===")
  print("\n1. Espaço em Disco (df -h):")
  subprocess.run(["df", "-h"])
  print("\n2. Memória RAM Livre:")
  subprocess.run(["free", "-h"])
  pausar()
  
# Speedtest Cli Yeah
def stcli():
  limpar_tela()
  try:
    subprocess.run("speedtest-cli", check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o Speed Test Cli", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o speedtest-cli não foi encontrado", file=sys.stderr)
    pausar()
    
# Logs
def logs():
  limpar_tela()
  try:
    with open("logKernel.txt", "w") as arquivo:
      subprocess.run(["dmesg"], stdout=arquivo, check=True)
    subprocess.run(["sudo", "nano", "logOxyohan.txt"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o dmesg", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o dmesg não foi encontrado", file=sys.stderr)
    pausar()
    
# APT update
def aptUpd():
  limpar_tela()
  try:
    subprocess.run(["sudo", "apt", "update"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o APT", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o apt não foi encontrado", file=sys.stderr)
    pausar()
    
# APT upgrade
def aptUpg():
  limpar_tela()
  try:
    subprocess.run(["sudo", "apt", "upgrade"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o APT", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o apt não foi encontrado", file=sys.stderr)
    pausar()
    
# See hardware
def lshw():
  try:
    subprocess.run(["sudo", "lshw"], check=True)
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o lshw", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o lshw não foi encontrado", file=sys.stderr)
    pausar()

# User Manager
def userctlYeah():
  limpar_tela()
  userserviceMgr()
  print("1 - Voltar ao Início")
  print("2 - Listar os Usuários")
  print("3 - Criar um Usuário (adduser)")
  print("4 - DELETAR um Usuário (deluser + perl)")
  print("5 - Mudar a SENHA de um usuario")
  print("6 - Mudar a SENHA do ROOT")
  
  inpush = input('-> ')
  
  if inpush == "1":
    sess = False
  elif inpush == "2":
    listUsr()
  elif inpush == "3":
    addUsr()
  elif inpush == "4":
    delUsr()
  elif inpush == "5":
    passUsr()
  elif inpush == "6":
    RootAss()
  else:
    print("Comando não detectado")
    
def listUsr():
  limpar_tela()
  print("=== Usuários no Sistema ===")
  try:
    subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o cut", file=sys.stderr)
    pausar()
  except FileNotFoundError:
    print("Erro 707 - Por algum motivo o cut não foi encontrado", file=sys.stderr)
    pausar()

def addUsr():
  limpar_tela()
  print("=== Adicionar um Usuário ===")
  print("Digite o nome (q - sair):")
  addname = input("-> ")
  
  if addname == "":
    print("Nome inválido")
    pausar()
  elif addname == "q":
    pausar()
  else:
    try:
      subprocess.run(["sudo", "adduser", addname], check=True)
      print("Usuário adicionado com susseso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 301 - Não foi possivel criar o usuário, provavelmente não tem permissão ou aconteceu de não funcioanr o comando 'adduser'", file=sys.stderr)
      pausar()
      
def delUsr():
  limpar_tela()
  print("=== DELETAR um Usuário ===")
  print("ISSO TAMBÉM DELETARÁ A PASTA DO USUÁRIO EM CASO DE VIRUS OU MALWARE")
  print("Digite o nome (q - sair):")
  addname = input("-> ")
  
  if addname == "":
    print("Nome inválido")
    pausar()
  elif addname == "q":
    pausar()
  else:
    try:
      subprocess.run(["sudo", "deluser", "--remove-home", addname], check=True)
      print("Usuário EVAPORADO com susseso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 301 - Não foi possivel criar o usuário, provavelmente não tem permissão, digitou o nome errado ou aconteceu de não funcioanr o comando 'adduser'", file=sys.stderr)
      pausar()
      
def passUsr():
  limpar_tela()
  print("=== Mudar a SENHA um Usuário ===")
  print("LEMBRE-SE da senha")
  print("Digite o nome do usuário (q - sair):")
  addname = input("-> ")
  
  if addname == "":
    print("Nome inválido")
    pausar()
  elif addname == "q":
    pausar()
  else:
    try:
      subprocess.run(["sudo", "passwd", addname], check=True)
      print("Usuário ALTERADO com susseso!")
      pausar()
    except subprocess.CalledProcessError:
      print("Erro 301 - Não foi possivel criar o usuário, provavelmente não tem permissão, digitou o nome errado ou aconteceu de não funcioanr o comando 'adduser'", file=sys.stderr)
      pausar()
      
def RootAss():
  limpar_tela()
  try:
    subprocess.run(["sudo", "passwd", "root"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para o alterar, BAKA!", file=sys.stderr)
    pausar()
    
def inxi():
  limpar_tela()
  try:
    subprocess.run(["sudo", "inxi"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Erro 103 - Você não tem permissão de root para rodar o inxi, BAKA!", file=sys.stderr)
    pausar()
    
def syu():
  limpar_tela()
  try:
    subprocess.run(["sudo", "pacman", "-Syu"], check=True)
    pausar()
  except subprocess.CalledProcessError:
    print("Você cancelou a atulização", file=sys.stderr)
    pausar()

# Input e ações
while session == True:
  # Cabecalho
  limpar_tela()
  print("===========================================================")
  print("|            Ultra Oxyohan Central Manager                |")
  print("|             Criado por JohnzinOmochain                  |")
  print("----------------------------------------------------------")
  print("|                      0.0.0.1a                           |")
  print("===========================================================")
  print("1 - Sair")
  print("2 - Mostrar data e hora")
  print("3 - Mostrar as particoes")
  print("4 - Gerenciar partições (cfdisk)")
  print("5 - Diagnóstico rápido (Espaço em disco / RAM)")
  print("6 - Monitorar o Sistema (6.1 - btop | 6.2 - htop) (Ctrl+C sai do btop e F10 do htop)")
  print("7 - Gerenciar redes (nmtui)")
  print("8 - Abrir o NANO (Para consertar algum arquivo de configuração)")
  print("9 - Verificar o PING")
  print("10 - Iniciar o Xorg")
  print("11 - Reiniciar")
  print("12 - Ver a versão do sistema")
  print("13 - Gerenciador de Servicos")
  print("14 - Testar a velocidade da Internet (Speed Test Cli)")
  print("15 - Ver os logs do kernel")
  print("16 - Atualizar o sistema (16.1 - APT update | 16.2 - APT upgrade)")
  print("17 - Gerenciador de Usuários")
  print("18 - Ver RESUMO do hardware do PC")
  inpuu = input('-> ')
  if inpuu == "1":
    # Fecha o programa
    session = False
  elif inpuu == "2":
    print(subprocess.run("date"))
  elif inpuu == "3":
    ver_particoes()
    limpar_tela()
  elif inpuu == "4":
    cfdisk()
    limpar_tela()
  elif inpuu == "5":
    verificar_integridade()
    limpar_tela()
  elif inpuu == "6.1":
    btop()
    limpar_tela()
  elif inpuu == "6.2":
    htop()
    limpar_tela()
  elif inpuu == "7":
    nmtui()
    limpar_tela()
  elif inpuu == "8":
    nano()
    limpar_tela()
  elif inpuu == "9":
    pingYeah()
    print("")
  elif inpuu == "10":
    XorgInit()
  elif inpuu == "11":
    print(subprocess.run("reboot"))
  elif inpuu == "12":
    versionYeah()
    limpar_tela()
  elif inpuu == "13":
    systemctl()
    limpar_tela()
  elif inpuu == "14":
    stcli()
    limpar_tela()
  elif inpuu == "15":
    logs()
    limpar_tela()
  elif inpuu == "16.1":
    aptUpd()
    limpar_tela()
  elif inpuu == "16.2":
    aptUpg()
    limpar_tela()
  elif inpuu == "17":
    userctlYeah()
    limpar_tela()
  elif inpuu == "18":
    inxi()
    limpar_tela()
  else:
    limpar_tela()
    print("Comando não encontrado")
    pausar()
