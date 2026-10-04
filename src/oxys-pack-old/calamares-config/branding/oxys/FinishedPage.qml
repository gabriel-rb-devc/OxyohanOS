import QtQuick 2.0
import QtQuick.Layouts 1.1

Item {
    id: root

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: asciiLogo
            Layout.alignment: Qt.AlignHCenter
            text: "
  ____   __  __ __     __ ____    ___   ____  
 / __ \\  \\ \\/ / \\ \\   / // ___|  / _ \\ / ___| 
| |  | |  \\  /   \\ \\ / / \\___ \\ | | | |\\___ \\ 
| |__| |  /  \\    \\ V /   ___) || |_| | ___) |
 \\____/  /_/\\_\\    \\_/   |____/  \\___/ |____/ 
                                              "
            font.family: "Monospace"
            font.pixelSize: 10
            color: "#4d7079" // Ciano/Azul cibernético
            horizontalAlignment: Text.AlignHCenter
        }

        Text {
            id: mainText
            Layout.alignment: Qt.AlignHCenter
            text: "Bem-vindo ao Oxys OS."
            font.pixelSize: 18
            color: "#FFFFFF"
            horizontalAlignment: Text.AlignHCenter
        }

        Text {
            id: secondaryText
            Layout.alignment: Qt.AlignHCenter
            text: "O processo foi concluído com sucesso."
            font.pixelSize: 14
            color: "#FFFFFF"
            horizontalAlignment: Text.AlignHCenter
        }
    }
}
