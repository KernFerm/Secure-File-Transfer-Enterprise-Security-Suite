# 🔐 Secure-File-Transfer-Enterprise-Security-Suite

A professional, secure file transfer application with multi-antivirus security support and enterprise-grade trusted device management. Features a modern CustomTkinter interface with automatic device discovery and comprehensive security features.

## ✨ What Makes This Special

### 🛡️ Multi-Antivirus Protection
- **ESET Integration**: Primary security service with enhanced protection
- **Kaspersky Support**: Full compatibility and real-time protection
- **Norton Security**: Complete enterprise security integration
- **Windows Defender**: Built-in Windows protection support
- **Bitdefender**: Professional antivirus integration
- **Avast/AVG**: Consumer antivirus support
- **McAfee**: Enterprise security compatibility
- **Auto-Detection**: Automatically detects your security software

### 🤖 Smart Auto-Discovery
- **Background Scanning**: Continuously finds new devices on your network
- **Auto-Trust Patterns**: Automatically trusts devices matching your rules
- **Smart Caching**: Remembers devices to reduce network load
- **Real-time Updates**: Live device status and connection monitoring
- **Configurable**: Set scan intervals from 10 seconds to 5 minutes

### 🔐 Advanced Security Features
- **Trust Levels**: Limited, Standard, and High security levels
- **Device Certificates**: Automatic certificate generation with expiration
- **Encryption**: Industry-standard Fernet encryption for all transfers
- **Input Validation**: Comprehensive protection against malicious inputs
- **File Integrity**: MD5 hash verification for all file transfers

### 📁 Universal File Support
- **All File Types**: Transfer any file format without restrictions (.exe, .pdf, .mp4, etc.)
- **Large File Support**: Configurable file size limits up to GB scale
- **Smart Validation**: Automatic file size checking with clear error messages
- **Flexible Limits**: Easily adjust maximum file sizes through configuration
- **Type Categories**: Helpful file type suggestions in selection dialog

### 📱 Modern User Interface
- **Dark Theme**: Professional CustomTkinter interface
- **Tabbed Design**: Send, Receive, Trusted Devices, and Security tabs
- **Progress Tracking**: Real-time progress bars and status updates
- **Keyboard Shortcuts**: Quick access to common functions
- **Responsive Design**: Works on different screen sizes

## � Getting Started

### 🔧 System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Python**: 3.11 
- **Memory**: 100MB RAM minimum
- **Storage**: Less than 50MB disk space
- **Network**: Local network access

### 📦 Installation

1. **Download** the application files to your computer
2. **Install Python dependencies**:
   ```bash
   pip install customtkinter cryptography psutil
   ```
3. **Run the application**:
   - **Easy Way**: Run `python launchers/launcher.py`
   - **Direct Way**: Run `python src/file_transfer_app.py`

### ⚙️ Configuration
The application uses `config/config.json` for settings:
- **File Size Limits**: Adjust `max_file_size_gb` for larger files (default: 2GB)
- **Network Settings**: Configure port and scan timeout
- **Security Options**: Customize trust and encryption settings

### 🎯 First Time Setup
1. **Launch** the application using any method above
2. **Check Security Tab** to see your detected antivirus
3. **Scan Network** to find other devices
4. **Trust Devices** you want to allow file transfers with
5. **Start Transferring** files securely!

## � How to Use

### 📤 Sending Files (Step by Step)

1. **📂 Select Your Files**
   - Click "🗂️ Select Files" button
   - Choose one or more files from your computer (ALL file types supported)
   - Files will appear in the list with their sizes
   - Maximum file size: 2GB (configurable in config.json)

2. **🔍 Find Devices**
   - Click "🔍 Scan Network" to discover devices
   - Wait for the scan to complete (usually takes 10-30 seconds)
   - Available devices will appear in the list

3. **🛡️ Trust Devices**
   - Click "✅ Trust" next to devices you want to allow
   - Only trusted devices can send/receive files
   - Trusted devices get a green shield icon

4. **🎯 Select Target**
   - Click "🎯 Select" on the device you want to send to
   - The device will be highlighted in green

5. **📤 Send Files**
   - Click "📤 Send Files" to start the transfer
   - Watch the progress bar and transfer status
   - Files will be encrypted and sent securely

### 📥 Receiving Files (Step by Step)

1. **📂 Choose Download Location**
   - The default is your Downloads folder
   - Click "📁 Browse" to change the location
   - Make sure you have enough disk space

2. **🟢 Start Receiver**
   - Click "🟢 Start Receiver" to listen for incoming files
   - The status will change to "🟢 Running"
   - Your device is now ready to receive files

