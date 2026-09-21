/**
 * Pancoran Slide Festival 2026 — Google Apps Script Backend
 * Deploy sebagai Web App dengan akses: Anyone
 *
 * SETUP:
 * 1. Buka script.google.com → New Project
 * 2. Paste seluruh kode ini
 * 3. Ganti SPREADSHEET_ID dan DRIVE_FOLDER_ID di bawah
 * 4. Deploy → Web App → Anyone → Copy URL
 * 5. Tempel URL ke SCRIPT_URL di index.html
 */

// ══════════════════════════════════════════
//  CONFIG — GANTI NILAI INI
// ══════════════════════════════════════════
const SPREADSHEET_ID  = 'GANTI_DENGAN_ID_SPREADSHEET_ANDA';
const DRIVE_FOLDER_ID = 'GANTI_DENGAN_ID_FOLDER_DRIVE_ANDA';
const SHEET_NAME      = 'Pendaftaran';
// ══════════════════════════════════════════

/** Headers Google Sheets */
const HEADERS = [
  'Timestamp',
  'Nama Lengkap',
  'Nama Panggilan (BIB)',
  'Jenis Kelamin',
  'Nomor WA',
  'Instagram',
  'TikTok',
  'Tiket',
  'Harga',
  'Setuju T&C',
  'Nama Pengirim Transfer',
  'Link Bukti Bayar',
];

function doPost(e) {
  try {
    const data    = JSON.parse(e.postData.contents);
    const ss      = SpreadsheetApp.openById(SPREADSHEET_ID);
    let   sheet   = ss.getSheetByName(SHEET_NAME);

    // Buat sheet baru + header jika belum ada
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length)
           .setFontWeight('bold')
           .setBackground('#1a5c2a')
           .setFontColor('#ffffff');
      sheet.setFrozenRows(1);
    }

    // Upload bukti bayar ke Google Drive
    let fileLink = '—';
    if (data.fileData && data.fileName) {
      const folder  = DriveApp.getFolderById(DRIVE_FOLDER_ID);
      const decoded = Utilities.base64Decode(data.fileData);
      const blob    = Utilities.newBlob(decoded, data.fileType, data.fileName);
      const file    = folder.createFile(blob);
      file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      fileLink = file.getUrl();
    }

    // Tulis baris baru
    sheet.appendRow([
      new Date(data.timestamp),
      data.fullname,
      data.nickname,
      data.gender,
      data.wa,
      data.instagram,
      data.tiktok,
      data.ticket,
      Number(data.price),
      data.tncAgreed ? 'Ya' : 'Tidak',
      data.senderName || '—',
      fileLink,
    ]);

    // Auto-fit kolom
    sheet.autoResizeColumns(1, HEADERS.length);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/** Test GET — buka URL di browser untuk cek apakah script berjalan */
function doGet() {
  return ContentService.createTextOutput('Pancoran Slide Festival API is running ✅');
}
