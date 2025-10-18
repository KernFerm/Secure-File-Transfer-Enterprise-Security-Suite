# 🔐 Secure File Transfer - Enterprise Security Suite v3.4.01c34

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.4.01c34-brightgreen.svg)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](README.md)
[![Security](https://img.shields.io/badge/security-enterprise%20grade-red.svg)](README.md#security--privacy)
[![Network](https://img.shields.io/badge/network-intelligent%20discovery-orange.svg)](README.md#enhanced-network-discovery)
[![Encryption](https://img.shields.io/badge/encryption-Fernet%20AES-blue.svg)](README.md#advanced-security-features)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-purple.svg)](README.md#modern-user-interface)
[![Status](https://img.shields.io/badge/status-production%20ready-success.svg)](README.md)

A professional, secure file transfer application with **enhanced network discovery**, multi-antivirus security support, and enterprise-grade trusted device management. Features intelligent device naming, real-time network scanning, and a modern CustomTkinter interface with comprehensive security features.

## ✨ What's New in v3.4.01c34

### 🚀 **Enhanced Network Discovery**
- **Smart Device Naming**: Real hostname detection with intelligent fallbacks
  - `DESKTOP-ABC123` - Your actual computer names when available
  - `Main-Router` - Primary network gateway (.1 addresses)
  - `Workstation-114` - Desktop/laptop computers (100-150 range)
  - `Infrastructure-41` - Network equipment (11-50 range)
  - `Server-156` - Server devices (151-199 range)
  - `Mobile-Device-201` - Mobile/IoT devices (200-254 range)

- **Multi-Method Discovery**: 
  - **DNS Reverse Lookup**: Finds real computer names like "DESKTOP-ABC123"
  - **NetBIOS Queries**: Windows computer name resolution
  - **ARP Table Scanning**: Pre-discovery of active devices
  - **Port Detection**: Smart device classification by open services
  - **Ping + Port Scanning**: Combined reachability testing

- **Optimized Performance**:
  - **500ms timeouts** for DNS/NetBIOS (balanced speed vs accuracy)
  - **No hanging** during network scans
  - **Intelligent caching** of discovered devices
  - **Real-time updates** as devices come online

### 🛡️ **Multi-Antivirus Protection**
- **ESET Integration**: Primary security service with enhanced protection
- **Kaspersky Support**: Full compatibility and real-time protection  
- **Norton Security**: Complete enterprise security integration
- **Windows Defender**: Built-in Windows protection support
- **Bitdefender**: Professional antivirus integration
- **Avast/AVG**: Consumer antivirus support
- **McAfee**: Enterprise security compatibility
- **Auto-Detection**: Automatically detects your security software

### 🤖 **Smart Auto-Discovery**
- **Background Scanning**: Continuously finds new devices on your network
- **Auto-Trust Patterns**: Automatically trusts devices matching your rules
- **Smart Caching**: Remembers devices to reduce network load
- **Real-time Updates**: Live device status and connection monitoring
- **Configurable Intervals**: Set scan intervals from 10 seconds to 5 minutes

### 🔐 **Advanced Security Features**
- **Zero-Trust Model**: All devices start as "Untrusted" by default
- **Trust Levels**: Limited, Standard, and High security levels
- **Device Certificates**: Automatic certificate generation with expiration
- **Fernet Encryption**: Industry-standard encryption for all transfers
- **Input Validation**: Comprehensive protection against malicious inputs
- **File Integrity**: MD5 hash verification for all file transfers

### 📁 **Universal File Support**
- **All File Types**: Transfer any file format without restrictions (.exe, .pdf, .mp4, etc.)
- **Large File Support**: Configurable file size limits up to GB scale (default: 2GB)
- **Smart Validation**: Automatic file size checking with clear error messages
- **Flexible Limits**: Easily adjust maximum file sizes through configuration
- **Type Categories**: Helpful file type suggestions in selection dialog

### 📱 **Modern User Interface**
- **Dark Theme**: Professional CustomTkinter interface
- **Tabbed Design**: Send, Receive, Trusted Devices, and Security tabs
- **Real-time Device List**: Live updates of network devices with meaningful names
- **Progress Tracking**: Real-time progress bars and status updates
- **Responsive Design**: Works on different screen sizes

## 🔍 How Network Discovery Works

### **Device Detection Process**
1. **ARP Table Scan**: Quickly finds active devices from system ARP cache
2. **Reachability Test**: Ping + port scan to confirm device availability
3. **Name Resolution**: Multi-method hostname discovery
4. **Service Detection**: Check for file transfer service on port 12345
5. **Smart Classification**: Categorize device based on IP and discovered services

### **Device Naming Intelligence**
```
192.168.1.1   → Main-Router        (Primary gateway)
192.168.1.2   → Secondary-Router  (Secondary gateway) 
192.168.1.41  → Infrastructure-41  (Network equipment)
192.168.1.103 → DESKTOP-ABC123    (Real computer name found)
192.168.1.114 → Workstation-114   (Desktop computer)
192.168.1.156 → Server-156        (Server device)
192.168.1.201 → Mobile-Device-201 (Mobile/IoT device)
```

**Note:** The application automatically detects your network range:
- `192.168.1.x` (most common home networks)
- `192.168.0.x` (alternative home networks)  
- `10.0.0.x` (some routers and corporate networks)
- `172.16.x.x` (corporate networks)

### **Trust Status Explained**
- **🔴 Untrusted**: Device discovered but not approved (security default)
- **✅ Trusted**: Device manually approved or auto-trusted by patterns
- **🟢 Available**: Device is trusted and ready for file transfers
- **⚠️ No Service**: Device found but not running file transfer service

## 🚀 Getting Started

### 🔧 System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: 3.11+ 
- **Memory**: 100MB RAM minimum
- **Storage**: Less than 50MB disk space
- **Network**: Local network access (WiFi or Ethernet)

### 📦 Installation

1. **Download** the application files to your computer
2. **Install Python dependencies**:
   ```bash
   pip install customtkinter cryptography psutil pyarmor
   ```
3. **Run the application**:
   - **Recommended**: `python launchers/launcher.py`
   - **Direct**: `python src/file_transfer_app.py`
   - **Executable**: Run `build_commands.bat` to create standalone .exe

### ⚙️ Configuration
The application uses `config/config.json` for settings:
```json
{
  "app_settings": {
    "version": "3.4.01c34",
    "max_file_size_gb": 2,
    "port": 12345,
    "scan_timeout": 30
  }
}
```

### 🎯 First Time Setup
1. **Launch** the application using `python launchers/launcher.py`
2. **Scan Network** - Click "🔍 Scan Network" to discover devices
3. **Review Devices** - See discovered devices with intelligent names
4. **Trust Devices** - Click "✅ Trust" on devices you want to allow
5. **Start Transferring** - Send/receive files securely!

### 🖥️ **IMPORTANT: Multi-Device Setup Required**
> **⚠️ Key Requirement**: To transfer files between devices, you must install and run this application on **ALL devices** you want to include in your secure network.

**Example Setup:**
- **Device A**: Install app → Trust Device B → Send files to Device B
- **Device B**: Install app → Trust Device A → Receive files from Device A
- **Both devices**: Must be on the same network and trust each other

**Why needed:** Each device runs its own secure file service. Without the app installed, devices cannot send or receive encrypted files.

## 📖 How to Use

### 📤 Sending Files (Complete Guide)

1. **📂 Select Your Files**
   - Click "🗂️ Select Files" button in the Send tab
   - Choose one or more files (ALL file types supported: .exe, .pdf, .mp4, .zip, etc.)
   - Files appear in the list with their sizes
   - Maximum: 2GB per file (configurable in config.json)

2. **🔍 Discover Network Devices**
   - Click "🔍 Scan Network" to find devices
   - Wait 10-30 seconds for comprehensive scan
   - Devices appear with intelligent names:
     - Real names like "OFFICE-LAPTOP" (when discoverable)
     - Smart fallbacks like "Workstation-114", "Main-Router"
   - Status shows: Available, Untrusted, or No Service

3. **🛡️ Trust Devices (Security Step)**
   - **Untrusted devices**: Click "✅ Trust" to approve them
   - **Only trusted devices** can send/receive files (zero-trust security)
   - Trusted devices show green indicators
   - View certificates and trust levels in "Trusted Devices" tab

4. **🎯 Select Target Device**
   - Click "🎯 Select" on your target device
   - Device highlights in green when selected
   - Must be a trusted device with file service running

5. **📤 Transfer Files**
   - Click "📤 Send Files" to start transfer
   - Watch progress bar and status updates
   - Files are encrypted during transfer
   - Completion notification appears

### 📥 Receiving Files (Complete Guide)

1. **📂 Set Download Location**
   - Default: Your Downloads folder
   - Click "📁 Browse" to choose different location
   - Ensure sufficient disk space available

2. **🟢 Start File Service**
   - Click "🟢 Start Receiver" in Receive tab
   - Status changes to "🟢 Running - Ready to receive files"
   - Your device now accepts incoming transfers
   - Other devices will see you as "Available"

3. **📋 Monitor Transfers**
   - Watch transfer log for incoming files
   - Real-time progress updates
   - Files automatically appear in download location
   - All transfers logged with timestamps and source

4. **🔧 Manage Service**
   - Click "🔴 Stop Receiver" when done
   - Service stops automatically on app close
   - Can change download folder anytime

### 🔧 Network Management

1. **🔍 Device Discovery**
   - **Manual Scan**: Click "🔍 Scan Network" anytime
   - **Auto-Scan**: Enable in Security tab for continuous discovery
   - **Scan Range**: Automatically detects your network (10.0.0.x, 192.168.x.x, etc.)
   - **Multi-Method**: Uses DNS, NetBIOS, ARP, and ping for comprehensive discovery

2. **🛡️ Device Security**
   - **Trust Management**: Only trust devices you recognize
   - **Trust Levels**: Set Limited, Standard, or High trust levels
   - **Auto-Trust Patterns**: Set rules for automatic device approval
   - **Certificate System**: Each device gets unique security certificate

3. **📊 Monitoring**
   - **Real-time Status**: See device connectivity in real-time  
   - **Connection History**: Track device connection counts
   - **Transfer Logs**: Complete history of all file transfers
   - **Security Events**: Monitor trust changes and security events

### ⌨️ Keyboard Shortcuts

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Ctrl+O` | Select Files | Open file selection dialog |
| `Ctrl+S` | Scan Network | Start network device discovery |
| `Ctrl+R` | Start Receiver | Begin listening for incoming files |
| `Ctrl+T` | Stop Receiver | Stop file service |
| `Ctrl+D` | Download Folder | Open downloads directory |
| `F5` | Refresh | Refresh device list |
| `F1` | Help | Show help information |
| `Escape` | Cancel | Cancel current operation |

## 🔧 Advanced Configuration

### 🎯 Auto-Trust Patterns
Set up rules to automatically trust specific devices:
```regex
.*-PC$          # Trusts devices ending with "-PC"
.*-LAPTOP$      # Trusts laptop devices  
OFFICE-.*       # Trusts devices starting with "OFFICE-"
DEV-.*          # Trusts development machines
[A-Z]{2,}-\d+   # Trusts pattern like "WS-01", "SRV-02"
```

### 🔐 Trust Levels
- **🔴 Limited**: Basic transfers, lower priority
- **🔵 Standard**: Normal transfers, standard priority  
- **🟢 High**: Maximum trust, highest priority, auto-accept

### 📊 Network Analysis
- **Device Categories**: Routers, Workstations, Servers, Mobile devices
- **Service Detection**: HTTP, HTTPS, SSH, SMB, RDP services
- **Connection Methods**: Ping responsive, Port/ARP detection, File service
- **Performance Metrics**: Scan time, success rate, device count

### ⚙️ Configuration Options (config.json)
```json
{
  "app_settings": {
    "app_name": "Secure File Transfer",
    "version": "3.4.01c34",
    "port": 12345,
    "max_file_size_gb": 2,
    "scan_timeout": 30,
    "encryption_enabled": true,
    "auto_accept_trusted": true
  },
  "security_settings": {
    "eset_integration": true,
    "require_device_trust": true,
    "verify_file_integrity": true,
    "encryption_algorithm": "Fernet"
  },
  "network_settings": {
    "discovery_methods": ["ping", "arp", "port_scan", "netbios"],
    "dns_timeout": 0.5,
    "netbios_timeout": 0.5,
    "port_scan_timeout": 0.15
  }
}
```

## 🆘 Troubleshooting

### 🔍 Network Discovery Issues

**❌ "No devices found" or "Only 1-2 devices"**
- ✅ **Check network**: Ensure you're on the same subnet (WiFi/Ethernet)
- ✅ **Firewall**: Temporarily disable Windows Firewall to test
- ✅ **Network range**: Application auto-detects 10.0.0.x, 192.168.x.x ranges
- ✅ **Router settings**: Some routers block device discovery
- ✅ **Wait longer**: Network scan takes 10-30 seconds for completion

**❌ "My PC doesn't show as trusted" (Fresh Install)**
- ✅ **This is CORRECT security behavior**: Fresh installs have zero trusted devices
- ✅ **Expected workflow**:
  1. Download/install application → No trusted devices (secure)
  2. Run application and click "🔍 Scan Network"
  3. Your PC appears as "Untrusted" (this is normal!)
  4. Click "✅ Trust" next to your PC to approve it
  5. Your PC now shows as trusted and ready for transfers
- ✅ **Why this happens**: Zero-trust security model prevents auto-trust
- ✅ **One-time setup**: You only need to trust your PC once

**❌ "Devices show as 'Untrusted'"**
- ✅ **This is normal**: All devices start untrusted for security
- ✅ **Manual trust**: Click "✅ Trust" on devices you recognize
- ✅ **Install on other PCs**: **CRITICAL** - Install the application on ALL devices you want to transfer files between
- ✅ **Start receiver**: Target devices need "Start Receiver" running to be "Available"

**❌ "Can't send files to other devices"**
- ✅ **Install app everywhere**: Other devices must have this application installed and running
- ✅ **Mutual trust required**: Both devices must trust each other (Device A trusts B, Device B trusts A)
- ✅ **Receiver must be running**: Target device must click "🟢 Start Receiver"
- ✅ **Same network**: All devices must be on the same WiFi/network

**❌ "Generic device names like 'Workstation-114'"**
- ✅ **DNS issues**: Some networks don't allow reverse DNS lookup
- ✅ **NetBIOS disabled**: Windows may have NetBIOS over TCP/IP disabled
- ✅ **Still functional**: Generic names don't affect file transfer functionality
- ✅ **Network admin**: Contact IT if in corporate environment

### 🔧 File Transfer Issues

**❌ "Transfer failed" or "Connection refused"**
- ✅ **Receiver running**: Target device must have "Start Receiver" active
- ✅ **Trust both ways**: Both devices must trust each other
- ✅ **Port 12345**: Ensure port isn't blocked by firewall/antivirus
- ✅ **Disk space**: Check available space on receiving device
- ✅ **File size**: Ensure file doesn't exceed 2GB limit (or configured limit)

**❌ "File too large" error**
- ✅ **Check config.json**: Look at "max_file_size_gb" setting
- ✅ **Increase limit**: Change value from 2 to higher number (e.g., 5 for 5GB)
- ✅ **Restart app**: Configuration changes require restart
- ✅ **Split files**: Consider splitting very large files

**❌ "Security service not detected"**  
- ✅ **Not critical**: Application works without antivirus detection
- ✅ **Windows Defender**: Always available as fallback
- ✅ **Antivirus running**: Ensure your security software is active
- ✅ **Silent mode**: Check if antivirus is in gaming/silent mode

### 🔧 Performance Optimization

**🚀 Speed up network discovery:**
- Use wired Ethernet connection instead of WiFi
- Ensure good signal strength for WiFi connections
- Close unnecessary network applications
- Restart router if discovery is very slow

**🚀 Speed up file transfers:**
- Use wired connections for both devices
- Close bandwidth-intensive applications
- Transfer during off-peak network hours
- Consider file compression for text/document files

**🚀 Reduce resource usage:**
- Disable auto-scan when not needed
- Close other Python applications
- Ensure sufficient RAM available
- Use SSD storage for better I/O performance

### 🐛 Getting Help

1. **📋 Check Logs**: Look at transfer log and debug output in console
2. **🔧 Reset Settings**: Use "Reset Application" in Tools menu  
3. **📊 System Info**: Use "Report Bug" to generate diagnostic information
4. **🧪 Run Tests**: Execute `python test_all_features.py` to verify functionality
5. **✅ Verification**: Run `python final_verification.py` for full system check

## 🔒 Security & Privacy

### 🛡️ Security Model
- **Zero-Trust Architecture**: No device trusted by default
- **Fernet Encryption**: All file transfers use industry-standard encryption
- **Local Network Only**: No internet connection required or used
- **Certificate-Based Auth**: Unique certificates for each trusted device
- **Input Validation**: Protection against path traversal and injection attacks

### 🔐 Privacy Protection  
- **No Data Collection**: All information stays on your local network
- **No Cloud Storage**: Files never leave your local network
- **Trusted Devices Only**: You control exactly who can send/receive
- **Automatic Cleanup**: Temporary files removed after transfer
- **Audit Trail**: Complete logs of all transfer activity

### 🚨 Security Best Practices
- **Review Trust List**: Regularly check trusted devices
- **Strong Device Names**: Use descriptive, unique device names
- **Monitor Transfers**: Watch logs for unexpected activity  
- **Update Software**: Keep antivirus and OS updated
- **Network Security**: Use WPA3 WiFi encryption
- **Physical Security**: Secure devices running the application

## 🎯 Use Cases

### 🏠 **Home Network**
- Transfer photos/videos between family computers
- Share documents between work laptop and personal desktop
- Move files to/from media center or NAS
- Backup important files to multiple devices

### 🏢 **Small Office** 
- Secure document sharing between workstations
- Transfer files to presentation/meeting room computers  
- Share resources between departments
- Backup files to server or storage devices

### 💻 **Development Team**
- Share code, builds, and assets securely
- Transfer large development files
- Distribute software to testing machines
- Backup project files across team devices

### 🎮 **Gaming/Media**
- Transfer game saves between computers
- Share media files, screenshots, recordings
- Move large game installations
- Backup gaming profiles and configurations

## 📈 What's Coming Next

### 🔮 Future Enhancements
- **Mobile Apps**: iOS and Android companion apps
- **Cloud Integration**: Optional secure cloud storage bridges
- **Advanced Encryption**: Additional encryption algorithms
- **Group Management**: Manage device groups and permissions
- **Bandwidth Controls**: QoS and transfer rate limiting
- **Remote Access**: Secure VPN-like connectivity

### 🤝 Contributing
- **Bug Reports**: Use built-in "Report Bug" feature
- **Feature Requests**: Use "Request Feature" functionality  
- **Testing**: Help test new features and report issues
- **Documentation**: Suggest improvements to this guide
- **Security**: Report security issues responsibly

## 📝 About

### 🎯 **Mission**
To provide enterprise-grade secure file transfer capabilities in an easy-to-use application suitable for home users, small businesses, and development teams. Emphasizing security, privacy, and user experience without complexity.

### 🔧 **Technical Excellence**
- **Python-Based**: Cross-platform compatibility and reliability
- **Modern UI**: CustomTkinter for professional appearance
- **Multi-Threading**: Responsive interface during network operations  
- **Robust Error Handling**: Graceful handling of network and file system issues
- **Comprehensive Testing**: Extensive test suite ensures reliability
- **Zero Dependencies**: Minimal external dependencies for security

### 🌟 **Key Advantages**
- **User-Friendly**: Intuitive interface with helpful tooltips and guidance
- **Secure by Default**: Zero-trust security model with encryption
- **Universal Compatibility**: Supports all file types and sizes
- **Network Intelligent**: Smart device discovery and classification  
- **Highly Configurable**: Extensive customization options
- **Professional Grade**: Enterprise security features in simple package

---

## 🎉 Ready to Get Started?

### 🚀 **Quick Start (2 Minutes)**

1. **Install Python** (if not already installed)
2. **Download** application files from GitHub
3. **Install dependencies**: 
   ```bash
   pip install customtkinter cryptography psutil
   ```
4. **Run application**:
   ```bash
   python launchers/launcher.py
   ```
5. **Scan network** and start transferring files securely!


---

**🔐 Secure File Transfer v3.4.01c34** - Professional file sharing with intelligent network discovery, enterprise security, and zero-trust architecture.

*Making secure file transfers simple, intelligent, and professional for everyone.*
