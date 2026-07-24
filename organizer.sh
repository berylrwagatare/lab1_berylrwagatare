#!/bin/bash
CSV_FILE="grades.csv"
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

mkdir -p "$ARCHIVE_DIR"

if [ -f "$CSV_FILE" ]; then
    ARCHIVE_NAME="${ARCHIVE_DIR}/grades_${TIMESTAMP}.csv"
    cp "$CSV_FILE" "$ARCHIVE_NAME"
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Archived $CSV_FILE to $ARCHIVE_NAME" >> "$LOG_FILE"
    echo "Archived existing $CSV_FILE to $ARCHIVE_NAME"
else
    echo "$(date +"%Y-%m-%d %H:%M:%S") - No $CSV_FILE found to archive" >> "$LOG_FILE"
    echo "No existing $CSV_FILE found, skipping archive step."
fi

echo "assignment,group,score,weight" > "$CSV_FILE"
echo "$(date +"%Y-%m-%d %H:%M:%S") - Created fresh $CSV_FILE" >> "$LOG_FILE"
echo "Created a fresh $CSV_FILE."
echo "Done. See $LOG_FILE for the log of this run."
