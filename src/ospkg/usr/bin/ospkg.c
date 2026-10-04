#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>

#define BASE_DIR "/usr/share/ospkg"

// Verifica se o arquivo existe e é acessível
int file_exists(const char *path) {
    return access(path, F_OK) == 0;
}

// Executa o script usando o bash
int execute_script(const char *path) {
    if (!file_exists(path)) {
        printf("Erro: O script '%s' nao foi encontrado.\n", path);
        return 1;
    }

    char command[512];
    snprintf(command, sizeof(command), "bash \"%s\"", path);
    printf("-> Executando: %s\n", command);
    
    int result = system(command);
    return WEXITSTATUS(result);
}

void show_usage() {
    printf("Uso do ospkg (Gerenciador de Pacotes):\n");
    printf("  ospkg install <pacote|caminho/script.sh>\n");
    printf("  ospkg uninstall <pacote|caminho/script.sh>\n");
    printf("  ospkg update\n");
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        show_usage();
        return 1;
    }

    char target_path[512];
    const char *command = argv[1];

    // Comando: ospkg update
    if (strcmp(command, "update") == 0) {
        snprintf(target_path, sizeof(target_path), "%s/update/update.sh", BASE_DIR);
        return execute_script(target_path);
    }

    // Para install e uninstall, um pacote ou arquivo .sh deve ser informado
    if (argc < 3) {
        printf("Erro: Informe o nome do pacote ou o caminho do arquivo .sh\n");
        show_usage();
        return 1;
    }

    const char *pkg = argv[2];

    // Verificação: Se o argumento é direto um arquivo .sh existente no sistema
    if (strstr(pkg, ".sh") != NULL && file_exists(pkg)) {
        snprintf(target_path, sizeof(target_path), "%s", pkg);
        return execute_script(target_path);
    }

    // Comando: ospkg install <pacote>
    if (strcmp(command, "install") == 0) {
        snprintf(target_path, sizeof(target_path), "%s/receita/%s.sh", BASE_DIR, pkg);
        return execute_script(target_path);
    }

    // Comando: ospkg uninstall <pacote>
    if (strcmp(command, "uninstall") == 0) {
        snprintf(target_path, sizeof(target_path), "%s/app-uninstall/%s.sh", BASE_DIR, pkg);
        return execute_script(target_path);
    }

    printf("Erro: Comando '%s' desconhecido.\n", command);
    show_usage();
    return 1;
}