3. **📋 Monitor Activity**
   - Watch the transfer log for incoming files
   - Files will appear in your chosen download location
   - All transfers are logged with timestamps

### 🔧 Managing Security

1. **🛡️ Security Tab**
   - View your detected antivirus software
   - See protection status and active service
   - Check device statistics and connection counts

2. **🔍 Auto-Scan Settings**
   - Toggle auto-scan on/off with the switch
   - Adjust scan interval (10-300 seconds)
   - Set up trust patterns for automatic device approval

3. **🛡️ Trusted Devices Tab**
   - View all trusted devices with detailed information
   - Change trust levels (Limited, Standard, High)
   - Remove devices or view their certificates
   - Export your trusted device list

### ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+O` | Select files |
| `Ctrl+S` | Scan network |
| `Ctrl+R` | Start receiver |
| `Ctrl+T` | Stop receiver |
| `Ctrl+D` | Open download folder |
| `F5` | Refresh devices |
| `F1` | Show help |
| `Ctrl+,` | Open settings |

## 🔧 Advanced Features

### 🎯 Auto-Trust Patterns
Set up rules to automatically trust devices:
- `.*-PC$` - Trusts any device ending with "-PC"
- `.*-LAPTOP$` - Trusts laptop devices
- `OFFICE-.*` - Trusts devices starting with "OFFICE-"
- `DEV-.*` - Trusts development machines

### 🔐 Trust Levels Explained
- **🔴 Limited**: Basic file transfers only
- **🔵 Standard**: Normal file transfers with full features
- **� High**: Maximum trust with priority handling

### 📊 Device Statistics
- **Total Devices**: Number of trusted devices
- **Connection Count**: How many times devices have connected
- **Auto-Trusted**: Devices automatically trusted by patterns
- **Manual Trusted**: Devices manually approved by you

### 🔒 Certificate Management
- **Auto-Generated**: Each trusted device gets a unique certificate
- **1-Year Validity**: Certificates expire after one year
- **Hash Verification**: Ensures device identity hasn't changed
- **Service Binding**: Tied to your security software

## 🛠️ Settings & Configuration

### � File Transfer Settings
- **File Size Limit**: Configure maximum file size (default: 2GB)
- **Supported Types**: All file formats supported (.exe, .pdf, .mp4, .zip, etc.)
- **Size Validation**: Automatic checking with clear error messages
- **Configuration File**: Edit `config/config.json` to adjust limits

### �📡 Network Settings
- **Port**: Default 12345 (configurable in config.json)
- **Scan Timeout**: How long to wait for device responses (configurable)
- **Max Threads**: Number of simultaneous device scans
- **Test Connection**: Check network connectivity

### 🎨 Interface Settings
- **Appearance**: Light, Dark, or System theme
- **Color Theme**: Blue, Green, or Dark-Blue
- **Auto-scan**: Enable/disable background scanning
- **Bug Reports**: Include system info in reports

### 🔧 Tools & Utilities
- **Clear Transfer Log**: Remove all transfer history
- **Clear Temp Files**: Clean up temporary files
- **Reset Application**: Restore default settings
- **Export Data**: Save trusted devices and logs

### ⚙️ Configuration File (config.json)
```json
{
  "app_settings": {
    "max_file_size_gb": 2,        // Maximum file size in GB
    "port": 12345,                // Network port for transfers
    "scan_timeout": 30,           // Device scan timeout in seconds
    "encryption_enabled": true     // Enable file encryption
  },
  "security_settings": {
    "require_device_trust": true,  // Only allow trusted devices
    "verify_file_integrity": true // Verify file integrity
  }
}
```

**Configuration Options:**
- **max_file_size_gb**: Set maximum file size (1-10 GB recommended)
- **port**: Change network port if 12345 is blocked
- **scan_timeout**: Adjust device discovery timeout
- **encryption_enabled**: Toggle file encryption on/off

## � File Organization
```
secure-file-transfer/
├── 📁 src/
│   ├── file_transfer_app.py      # Main application with GUI
│   └── file_transfer_server.py   # Network server for transfers
├── 📁 launchers/
│   └── launcher.py              # Python launcher script
├── 📁 config/
│   └── config.json              # Application settings & file size limits
├── 📁 docs/
│   └── README.md                # This documentation
├── trusted_devices.json         # Your trusted devices (auto-created)
├── requirements.txt             # Python dependencies
├── test_config.py               # Configuration test script
└── .gitignore                   # Git ignore file
```

## 🆘 Troubleshooting

### 🔍 Common Issues & Solutions

**❌ "No devices found"**
- ✅ Check your network connection
- ✅ Make sure other devices are on the same network
- ✅ Try disabling/enabling Windows Firewall temporarily
- ✅ Ensure port 12345 is not blocked

