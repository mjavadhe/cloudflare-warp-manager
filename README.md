
# Cloudflare WARP Manager

This project is a Python-based application to manage Cloudflare WARP, including connecting, disconnecting, checking status, and setting DNS. The application provides a graphical user interface (GUI) built using `tkinter`.

## Requirements

- Python 3.6+
- Linux (Ubuntu/Debian-based or RedHat-based distributions)
- Cloudflare WARP installed

## Install required Python packages

```bash
pip3 install -r requirements.txt
```

### Prerequisites

1. Install Python and `pip` (Python package manager).
2. Create a virtual environment for the project.
3. Install required dependencies using `pip`.

## Steps to Install Cloudflare WARP on Linux

Before running the application, you need to install Cloudflare WARP on your Linux machine.

### For Debian/Ubuntu-based systems:

1. Update your package list:

```bash
sudo apt update
```

2. Install Cloudflare's official package repository:

```bash
curl -s https://pkg.cloudflare.com/install.sh | sudo bash
```

3. Install `warp-cli`:

```bash
sudo apt install cloudflare-warp
```

4. Register with Cloudflare:

```bash
warp-cli registration new
```

5. Connect to Cloudflare WARP:

```bash
warp-cli connect
```

6. Run Cloudflare WARP Manager:

```bash
python3 cloadflare-warp-manager.py  
```

### For RedHat/CentOS-based systems:

1. Install the necessary dependencies:

```bash
sudo yum install -y curl
```

2. Add Cloudflare's repository:

```bash
curl -s https://pkg.cloudflare.com/install.sh | sudo bash
```

3. Install Cloudflare WARP:

```bash
sudo yum install cloudflare-warp
```

4. Register with Cloudflare:

```bash
warp-cli registration new
```

5. Connect to Cloudflare WARP:

```bash
warp-cli connect
```

### Check if WARP is running:

```bash
warp-cli status
```

## Setting Up the Python Application

### 1. Clone the Repository:

Clone the repository from GitHub:

```bash
git clone https://github.com/mjavadhe/cloudflare-warp-manager.git
cd cloudflare-warp-manager
```

### 2. Set up a Virtual Environment:

Create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux
```

### 3. Install the Dependencies:

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Running the Application:

Run the application using:

```bash
python app.py
```

### Commands Summary:

- **Connect to WARP**: `warp-cli connect`
- **Disconnect from WARP**: `warp-cli disconnect`
- **Check WARP status**: `warp-cli status`
- **Set DNS**: `warp-cli set-dns <dns_addresses>`

## About Me

Hello, I am Mohammad Javad Heydarpanah, a Python and Django programmer. I hope you enjoy this program. In the "Tell Me" section, you can see ways to contact me. If you want to contact me, good luck and enjoy.

## Contact Me

- [GitHub](https://github.com/mjavadhe)
- [LinkedIn](https://linkedin.com/in/mohamadjavad-heydarpanah-13377223b/)
- [Telegram](https://t.me/mjavad_he)
- [Instagram](https://instagram.com/mjavad.he)

## Help

This program is an open-source software written in Python. If you want to make changes to this program, you can clone the repository, apply the necessary changes, and run the program.

- [Cloudflare WARP Manager repository](https://github.com/mjavadhe/cloudflare-warp-manager)

## Download the application

- (https://github.com/mjavadhe/cloudflare-warp-manager/raw/refs/heads/master/Application/cloudflare-warp-manager)