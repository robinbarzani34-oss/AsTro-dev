
set -e


RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_info()    { echo -e "${BLUE}[*]${NC} $1"; }
print_success() { echo -e "${GREEN}[+]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
print_error()   { echo -e "${RED}[-]${NC} $1"; }

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
        OS="windows"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        print_error "Nieznany system: $OSTYPE"
        exit 1
    fi
    print_info "Wykryto system: $OS"
}

check_python() {
    if command -v python3 &>/dev/null; then
        PYTHON="python3"
    elif command -v python &>/dev/null; then
        PYTHON="python"
    else
        print_error "Python nie jest zainstalowany!"
        exit 1
    fi
    print_success "Python znaleziony: $($PYTHON --version)"
}

setup_venv() {
    if [ ! -d ".venv" ]; then
        print_info "Tworzenie virtualenv..."
        $PYTHON -m venv .venv
        print_success "Virtualenv utworzony"
    else
        print_warning "Virtualenv już istnieje, pomijam"
    fi
}


check_venv() {
    if [[ "$OS" == "linux" || "$OS" == "macos" ]]; then
        if [[ -z "$VIRTUAL_ENV" ]]; then
            print_warning "Nie jesteś w virtualenv, aktywuję..."
        else
            print_success "Virtualenv już aktywny: $VIRTUAL_ENV"
        fi
    fi
}

activate_venv() {
    if [[ "$OS" == "windows" ]]; then
        VENV_ACTIVATE=".venv/Scripts/activate"
    else
        VENV_ACTIVATE=".venv/bin/activate"
    fi
    source "$VENV_ACTIVATE"
    print_success "Virtualenv aktywowany"
}

install_requirements() {
    if [ ! -f "requirements.txt" ]; then
        print_error "Brak pliku requirements.txt!"
        exit 1
    fi
    print_info "Instalowanie zależności..."
    pip install --upgrade pip -q
    pip install -r requirements.txt
    print_success "Zależności zainstalowane"
}

main() {
    echo -e "${BLUE}"
    echo "  ██████╗██╗     ██╗    ████████╗███████╗███╗   ███╗██████╗ ██╗      █████╗ ████████╗███████╗"
    echo " ██╔════╝██║     ██║    ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔══██╗╚══██╔══╝██╔════╝"
    echo " ██║     ██║     ██║       ██║   █████╗  ██╔████╔██║██████╔╝██║     ███████║   ██║   █████╗  "
    echo " ██║     ██║     ██║       ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══██║   ██║   ██╔══╝  "
    echo " ╚██████╗███████╗██║       ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗██║  ██║   ██║   ███████╗"
    echo "  ╚═════╝╚══════╝╚═╝       ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝"
    echo -e "${NC}"

    detect_os
    check_python
    setup_venv
    check_venv      
    activate_venv
    install_requirements

    echo ""
    print_success "Setup zakończony! Uruchom narzędzie:"
    if [[ "$OS" == "windows" ]]; then
        echo -e "  ${YELLOW}.venv\\Scripts\\activate${NC}"
    else
        echo -e "  ${YELLOW}source .venv/bin/activate${NC}"
    fi
    echo -e "  ${YELLOW}python main.py${NC}"
}

main