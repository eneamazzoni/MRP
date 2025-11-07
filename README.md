# MRP – Mazzoni Recovery Protocol

> **Any public text + one mental rule = 24, 48, or 72 BIP39 words — all in your head.**

**One protocol. One sentence. Infinite entropy.**

---

## Core Protocol

1. **Choose any stable public text**  
2. **Define one mental rule** (in your head only)  
3. **Extract 24, 48, or 72 words** → map to BIP39  
4. **Enter into Ledger**

→ **No backup. No risk. Just you + literature.**

---

## Memory Rule (applies to all)

> **"Gandalf, Bilbo, Winston: after each chapter, take the first noun."**

→ **One sentence = 72 words in your head.**

---

## Examples

### 1. Beginner (24 words)  
- **Text**: LOTR (2004)  
- **Rule**: 1st noun per chapter  
- **Output**: see [`lotr_2004.csv`](lotr_2004.csv)  
- **Entropy**: ~80 bit

### 2. Advanced (24 words)  
- **Text**: 3 books × 8 chapters  
- **Rule**: see [`rule_variants.md`](rule_variants.md)  
- **Entropy**: ~256 bit

###  3. Whale (48 words)  
- **Text**: LOTR + Hobbit (1–24 each)  
- **Rule**: 1st noun per chapter  
- **Entropy**: ~528 bit

### 4. Quantum (72 words)  
- **Text**: LOTR + Hobbit + 1984 (1–24 each)  
- **Rule**: 1st noun per chapter  
- **Entropy**: **792 bit**

---

## Tools & Templates

| File | Use |
|------|-----|
| [`lotr_2004.csv`](lotr_2004.csv) | Full 22-word list from LOTR (Example 1) |
| [`rule_variants.md`](rule_variants.md) | 10 mental rule ideas |
| [`mapper.py`](mapper.py) | Auto-map non-BIP39 words to BIP39 |
| [`notary_template.txt`](notary_template.txt) | Swiss notary letter (post-mortem access) |


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

