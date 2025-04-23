# Excel Translator Web App

Una semplice web app per tradurre colonne di file Excel multilingua usando OpenAI GPT-4, con coerenza e terminologia tecnica.

## ✅ Funzionalità

- Caricamento file `.xlsx`
- Selezione sheet, riga iniziale/finale e colonna da tradurre (es. `POL`)
- Traduzione automatica usando GPT-4
- Output in formato Excel solo con il blocco tradotto

## 📦 Requisiti

- Python 3.9+
- Chiave API OpenAI valida

## 🧰 Installazione locale

1. Clona il repository:
```bash
git clone https://github.com/tuo-username/excel-translator.git
cd excel-translator
```

2. Installa i pacchetti:
```bash
pip install -r requirements.txt
```

3. Inserisci la tua chiave API in `utils.py`:
```python
openai.api_key = "LA_TUA_API_KEY"
```

4. Avvia il server:
```bash
python app.py
```

Vai su `http://localhost:5000` per usare l'app.

## 🌐 Deploy gratuito su Render.com

1. Crea un nuovo repository su GitHub e carica tutti i file del progetto.
2. Vai su [Render.com](https://render.com) e clicca su **New → Web Service**.
3. Collega il tuo GitHub e seleziona il repo.
4. Configura:

| Campo            | Valore                            |
|------------------|-----------------------------------|
| Build Command    | `pip install -r requirements.txt` |
| Start Command    | `python app.py`                   |
| Python version   | >= 3.9                            |

5. Attiva il piano gratuito e deploya.

## 📂 Struttura del progetto

```
.
├── app.py              # Flask web app
├── utils.py            # Funzioni di traduzione con OpenAI
├── requirements.txt    # Librerie necessarie
└── templates/
    └── index.html      # Interfaccia web
```

## ✨ Esempio di utilizzo

1. Carica un file Excel con colonne `ITA`, `ENG` e `POL`.
2. Indica il nome della scheda (es. "Entities"), le righe da 650 a 700 e la colonna `POL`.
3. Clicca su “Traduci” e scarica il blocco elaborato.

---

Realizzato per garantire traduzioni coerenti, senza mai copiare da `ENG` o `ITA`, sfruttando la potenza di GPT.
