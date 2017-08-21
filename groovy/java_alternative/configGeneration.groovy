/* ============================ */
/* Update this properties first */
/* ============================ */
JDK_HOME = '/usr/lib/jvm/java-8-oracle-amd64'
JDK_LINK = '/usr/lib/jvm/jdk1.8'
PRIORITY = 1820
/* ============================ */

def parentDirectory = new File(JDK_HOME).parent
def jdkName = new File(JDK_HOME).name
def linkName = new File(JDK_LINK).name

private List<String> getBinaries(String path) {
    def binaries = new File(path)
    if(!binaries.exists() || !binaries.directory) {
        return null
    }

    def binaryFiles = []
    binaries.eachFile() { file ->
        if(file.isFile() && file.canExecute()) {
            binaryFiles << file.name
        }

    }
    binaryFiles
}

def getJreBinaries() {
    return getBinaries("${JDK_HOME}/jre/bin")
}

def getJdkBinaries() {
    return getBinaries("${JDK_HOME}/bin")
}

if(! new File(JDK_HOME).exists()) {
    println "JDK_HOME not found in ${JDK_HOME}"
    return
}

if(!new File(JDK_LINK).exists()) {
    println "Create symbolic link before : ${JDK_LINK}"
    return

}

def jinfoFile = new File(".${linkName}.jinfo")
def alternativesFile = new File("alternatives.sh")
def ln = System.getProperty('line.separator')

if(jinfoFile.exists()) {
    jinfoFile.delete()
}
if(alternativesFile.exists()) {
    alternativesFile.delete()
}

jinfoFile << "alias=${linkName}$ln"
jinfoFile << "section=non-free$ln"

jreBinaries.each() {
   jinfoFile << "jre ${it} ${JDK_LINK}/jre/bin/${it}$ln"
   alternativesFile << "update-alternatives --install /usr/bin/${it} ${it}  ${JDK_LINK}/jre/bin/${it} ${PRIORITY}$ln"
}

def subJdk = jdkBinaries.findAll { !jreBinaries.contains(it)}
subJdk.each() {
    jinfoFile << "jdk ${it} ${JDK_LINK}/bin/${it}$ln"
    alternativesFile << "update-alternatives --install /usr/bin/${it} ${it}  ${JDK_LINK}/bin/${it} ${PRIORITY}$ln"
}

alternativesFile << "update-alternatives --install /usr/lib/xulrunner-addons/plugins/libjavaplugin.so xulrunner-1.9-javaplugin.so ${JDK_LINK}/jre/lib/amd64/libnpjp2.so ${PRIORITY}$ln"
alternativesFile << "update-alternatives --install /usr/lib/mozilla/plugins/libjavaplugin.so mozilla-javaplugin.so ${JDK_LINK}/jre/lib/amd64/libnpjp2.so ${PRIORITY}$ln"
