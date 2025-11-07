# MRP
Mazzoni Recovery Protocol – Seed phrases from literature. Mind-backed. Notary-sealed.
# MRP – Mazzoni Recovery Protocol™

> **A seed phrase that lives in a book, your mind, and a notary.**

No paper. No metal. No cloud.  
Just literature + brain + law.

---

## How it works

1. **Choose a stable public book** (e.g. LOTR, 1984, Dune)  
2. **Define a mental rule** (e.g. "1st common noun per chapter")  
3. **Extract 24 words** → map to BIP39 if needed  
4. **Enter into Ledger**  
5. **Seal rule + book ref with notary** (post-mortem access)

---

## Example: LOTR (HarperCollins 2004)

| Chapter | Word |
|-------|------|
| 1 | party |
| 2 | shadow |
| 3 | company |
| ... | ... |
| 22 | breaking |

→ Full list in `lotr_2004.csv`

---

## Files

- `notary_template.txt` – Swiss notary letter  
- `bip39_wordlist.txt`  
- `lotr_2004.csv` – 24 words  
- `rule_variants.md` – 10 rule ideas  
- `mapper.py` – auto-map non-BIP39 words

---

## Security

- Book = public  
- Rule = private (mental)  
- Notary = legal trigger

**Your seed is safe even if this repo is public.**

---

## License

MIT © 2025 Enea Mazzoni (@eneamazzoni)

---

> **"Not your keys, not your coins.  
> Not your rule, not your seed."**
