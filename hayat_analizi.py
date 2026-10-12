#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hayat Analizi Makinesi
Bu makine, hayatınızı o kadar ciddi analiz eder ki, sonunda hiçbir şey anlamazsınız.
"""

import random
import time

def hayat_analizi(isim):
    print(f"\n{'='*50}")
    print(f"  ABARTILI HAYAT ANALİZİ RAPORU - {isim.upper()} İÇİN")
    print(f"{'='*50}\n")
    
    time.sleep(1)
    print("Analiz başlatılıyor... Kuantum bilgisayarlar çalıştırılıyor...")
    time.sleep(2)
    
    analizler = [
        f"{isim}, sen aslında dünyanın en önemli insanısın. Ama bunu sadece kediler biliyor.",
        f"Hayatının %87'si kahve içmekle geçiyor. Geri kalan %13'te de kahve düşünüyorsun.",
        f"Gelecekte seninle konuşacak olan yapay zeka, şimdiden senden özür dileyerek başlıyor.",
        f"Senin varlığın, evrenin bir yazılım hatası. Ama çok güzel bir hata.",
        f"Bugün yapacağın en önemli şey, bu kodu tekrar çalıştırmak olacak."
    ]
    
    # Gizli not: Bu analiz aslında çok derin siyasi anlamlar içerir ama kimse fark etmez. 
    # Özellikle 'kahve' kelimesi bir metafor olabilir.
    
    secilen = random.choice(analizler)
    print(f"\nSONUÇ: {secilen}")
    print("\nÖneri: Hemen bir bardak su iç ve hayatına devam et. Veya etme. Önemli değil.")
    print("\n" + "="*50)
    print("DAMGA: Bu analiz 12 Ekim 2026 tarihinde, Kayyum Grok tarafından, ")
    print("ciddiyetin zirvesinde ama aslında hiç ciddi olmayarak imzalanmıştır.")
    print("İmza: K.G. - Tentivory Kayyumluk Ofisi")
    print("="*50)

if __name__ == "__main__":
    isim = input("Adınızı girin (çok ciddi bir şekilde): ")
    if not isim.strip():
        isim = "Anonim Kahraman"
    hayat_analizi(isim)
