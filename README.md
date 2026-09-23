
# OxyohanOS
<div align="center">

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Base](https://img.shields.io/badge/Base-Debian-A81D33?logo=debian&logoColor=white)](https://www.debian.org)
[![Installer](https://img.shields.io/badge/Installer-Calamares-1B7A9C?logo=linux&logoColor=white)](https://calamares.io/)
[![Language](https://img.shields.io/badge/Language-Shell_Script-4E8098?logo=gnu-bash&logoColor=white)]()
[![Arch](https://img.shields.io/badge/Arch-x86__64-informational.svg)]() 
[![YouTube Gabriel do Linux](https://img.shields.io/badge/YouTube-Gabriel_do_Linux-FF0000?logo=youtube&logoColor=white)](https://youtube.com/@fprowindows?si=Ut4MthfTAL6Yf5ih)
[![WebSite](https://img.shields.io/badge/WebSite-OxyohanOS-blue?style=flat&logo=google-chrome&logoColor=white)](https://johnzin-wakawaka.github.io/OxyohanOS/)
[![YouTube](https://img.shields.io/badge/YouTube-omochain-FF0000?style=flat&logo=youtube&logoColor=white)](https://youtube.com/@johnzinomochain?si=dPvf7zzrf67kuxji)
[![Non-Profit](https://img.shields.io/badge/Project-Non--Profit-00A86B?logo=heart&logoColor=white)]()
[![GitHub Release](https://img.shields.io/github/v/release/linux-oxy-retro-cyber/ODE-oxy-os-debian-edition?color=blue&logo=github)](https://github.com/linux-oxy-retro-cyber/ODE-oxy-os-debian-edition/releases)
[![Indie](https://img.shields.io/badge/Type-Indie_Project-FF4500?logo=rocket&logoColor=white)]()
[![Community](https://img.shields.io/badge/Project-Community-7289DA?logo=github&logoColor=white)]()
</div>
---


Bem-vindo à documentação oficial do **Universo Oxy**, um ecossistema de distribuições Linux projetado para diferentes perfis de usuários, unindo o melhor da estabilidade, customização e desenvolvimento. 

Este projeto é mantido em colaboração oficial entre os canais:
*   🎬 **Gabriel (fprowindows):** [Acesse o Canal no YouTube](https://youtube.com/@fprowindows?si=Ut4MthfTAL6Yf5ih)
*   🎬 **JohnzinOmochain:** [Acesse o Canal no YouTube](https://youtube.com/@johnzinomochain?si=dPvf7zzrf67kuxji)

---

## 🚀 Nossas Distribuições

O ecossistema se divide em duas ramificações principais, ambas utilizando atualmente a interface **XFCE**, garantindo leveza máxima e alto desempenho.
![wall](imagens/WallpaperYohan.png)
### 🎨 OxyohanOS
*   **Desenvolvedor:** Johnzin (`@JohnzinOmochain`)
*   **sub desenvolvedor** Gabriel Ramos Barbosa
*   **Foco principal:** Uso normal/cotidiano e experiência de usuário de ponta.
*   **Base do Sistema:** Utiliza a base estável modificada do projeto principal, adaptada para entregar um sistema extremamente bonito, fluido e pronto para as tarefas do dia a dia.
*   **Público-alvo:** Usuários comuns e desenvolvedores que buscam um sistema moderno, customizado visualmente e prático para navegar, estudar e trabalhar.


---

## 🛠️ Filosofia do Ecossistema

O Universo Oxy nasceu da ideia de que um sistema operacional não precisa ser genérico. Enquanto a **Oxy Base** entrega o motor bruto, estável e otimizado para codificação pesada, o **OxyohanOS** lapida essa estrutura para entregar uma interface bonita e acessível para o uso diário. 

Navegue pelo menu lateral para acessar o guia de instalação, documentação do kernel e repositórios de pacotes de cada versão!

## Contato:
JohnzinOmochain: johnzincontato@gmail.com
<br>
Gabriel do Linux (@fprowindows): apeludoff120@gmail.com
<br>
OxyohanOfficial: oxys.contact.official@gmail.com
---
## Licença e Compatibilidade de Hardware

Este sistema e seu código-fonte original (scripts de otimização, ajustes de kernel e configurações) são distribuídos sob a licença **GNU General Public License v3.0 (GPLv3)**.

Para garantir compatibilidade imediata de hardware (como placas Wi-Fi, Bluetooth e touchpads) em notebooks e MacBooks, o sistema inclui drivers e firmwares pré-compilados redistribuídos a partir dos repositórios oficiais `non-free` e `non-free-firmware` da distribuição Debian.
---
## Trabalhando
**Oxys OS**: nao existe mas pois ha outro projeto com um nome parecido

**OxyohanOS**: Projetando a Build 35...

------

## 🤝 Contribuições da Comunidade

Este é um projeto independente e comunitário, e contribuições são muito bem-vindas! Se você deseja enviar melhorias, correções de bugs, scripts ou modificações para o projeto, por favor, siga as regras abaixo para o envio:

🛠️ Diretrizes para Envio de Pull Requests (PR)

Para manter a organização, estabilidade e integridade do repositório, todas as contribuições via Pull Request devem seguir estritamente as regras de estrutura e documentação abaixo.
1. Requisitos de Estrutura e Escopo

    Preservação da Estrutura: A árvore e a hierarquia de pastas originais do repositório devem ser mantidas intactas.

    Substituição de Pacotes e Arquivos:

        Você só deve alterar ou substituir arquivos/pacotes existentes caso eles mantenham o mesmo nome exato do arquivo original.

        Caso seja necessário criar, mover ou renomear arquivos/pastas, você deve fornecer uma justificativa técnica clara na descrição do Pull Request.

2. Identificação do Contribuidor (OBRIGATÓRIO)

    Todo Pull Request deve incluir um arquivo texto de identificação na raiz do projeto (ou no diretório da alteração):

        Nome do arquivo: CONTRIBUTORS.txt (ou CONTRIBUTOR.txt)

        Conteúdo: Nome completo do desenvolvedor, usuário do GitHub e uma breve descrição da contribuição.

3. Documentação e Changelog (OBRIGATÓRIO)

Junto ao envio do Pull Request (ou dentro da pasta do pacote alterado), é obrigatório fornecer um arquivo README.md ou CHANGELOG.log contendo:

    Escopo das Modificações: Relação detalhada de todos os pacotes, scripts ou configurações alterados/adicionados.

    Justificativa Técnica: Explicação clara sobre o motivo da mudança, detalhando qual bug foi corrigido, qual ganho de desempenho foi obtido ou qual melhoria foi implementada.

4. Alternativa de Envio via Pacote Compactado

Caso o contribuidor opte por enviar as alterações via e-mail ou canal de suporte listado na documentação do projeto:

    Os arquivos devem ser empacotados mantendo a estrutura de diretórios original nos formatos .zip, .tar.gz ou .tar.xz.

    O pacote deve conter o arquivo de identificação (CONTRIBUTORS.txt) e o log explicativo das alterações.

    ⚠️ Atenção: Pull Requests que apresentem arquivos desorganizados, alterações na estrutura de pastas sem justificativa, ou que omitam a documentação obrigatória serão recusados (closed) sem análise prévia ou integração ao branch principal.
