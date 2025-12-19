# Backup System extension to File Organizer

A Python desktop application that automatically organizes files by extension and creates compressed backups with versioning and logging.

##  Features

### Backup System 
- **Automatic ZIP Compression** - Creates compressed archives of your folders
- **Smart Versioning** - Automatically increments version numbers (backup_2025-12-19.zip, backup_2025-12-19_v1.zip, etc.)
- **Detailed Logging** - Tracks all backup operations with timestamps, file counts, and durations
- **Fast Performance** - Compresses files efficiently using ZIP_DEFLATED algorithm
- **Error Handling** - Gracefully handles permissions issues and file access errors

### File Organization
For complete file organization features, see the [previous repository](https://github.com/byInola/Smart-File-Organizer).


## Getting Started

### Prerequisites
- Python 3.7 or higher
- tkinter (usually included with Python)

**No additional packages required** - Uses only Python standard library:
   - `tkinter` - GUI interface
   - `zipfile` - Backup compression
   - `shutil` - File operations
   - `pathlib` - Path handling
   - `json` - Configuration storage
   - `threading` - Async operations

**Run the application**
```bash
python smartFO.py
```

## HOW IT WORKS

### Initial Interface
![Empty interface](screenshot/sc_1.png)
*Clean, modern interface with folder selection and action buttons*

### Organizing Files
![Files being organized](screenshot/sc_2.png)
*Real-time activity log showing files being sorted into folders by extension*

### Backup Creation
![Backup success dialog](screenshot/sc_3.png)
*Confirmation dialog showing backup details: location, file count, and processing time*

### Backup Files Structure
![Backup folder structure](screenshot/sc_4.png)
*Generated backup files in the file explorer showing ZIP archive and log file*

![Folder hierarchy](screenshot/sc_5.png)
*Complete project structure showing organized folders and backup system*


## How to Use

### Creating a Backup

1. **Select Folder** - Click "Browse" and choose the folder you want to backup
2. **Create Backup** - Click the orange "💾 Create Backup" button
3. **Wait for Completion** - The activity log shows real-time progress
4. **Check Results** - A success dialog displays:
   - Backup file location
   - Number of files backed up
   - Processing time


### Log File Format

The `backup.log` file tracks all operations:

```
[2025-12-19 18:08:31] OK | backup_2025-12-19.zip | files=14 | 0.74s
```

Each entry includes:
- Timestamp
- Status (OK/ERROR)
- Archive name
- File count
- Duration


## Project Structure

```
backup-files/
├── scripts/
│   ├── backup_manager.py   # Backup logic and compression
│   └── smartFO.py          # Main application with GUI
├── backups/                # Generated backups (created at runtime)
│   ├── backup_*.zip        # Compressed backup archives
│   └── backup.log          # Operation log file
├── screenshot/            
│   ├── sc_1.png
│   ├── sc_2.png
│   ├── sc_3.png
│   ├── sc_4.png
│   └── sc_5.png
├── test_folder/            
│   ├── sorted_folders/     # Organized files by extension
│   │   ├── doc/
│   │   ├── jpg/
│   │   ├── pdf/
│   │   └── zip/
│   └── history.json        # Organization history
└── README.md               
```


##  Technical Implementation

### Object-Oriented Design

The application uses clean OOP principles:

**`BackupManager` Class** (`backup_manager.py`)
- Handles all backup operations
- Manages versioning automatically
- Creates compressed ZIP archives
- Logs operations with timestamps

**`FileOrganizer` Class** (`smartFO.py`)
- Organizes files by extension
- Maintains operation history
- Supports undo functionality

**`FileOrganizerApp` Class** (`smartFO.py`)
- Tkinter GUI implementation
- Threaded operations for responsiveness
- Real-time activity logging

### Key Methods

#### BackupManager
```python
create_backup()  # Creates versioned ZIP backup with logging
_log(msg)        # Internal logging with timestamps
```

## Checklist

-  Research folder copying with `shutil`
-  Implement folder selection
-  Add timestamped backup names with versioning
-  Error handling and logging
-  Code organization with `backup_manager.py`
-  ZIP compression implementation
-  Enhanced log format (time, files, duration)
-  Tkinter GUI integration
-  Final testing with real data


## Error Handling

The application handles common errors gracefully:

- **Missing folder** - Shows error dialog
- **Permission denied** - Logs error and notifies user
- **Invalid path** - Validates before processing
- **Disk full** - Catches and reports exception


## Performance

Typical backup performance:
- **14 files** → **0.74 seconds**
- **Compression ratio** → ~90% (25.7 MB compressed)
- **Thread-safe** → Non-blocking UI operations