**❌ "Transfer failed"**
- ✅ Verify both devices are trusted
- ✅ Check if receiving device has receiver running
- ✅ Ensure sufficient disk space on receiving device
- ✅ Check file size doesn't exceed limit (default 2GB)
- ✅ Try restarting both applications

**❌ "File too large"**
- ✅ Check current file size limit in config.json
- ✅ Increase `max_file_size_gb` value if needed
- ✅ Restart application after changing configuration
- ✅ Consider splitting large files into smaller parts

**❌ "Security service not detected"**
- ✅ Make sure your antivirus is running
- ✅ Check if antivirus is in silent/gaming mode
- ✅ Try restarting the application
- ✅ Windows Defender is always available as fallback

**❌ "Auto-trust not working"**
- ✅ Check your trust pattern syntax (use regex)
- ✅ Ensure auto-scan is enabled
- ✅ Verify devices match your patterns exactly
- ✅ Try manual trust first to test connectivity

**❌ "Application won't start"**
- ✅ Install Python 3.8+ and required packages
- ✅ Check if all files are in correct locations
- ✅ Try running from command line to see error messages
- ✅ Ensure antivirus isn't blocking the application

### 🐛 Getting Help

1. **📋 Check Transfer Log**: Look for error messages in the log
2. **🔧 Try Reset**: Use "Reset Application" in Tools menu
3. **📊 System Info**: Use "Report Bug" to generate system information
4. **💡 Feature Request**: Use "Request Feature" for suggestions

### 🔧 Performance Tips

- **Network Speed**: Use wired connection for faster transfers
- **File Size**: Large files (GB scale) are fully supported
- **File Types**: All file formats transfer equally well
- **Configuration**: Adjust file size limits in config.json as needed
- **Firewall**: Add application to firewall exceptions
- **Antivirus**: Add application folder to antivirus exceptions

## 🔒 Security & Privacy

### 🛡️ What's Protected
- **All file transfers** are encrypted with industry-standard encryption
- **Device authentication** prevents unauthorized access
- **Input validation** protects against malicious data
- **Path protection** prevents directory traversal attacks
- **File integrity** ensures files aren't corrupted during transfer

### 🔐 Privacy Features
- **Local network only** - no internet connection required
- **No data collection** - all information stays on your network
- **Trusted devices only** - you control who can send/receive
- **Automatic cleanup** - temporary files are removed after transfer
- **Secure certificates** - each device gets unique identification

### 🚨 Best Practices
- **Review trusted devices** regularly
- **Use strong device names** (avoid generic names)
- **Monitor transfer logs** for suspicious activity
- **Keep security software updated**
- **Use appropriate trust levels** for different devices

## 📝 About This Application

### 🎯 Purpose
This application was designed to provide secure, easy-to-use file transfers on local networks with enterprise-grade security features. It's perfect for:
- **Home networks** with multiple computers
- **Small offices** needing secure file sharing
- **Development teams** sharing files safely
- **Anyone** wanting encrypted file transfers

### 🔧 Technical Details
- **Built with Python** for cross-platform compatibility
- **CustomTkinter UI** for modern interface
- **Fernet encryption** for security
- **Multi-threaded scanning** for performance
- **JSON configuration** for easy customization
- **Universal file support** - no file type restrictions
- **Configurable limits** - adjust file sizes up to GB scale

### 🌟 Key Benefits
- **Easy to use** - intuitive interface with helpful icons
- **Secure by default** - encryption and authentication built-in
- **Flexible** - works with any antivirus or security software
- **Universal** - supports all file types without restrictions
- **Scalable** - handles files up to GB scale with configurable limits
- **Reliable** - robust error handling and recovery
- **Professional** - enterprise-grade features in simple package

---

## 🎉 Ready to Get Started?

1. **Download** the application files
2. **Install** Python dependencies: `pip install customtkinter cryptography psutil`
3. **Test configuration** (optional): `python test_config.py`
4. **Run** `python launchers/launcher.py`
5. **Scan** for devices and start trusting them
6. **Transfer** files securely - any file type, up to 2GB!

**🔐 Secure File Transfer** - Making secure file sharing simple and professional.

### 🧪 Testing Your Setup
Run the configuration test to verify everything works:
```bash
python test_config.py
```
This will verify:
- Configuration loading (file size limits, port settings)
- File size validation (shows current 2GB limit)
- File type support (confirms all types are supported)
- Network settings (port and timeout configuration)

---

*Need help? Check the troubleshooting section above or use the built-in "Report Bug" feature to generate detailed system information.*
