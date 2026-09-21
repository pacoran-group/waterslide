# build script
import os

with open(r"e:\Waterslide\index.html", "w", encoding="utf-8") as f:
    f.write("")

def add(s):
    with open(r"e:\Waterslide\index.html", "a", encoding="utf-8") as f:
        f.write(s)
add("""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pancoran Slide Festival 2026 – Interactive Registration</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background: #0d2e15;
      color: #142817;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }
    :root {
      --green-darkest: #0a2411;
      --green-dark:    #124e23;
      --green-mid:     #1f833a;
      --green-light:   #34a853;
      --green-pale:    #ecfdf3;
      --green-border:  #b8e2c0;
      --accent-gold:   #f59e0b;
      --red:           #dc2626;
      --radius-xl:     24px;
      --radius-lg:     16px;
      --radius-md:     12px;
    }
    .typeform-navbar {
      background: rgba(10,36,17,0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.12);
      padding: 12px 24px;
      position: sticky; top: 0; z-index: 50;
      display: flex; align-items: center; justify-content: space-between;
    }
    .nav-brands { display: flex; align-items: center; gap: 16px; }
    .nav-logo-pg { height: 30px; width: auto; object-fit: contain; }
    .nav-logo-wp { height: 32px; width: auto; background: #fff; padding: 3px 8px; border-radius: 6px; }
    .progress-bar-wrap {
      position: fixed; top: 57px; left: 0; right: 0; height: 4px;
      background: rgba(255,255,255,0.1); z-index: 49;
    }
    .progress-bar-fill {
      height: 100%; width: 20%;
      background: linear-gradient(90deg, var(--green-light), var(--accent-gold));
      transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 0 10px rgba(52,168,83,0.7);
    }
""")
add("""
    .app-viewport {
      flex: 1; display: flex; align-items: center; justify-content: center;
      padding: 24px 20px 40px;
      background: radial-gradient(circle at 10% 20%, rgba(31,131,58,0.25) 0%, rgba(10,36,17,0.95) 90%);
      min-height: calc(100vh - 60px);
    }
    .split-card {
      width: 100%; max-width: 1120px; background: #ffffff;
      border-radius: var(--radius-xl);
      box-shadow: 0 25px 60px -10px rgba(0,0,0,0.35);
      display: grid; grid-template-columns: 380px 1fr;
      overflow: hidden; min-height: 640px;
      border: 1px solid rgba(255,255,255,0.15); position: relative;
    }
    @media (max-width: 900px) { .split-card { grid-template-columns: 1fr; max-width: 680px; } }
    .promo-panel {
      position: relative; background: #0f3d1c; color: #fff;
      padding: 36px 30px; display: flex; flex-direction: column;
      justify-content: space-between; overflow: hidden;
    }
    .promo-panel-bg {
      position: absolute; inset: 0;
      background: url('poster.jpg') center 20% / cover no-repeat;
      filter: brightness(0.38) saturate(1.15); z-index: 0;
    }
    .promo-panel-gradient {
      position: absolute; inset: 0;
      background: linear-gradient(to bottom, rgba(13,56,25,0.85) 0%, rgba(13,56,25,0.95) 100%);
      z-index: 1;
    }
    .promo-panel-content {
      position: relative; z-index: 2; height: 100%;
      display: flex; flex-direction: column; justify-content: space-between;
    }
    .promo-tag {
      display: inline-flex; align-items: center; gap: 6px;
      background: rgba(245,158,11,0.2); border: 1px solid var(--accent-gold);
      color: #fef08a; font-size: 0.72rem; font-weight: 700;
      padding: 4px 12px; border-radius: 30px; text-transform: uppercase;
      align-self: flex-start; margin-bottom: 12px;
    }
    .promo-title { font-size: 1.8rem; font-weight: 800; line-height: 1.15; margin-bottom: 8px; }
    .promo-title span { color: var(--accent-gold); }
    .promo-subtitle { font-size: 0.85rem; color: #d1fae5; line-height: 1.5; margin-bottom: 20px; }
    .promo-pill {
      background: rgba(255,255,255,0.12); backdrop-filter: blur(6px);
      border: 1px solid rgba(255,255,255,0.2); border-radius: 12px;
      padding: 10px 14px; font-size: 0.82rem; display: flex; align-items: center; gap: 10px; margin-bottom: 10px;
    }
    .mini-cart {
      background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.18);
      border-radius: 16px; padding: 16px; backdrop-filter: blur(8px);
    }
    .mini-cart-header {
      font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;
      color: var(--accent-gold); font-weight: 700; margin-bottom: 6px; display: flex; justify-content: space-between;
    }
    .mini-cart-ticket { font-size: 1rem; font-weight: 700; color: #fff; }
    .mini-cart-price { font-size: 1.4rem; font-weight: 800; color: #4ade80; margin-top: 2px; }
    @media (max-width: 900px) { .promo-panel { display: none; } }
""")
add("""
    .interactive-canvas {
      padding: 38px 44px 30px; display: flex; flex-direction: column;
      justify-content: space-between; position: relative; background: #ffffff;
    }
    @media (max-width: 600px) { .interactive-canvas { padding: 24px 18px 20px; } }
    .step-counter-tag {
      display: inline-flex; align-items: center; gap: 8px; font-size: 0.76rem;
      font-weight: 700; color: var(--green-mid); text-transform: uppercase;
      letter-spacing: 0.5px; margin-bottom: 6px;
    }
    .step-num-bubble {
      background: var(--green-pale); color: var(--green-mid); width: 24px; height: 24px;
      border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem;
    }
    .step-headline {
      font-size: clamp(1.35rem, 2.8vw, 1.75rem); font-weight: 800; color: var(--green-darkest);
      line-height: 1.25; letter-spacing: -0.5px; margin-bottom: 6px;
    }
    .step-subtext { font-size: 0.88rem; color: #4b5563; margin-bottom: 22px; line-height: 1.5; }
    .interactive-step { display: none; animation: tfFadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
    .interactive-step.active-step { display: block; }
    @keyframes tfFadeIn { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
    .tf-input-wrap { margin-bottom: 18px; }
    .tf-label { display: block; font-size: 0.84rem; font-weight: 700; color: #1f2937; margin-bottom: 6px; }
    .tf-label .req { color: var(--red); margin-left: 2px; }
    .tf-input {
      width: 100%; padding: 13px 16px; font-size: 1rem; font-family: inherit; color: #111827;
      background: #f9fafb; border: 2px solid #e5e7eb; border-radius: var(--radius-md); outline: none; transition: all 0.2s;
    }
    .tf-input:focus { background: #ffffff; border-color: var(--green-mid); box-shadow: 0 0 0 4px rgba(31,131,58,0.15); }
    .tf-hint { font-size: 0.76rem; color: #6b7280; margin-top: 5px; }
    .gender-picker { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    .gender-card {
      border: 2px solid #e5e7eb; background: #f9fafb; padding: 13px; border-radius: var(--radius-md);
      cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;
      font-weight: 700; font-size: 0.92rem; transition: all 0.2s; user-select: none;
    }
    .gender-card input { display: none; }
    .gender-card:hover { border-color: var(--green-mid); background: var(--green-pale); }
    .gender-card:has(input:checked) { border-color: var(--green-mid); background: var(--green-pale); color: var(--green-dark); box-shadow: 0 0 0 3px rgba(31,131,58,0.2); }
    .tickets-stack { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px; }
    @media (max-width: 600px) { .tickets-stack { grid-template-columns: 1fr; } }
    .ticket-choice {
      border: 2px solid #e5e7eb; border-radius: var(--radius-lg); padding: 15px; background: #f9fafb;
      cursor: pointer; position: relative; transition: all 0.25s; display: flex; flex-direction: column; justify-content: space-between;
    }
    .ticket-choice input { position: absolute; opacity: 0; pointer-events: none; }
    .ticket-choice:hover { border-color: var(--green-mid); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(31,131,58,0.12); }
    .ticket-choice:has(input:checked) { border-color: var(--green-mid); background: #ffffff; box-shadow: 0 0 0 3px rgba(31,131,58,0.2), 0 10px 24px rgba(31,131,58,0.14); }
    .ticket-choice-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 6px; }
    .key-badge { font-size: 0.68rem; font-weight: 800; background: #e5e7eb; color: #374151; padding: 2px 7px; border-radius: 6px; border: 1px solid #d1d5db; }
    .ticket-choice:has(input:checked) .key-badge { background: var(--green-mid); color: #fff; border-color: var(--green-mid); }
    .ticket-choice-title { font-size: 0.95rem; font-weight: 800; color: var(--green-darkest); margin-bottom: 2px; }
    .ticket-choice-price { font-size: 1.2rem; font-weight: 900; color: var(--green-mid); margin-bottom: 6px; }
    .ticket-choice-features { list-style: none; font-size: 0.72rem; color: #4b5563; line-height: 1.5; border-top: 1px dashed #d1d5db; padding-top: 6px; }
    .ticket-choice-features li::before { content: '✓ '; color: var(--green-mid); font-weight: bold; }
    .waiver-box { background: #fefce8; border: 1.5px solid #fde047; border-radius: var(--radius-md); padding: 12px 14px; margin-bottom: 12px; display: flex; gap: 10px; align-items: flex-start; }
    .waiver-scroll { max-height: 180px; overflow-y: auto; border: 1.5px solid #e5e7eb; border-radius: var(--radius-md); padding: 12px; font-size: 0.78rem; line-height: 1.6; color: #374151; background: #f9fafb; margin-bottom: 12px; }
    .waiver-scroll h5 { color: var(--green-darkest); font-size: 0.84rem; margin: 8px 0 3px; }
    .waiver-scroll h5:first-child { margin-top: 0; }
    .waiver-scroll ol, .waiver-scroll ul { padding-left: 18px; margin-bottom: 4px; }
    .tf-checkbox-label { display: flex; gap: 10px; align-items: flex-start; cursor: pointer; font-size: 0.83rem; font-weight: 600; color: #1f2937; user-select: none; }
    .tf-checkbox-label input { width: 18px; height: 18px; accent-color: var(--green-mid); margin-top: 2px; flex-shrink: 0; }
    .payment-cards-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px; }
    @media (max-width: 540px) { .payment-cards-grid { grid-template-columns: 1fr; } }
    .bank-card-clean { border: 1.5px solid var(--green-border); background: var(--green-pale); border-radius: var(--radius-md); padding: 12px; display: flex; flex-direction: column; justify-content: space-between; }
    .bank-card-num { font-family: monospace; font-size: 1.1rem; font-weight: 900; color: #111827; margin: 3px 0; }
    .qris-card-clean { border: 1.5px solid var(--green-border); background: var(--green-pale); border-radius: var(--radius-md); padding: 12px; display: flex; gap: 10px; align-items: center; }
    .tf-dropzone { border: 2px dashed #9ca3af; border-radius: var(--radius-md); background: #f9fafb; padding: 20px 14px; text-align: center; cursor: pointer; transition: all 0.2s; position: relative; margin-bottom: 10px; }
    .tf-dropzone:hover, .tf-dropzone.dragover { border-color: var(--green-mid); background: var(--green-pale); }
    .tf-dropzone input[type="file"] { position: absolute; inset: 0; opacity: 0; width: 100%; height: 100%; cursor: pointer; }
    .tf-nav-bar { border-top: 1.5px solid #f3f4f6; padding-top: 18px; display: flex; align-items: center; justify-content: space-between; gap: 14px; margin-top: 16px; }
    .tf-btn-back { background: none; border: none; color: #6b7280; font-weight: 700; font-size: 0.88rem; cursor: pointer; display: flex; align-items: center; gap: 6px; padding: 8px 12px; border-radius: 8px; }
    .tf-btn-back:hover { color: #111827; background: #f3f4f6; }
    .tf-btn-next {
      background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-mid) 100%); color: #fff; border: none;
      border-radius: var(--radius-md); padding: 12px 22px; font-size: 0.93rem; font-weight: 800; cursor: pointer;
      display: flex; align-items: center; gap: 8px; transition: all 0.22s; box-shadow: 0 4px 12px rgba(18,78,35,0.3);
    }
    .tf-btn-next:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(18,78,35,0.45); }
    .tf-btn-next:disabled { background: #9ca3af; cursor: not-allowed; box-shadow: none; transform: none; }
    .keyboard-hint { font-size: 0.72rem; color: #9ca3af; margin-left: 4px; font-weight: 500; }
    .summary-review-box { background: #f9fafb; border: 1.5px solid var(--green-border); border-radius: var(--radius-lg); padding: 16px; margin-bottom: 16px; }
    .review-row { display: flex; justify-content: space-between; padding: 7px 0; border-bottom: 1px solid #e5e7eb; font-size: 0.85rem; }
    .review-row:last-child { border-bottom: none; }
    .review-label { color: #6b7280; font-weight: 500; }
    .review-val { color: #111827; font-weight: 700; text-align: right; }
    .review-total-val { font-size: 1.35rem; font-weight: 900; color: var(--green-mid); }
    .tf-error { color: var(--red); font-size: 0.75rem; font-weight: 600; margin-top: 4px; display: none; }
    .has-error .tf-input, .has-error .tf-dropzone { border-color: var(--red) !important; }
    .has-error .tf-error { display: block; }
    #step-success { text-align: center; padding: 36px 10px; }
    .success-icon-big { font-size: 3.8rem; margin-bottom: 12px; }
    .success-title { font-size: 1.6rem; color: var(--green-dark); font-weight: 800; margin-bottom: 8px; }
    .success-desc { font-size: 0.92rem; color: #4b5563; line-height: 1.6; max-width: 460px; margin: 0 auto; }
  </style>
</head>
<body>
""")
add("""
  <!-- TOP NAVBAR -->
  <nav class="typeform-navbar">
    <div class="nav-brands">
      <img src="logo_psf.png" alt="Pancoran Group" class="nav-logo-pg" />
      <img src="logo_waterpark.png" alt="Pancoran Waterpark" class="nav-logo-wp" />
    </div>
    <div class="nav-controls">
      <a href="https://wa.me/628133278031?text=Halo%20Panitia%20Pancoran%20Slide%20Festival%202026" target="_blank" class="mode-toggle-btn" style="background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.25); color:#fff; font-size:0.8rem; font-weight:600; padding:6px 14px; border-radius:30px; text-decoration:none; display:flex; align-items:center; gap:6px;">
        <span>💬</span> <span>Helpdesk WA</span>
      </a>
    </div>
  </nav>

  <!-- TYPEFORM PROGRESS BAR -->
  <div class="progress-bar-wrap">
    <div class="progress-bar-fill" id="progress-bar"></div>
  </div>

  <!-- MAIN APP VIEWPORT -->
  <main class="app-viewport">
    <div class="split-card">

      <!-- LEFT PANEL (SOFTR.IO PROMO DISPLAY) -->
      <aside class="promo-panel">
        <div class="promo-panel-bg"></div>
        <div class="promo-panel-gradient"></div>
        <div class="promo-panel-content">
          <div>
            <div class="promo-tag">⭐ Official Registration</div>
            <h1 class="promo-title">Pancoran<br /><span>Slide Festival</span><br />2026</h1>
            <p class="promo-subtitle">Sensasi seluncur air 20 meter, festival lari seru, dan hadiah uang tunai di Pancoran Waterpark!</p>

            <div class="promo-pill">
              <span>📅</span>
              <div><strong>Minggu, 4 Oktober 2026</strong><br /><small style="color:#d1fae5;">Pukul 06.00 WIB - Selesai</small></div>
            </div>
            <div class="promo-pill">
              <span>📍</span>
              <div><strong>Pancoran Waterpark</strong><br /><small style="color:#d1fae5;">Semua wahana all access</small></div>
            </div>
          </div>

          <!-- Live Order Recap Card -->
          <div class="mini-cart">
            <div class="mini-cart-header">
              <span>Ringkasan Pilihan</span>
              <span>LIVE</span>
            </div>
            <div class="mini-cart-ticket" id="mini-cart-ticket-name">— Pilih Tiket —</div>
            <div class="mini-cart-price" id="mini-cart-price-val">Rp 0</div>
          </div>
        </div>
      </aside>

      <!-- RIGHT INTERACTIVE CANVAS (TYPEFORM FLOW) -->
      <div class="interactive-canvas">
        <form id="typeform-form" novalidate autocomplete="off">

          <!-- ════ STEP 1: DATA DIRI ════ -->
          <div class="interactive-step active-step" id="step-1">
            <div class="step-counter-tag">
              <span class="step-num-bubble">1</span> Langkah 1 dari 5
            </div>
            <h2 class="step-headline">Selamat datang! Siapa nama Anda? 👋</h2>
            <p class="step-subtext">Data ini akan digunakan untuk pencetakan nomor BIB peserta dan sertifikat.</p>

            <div class="tf-input-wrap" id="wrap-fullname">
              <label class="tf-label" for="fullname">Nama Lengkap <span class="req">*</span></label>
              <input type="text" id="fullname" class="tf-input" placeholder="Ketik nama lengkap Anda..." autofocus />
              <div class="tf-error">Nama lengkap wajib diisi.</div>
            </div>

            <div class="tf-input-wrap" id="wrap-nickname">
              <label class="tf-label" for="nickname">Nama Panggilan (untuk nomor BIB) <span class="req">*</span></label>
              <input type="text" id="nickname" class="tf-input" placeholder="Contoh: RUDI" />
              <div class="tf-hint">Maksimal 10 karakter untuk dicetak di nomor BIB.</div>
              <div class="tf-error">Nama panggilan BIB wajib diisi.</div>
            </div>
          </div>

          <!-- ════ STEP 2: KONTAK & SOSMED ════ -->
          <div class="interactive-step" id="step-2">
            <div class="step-counter-tag">
              <span class="step-num-bubble">2</span> Langkah 2 dari 5
            </div>
            <h2 class="step-headline">Informasi Kontak &amp; Media Sosial 📱</h2>
            <p class="step-subtext">E-tiket dan konfirmasi resmi akan dikirimkan langsung ke nomor WhatsApp Anda.</p>

            <div class="tf-input-wrap" id="wrap-gender">
              <label class="tf-label">Jenis Kelamin <span class="req">*</span></label>
              <div class="gender-picker">
                <label class="gender-card">
                  <input type="radio" name="gender" value="Laki-laki" />
                  <span>🏃 Laki-laki</span>
                </label>
                <label class="gender-card">
                  <input type="radio" name="gender" value="Perempuan" />
                  <span>🏃‍♀️ Perempuan</span>
                </label>
              </div>
              <div class="tf-error" id="gender-err">Silakan pilih jenis kelamin.</div>
            </div>

            <div class="tf-input-wrap" id="wrap-wa">
              <label class="tf-label" for="wa">Nomor WhatsApp Aktif <span class="req">*</span></label>
              <input type="tel" id="wa" class="tf-input" placeholder="Contoh: 081234567890" />
              <div class="tf-hint">Nomor wajib aktif terhubung ke WhatsApp.</div>
              <div class="tf-error">Nomor WhatsApp aktif wajib diisi (minimal 10 digit).</div>
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
              <div class="tf-input-wrap" id="wrap-ig">
                <label class="tf-label" for="instagram">Instagram <span class="req">*</span></label>
                <input type="text" id="instagram" class="tf-input" placeholder="@username" />
                <div class="tf-error">Akun Instagram wajib diisi.</div>
              </div>
              <div class="tf-input-wrap" id="wrap-tiktok">
                <label class="tf-label" for="tiktok">TikTok <small style="color:#6b7280;">(opsional)</small></label>
                <input type="text" id="tiktok" class="tf-input" placeholder="@username" />
              </div>
            </div>
          </div>

          <!-- ════ STEP 3: PILIH KATEGORI TIKET ════ -->
          <div class="interactive-step" id="step-3">
            <div class="step-counter-tag">
              <span class="step-num-bubble">3</span> Langkah 3 dari 5
            </div>
            <h2 class="step-headline">Pilih Kategori Acara Anda 🎟️</h2>
            <p class="step-subtext">Pilih tantangan yang ingin Anda ikuti di Pancoran Slide Festival 2026.</p>

            <div class="tickets-stack">
              <label class="ticket-choice">
                <input type="radio" name="ticket" value="Lari 6K" data-price="35000" />
                <div>
                  <div class="ticket-choice-top">
                    <span class="key-badge">1</span>
                    <span style="font-size:0.68rem; font-weight:700; background:#e0f2fe; color:#0369a1; padding:2px 8px; border-radius:20px;">FUN RUN</span>
                  </div>
                  <h4 class="ticket-choice-title">Lari 6K</h4>
                  <div class="ticket-choice-price">Rp 35.000</div>
                </div>
                <ul class="ticket-choice-features">
                  <li>All akses wahana Pancoran</li>
                  <li>Refreshment &amp; fun games</li>
                  <li>Dokumentasi foto digital</li>
                  <li>Produk Bejo Jahe Merah</li>
                </ul>
              </label>

              <label class="ticket-choice">
                <input type="radio" name="ticket" value="Slide Challenge" data-price="45000" />
                <div>
                  <div class="ticket-choice-top">
                    <span class="key-badge">2</span>
                    <span style="font-size:0.68rem; font-weight:700; background:#fef3c7; color:#b45309; padding:2px 8px; border-radius:20px;">CHALLENGE</span>
                  </div>
                  <h4 class="ticket-choice-title">Slide Challenge</h4>
                  <div class="ticket-choice-price">Rp 45.000</div>
                </div>
                <ul class="ticket-choice-features">
                  <li>All akses wahana Pancoran</li>
                  <li>Peluang hadiah uang tunai</li>
                  <li>Dokumentasi foto digital</li>
                  <li>Produk Bejo Jahe Merah</li>
                </ul>
              </label>

              <label class="ticket-choice">
                <input type="radio" name="ticket" value="Extreme Running" data-price="80000" />
                <div>
                  <div class="ticket-choice-top">
                    <span class="key-badge">3</span>
                    <span style="font-size:0.68rem; font-weight:700; background:#dcfce7; color:#15803d; padding:2px 8px; border-radius:20px;">COMBO 🔥</span>
                  </div>
                  <h4 class="ticket-choice-title">Extreme Running</h4>
                  <div class="ticket-choice-price">Rp 80.000</div>
                </div>
                <ul class="ticket-choice-features">
                  <li>Lari 6K + Slide Challenge</li>
                  <li>Peluang hadiah uang tunai</li>
                  <li>Dokumentasi foto digital</li>
                  <li>Produk Bejo Jahe Merah</li>
                </ul>
              </label>

              <label class="ticket-choice">
                <input type="radio" name="ticket" value="Extreme Running Lengkap" data-price="120000" />
                <div>
                  <div class="ticket-choice-top">
                    <span class="key-badge">4</span>
                    <span style="font-size:0.68rem; font-weight:700; background:#fee2e2; color:#b91c1c; padding:2px 8px; border-radius:20px;">BEST VALUE ⭐</span>
                  </div>
                  <h4 class="ticket-choice-title">Extreme Running Lengkap</h4>
                  <div class="ticket-choice-price">Rp 120.000</div>
                </div>
                <ul class="ticket-choice-features">
                  <li>Semua benefit Extreme Running</li>
                  <li><strong>Official Merch Slow Burn</strong></li>
                  <li>Hadiah tunai &amp; foto digital</li>
                  <li>Produk Bejo Jahe Merah</li>
                </ul>
              </label>
            </div>
            <div class="tf-error" id="ticket-err">Silakan klik salah satu tiket untuk memilih.</div>
          </div>
""")
add("""
          <!-- ════ STEP 4: SAFETY WAIVER & T&C ════ -->
          <div class="interactive-step" id="step-4">
            <div class="step-counter-tag">
              <span class="step-num-bubble">4</span> Langkah 4 dari 5
            </div>
            <h2 class="step-headline">Safety Waiver &amp; Kesepakatan 🦺</h2>
            <p class="step-subtext">Karena Anda memilih tantangan seluncuran air, mohon baca dan setujui ketentuan keselamatan berikut.</p>

            <div class="waiver-box">
              <span style="font-size:1.3rem;">⚠️</span>
              <div style="font-size:0.82rem; color:#713f12; line-height:1.45;">
                Aktivitas <strong>Slide Challenge</strong> memerlukan kondisi fisik yang sehat serta kepatuhan terhadap arahan instruktur &amp; lifeguard.
              </div>
            </div>

            <div class="waiver-scroll">
              <h5>A. KETENTUAN UMUM</h5>
              <ol>
                <li>Pancoran Slide Festival 2026 diselenggarakan pada Minggu, 4 Oktober 2026 di Pancoran Waterpark.</li>
                <li>Tiket yang dibeli non-refundable, kecuali acara dibatalkan penyelenggara.</li>
                <li>Peserta wajib mematuhi arahan panitia, lifeguard, dan petugas keamanan.</li>
              </ol>
              <h5>B. SYARAT PESERTA SLIDE CHALLENGE</h5>
              <ol>
                <li>Pakaian renang/olahraga ringan, tidak menggunakan aksesoris keras atau benda tajam.</li>
                <li>Persyaratan Slider:
                  <ul>
                    <li>Regular: Usia ≥15 th, Tinggi >150 cm, Berat 40-70 kg</li>
                    <li>Heavy: Usia ≥15 th, Tinggi >150 cm, Berat >70 kg</li>
                  </ul>
                </li>
                <li>Dilarang berdiri saat meluncur atau mendorong peserta lain.</li>
              </ol>
              <h5>C. HADIAH &amp; PERSETUJUAN</h5>
              <p>Kategori challenge: Best Freestyle, Loudest Slider, Smoothest Splash, Best Crowd mendapatkan hadiah uang tunai.</p>
            </div>

            <label class="tf-checkbox-label">
              <input type="checkbox" id="tnc-agree" />
              <span>Saya telah membaca, memahami, dan <strong>menyetujui seluruh syarat &amp; ketentuan serta safety waiver</strong> di atas.</span>
            </label>
            <div class="tf-error" id="tnc-err">Anda wajib menyetujui ketentuan keselamatan untuk melanjutkan.</div>
          </div>

          <!-- ════ STEP 5: PEMBAYARAN & UPLOAD ════ -->
          <div class="interactive-step" id="step-5">
            <div class="step-counter-tag">
              <span class="step-num-bubble">5</span> Langkah 5 dari 5
            </div>
            <h2 class="step-headline">Pembayaran &amp; Upload Bukti 💳</h2>
            <p class="step-subtext">Transfer sesuai nominal tiket yang dipilih dan lampirkan bukti pembayaran Anda.</p>

            <div class="payment-cards-grid">
              <div class="bank-card-clean">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                  <span style="font-weight:800; font-size:0.85rem; color:var(--green-dark);">🏦 Bank BCA</span>
                  <button type="button" onclick="copyBCA('082892121120')" style="background:#fff; border:1px solid var(--green-border); border-radius:6px; padding:3px 8px; font-size:0.75rem; font-weight:700; cursor:pointer;">
                    <span id="bca-copy-label">📋 Salin</span>
                  </button>
                </div>
                <div class="bank-card-num">0828 9212 1120</div>
                <div style="font-size:0.75rem; color:#4b5563;">a.n. Panitia Pancoran Slide Festival</div>
              </div>

              <div class="qris-card-clean">
                <div style="width:70px; height:70px; background:#fff; border:1.5px dashed var(--green-border); border-radius:8px; display:flex; flex-direction:column; align-items:center; justify-content:center; font-size:0.65rem; text-align:center;">
                  📱<br /><strong>QRIS</strong><br />Scan
                </div>
                <div>
                  <h6 style="font-weight:800; font-size:0.82rem; color:var(--green-dark);">QRIS All Payment</h6>
                  <p style="font-size:0.72rem; color:#4b5563; line-height:1.35;">BCA, Mandiri, ShopeePay, GoPay, OVO, Dana, LinkAja</p>
                </div>
              </div>
            </div>

            <div class="tf-input-wrap" id="wrap-sender">
              <label class="tf-label" for="sender_name">Nama Pemilik Rekening / Pengirim <span class="req">*</span></label>
              <input type="text" id="sender_name" class="tf-input" placeholder="Contoh: Rudi Pratama (sesuai mutasi rekening)" />
              <div class="tf-error">Nama pengirim transfer wajib diisi.</div>
            </div>

            <div class="tf-input-wrap" id="wrap-file">
              <label class="tf-label">Upload Bukti Transfer <span class="req">*</span></label>
              <div class="tf-dropzone" id="dropzone">
                <input type="file" id="file_input" accept="image/*,.pdf" />
                <div style="font-size:2rem; margin-bottom:4px;">📎</div>
                <div style="font-weight:700; font-size:0.9rem; color:var(--green-dark);" id="dropzone-text">Klik atau seret file bukti transfer ke sini</div>
                <div style="font-size:0.75rem; color:#6b7280; margin-top:2px;">JPG, PNG, atau PDF (Maksimal 5 MB)</div>
              </div>
              <div class="tf-error" id="file-err">Bukti pembayaran wajib dilampirkan.</div>
            </div>
          </div>

          <!-- ════ STEP 6: REVIEW & SUBMIT ════ -->
          <div class="interactive-step" id="step-6">
            <div class="step-counter-tag">
              <span class="step-num-bubble">✓</span> Konfirmasi Terakhir
            </div>
            <h2 class="step-headline">Periksa kembali data Anda 📋</h2>
            <p class="step-subtext">Pastikan semua data sudah benar sebelum pendaftaran dikirimkan.</p>

            <div class="summary-review-box">
              <div class="review-row">
                <span class="review-label">Nama Lengkap</span>
                <span class="review-val" id="rev-fullname">-</span>
              </div>
              <div class="review-row">
                <span class="review-label">Nama Panggilan BIB</span>
                <span class="review-val" id="rev-nickname">-</span>
              </div>
              <div class="review-row">
                <span class="review-label">WhatsApp</span>
                <span class="review-val" id="rev-wa">-</span>
              </div>
              <div class="review-row">
                <span class="review-label">Kategori Tiket</span>
                <span class="review-val" id="rev-ticket">-</span>
              </div>
              <div class="review-row">
                <span class="review-label">Pengirim Transfer</span>
                <span class="review-val" id="rev-sender">-</span>
              </div>
              <div class="review-row" style="align-items:center; padding-top:12px;">
                <span class="review-label" style="font-weight:800; font-size:1rem; color:var(--green-dark);">Total Pembayaran</span>
                <span class="review-total-val" id="rev-price">Rp 0</span>
              </div>
            </div>

            <div style="font-size:0.8rem; color:#4b5563; margin-bottom:16px; display:flex; align-items:center; gap:8px;">
              <span>🔒</span>
              <span>Data aman &amp; konfirmasi e-tiket akan otomatis dikirimkan via WhatsApp setelah verifikasi tim panitia.</span>
            </div>
          </div>

          <!-- ════ STEP SUCCESS: SELESAI ════ -->
          <div class="interactive-step" id="step-success">
            <div class="success-icon-big">🎉</div>
            <h2 class="success-title">Pendaftaran Berhasil Dikirim!</h2>
            <p class="success-desc">
              Terima kasih, <strong id="success-name-display">Sahabat Pancoran</strong>!<br />
              Data pendaftaran dan bukti pembayaran Anda telah kami terima.<br />
              Tim panitia akan memverifikasi dan menghubungi Anda via WhatsApp di nomor yang terdaftar.
            </p>
            <br />
            <button type="button" onclick="location.reload()" class="tf-btn-next" style="margin: 0 auto;">
              Daftarkan Peserta Lain
            </button>
          </div>

          <!-- ── BOTTOM NAVIGATION ── -->
          <div class="tf-nav-bar" id="nav-action-bar">
            <button type="button" class="tf-btn-back" id="btn-prev">
              <span>←</span> <span>Sebelumnya</span>
            </button>
            <div style="display:flex; align-items:center;">
              <button type="button" class="tf-btn-next" id="btn-next">
                <span id="btn-next-label">Lanjutkan</span>
                <span class="keyboard-hint">(Enter ↵)</span>
              </button>
            </div>
          </div>

        </form>
      </div>

    </div>
  </main>
""")
add("""
  <script>
    const SCRIPT_URL = 'YOUR_GOOGLE_APPS_SCRIPT_URL_HERE';
    const fmt = n => 'Rp ' + Number(n).toLocaleString('id-ID');

    function copyBCA(acc) {
      navigator.clipboard.writeText(acc).then(() => {
        const lbl = document.getElementById('bca-copy-label');
        if (lbl) {
          lbl.textContent = '✓ Tersalin!';
          setTimeout(() => { lbl.textContent = '📋 Salin'; }, 2000);
        }
      }).catch(() => {
        alert('Nomor BCA: ' + acc);
      });
    }

    let currentStep = 1;
    const progressBar = document.getElementById('progress-bar');
    const btnPrev = document.getElementById('btn-prev');
    const btnNext = document.getElementById('btn-next');
    const btnNextLabel = document.getElementById('btn-next-label');

    const CHALLENGE_TICKETS = ['Slide Challenge', 'Extreme Running', 'Extreme Running Lengkap'];

    function updateProgressBar() {
      const pct = Math.min(100, Math.round((currentStep / 5) * 100));
      progressBar.style.width = pct + '%';
    }

    function showStep(stepIndex) {
      document.querySelectorAll('.interactive-step').forEach(s => s.classList.remove('active-step'));
      const stepEl = document.getElementById('step-' + stepIndex);
      if (stepEl) {
        stepEl.classList.add('active-step');
        const firstInput = stepEl.querySelector('input:not([type=\"radio\"]):not([type=\"checkbox\"]):not([type=\"file\"])');
        if (firstInput) firstInput.focus();
      }

      btnPrev.style.visibility = (stepIndex === 1 || stepIndex > 6) ? 'hidden' : 'visible';

      if (stepIndex === 6) {
        btnNextLabel.textContent = '🚀 Kirim Pendaftaran';
      } else {
        btnNextLabel.textContent = 'Lanjutkan';
      }

      updateProgressBar();
    }

    const ticketRadios = document.querySelectorAll('input[name=\"ticket\"]');
    const miniTicket = document.getElementById('mini-cart-ticket-name');
    const miniPrice = document.getElementById('mini-cart-price-val');

    ticketRadios.forEach(radio => {
      radio.addEventListener('change', () => {
        miniTicket.textContent = radio.value;
        miniPrice.textContent = fmt(radio.dataset.price);
        document.getElementById('ticket-err').style.display = 'none';
      });
    });

    const fileInput = document.getElementById('file_input');
    const dropzone = document.getElementById('dropzone');
    const dropzoneText = document.getElementById('dropzone-text');
    const fileErr = document.getElementById('file-err');

    fileInput.addEventListener('change', () => {
      const f = fileInput.files[0];
      if (!f) return;
      if (f.size > 5 * 1024 * 1024) {
        alert('File melebihi batas 5 MB!');
        fileInput.value = '';
        return;
      }
      dropzoneText.textContent = '📄 ' + f.name + ' (' + (f.size/1024).toFixed(0) + ' KB)';
      fileErr.style.display = 'none';
    });

    dropzone.addEventListener('dragover', e => { e.preventDefault(); dropzone.classList.add('dragover'); });
    dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
    dropzone.addEventListener('drop', e => {
      e.preventDefault(); dropzone.classList.remove('dragover');
      if (e.dataTransfer.files.length) {
        const dt = new DataTransfer(); dt.items.add(e.dataTransfer.files[0]);
        fileInput.files = dt.files;
        dropzoneText.textContent = '📄 ' + e.dataTransfer.files[0].name;
        fileErr.style.display = 'none';
      }
    });

    function setWrapError(id, isErr) {
      const el = document.getElementById(id);
      if (el) el.classList.toggle('has-error', isErr);
    }

    function validateCurrentStep() {
      if (currentStep === 1) {
        const fn = document.getElementById('fullname').value.trim();
        const nn = document.getElementById('nickname').value.trim();
        setWrapError('wrap-fullname', !fn);
        setWrapError('wrap-nickname', !nn);
        return fn && nn;
      }

      if (currentStep === 2) {
        const gender = document.querySelector('input[name=\"gender\"]:checked');
        const gErr = document.getElementById('gender-err');
        if (!gender) { gErr.style.display = 'block'; } else { gErr.style.display = 'none'; }

        const wa = document.getElementById('wa').value.replace(/\\D/g, '');
        setWrapError('wrap-wa', wa.length < 10);

        const ig = document.getElementById('instagram').value.trim();
        setWrapError('wrap-ig', !ig);

        return gender && (wa.length >= 10) && ig;
      }

      if (currentStep === 3) {
        const tc = document.querySelector('input[name=\"ticket\"]:checked');
        const terr = document.getElementById('ticket-err');
        if (!tc) { terr.style.display = 'block'; return false; }
        terr.style.display = 'none';
        return true;
      }

      if (currentStep === 4) {
        const agreed = document.getElementById('tnc-agree').checked;
        const terr = document.getElementById('tnc-err');
        if (!agreed) { terr.style.display = 'block'; return false; }
        terr.style.display = 'none';
        return true;
      }

      if (currentStep === 5) {
        const sn = document.getElementById('sender_name').value.trim();
        setWrapError('wrap-sender', !sn);

        const file = fileInput.files[0];
        if (!file) { fileErr.style.display = 'block'; } else { fileErr.style.display = 'none'; }

        return sn && file;
      }

      return true;
    }

    function populateReview() {
      const tc = document.querySelector('input[name=\"ticket\"]:checked');
      document.getElementById('rev-fullname').textContent = document.getElementById('fullname').value.trim();
      document.getElementById('rev-nickname').textContent = document.getElementById('nickname').value.trim();
      document.getElementById('rev-wa').textContent = document.getElementById('wa').value.trim();
      document.getElementById('rev-ticket').textContent = tc ? tc.value : '-';
      document.getElementById('rev-sender').textContent = document.getElementById('sender_name').value.trim();
      document.getElementById('rev-price').textContent = tc ? fmt(tc.dataset.price) : 'Rp 0';
    }

    btnNext.addEventListener('click', () => {
      if (!validateCurrentStep()) return;

      if (currentStep === 3) {
        const selectedTicket = document.querySelector('input[name=\"ticket\"]:checked').value;
        if (!CHALLENGE_TICKETS.includes(selectedTicket)) {
          currentStep = 5;
          showStep(currentStep);
          return;
        }
      }

      if (currentStep === 5) {
        populateReview();
        currentStep = 6;
        showStep(currentStep);
        return;
      }

      if (currentStep === 6) {
        submitRegistration();
        return;
      }

      currentStep++;
      showStep(currentStep);
    });

    btnPrev.addEventListener('click', () => {
      if (currentStep === 5) {
        const selectedTicket = document.querySelector('input[name=\"ticket\"]:checked')?.value;
        if (selectedTicket && !CHALLENGE_TICKETS.includes(selectedTicket)) {
          currentStep = 3;
          showStep(currentStep);
          return;
        }
      }

      if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
      }
    });

    window.addEventListener('keydown', e => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        btnNext.click();
      }
      if (currentStep === 3) {
        if (e.key === '1') { const r = document.querySelector('input[value=\"Lari 6K\"]'); if (r) { r.checked = true; r.dispatchEvent(new Event('change')); } }
        if (e.key === '2') { const r = document.querySelector('input[value=\"Slide Challenge\"]'); if (r) { r.checked = true; r.dispatchEvent(new Event('change')); } }
        if (e.key === '3') { const r = document.querySelector('input[value=\"Extreme Running\"]'); if (r) { r.checked = true; r.dispatchEvent(new Event('change')); } }
        if (e.key === '4') { const r = document.querySelector('input[value=\"Extreme Running Lengkap\"]'); if (r) { r.checked = true; r.dispatchEvent(new Event('change')); } }
      }
    });

    function fileToBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(',')[1]);
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
    }

    async function submitRegistration() {
      btnNext.disabled = true;
      btnNextLabel.textContent = 'Mengirim data...';

      const tc = document.querySelector('input[name=\"ticket\"]:checked');
      const file = fileInput.files[0];
      const base64Data = file ? await fileToBase64(file) : '';

      const payload = {
        fullname:   document.getElementById('fullname').value.trim(),
        nickname:   document.getElementById('nickname').value.trim(),
        gender:     document.querySelector('input[name=\"gender\"]:checked')?.value || '',
        wa:         document.getElementById('wa').value.trim(),
        instagram:  document.getElementById('instagram').value.trim(),
        tiktok:     document.getElementById('tiktok').value.trim(),
        ticket:     tc.value,
        price:      tc.dataset.price,
        tncAgreed:  document.getElementById('tnc-agree').checked,
        senderName: document.getElementById('sender_name').value.trim(),
        fileName:   file ? file.name : '',
        fileData:   base64Data,
        fileType:   file ? file.type : '',
        timestamp:  new Date().toISOString()
      };

      try {
        await fetch(SCRIPT_URL, {
          method: 'POST',
          body: JSON.stringify(payload)
        });

        document.querySelectorAll('.interactive-step').forEach(s => s.classList.remove('active-step'));
        document.getElementById('step-success').classList.add('active-step');
        document.getElementById('success-name-display').textContent = payload.fullname;
        document.getElementById('nav-action-bar').style.display = 'none';
        progressBar.style.width = '100%';
      } catch (err) {
        console.error(err);
        alert('Gagal mengirim data. Silakan cek koneksi internet Anda dan coba lagi.');
        btnNext.disabled = false;
        btnNextLabel.textContent = '🚀 Kirim Pendaftaran';
      }
    }

    showStep(1);
  </script>
</body>
</html>
""")