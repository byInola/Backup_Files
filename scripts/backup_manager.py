import zipfile
import time
from pathlib import Path
from datetime import datetime


class BackupManager:
    def __init__(self, source_folder):
        self.source = Path(source_folder)
        self.backup_root = self.source.parent / "backups"
        self.backup_root.mkdir(exist_ok=True)
        self.log_file = self.backup_root / "backup.log"

    def _log(self, msg):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{time_str}] {msg}\n")

    def create_backup(self):
        start_time = time.time()
        date = datetime.now().strftime("%Y-%m-%d")
        base_name = f"backup_{date}"
        name = base_name
        count = 1

        while (self.backup_root / f"{name}.zip").exists():
            name = f"{base_name}_v{count}"
            count += 1

        zip_path = self.backup_root / f"{name}.zip"

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in self.source.rglob("*"):
                zipf.write(file, file.relative_to(self.source))

        duration = time.time() - start_time
        file_count = len(list(self.source.rglob("*")))

        self._log(f"OK | {zip_path.name} | files={file_count} | {duration:.2f}s")
        return zip_path, file_count, duration
