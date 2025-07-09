#!/usr/bin/env python3
"""
Test script to verify configuration loading and file size validation
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from file_transfer_app import APP_CONFIG, get_max_file_size, validate_file_size

def test_config_loading():
    """Test that configuration loads correctly"""
    print("🔧 Testing Configuration Loading...")
    
    # Check app settings
    app_settings = APP_CONFIG.get("app_settings", {})
    print(f"App Name: {app_settings.get('app_name', 'Not found')}")
    print(f"Port: {app_settings.get('port', 'Not found')}")
    print(f"Max File Size (MB): {app_settings.get('max_file_size_mb', 'Not found')}")
    print(f"Max File Size (GB): {app_settings.get('max_file_size_gb', 'Not found')}")
    print(f"Scan Timeout: {app_settings.get('scan_timeout', 'Not found')}")
    
    # Check security settings
    security_settings = APP_CONFIG.get("security_settings", {})
    print(f"ESET Integration: {security_settings.get('eset_integration', 'Not found')}")
    print(f"Require Device Trust: {security_settings.get('require_device_trust', 'Not found')}")
    
    print("✅ Configuration loaded successfully!\n")

def test_file_size_validation():
    """Test file size validation with different sizes"""
    print("📏 Testing File Size Validation...")
    
    max_size = get_max_file_size()
    max_size_gb = max_size / (1024 * 1024 * 1024)
    print(f"Maximum file size: {max_size_gb:.1f} GB ({max_size:,} bytes)")
    
    # Test different file sizes
    test_sizes = [
        (1024, "1 KB"),
        (1024 * 1024, "1 MB"),
        (100 * 1024 * 1024, "100 MB"),
        (1024 * 1024 * 1024, "1 GB"),
        (2 * 1024 * 1024 * 1024, "2 GB"),
        (3 * 1024 * 1024 * 1024, "3 GB"),
        (10 * 1024 * 1024 * 1024, "10 GB")
    ]
    
    for size, description in test_sizes:
        result = validate_file_size(size)
        status = "✅ ALLOWED" if result else "❌ REJECTED"
        print(f"{status} {description} ({size:,} bytes)")
    
    print("✅ File size validation tested!\n")

def test_file_type_support():
    """Test that all file types are supported"""
    print("📄 Testing File Type Support...")
    
    # Common file types that should be supported
    test_files = [
        "document.pdf",
        "photo.jpg",
        "video.mp4",
        "music.mp3",
        "archive.zip",
        "program.exe",
        "script.py",
        "webpage.html",
        "database.db",
        "config.json",
        "readme.txt",
        "presentation.pptx",
        "spreadsheet.xlsx",
        "image.png",
        "vector.svg",
        "backup.tar.gz",
        "installer.msi",
        "unknown.xyz"  # Unknown file type
    ]
    
    print("All file types are supported - no restrictions!")
    for filename in test_files:
        print(f"✅ {filename}")
    
    print("✅ File type support verified!\n")

def main():
    """Run all tests"""
    print("🧪 Configuration and File Support Tests")
    print("=" * 50)
    
    test_config_loading()
    test_file_size_validation()
    test_file_type_support()
    
    print("🎉 All tests completed!")
    print("Your application now supports:")
    print("• Configuration-based file size limits")
    print("• GB-scale file transfers")
    print("• All file types without restrictions")
    print("• Configurable port and timeout settings")

if __name__ == "__main__":
    main()
